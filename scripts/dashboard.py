#!/usr/bin/env python3
"""taste-lab dashboard: one page over the whole repo. No dependencies.

  python3 scripts/dashboard.py --serve          # open http://localhost:8765 and refresh to update
  python3 scripts/dashboard.py                  # just write dashboard.html
  python3 scripts/dashboard.py --due 2026-11-24 # set the deadline countdown

Reads: 01-papers (frontmatter: section, status, relevance), 02-concepts, 03-threads, 05-digests,
00-inbox/HANDOFF.md, 07-drafts/litreview/{outline,matrix,gaps}.md
"""
import argparse
import datetime as dt
import html
import http.server
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "dashboard.json"   # optional: {"due": "2026-11-24", "title": "...", "sections": {"2": "Foundations", ...}}

DEFAULT_SECTIONS = {
    "1": "Introduction", "2": "Foundations", "3": "Monitoring", "4": "Evaluation signals",
    "5": "Persistent control", "6": "Limits", "7": "Taste & open-endedness", "8": "Synthesis", "9": "Conclusion",
}
READ_STATES = {"read", "deep", "done"}


# ---------------- parsing ----------------
def split_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm_raw, body = text[3:end], text[end + 4:]
            fm = {}
            for line in fm_raw.splitlines():
                if ":" in line and not line.startswith(" "):
                    k, v = line.split(":", 1)
                    v = v.split(" #")[0].strip()
                    fm[k.strip()] = v.strip("'\"")
            return fm, body
    return {}, text


def section_of(body, name):
    """Text under a '## name' heading (case-insensitive prefix match)."""
    m = re.search(rf"^##\s+{re.escape(name)}[^\n]*\n(.*?)(?=^##\s|\Z)", body, re.M | re.S | re.I)
    if not m:
        return ""
    out = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S).strip()
    return out


def title_of(body, fallback):
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else fallback


def one_line(body):
    m = re.search(r"\*\*One line:\*\*\s*(.+)", body)
    return m.group(1).strip() if m else ""


def load_papers():
    papers = []
    for p in sorted((ROOT / "01-papers").glob("*.md")):
        fm, body = split_frontmatter(p.read_text(errors="ignore"))
        sec = str(fm.get("section", "")).strip() or "?"
        mine = section_of(body, "Harshit") or section_of(body, "My notes") or section_of(body, "My takeaway")
        papers.append({
            "file": p.stem,
            "title": title_of(body, p.stem),
            "oneline": one_line(body),
            "status": (fm.get("status") or "unread").lower(),
            "relevance": fm.get("relevance", ""),
            "section": sec,
            "tier": (fm.get("tier") or "").lower(),
            "year": fm.get("year", ""),
            "url": fm.get("url") or (f"https://arxiv.org/abs/{fm['arxiv']}" if re.match(r"\d{4}\.\d+", fm.get("arxiv", "")) else ""),
            "mine": mine,
            "body": body,
        })
    return papers


def read_md(rel):
    p = ROOT / rel
    return p.read_text(errors="ignore") if p.exists() else ""


def latest(folder, pattern="*.md"):
    files = sorted((ROOT / folder).glob(pattern)) if (ROOT / folder).exists() else []
    files = [f for f in files if not f.name.startswith(".")]
    return files[-1] if files else None


def last_handoff():
    t = read_md("00-inbox/HANDOFF.md")
    parts = re.split(r"(?=^## \d{4}-\d{2}-\d{2})", t, flags=re.M)
    entries = [x for x in parts if x.startswith("## ")]
    return entries[-1] if entries else ""


def drafts():
    out = []
    d = ROOT / "07-drafts" / "litreview"
    if d.exists():
        for f in sorted(d.glob("*.md")):
            if f.stem in {"outline", "matrix", "references", "gaps"} or f.stem.startswith("quiz"):
                continue
            _, body = split_frontmatter(f.read_text(errors="ignore"))
            words = len(re.findall(r"\b\w+\b", re.sub(r"[#*`>\-|]", " ", body)))
            out.append({"name": f.stem, "words": words, "body": body})
    return out


def threads():
    out = []
    for f in sorted((ROOT / "03-threads").glob("*.md")):
        fm, body = split_frontmatter(f.read_text(errors="ignore"))
        out.append({"name": title_of(body, f.stem), "status": fm.get("status", ""), "body": body})
    return out


# ---------------- tiny markdown → html ----------------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank">\1</a>', s)
    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: f'<a class="wl" data-note="{m.group(1)}">{m.group(2) or m.group(1)}</a>', s)
    return s


def md(text):
    lines, out, i = text.strip("\n").splitlines(), [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                buf.append(lines[j]); j += 1
            out.append("<pre><code>" + html.escape("\n".join(buf)) + "</code></pre>")
            i = j + 1; continue
        if ln.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows, j = [], i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")]); j += 1
            t = "<div class='tw'><table><thead><tr>" + "".join(f"<th>{inline(h)}</th>" for h in head) + "</tr></thead><tbody>"
            for r in rows:
                t += "<tr>" + "".join(f"<td>{inline(c) if c else '<span class=empty>·</span>'}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table></div>")
            i = j; continue
        m = re.match(r"^(#{1,4})\s+(.*)", ln)
        if m:
            lvl = min(len(m.group(1)) + 1, 5)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if re.match(r"^\s*([-*]|\d+\.)\s+", ln):
            tag = "ol" if re.match(r"^\s*\d+\.", ln) else "ul"
            items = []
            while i < len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                it = re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i])
                it = re.sub(r"^\[ \]\s*", "☐ ", it); it = re.sub(r"^\[x\]\s*", "☑ ", it, flags=re.I)
                items.append(f"<li>{inline(it)}</li>"); i += 1
            out.append(f"<{tag}>{''.join(items)}</{tag}>"); continue
        if ln.startswith(">"):
            out.append(f"<blockquote>{inline(ln.lstrip('> '))}</blockquote>"); i += 1; continue
        if ln.strip() in {"---", "***"}:
            out.append("<hr>"); i += 1; continue
        if ln.strip():
            para = [ln]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"^(#|\s*[-*]\s|\s*\d+\.\s|\||>|```)", lines[i + 1]):
                i += 1; para.append(lines[i])
            out.append(f"<p>{inline(' '.join(para))}</p>")
        i += 1
    return "\n".join(out)


# ---------------- page ----------------
def build(due=None):
    cfg = json.loads(CONFIG.read_text()) if CONFIG.exists() else {}
    due = due or cfg.get("due")
    sections = {**DEFAULT_SECTIONS, **cfg.get("sections", {})}
    title = cfg.get("title", "Metacognition in Reasoning Models — Literature Review")

    papers = load_papers()
    total = len(papers)
    done = [p for p in papers if p["status"] in READ_STATES]
    with_mine = [p for p in papers if p["mine"]]

    def sec_key(s):
        return (0, int(s)) if s.isdigit() else (1, s)

    by_sec = {}
    for p in papers:
        by_sec.setdefault(p["section"], []).append(p)
    ordered = sorted(by_sec, key=sec_key)

    nxt = next((p for s in ordered for p in sorted(by_sec[s], key=lambda x: (x["tier"] != "deep", x["file"]))
                if p["status"] not in READ_STATES), None)

    days_left = ""
    if due:
        try:
            d = (dt.date.fromisoformat(due) - dt.date.today()).days
            days_left = f"{d} day{'s' if d != 1 else ''} left" if d >= 0 else f"{-d} days overdue"
        except ValueError:
            pass

    dr = drafts()
    words = sum(d["words"] for d in dr)
    gaps_md = read_md("07-drafts/litreview/gaps.md") or read_md("03-threads/landscape-gap-table.md")
    matrix_md = read_md("07-drafts/litreview/matrix.md")
    outline_md = read_md("07-drafts/litreview/outline.md")
    dig = latest("05-digests")
    digest_md = dig.read_text(errors="ignore") if dig else ""
    handoff = last_handoff()
    th = threads()
    concepts = {f.stem: f.read_text(errors="ignore") for f in sorted((ROOT / "02-concepts").glob("*.md"))}

    # notes index for wikilink popups
    notes = {p["file"]: md(p["body"]) for p in papers}
    notes.update({k: md(split_frontmatter(v)[1]) for k, v in concepts.items()})

    # section progress rows
    sec_rows = ""
    for s in ordered:
        ps = by_sec[s]
        r = sum(1 for p in ps if p["status"] in READ_STATES)
        pct = int(100 * r / len(ps)) if ps else 0
        name = sections.get(s, "Unsorted" if s == "?" else f"Section {s}")
        sec_rows += (f"<div class='sec' data-sec='{s}'><div class='sec-name'><span class='num'>{html.escape(s)}</span>{html.escape(name)}</div>"
                     f"<div class='bar'><i style='width:{pct}%'></i></div><div class='sec-count'>{r}/{len(ps)}</div></div>")

    # paper cards
    cards = ""
    for s in ordered:
        name = sections.get(s, "Unsorted" if s == "?" else f"Section {s}")
        cards += f"<h3 class='group' data-sec='{s}'><span class='num'>{html.escape(s)}</span>{html.escape(name)}</h3><div class='cards' data-sec='{s}'>"
        for p in sorted(by_sec[s], key=lambda x: (x["tier"] != "deep", x["file"])):
            st = "read" if p["status"] in READ_STATES else p["status"]
            tier = f"<span class='pill {p['tier']}'>{p['tier']}</span>" if p["tier"] else ""
            rel = f"<span class='pill rel'>rel {p['relevance']}</span>" if p["relevance"] else ""
            link = f"<a href='{html.escape(p['url'])}' target='_blank' class='ext'>paper ↗</a>" if p["url"] else ""
            mine = (f"<div class='mine'><div class='lbl'>My takeaway</div>{md(p['mine'])}</div>" if p["mine"]
                    else "<div class='mine missing'><div class='lbl'>My takeaway</div>not written yet</div>")
            search = html.escape((p["title"] + " " + p["oneline"] + " " + p["mine"]).lower())
            cards += (f"<article class='card {st}' data-status='{st}' data-search='{search}'>"
                      f"<div class='meta'><span class='pill st-{st}'>{st}</span>{tier}{rel}<span class='yr'>{html.escape(p['year'])}</span>{link}</div>"
                      f"<h4><a class='wl' data-note='{p['file']}'>{html.escape(p['title'])}</a></h4>"
                      f"<p class='one'>{inline(p['oneline']) if p['oneline'] else '<span class=empty>no summary yet</span>'}</p>{mine}</article>")
        cards += "</div>"

    thread_rows = "".join(
        f"<div class='thread'><span class='pill st-{html.escape(t['status'])}'>{html.escape(t['status'] or '—')}</span>{html.escape(t['name'])}</div>"
        for t in th)
    draft_rows = "".join(f"<div class='draft'><span>{html.escape(d['name'])}</span><b>{d['words']:,}</b></div>" for d in dr) \
        or "<p class='empty'>No section drafts yet. Put them in 07-drafts/litreview/ (e.g. 03-monitoring.md).</p>"
    draft_bodies = "".join(f"<details><summary>{html.escape(d['name'])} · {d['words']:,} words</summary>{md(d['body'])}</details>" for d in dr)

    next_html = "<p class='empty'>Everything is read.</p>"
    if nxt:
        next_html = (f"<div class='next-title'><a class='wl' data-note='{nxt['file']}'>{html.escape(nxt['title'])}</a></div>"
                     f"<p>{inline(nxt['oneline'])}</p><p class='hint'>In Claude Code: <code>/next</code></p>")

    data = json.dumps(notes)
    now = dt.datetime.now().strftime("%a %d %b, %H:%M")
    pct_all = int(100 * len(done) / total) if total else 0

    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>taste-lab · dashboard</title>
<style>
:root{{--bg:#f6f4ef;--panel:#fffdf8;--ink:#1d1b18;--mute:#77716a;--line:#e4ded3;--acc:#b4532a;--acc2:#2f6b5e;--warn:#c08a1e;--soft:#efe9de}}
@media (prefers-color-scheme:dark){{:root{{--bg:#15140f;--panel:#1d1c17;--ink:#ece7dc;--mute:#9a9388;--line:#2f2d26;--acc:#e07a4c;--acc2:#6bb3a1;--warn:#d9a640;--soft:#26241e}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Inter,sans-serif}}
header{{padding:28px 32px 18px;border-bottom:1px solid var(--line);display:flex;gap:24px;align-items:flex-end;flex-wrap:wrap}}
h1{{font:600 22px/1.2 ui-serif,Georgia,serif;margin:0;letter-spacing:-.01em;flex:1;min-width:280px}}
.stat{{text-align:right}}.stat b{{display:block;font:600 22px/1 ui-serif,Georgia,serif}}.stat span{{color:var(--mute);font-size:12px;text-transform:uppercase;letter-spacing:.06em}}
.due b{{color:var(--acc)}}
nav{{display:flex;gap:4px;padding:10px 32px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:5;flex-wrap:wrap}}
nav button{{border:0;background:none;color:var(--mute);font:500 14px system-ui;padding:8px 12px;border-radius:8px;cursor:pointer}}
nav button.on{{background:var(--soft);color:var(--ink)}}nav .upd{{margin-left:auto;color:var(--mute);font-size:12px;align-self:center}}
main{{padding:24px 32px 80px;max-width:1280px}}.tab{{display:none}}.tab.on{{display:block}}
.grid{{display:grid;grid-template-columns:1.1fr 1fr;gap:20px}}@media(max-width:900px){{.grid{{grid-template-columns:1fr}}header,nav,main{{padding-left:16px;padding-right:16px}}}}
.panel{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 20px}}
.panel>h2{{font:600 12px system-ui;text-transform:uppercase;letter-spacing:.08em;color:var(--mute);margin:0 0 12px}}
.next{{border-left:4px solid var(--acc)}}.next-title{{font:600 19px/1.3 ui-serif,Georgia,serif;margin-bottom:6px}}
.hint{{color:var(--mute);font-size:13px}}
.sec{{display:grid;grid-template-columns:1fr 2fr 44px;gap:12px;align-items:center;padding:7px 0;border-bottom:1px dashed var(--line);cursor:pointer}}
.sec:last-child{{border:0}}.sec-name{{font-weight:500}}.sec-count{{text-align:right;color:var(--mute);font-variant-numeric:tabular-nums}}
.num{{display:inline-block;min-width:20px;color:var(--acc);font-weight:600;margin-right:6px}}
.bar{{height:8px;background:var(--soft);border-radius:99px;overflow:hidden}}.bar i{{display:block;height:100%;background:var(--acc2);border-radius:99px}}
.big-bar{{height:10px;margin:8px 0 4px}}
.draft,.thread{{display:flex;justify-content:space-between;gap:10px;padding:6px 0;border-bottom:1px dashed var(--line)}}.thread{{justify-content:flex-start}}
.tools{{display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap}}.tools input{{flex:1;min-width:220px;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--panel);color:var(--ink);font:inherit}}
.tools button{{border:1px solid var(--line);background:var(--panel);color:var(--ink);padding:8px 12px;border-radius:10px;cursor:pointer;font:inherit}}.tools button.on{{background:var(--ink);color:var(--bg)}}
h3.group{{font:600 17px ui-serif,Georgia,serif;margin:26px 0 10px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:14px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:8px}}
.card.read{{border-color:color-mix(in srgb,var(--acc2) 45%,var(--line))}}.card h4{{margin:0;font:600 15.5px/1.35 ui-serif,Georgia,serif}}
.card .one{{margin:0;color:var(--ink);font-size:14px}}.meta{{display:flex;gap:6px;align-items:center;flex-wrap:wrap;font-size:12px}}
.pill{{white-space:nowrap;flex-shrink:0;font-size:11px;padding:2px 8px;border-radius:99px;background:var(--soft);color:var(--mute);text-transform:lowercase}}
.pill.deep{{background:color-mix(in srgb,var(--acc) 18%,transparent);color:var(--acc)}}.st-read,.st-active,.st-answered{{background:color-mix(in srgb,var(--acc2) 20%,transparent)!important;color:var(--acc2)!important}}
.st-proposed{{color:var(--warn)!important}}.yr{{color:var(--mute)}}.ext{{margin-left:auto;color:var(--mute);font-size:12px}}
.mine{{background:var(--soft);border-radius:10px;padding:8px 10px;font-size:13.5px}}.mine p{{margin:.2em 0}}.mine.missing{{color:var(--mute);font-style:italic}}
.lbl{{font-size:10.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--acc);font-style:normal;margin-bottom:2px}}
a{{color:var(--acc2)}}a.wl{{cursor:pointer;text-decoration:none;color:inherit;border-bottom:1px dotted var(--mute)}}a.wl:hover{{color:var(--acc)}}
.doc{{max-width:900px}}.doc h2,.doc h3{{font-family:ui-serif,Georgia,serif}}.tw{{overflow-x:auto}}
table{{border-collapse:collapse;width:100%;font-size:13.5px;background:var(--panel)}}th,td{{border:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}}th{{background:var(--soft);font-weight:600}}
.empty{{color:var(--mute);font-style:italic}}code{{background:var(--soft);padding:1px 5px;border-radius:5px;font-size:.92em}}pre{{background:var(--soft);padding:12px;border-radius:10px;overflow:auto}}
blockquote{{border-left:3px solid var(--line);margin:8px 0;padding:2px 12px;color:var(--mute)}}details{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:10px 14px;margin-bottom:10px}}summary{{cursor:pointer;font-weight:600}}
#modal{{position:fixed;inset:0;background:rgba(0,0,0,.45);display:none;align-items:flex-start;justify-content:center;padding:5vh 16px;z-index:20}}#modal.on{{display:flex}}
#modal .box{{background:var(--panel);border-radius:16px;max-width:820px;width:100%;max-height:90vh;overflow:auto;padding:22px 26px;position:relative}}#modal .x{{position:sticky;top:0;float:right;border:0;background:var(--soft);color:var(--ink);border-radius:8px;padding:4px 10px;cursor:pointer}}
</style></head><body>
<header><h1>{html.escape(title)}</h1>
<div class="stat"><b>{len(done)}/{total}</b><span>papers read</span></div>
<div class="stat"><b>{len(with_mine)}</b><span>my takeaways</span></div>
<div class="stat"><b>{words:,}</b><span>words drafted</span></div>
{f'<div class="stat due"><b>{days_left}</b><span>due {html.escape(due)}</span></div>' if days_left else ''}
</header>
<nav><button class="on" data-t="home">Overview</button><button data-t="papers">Papers</button><button data-t="gaps">Gaps & patterns</button>
<button data-t="matrix">Matrix</button><button data-t="draft">My draft</button><button data-t="outline">Outline</button><button data-t="log">Digest & log</button>
<span class="upd">updated {now} · refresh to update</span></nav>
<main>
<section class="tab on" id="home"><div class="grid">
 <div style="display:flex;flex-direction:column;gap:20px">
  <div class="panel next"><h2>Read next</h2>{next_html}</div>
  <div class="panel"><h2>Progress by section · {pct_all}% overall</h2><div class="bar big-bar"><i style="width:{pct_all}%"></i></div>{sec_rows or "<p class=empty>No papers yet.</p>"}</div>
 </div>
 <div style="display:flex;flex-direction:column;gap:20px">
  <div class="panel"><h2>Gaps & patterns (latest)</h2><div class="doc">{md(gaps_md)[:6000] if gaps_md else "<p class=empty>Run /gaps in Claude Code after a few papers.</p>"}</div></div>
  <div class="panel"><h2>My draft</h2>{draft_rows}</div>
  <div class="panel"><h2>Research questions</h2>{thread_rows or "<p class=empty>none</p>"}</div>
 </div></div></section>
<section class="tab" id="papers"><div class="tools"><input id="q" placeholder="Search titles, summaries, my takeaways…">
<button class="f on" data-f="all">All</button><button class="f" data-f="unread">Unread</button><button class="f" data-f="read">Read</button><button class="f" data-f="nomine">No takeaway yet</button></div>{cards}</section>
<section class="tab" id="gaps"><div class="doc">{md(gaps_md) if gaps_md else "<p class=empty>No gaps file yet. Run /gaps in Claude Code; it saves to 07-drafts/litreview/gaps.md.</p>"}</div></section>
<section class="tab" id="matrix"><div class="doc" style="max-width:none">{md(matrix_md) if matrix_md else "<p class=empty>No matrix yet (07-drafts/litreview/matrix.md).</p>"}</div></section>
<section class="tab" id="draft"><div class="doc">{draft_bodies or "<p class=empty>No drafts yet.</p>"}</div></section>
<section class="tab" id="outline"><div class="doc">{md(outline_md) if outline_md else "<p class=empty>No outline yet.</p>"}</div></section>
<section class="tab" id="log"><div class="grid"><div class="panel doc"><h2>Latest digest</h2>{md(split_frontmatter(digest_md)[1]) if digest_md else "<p class=empty>none</p>"}</div>
<div class="panel doc"><h2>Last handoff</h2>{md(handoff) if handoff else "<p class=empty>none</p>"}</div></div></section>
</main>
<div id="modal"><div class="box"><button class="x">close ✕</button><div id="mbody" class="doc"></div></div></div>
<script>
const NOTES={data};
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
function show(t){{$$('nav button[data-t]').forEach(b=>b.classList.toggle('on',b.dataset.t===t));$$('.tab').forEach(x=>x.classList.toggle('on',x.id===t));try{{localStorage.setItem('tab',t)}}catch(e){{}}}}
$$('nav button[data-t]').forEach(b=>b.onclick=()=>show(b.dataset.t));
try{{const t=localStorage.getItem('tab');if(t&&document.getElementById(t))show(t)}}catch(e){{}}
document.addEventListener('click',e=>{{const a=e.target.closest('a.wl');if(!a)return;const n=a.dataset.note;
 $('#mbody').innerHTML=NOTES[n]||'<p class=empty>No note called "'+n+'" yet.</p>';$('#modal').classList.add('on')}});
$('#modal').onclick=e=>{{if(e.target.id==='modal'||e.target.classList.contains('x'))$('#modal').classList.remove('on')}};
document.addEventListener('keydown',e=>{{if(e.key==='Escape')$('#modal').classList.remove('on')}});
let F='all';function filt(){{const q=$('#q').value.toLowerCase();$$('.card').forEach(c=>{{const st=c.dataset.status,nm=c.querySelector('.mine.missing');
 let ok=F==='all'||(F==='read'&&st==='read')||(F==='unread'&&st!=='read')||(F==='nomine'&&nm);if(q&&!c.dataset.search.includes(q))ok=false;c.style.display=ok?'':'none'}});
 $$('.cards').forEach(g=>{{const vis=[...g.children].some(c=>c.style.display!=='none');g.style.display=vis?'':'none';const h=document.querySelector('h3.group[data-sec="'+g.dataset.sec+'"]');if(h)h.style.display=vis?'':'none'}})}}
$('#q').oninput=filt;$$('.f').forEach(b=>b.onclick=()=>{{F=b.dataset.f;$$('.f').forEach(x=>x.classList.toggle('on',x===b));filt()}});
$$('.sec').forEach(s=>s.onclick=()=>{{show('papers');const h=document.querySelector('h3.group[data-sec="'+s.dataset.sec+'"]');if(h)h.scrollIntoView({{behavior:'smooth'}})}});
</script></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--due")
    args = ap.parse_args()

    if not args.serve:
        (ROOT / "dashboard.html").write_text(build(args.due))
        print(f"wrote {ROOT / 'dashboard.html'}")
        return

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path not in ("/", "/index.html"):
                self.send_response(404); self.end_headers(); return
            body = build(args.due).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    print(f"dashboard → http://localhost:{args.port}  (refresh the page to update · Ctrl+C to stop)")
    http.server.HTTPServer(("127.0.0.1", args.port), H).serve_forever()


if __name__ == "__main__":
    main()
