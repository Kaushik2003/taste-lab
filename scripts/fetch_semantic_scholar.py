#!/usr/bin/env python3
"""Backfill fetcher: Semantic Scholar search for foundations and adjacent areas.

arXiv's API sorts by submission date, so it never surfaces the old foundational
papers or the adjacent areas (world models, intrinsic motivation, active
inference) that research.yaml's s2_queries block names. This script fills that.

Usage:
  python3 scripts/fetch_semantic_scholar.py                     # all buckets
  python3 scripts/fetch_semantic_scholar.py --bucket foundations_backfill --min-citations 50
  python3 scripts/fetch_semantic_scholar.py --since-year 2023 --max-per-query 40

Writes 9 Claude files/Inbox/candidates/backfill-YYYY-MM-DD.json and .md, skipping papers
already in 2 Papers/ (by arXiv ID in frontmatter) or in any existing
candidates file. No third-party deps. No API key needed (shared rate pool,
the script sleeps between calls); set S2_API_KEY in .env for a private pool.
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
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = "title,authors,year,abstract,externalIds,citationCount,url,publicationDate,venue"


def load_env(path: Path = ROOT / ".env") -> None:
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("'\""))


def load_config(path: Path) -> dict:
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text())
    except ImportError:
        # reuse the minimal reader from fetch_arxiv
        sys.path.insert(0, str(ROOT / "scripts"))
        from fetch_arxiv import load_config as lc  # type: ignore
        return lc(path)


def s2_search(query: str, limit: int, year: str | None, min_citations: int, api_key: str | None) -> list[dict]:
    params = {"query": query, "limit": min(limit, 100), "fields": FIELDS}
    if year:
        params["year"] = year
    req = urllib.request.Request(f"{API}?{urllib.parse.urlencode(params)}",
                                 headers={"User-Agent": "taste-lab-scout/0.2"})
    if api_key:
        req.add_header("x-api-key", api_key)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read())
    out = []
    for p in data.get("data", []):
        if p.get("citationCount", 0) < min_citations:
            continue
        ext = p.get("externalIds") or {}
        out.append({
            "title": " ".join((p.get("title") or "").split()),
            "authors": [a.get("name", "") for a in (p.get("authors") or [])],
            "year": p.get("year"),
            "published": p.get("publicationDate") or str(p.get("year") or ""),
            "venue": p.get("venue") or "",
            "citations": p.get("citationCount", 0),
            "arxiv_id": ext.get("ArXiv"),
            "doi": ext.get("DOI"),
            "url": f"https://arxiv.org/abs/{ext['ArXiv']}" if ext.get("ArXiv") else p.get("url"),
            "summary": " ".join((p.get("abstract") or "").split()),
        })
    return out


def known_ids() -> set[str]:
    ids = set()
    for p in (ROOT / "2 Papers").glob("*.md"):
        for m in re.finditer(r"^arxiv:\s*(\d{4}\.\d{4,5})", p.read_text(errors="ignore"), re.M):
            ids.add(m.group(1))
    cand = ROOT / "9 Claude files/Inbox" / "candidates"
    if cand.exists():
        for f in cand.glob("*.json"):
            try:
                for p in json.loads(f.read_text()):
                    if p.get("arxiv_id"):
                        ids.add(str(p["arxiv_id"]))
            except Exception:
                continue
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bucket", default=None, help="only this s2_queries bucket")
    ap.add_argument("--min-citations", type=int, default=20)
    ap.add_argument("--since-year", type=int, default=None, help="only papers from this year on")
    ap.add_argument("--until-year", type=int, default=None)
    ap.add_argument("--max-per-query", type=int, default=25)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    load_env()

    cfg = load_config(ROOT / "research.yaml")
    buckets = cfg.get("s2_queries") or {}
    if args.bucket:
        buckets = {args.bucket: buckets[args.bucket]}

    year = None
    if args.since_year or args.until_year:
        year = f"{args.since_year or ''}-{args.until_year or ''}"

    if args.dry:
        for b, qs in buckets.items():
            for q in qs:
                print(f"[{b}] {q}")
        return

    have = known_ids()
    seen = {}
    jobs = [(b, q) for b, qs in buckets.items() for q in qs]
    print(f"{len(jobs)} queries", file=sys.stderr)
    for i, (bucket, q) in enumerate(jobs):
        if i:
            time.sleep(3.1)  # shared pool etiquette without a key
        try:
            results = s2_search(q, args.max_per_query, year, args.min_citations, os.environ.get("S2_API_KEY"))
        except Exception as ex:
            print(f"! {bucket}: {ex}", file=sys.stderr)
            time.sleep(10)  # back off on 429s
            continue
        for p in results:
            key = p["arxiv_id"] or p["title"].lower()
            if (p["arxiv_id"] and p["arxiv_id"] in have) or key in seen:
                if key in seen:
                    seen[key]["matched"].append(bucket)
                continue
            p["matched"] = [bucket]
            seen[key] = p

    ranked = sorted(seen.values(), key=lambda p: (len(p["matched"]), p["citations"]), reverse=True)
    today = dt.date.today().isoformat()
    outdir = ROOT / "9 Claude files/Inbox" / "candidates"
    outdir.mkdir(parents=True, exist_ok=True)
    json_path = outdir / f"backfill-{today}.json"
    md_path = outdir / f"backfill-{today}.md"
    # Merge with any earlier run today so a rate-limited re-run never
    # clobbers candidates already found. Keyed by arxiv id, else title.
    if json_path.exists():
        try:
            prior = json.loads(json_path.read_text())
        except Exception:
            prior = []
        merged = {}
        for p in prior:
            merged[p["arxiv_id"] or p["title"].lower()] = p
        for p in ranked:
            key = p["arxiv_id"] or p["title"].lower()
            if key in merged:
                have_matched = set(merged[key]["matched"])
                merged[key]["matched"] = list(dict.fromkeys(merged[key]["matched"] + [m for m in p["matched"] if m not in have_matched]))
            else:
                merged[key] = p
        ranked = sorted(merged.values(), key=lambda p: (len(p["matched"]), p["citations"]), reverse=True)
    if not ranked and md_path.exists():
        print(f"0 new candidates and existing backfill-{today}.md kept (rate-limited run)")
        return
    json_path.write_text(json.dumps(ranked, indent=2))
    lines = [f"# S2 backfill candidates {today} ({len(ranked)} new, min {args.min_citations} citations)\n"]
    for p in ranked:
        lines.append(f"- **{p['title']}** — {', '.join(p['authors'][:3])}{' et al.' if len(p['authors']) > 3 else ''}"
                     f" · {p['published']} · {p['citations']} cites · [{p['arxiv_id'] or 'link'}]({p['url']})"
                     f" · matched: {', '.join(p['matched'])}")
    md_path.write_text("\n".join(lines) + "\n")
    print(f"{len(ranked)} backfill candidates → 9 Claude files/Inbox/candidates/backfill-{today}.md")


if __name__ == "__main__":
    main()
