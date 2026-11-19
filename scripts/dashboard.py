#!/usr/bin/env python3
"""taste-lab dashboard: one page over the whole repo. No dependencies.

  python3 scripts/dashboard.py --serve          # open http://localhost:8765; the page updates itself
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
import math
import os
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


def as_list(v):
    """'[a, b]' or 'a, b' from frontmatter -> ['a', 'b']."""
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    return [x.strip().strip("'\"") for x in v.split(",") if x.strip()]


def heading_flag(body, name):
    """The tag after a heading, e.g. 'main threat' from '## Relevance to taste-lab: **main threat**'."""
    m = re.search(rf"^##\s+{re.escape(name)}[^\n:]*:\s*(.+)$", body, re.M | re.I)
    return m.group(1).strip().strip("*").strip() if m else ""


def drop_sections(body, names):
    for n in names:
        body = re.sub(rf"^##\s+{re.escape(n)}[^\n]*\n?.*?(?=^##\s|\Z)", "", body, flags=re.M | re.S | re.I)
    return body


def first_item(text):
    """First non-empty line of a section, without list or checkbox markers."""
    for line in text.splitlines():
        line = re.sub(r"^\s*([-*]|\d+\.)\s+", "", line)
        line = re.sub(r"^\[[ xX]\]\s*", "", line).strip()
        if line:
            return line
    return ""


def load_papers():
    papers = []
    for p in sorted((ROOT / "01-papers").glob("*.md")):
        fm, body = split_frontmatter(p.read_text(errors="ignore"))
        sec = str(fm.get("section", "")).strip() or "?"
        mine = section_of(body, "Harshit") or section_of(body, "My notes") or section_of(body, "My takeaway")
        papers.append({
            "why": section_of(body, "Relevance"),
            "flag": heading_flag(body, "Relevance"),
            "tests": as_list(fm.get("tests")),
            "components": as_list(fm.get("components")),
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
    """Active threads first, then by T-number."""
    out = []
    for f in (ROOT / "03-threads").glob("*.md"):
        fm, body = split_frontmatter(f.read_text(errors="ignore"))
        status = fm.get("status", "")
        m = re.search(r"-T(\d+)$", f.stem)
        out.append({"file": f.stem, "name": title_of(body, f.stem), "status": status, "body": body,
                    "next": first_item(section_of(body, "Next action")),
                    "rank": (status != "active", int(m.group(1)) if m else 99, f.stem)})
    return sorted(out, key=lambda t: t["rank"])


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
TESTS = ["divergent", "stable", "grounded", "self-reinforcing"]
COMPONENTS = ["valence", "monitoring", "controller", "consolidation", "anchor"]


def fingerprint():
    """Changes whenever a note or config file changes. The served page polls it and reloads itself."""
    n, newest = 0, 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "__pycache__"]
        for f in filenames:
            if f.endswith((".md", ".json")):
                n += 1
                newest = max(newest, os.stat(os.path.join(dirpath, f)).st_mtime_ns)
    return f"{n}-{newest}"


def esc(s):
    return html.escape(str(s), quote=True)


def shorten(text, limit=260):
    """First paragraph of a section on one line, cut at a sentence end near the limit."""
    para = re.split(r"\n\s*\n", text.strip(), maxsplit=1)[0]
    para = " ".join(re.sub(r"^\s*([-*]|\d+\.)\s+", "", l).strip() for l in para.splitlines())
    if len(para) > limit:
        cut = para.rfind(". ", 0, limit)
        para = para[:cut + 1] if cut > limit // 2 else para[:limit].rsplit(" ", 1)[0] + "…"
    if para.count("**") % 2:
        para = para.replace("**", "")
    return para


def is_read(p):
    return p["status"] in READ_STATES


def pills(p, sections, with_section=False):
    st = "read" if is_read(p) else p["status"]
    out = f"<span class='pill st-{esc(st)}'>{esc(st)}</span>"
    if p["tier"]:
        out += f"<span class='pill {esc(p['tier'])}'>{esc(p['tier'])}</span>"
    if with_section:
        out += f"<span class='pill'>§{esc(p['section'])} {esc(sections.get(p['section'], 'unsorted'))}</span>"
    if p["relevance"]:
        out += f"<span class='pill rel'>rel {esc(p['relevance'])}</span>"
    if p["year"]:
        out += f"<span class='yr'>{esc(p['year'])}</span>"
    if p["url"].startswith("http"):
        out += f"<a href='{esc(p['url'])}' target='_blank' class='ext'>paper ↗</a>"
    return out


def why_box(p, short=True):
    if not p["why"]:
        return ""
    flag = f"<span class='flag'>{inline(p['flag'])}</span>" if p["flag"] else ""
    body = f"<p>{inline(shorten(p['why']))}</p>" if short else md(p["why"])
    return f"<div class='why'><div class='lbl'>Why it matters to us{flag}</div>{body}</div>"


def chips(p):
    items = [f"<span class='chip t'>{esc(t)}</span>" for t in p["tests"]]
    items += [f"<span class='chip'>{esc(c)}</span>" for c in p["components"]]
    return f"<div class='chips'>{''.join(items)}</div>" if items else ""


def mine_box(p, reader=False):
    if p["mine"]:
        return f"<div class='mine'><div class='lbl'>My takeaway</div>{md(p['mine'])}</div>"
    hint = " When you finish, run <code>/next done &lt;takeaway&gt;</code> in Claude Code." if reader else ""
    return f"<div class='mine missing'><div class='lbl'>My takeaway</div>not written yet.{hint}</div>"


def reader(p, sections):
    """Full paper view: summary and why-it-matters first, details after, my takeaway last."""
    rest = re.sub(r"^#\s+[^\n]*\n?", "", p["body"], count=1, flags=re.M)
    rest = re.sub(r"^\*\*One line:\*\*[^\n]*\n?", "", rest, count=1, flags=re.M)
    rest = drop_sections(rest, ["Relevance", "Harshit", "My notes", "My takeaway"])
    one = f"<p class='rone'>{inline(p['oneline'])}</p>" if p["oneline"] else ""
    return (f"<div class='meta'>{pills(p, sections, True)}</div><h2 class='rtitle'>{esc(p['title'])}</h2>{one}"
            f"{why_box(p, short=False)}{chips(p)}{md(rest)}{mine_box(p, reader=True)}")


CSS = """
:root{--bg:#f6f4ef;--panel:#fffdf8;--ink:#1d1b18;--mute:#77716a;--line:#e4ded3;--acc:#b4532a;--acc2:#2f6b5e;--warn:#c08a1e;--soft:#efe9de}
@media (prefers-color-scheme:dark){:root{--bg:#15140f;--panel:#1d1c17;--ink:#ece7dc;--mute:#9a9388;--line:#2f2d26;--acc:#e07a4c;--acc2:#6bb3a1;--warn:#d9a640;--soft:#26241e}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Inter,sans-serif}
header{padding:28px 32px 18px;border-bottom:1px solid var(--line);display:flex;gap:24px;align-items:flex-end;flex-wrap:wrap}
h1{font:600 22px/1.2 ui-serif,Georgia,serif;margin:0;letter-spacing:-.01em;flex:1;min-width:280px}
.stat{text-align:right}.stat b{display:block;font:600 22px/1 ui-serif,Georgia,serif}.stat span{color:var(--mute);font-size:12px;text-transform:uppercase;letter-spacing:.06em}
.due b{color:var(--acc)}
nav{display:flex;gap:4px;padding:10px 32px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:5;flex-wrap:wrap}
nav button{border:0;background:none;color:var(--mute);font:500 14px system-ui;padding:8px 12px;border-radius:8px;cursor:pointer}
nav button.on{background:var(--soft);color:var(--ink)}nav .upd{margin-left:auto;color:var(--mute);font-size:12px;align-self:center}
main{padding:24px 32px 80px;max-width:1280px}.tab{display:none}.tab.on{display:block}
.grid{display:grid;grid-template-columns:1.1fr 1fr;gap:20px}@media(max-width:900px){.grid{grid-template-columns:1fr}header,nav,main{padding-left:16px;padding-right:16px}}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 20px}
.panel>h2{font:600 12px system-ui;text-transform:uppercase;letter-spacing:.08em;color:var(--mute);margin:0 0 12px}
.next{border-left:4px solid var(--acc)}.next-title{font:600 19px/1.3 ui-serif,Georgia,serif;margin:6px 0 4px}
.hint{color:var(--mute);font-size:13px}.pace{margin:0 0 12px;color:var(--mute);font-size:13.5px}
.first>p{margin:.2em 0 .7em}
.queue{margin:6px 0 0;padding-left:20px}.queue li{margin:7px 0}.q1{color:var(--mute);font-size:13px}
.sec{display:grid;grid-template-columns:minmax(0,1.5fr) 1.5fr 52px;gap:12px;align-items:center;padding:7px 0;border-bottom:1px dashed var(--line);cursor:pointer}
.sec:last-child{border:0}.sec.nil{opacity:.5;cursor:default}.sec-name{font-weight:500}
.sec-name small{display:block;color:var(--mute);font-weight:400;font-size:12px;margin-left:26px}
.sec-count{text-align:right;color:var(--mute);font-variant-numeric:tabular-nums;font-size:13px}
@media(max-width:600px){.sec{grid-template-columns:minmax(0,2fr) 1fr 44px}}
.num{display:inline-block;min-width:20px;color:var(--acc);font-weight:600;margin-right:6px}
.bar{height:8px;background:var(--soft);border-radius:99px;overflow:hidden}.bar i{display:block;height:100%;background:var(--acc2);border-radius:99px}
.big-bar{height:10px;margin:8px 0 4px}
.draft{display:flex;justify-content:space-between;gap:10px;padding:6px 0;border-bottom:1px dashed var(--line)}
.thread{padding:9px 0;border-bottom:1px dashed var(--line)}.thread:last-child,.draft:last-child{border:0}.thread .pill{margin-right:8px}
.tnext{color:var(--mute);font-size:13px;margin-top:3px}.tnext .lbl{display:inline;margin-right:6px}
.more{margin-top:10px;border:1px solid var(--line);background:var(--soft);color:var(--ink);padding:6px 12px;border-radius:8px;cursor:pointer;font:inherit;font-size:13px}
.tools{display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap}.tools input{flex:1;min-width:220px;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--panel);color:var(--ink);font:inherit}
.tools button{border:1px solid var(--line);background:var(--panel);color:var(--ink);padding:8px 12px;border-radius:10px;cursor:pointer;font:inherit}.tools button.on{background:var(--ink);color:var(--bg)}
h3.group{font:600 17px ui-serif,Georgia,serif;margin:26px 0 10px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;cursor:pointer}
.card:hover{border-color:var(--mute)}.card.read{border-color:color-mix(in srgb,var(--acc2) 45%,var(--line))}
.card h4{margin:0;font:600 15.5px/1.35 ui-serif,Georgia,serif}
.card .one{margin:0;color:var(--ink);font-size:14px}.meta{display:flex;gap:6px;align-items:center;flex-wrap:wrap;font-size:12px}
.pill{white-space:nowrap;flex-shrink:0;font-size:11px;padding:2px 8px;border-radius:99px;background:var(--soft);color:var(--mute);text-transform:lowercase}
.pill.deep{background:color-mix(in srgb,var(--acc) 18%,transparent);color:var(--acc)}.st-read,.st-active,.st-answered{background:color-mix(in srgb,var(--acc2) 20%,transparent)!important;color:var(--acc2)!important}
.st-proposed{color:var(--warn)!important}.yr{color:var(--mute)}.ext{margin-left:auto;color:var(--mute);font-size:12px}
.why{border-left:3px solid var(--acc);background:color-mix(in srgb,var(--acc) 6%,transparent);border-radius:0 10px 10px 0;padding:7px 10px;font-size:13.5px}.why p{margin:.15em 0}
.flag{display:inline-block;margin-left:8px;padding:0 7px;border-radius:99px;background:var(--acc);color:var(--panel);text-transform:none;letter-spacing:0;font-size:10.5px;font-style:normal}
.chips{display:flex;gap:4px;flex-wrap:wrap}.chip{font-size:10.5px;padding:1px 7px;border:1px solid var(--line);border-radius:99px;color:var(--mute)}
.chip.t{border-color:color-mix(in srgb,var(--acc2) 50%,var(--line));color:var(--acc2)}
.mine{background:var(--soft);border-radius:10px;padding:8px 10px;font-size:13.5px}.mine p{margin:.2em 0}.mine.missing{color:var(--mute);font-style:italic}
.lbl{font-size:10.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--acc);font-style:normal;margin-bottom:2px}
a{color:var(--acc2)}a.wl{cursor:pointer;text-decoration:none;color:inherit;border-bottom:1px dotted var(--mute)}a.wl:hover{color:var(--acc)}
.doc{max-width:900px}.doc h2,.doc h3{font-family:ui-serif,Georgia,serif}.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:13.5px;background:var(--panel)}th,td{border:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}th{background:var(--soft);font-weight:600}
.mx th.c,.mx td.c{text-align:center;white-space:nowrap}.mx th.grp{text-align:center}.mx tbody td.c{color:var(--acc2);font-size:18px;line-height:1.2}
.mx td .pill{margin-left:6px}.mx tfoot td{font-weight:600;background:var(--soft)}.mx tfoot td.zero{color:var(--acc)}
.empty{color:var(--mute);font-style:italic}code{background:var(--soft);padding:1px 5px;border-radius:5px;font-size:.92em}pre{background:var(--soft);padding:12px;border-radius:10px;overflow:auto}
blockquote{border-left:3px solid var(--line);margin:8px 0;padding:2px 12px;color:var(--mute)}details{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:10px 14px;margin-bottom:10px}summary{cursor:pointer;font-weight:600}
#modal{position:fixed;inset:0;background:rgba(0,0,0,.45);display:none;align-items:flex-start;justify-content:center;padding:4vh 16px;z-index:20}#modal.on{display:flex}
#modal .box{background:var(--panel);border-radius:16px;max-width:820px;width:100%;max-height:92vh;overflow:auto;padding:0 28px 26px}
.mbar{position:sticky;top:0;z-index:2;display:flex;gap:6px;align-items:center;background:var(--panel);padding:12px 0;border-bottom:1px solid var(--line);margin-bottom:6px}
.mbar button{border:1px solid var(--line);background:var(--soft);color:var(--ink);border-radius:8px;padding:4px 10px;cursor:pointer;font:inherit;font-size:13px}
.mbar button:disabled{opacity:.4;cursor:default}.mbar .sp{flex:1}#mpos{color:var(--mute);font-size:12.5px;padding:0 4px}
.rtitle{font:600 23px/1.25 ui-serif,Georgia,serif;margin:12px 0 6px}.rone{font:17px/1.5 ui-serif,Georgia,serif;margin:0 0 14px}
#mbody .why{font-size:14.5px;margin-bottom:10px}#mbody .mine{margin-top:18px;font-size:14.5px}
[hidden]{display:none!important}
"""

JS = """
const NOTES=__NOTES__, ORDER=__ORDER__, FP=__FP__;
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const store={get(k){try{return sessionStorage.getItem(k)}catch(e){return null}},set(k,v){try{sessionStorage.setItem(k,v)}catch(e){}},del(k){try{sessionStorage.removeItem(k)}catch(e){}}};
function show(t){$$('nav button[data-t]').forEach(b=>b.classList.toggle('on',b.dataset.t===t));$$('.tab').forEach(x=>x.classList.toggle('on',x.id===t));try{localStorage.setItem('tab',t)}catch(e){}}
$$('nav button[data-t]').forEach(b=>b.onclick=()=>show(b.dataset.t));
try{const t=localStorage.getItem('tab');if(t&&document.getElementById(t))show(t)}catch(e){}

// reader: open any note; papers can be flipped through in reading order
let cur=null,stack=[];
function render(){
  const i=ORDER.indexOf(cur),b=$('#mbody');
  if(NOTES[cur]!==undefined){b.innerHTML=NOTES[cur]}else{b.textContent='';const p=document.createElement('p');p.className='empty';p.textContent='No note called "'+cur+'" yet.';b.append(p)}
  $('#mback').hidden=!stack.length;
  $('#mprev').hidden=$('#mnext').hidden=$('#mpos').hidden=i<0;
  if(i>=0){$('#mpos').textContent='paper '+(i+1)+' of '+ORDER.length;$('#mprev').disabled=i===0;$('#mnext').disabled=i===ORDER.length-1}
  $('#modal').classList.add('on');$('#modal .box').scrollTop=0;document.body.style.overflow='hidden';store.set('note',cur);
}
function openNote(n){if(cur&&cur!==n)stack.push(cur);cur=n;render()}
function step(d){const j=ORDER.indexOf(cur)+d;if(ORDER.indexOf(cur)<0||j<0||j>=ORDER.length)return;cur=ORDER[j];render()}
function closeM(){$('#modal').classList.remove('on');cur=null;stack=[];document.body.style.overflow='';store.del('note')}
$('#mback').onclick=()=>{cur=stack.pop();render()};
$('#mprev').onclick=()=>step(-1);$('#mnext').onclick=()=>step(1);$('#mclose').onclick=closeM;
document.addEventListener('click',e=>{
  const go=e.target.closest('[data-go]');if(go){show(go.dataset.go);window.scrollTo(0,0);return}
  const a=e.target.closest('a.wl');if(a){e.preventDefault();openNote(a.dataset.note);return}
  const c=e.target.closest('article.card');if(c&&!e.target.closest('a'))openNote(c.dataset.note);
});
$('#modal').onclick=e=>{if(e.target.id==='modal')closeM()};
document.addEventListener('keydown',e=>{if(!$('#modal').classList.contains('on'))return;
  if(e.key==='Escape')closeM();else if(e.key==='ArrowRight')step(1);else if(e.key==='ArrowLeft')step(-1)});

// paper filters
let F='all';function filt(){const q=$('#q').value.toLowerCase();$$('.card').forEach(c=>{const st=c.dataset.status,nm=c.querySelector('.mine.missing');
 let ok=F==='all'||(F==='read'&&st==='read')||(F==='unread'&&st!=='read')||(F==='nomine'&&nm);if(q&&!c.dataset.search.includes(q))ok=false;c.style.display=ok?'':'none'});
 $$('.cards').forEach(g=>{const vis=[...g.children].some(c=>c.style.display!=='none');g.style.display=vis?'':'none';const h=document.querySelector('h3.group[data-sec="'+g.dataset.sec+'"]');if(h)h.style.display=vis?'':'none'})}
$('#q').oninput=filt;$$('.f').forEach(b=>b.onclick=()=>{F=b.dataset.f;$$('.f').forEach(x=>x.classList.toggle('on',x===b));filt()});
$$('.sec').forEach(s=>s.onclick=()=>{const h=document.querySelector('h3.group[data-sec="'+s.dataset.sec+'"]');if(!h)return;show('papers');h.scrollIntoView({behavior:'smooth'})});

// keep your place across reloads, and reload by itself when notes change (only when served)
{const y=store.get('y');if(y!==null){window.scrollTo(0,+y);store.del('y')}
 const n=store.get('note');if(n){cur=n;render();const my=store.get('my');if(my!==null){$('#modal .box').scrollTop=+my;store.del('my')}}}
if(location.protocol.startsWith('http')){
  $('#live').textContent='live · updates itself when notes change';
  setInterval(async()=>{try{const r=await fetch('/v',{cache:'no-store'});
    if(r.ok&&(await r.text())!==FP){store.set('y',scrollY);store.set('my',$('#modal .box').scrollTop);location.reload()}}catch(e){}},2000);
}
"""


def build(due=None):
    cfg = json.loads(CONFIG.read_text()) if CONFIG.exists() else {}
    due = due or cfg.get("due")
    sections = {**DEFAULT_SECTIONS, **cfg.get("sections", {})}
    title = cfg.get("title", "Metacognition in Reasoning Models — Literature Review")
    fp = fingerprint()

    papers = load_papers()
    total = len(papers)
    done = [p for p in papers if is_read(p)]
    with_mine = [p for p in papers if p["mine"]]

    def sec_key(s):
        return (0, int(s)) if s.isdigit() else (1, s)

    def sec_name(s):
        return sections.get(s, "Unsorted" if s == "?" else f"Section {s}")

    by_sec = {}
    for p in papers:
        by_sec.setdefault(p["section"], []).append(p)
    for ps in by_sec.values():
        ps.sort(key=lambda x: (x["tier"] != "deep", x["file"]))
    ordered = sorted(set(by_sec) | set(sections), key=sec_key)   # every section, even ones with no papers yet
    order = [p for s in ordered for p in by_sec.get(s, [])]      # reading order: section, deep before skim, file name
    unread = [p for p in order if not is_read(p)]

    days, days_left = None, ""
    if due:
        try:
            days = (dt.date.fromisoformat(due) - dt.date.today()).days
            days_left = f"{days} day{'s' if days != 1 else ''} left" if days >= 0 else f"{-days} days overdue"
        except ValueError:
            pass

    # today: the next paper plus enough others to finish reading by the due date
    if not unread:
        today_html = "<p class='empty'>Everything is read.</p>"
    else:
        if days is None:
            per_day = min(3, len(unread))
        elif days <= 0:
            per_day = len(unread)
        else:
            per_day = math.ceil(len(unread) / days)
        first, rest = unread[0], unread[1:per_day]
        pace = f"{len(unread)} unread"
        if days and days > 0:
            pace += f" · {days_left} · about {per_day} a day keeps you on pace"
        elif days_left:
            pace += f" · {days_left}"
        today_html = (f"<p class='pace'>{esc(pace)}</p><div class='first'><div class='meta'>{pills(first, sections, True)}</div>"
                      f"<div class='next-title'><a class='wl' data-note='{esc(first['file'])}'>{esc(first['title'])}</a></div>"
                      f"<p>{inline(first['oneline'])}</p>{why_box(first)}</div>")
        if rest:
            today_html += "<div class='lbl' style='margin-top:14px'>Also today</div><ol class='queue'>" + "".join(
                f"<li><a class='wl' data-note='{esc(p['file'])}'>{esc(p['title'])}</a>"
                + (f" <span class='pill {esc(p['tier'])}'>{esc(p['tier'])}</span>" if p["tier"] else "")
                + f"<div class='q1'>{inline(p['oneline'])}</div></li>" for p in rest) + "</ol>"
        today_html += "<p class='hint'>In Claude Code: <code>/next</code> for a briefing, then <code>/next done &lt;takeaway&gt;</code> when you finish.</p>"

    dr = drafts()
    words = sum(d["words"] for d in dr)
    words_by_sec = {}
    for d in dr:
        m = re.match(r"0*(\d+)", d["name"])
        if m:
            words_by_sec[m.group(1)] = words_by_sec.get(m.group(1), 0) + d["words"]

    gaps_md = read_md("07-drafts/litreview/gaps.md") or split_frontmatter(read_md("03-threads/landscape-gap-table.md"))[1]
    matrix_md = read_md("07-drafts/litreview/matrix.md")
    outline_md = read_md("07-drafts/litreview/outline.md")
    dig = latest("05-digests")
    digest_md = dig.read_text(errors="ignore") if dig else ""
    handoff = last_handoff()
    th = threads()
    concepts = {f.stem: f.read_text(errors="ignore") for f in sorted((ROOT / "02-concepts").glob("*.md"))}

    # notes index for the reader: papers, concepts and threads
    notes = {p["file"]: reader(p, sections) for p in papers}
    notes.update({k: md(split_frontmatter(v)[1]) for k, v in concepts.items()})
    notes.update({t["file"]: f"<div class='meta'><span class='pill st-{esc(t['status'])}'>{esc(t['status'] or 'none')}</span></div>{md(t['body'])}"
                  for t in th})

    # section progress rows, including sections with nothing in them yet
    sec_rows = ""
    for s in ordered:
        ps = by_sec.get(s, [])
        r = sum(1 for p in ps if is_read(p))
        pct = int(100 * r / len(ps)) if ps else 0
        w = words_by_sec.get(s)
        sub = f"<small>{w:,} words drafted</small>" if w else ""
        sec_rows += (f"<div class='sec{'' if ps else ' nil'}' data-sec='{esc(s)}'><div class='sec-name'><span class='num'>{esc(s)}</span>{esc(sec_name(s))}{sub}</div>"
                     f"<div class='bar'><i style='width:{pct}%'></i></div><div class='sec-count'>{f'{r}/{len(ps)}' if ps else 'none'}</div></div>")

    # paper cards
    cards = ""
    for s in ordered:
        if s not in by_sec:
            continue
        cards += f"<h3 class='group' data-sec='{esc(s)}'><span class='num'>{esc(s)}</span>{esc(sec_name(s))}</h3><div class='cards' data-sec='{esc(s)}'>"
        for p in by_sec[s]:
            st = "read" if is_read(p) else p["status"]
            search = esc(" ".join([p["title"], p["oneline"], p["why"], p["mine"]]).lower())
            cards += (f"<article class='card {esc(st)}' data-note='{esc(p['file'])}' data-status='{esc(st)}' data-search='{search}'>"
                      f"<div class='meta'>{pills(p, sections)}</div>"
                      f"<h4><a class='wl' data-note='{esc(p['file'])}'>{esc(p['title'])}</a></h4>"
                      f"<p class='one'>{inline(p['oneline']) if p['oneline'] else '<span class=empty>no summary yet</span>'}</p>"
                      f"{why_box(p)}{mine_box(p)}{chips(p)}</article>")
        cards += "</div>"

    # coverage matrix from frontmatter: a 0 in the bottom row is a hole in the reading list
    tests = TESTS + sorted({t for p in papers for t in p["tests"]} - set(TESTS))
    comps = COMPONENTS + sorted({c for p in papers for c in p["components"]} - set(COMPONENTS))
    mx_head = (f"<tr><th rowspan=2>Paper</th><th rowspan=2 class='c'>§</th><th colspan={len(tests)} class='grp'>Four tests</th>"
               f"<th colspan={len(comps)} class='grp'>Architecture</th></tr><tr>" + "".join(f"<th class='c'>{esc(x)}</th>" for x in tests + comps) + "</tr>")
    mx_body = ""
    for p in order:
        st = "read" if is_read(p) else p["status"]
        cells = "".join(f"<td class='c'>{'●' if x in p['tests'] else ''}</td>" for x in tests)
        cells += "".join(f"<td class='c'>{'●' if x in p['components'] else ''}</td>" for x in comps)
        mx_body += (f"<tr><td><a class='wl' data-note='{esc(p['file'])}'>{esc(p['title'])}</a><span class='pill st-{esc(st)}'>{esc(st)}</span></td>"
                    f"<td class='c'>{esc(p['section'])}</td>{cells}</tr>")
    counts = [sum(x in p["tests"] for p in papers) for x in tests] + [sum(x in p["components"] for p in papers) for x in comps]
    mx_foot = "<tr><td>Papers covering it</td><td></td>" + "".join(f"<td class='c{' zero' if n == 0 else ''}'>{n}</td>" for n in counts) + "</tr>"
    matrix_html = (f"<p class='hint'>Built from each paper's <code>tests</code> and <code>components</code>. A 0 in the bottom row means no paper covers it yet.</p>"
                   f"<div class='tw'><table class='mx'><thead>{mx_head}</thead><tbody>{mx_body}</tbody><tfoot>{mx_foot}</tfoot></table></div>"
                   + (f"<h2>My matrix</h2>{md(matrix_md)}" if matrix_md else ""))

    thread_rows = "".join(
        f"<div class='thread'><span class='pill st-{esc(t['status'])}'>{esc(t['status'] or 'none')}</span>"
        f"<a class='wl' data-note='{esc(t['file'])}'>{esc(t['name'])}</a>"
        + (f"<div class='tnext'><span class='lbl'>Next</span>{inline(t['next'])}</div>" if t["next"] else "") + "</div>"
        for t in th)
    draft_rows = "".join(f"<div class='draft'><span>{esc(d['name'])}</span><b>{d['words']:,}</b></div>" for d in dr) \
        or "<p class='empty'>No section drafts yet. Put them in 07-drafts/litreview/ (e.g. 03-monitoring.md).</p>"
    draft_bodies = "".join(f"<details><summary>{esc(d['name'])} · {d['words']:,} words</summary>{md(d['body'])}</details>" for d in dr)

    # overview shows only the top of gaps.md (the gap table); the full file is on its own tab
    gaps_parts = re.split(r"(?=^## )", gaps_md, flags=re.M) if gaps_md else []
    gaps_preview = (md("".join(gaps_parts[:2])) + ("<button class='more' data-go='gaps'>See all gaps & patterns</button>" if len(gaps_parts) > 2 else "")
                    if gaps_md else "<p class=empty>Run /gaps in Claude Code after a few papers.</p>")

    js = (JS.replace("__NOTES__", json.dumps(notes).replace("</", "<\\/"))
            .replace("__ORDER__", json.dumps([p["file"] for p in order]))
            .replace("__FP__", json.dumps(fp)))
    now = dt.datetime.now().strftime("%a %d %b, %H:%M")
    pct_all = int(100 * len(done) / total) if total else 0

    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>taste-lab · dashboard</title>
<style>{CSS}</style></head><body>
<header><h1>{esc(title)}</h1>
<div class="stat"><b>{len(done)}/{total}</b><span>papers read</span></div>
<div class="stat"><b>{len(with_mine)}</b><span>my takeaways</span></div>
<div class="stat"><b>{words:,}</b><span>words drafted</span></div>
{f'<div class="stat due"><b>{days_left}</b><span>due {esc(due)}</span></div>' if days_left else ''}
</header>
<nav><button class="on" data-t="home">Overview</button><button data-t="papers">Papers</button><button data-t="gaps">Gaps & patterns</button>
<button data-t="matrix">Matrix</button><button data-t="draft">My draft</button><button data-t="outline">Outline</button><button data-t="log">Digest & log</button>
<span class="upd" id="live">updated {now} · refresh to update</span></nav>
<main>
<section class="tab on" id="home"><div class="grid">
 <div style="display:flex;flex-direction:column;gap:20px">
  <div class="panel next"><h2>Today</h2>{today_html}</div>
  <div class="panel"><h2>Progress by section · {pct_all}% overall</h2><div class="bar big-bar"><i style="width:{pct_all}%"></i></div>{sec_rows}</div>
 </div>
 <div style="display:flex;flex-direction:column;gap:20px">
  <div class="panel"><h2>Gaps & patterns (latest)</h2><div class="doc">{gaps_preview}</div></div>
  <div class="panel"><h2>Research questions</h2>{thread_rows or "<p class=empty>none</p>"}</div>
  <div class="panel"><h2>My draft</h2>{draft_rows}</div>
 </div></div></section>
<section class="tab" id="papers"><div class="tools"><input id="q" placeholder="Search titles, summaries, why it matters, my takeaways…">
<button class="f on" data-f="all">All</button><button class="f" data-f="unread">Unread</button><button class="f" data-f="read">Read</button><button class="f" data-f="nomine">No takeaway yet</button></div>{cards}</section>
<section class="tab" id="gaps"><div class="doc">{md(gaps_md) if gaps_md else "<p class=empty>No gaps file yet. Run /gaps in Claude Code; it saves to 07-drafts/litreview/gaps.md.</p>"}</div></section>
<section class="tab" id="matrix"><div class="doc" style="max-width:none">{matrix_html}</div></section>
<section class="tab" id="draft"><div class="doc">{draft_bodies or "<p class=empty>No drafts yet.</p>"}</div></section>
<section class="tab" id="outline"><div class="doc">{md(outline_md) if outline_md else "<p class=empty>No outline yet.</p>"}</div></section>
<section class="tab" id="log"><div class="grid"><div class="panel doc"><h2>Latest digest</h2>{md(split_frontmatter(digest_md)[1]) if digest_md else "<p class=empty>none</p>"}</div>
<div class="panel doc"><h2>Last handoff</h2>{md(handoff) if handoff else "<p class=empty>none</p>"}</div></div></section>
</main>
<div id="modal"><div class="box"><div class="mbar"><button id="mback" hidden>← Back</button><button id="mprev">‹ Prev</button><span id="mpos"></span>
<button id="mnext">Next ›</button><span class="sp"></span><button id="mclose">Close ✕</button></div><div id="mbody" class="doc"></div></div></div>
<script>{js}</script></body></html>"""


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
            path = self.path.split("?")[0]
            if path == "/v":
                body, ctype = fingerprint().encode(), "text/plain"
            elif path in ("/", "/index.html"):
                body, ctype = build(args.due).encode(), "text/html; charset=utf-8"
            else:
                self.send_response(404); self.end_headers(); return
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    print(f"dashboard → http://localhost:{args.port}  (updates itself when notes change · Ctrl+C to stop)")
    http.server.ThreadingHTTPServer(("127.0.0.1", args.port), H).serve_forever()


if __name__ == "__main__":
    main()
