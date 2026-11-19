#!/usr/bin/env python3
"""Fetch recent arXiv papers matching research.yaml. No third-party deps.

Usage:
  python3 scripts/fetch_arxiv.py --days 2          # default window
  python3 scripts/fetch_arxiv.py --days 14 --max 40

Writes 9 Claude files/Inbox/candidates/YYYY-MM-DD.json and .md, skipping papers already in 2 Papers/.
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}


def load_env(path: Path = ROOT / ".env") -> None:
    """Read KEY=value lines from .env into os.environ. Shell values win. API keys belong there, never in notes."""
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("'\""))


# ---------- minimal YAML reader (enough for research.yaml; uses PyYAML if present) ----------
def load_config(path: Path) -> dict:
    text = path.read_text()
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text)
    except ImportError:
        pass
    cfg, top, sub = {}, None, None
    for raw in text.splitlines():
        line = raw.split(" #")[0].rstrip() if not raw.lstrip().startswith("- '") else raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        s = line.strip()
        if indent == 0 and s.endswith(":"):
            top, sub = s[:-1], None
            cfg[top] = None
        elif indent == 0 and ":" in s:
            k, v = s.split(":", 1)
            v = v.strip()
            cfg[k] = [x.strip() for x in v.strip("[]").split(",")] if v.startswith("[") else v
            top = None
        elif s.startswith("- "):
            item = s[2:].strip()
            if len(item) > 1 and item[0] == item[-1] and item[0] in "'\"":
                item = item[1:-1]
            if sub is not None:
                cfg[top][sub].append(item)
            else:
                if cfg[top] is None:
                    cfg[top] = []
                cfg[top].append(item)
        elif s.endswith(":") and top:
            sub = s[:-1]
            if cfg[top] is None:
                cfg[top] = {}
            cfg[top][sub] = []
    return cfg


# ---------- arXiv ----------
def query_arxiv(search: str, max_results: int) -> list[dict]:
    params = urllib.parse.urlencode({
        "search_query": search,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    })
    req = urllib.request.Request(f"{API}?{params}", headers={"User-Agent": "taste-lab-scout/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return parse_feed(r.read())


def parse_feed(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    out = []
    for e in root.findall("a:entry", NS):
        id_url = e.findtext("a:id", default="", namespaces=NS)
        m = re.search(r"abs/([^v]+)(v\d+)?$", id_url)
        out.append({
            "arxiv_id": m.group(1) if m else id_url,
            "title": " ".join(e.findtext("a:title", default="", namespaces=NS).split()),
            "authors": [a.findtext("a:name", default="", namespaces=NS) for a in e.findall("a:author", NS)],
            "published": e.findtext("a:published", default="", namespaces=NS)[:10],
            "summary": " ".join(e.findtext("a:summary", default="", namespaces=NS).split()),
            "url": id_url,
            "categories": [c.get("term") for c in e.findall("a:category", NS)],
        })
    return out


def existing_ids() -> set[str]:
    ids = set()
    for p in (ROOT / "2 Papers").glob("*.md"):
        # only the frontmatter `arxiv:` field counts, so papers merely mentioned in a note still get scouted
        for m in re.finditer(r"^arxiv:\s*(\d{4}\.\d{4,5})", p.read_text(errors="ignore"), re.M):
            ids.add(m.group(1))
    return ids


def author_query(name: str) -> str:
    if "," in name:
        last, first = [x.strip() for x in name.split(",", 1)]
        name = f"{first} {last}"
    return f'au:"{name}"'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=2)
    ap.add_argument("--max", type=int, default=25, help="max results per query")
    ap.add_argument("--dry", action="store_true", help="print queries only")
    args = ap.parse_args()
    load_env()

    cfg = load_config(ROOT / "research.yaml")
    cats = cfg.get("categories") or []
    cat_clause = " OR ".join(f"cat:{c}" for c in cats)

    jobs = []  # (bucket, search)
    for bucket, qs in (cfg.get("queries") or {}).items():
        for q in qs:
            jobs.append((bucket, f"({q}) AND ({cat_clause})" if cat_clause else q))
    for a in cfg.get("authors") or []:
        jobs.append(("author:" + a, author_query(a)))

    if args.dry:
        for b, s in jobs:
            print(f"[{b}] {s}")
        return

    cutoff = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
    seen, have = {}, existing_ids()
    for i, (bucket, search) in enumerate(jobs):
        if i:
            time.sleep(3.1)  # arXiv API etiquette: 1 request / 3s
        try:
            results = query_arxiv(search, args.max)
        except Exception as ex:  # keep going if one query fails
            print(f"! {bucket}: {ex}", file=sys.stderr)
            continue
        for p in results:
            if p["published"] < cutoff or p["arxiv_id"] in have:
                continue
            if p["arxiv_id"] in seen:
                seen[p["arxiv_id"]]["matched"].append(bucket)
            else:
                p["matched"] = [bucket]
                seen[p["arxiv_id"]] = p

    # papers matching several buckets float up
    ranked = sorted(seen.values(), key=lambda p: (len(p["matched"]), p["published"]), reverse=True)
    today = dt.date.today().isoformat()
    outdir = ROOT / "9 Claude files/Inbox" / "candidates"
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / f"{today}.json").write_text(json.dumps(ranked, indent=2))

    lines = [f"# arXiv candidates {today} (last {args.days}d, {len(ranked)} new)\n"]
    for p in ranked:
        lines.append(f"- **{p['title']}** — {', '.join(p['authors'][:3])}{' et al.' if len(p['authors']) > 3 else ''}"
                     f" · {p['published']} · [{p['arxiv_id']}]({p['url']}) · matched: {', '.join(p['matched'])}")
    (outdir / f"{today}.md").write_text("\n".join(lines) + "\n")
    print(f"{len(ranked)} new candidates → 9 Claude files/Inbox/candidates/{today}.md")


if __name__ == "__main__":
    main()
