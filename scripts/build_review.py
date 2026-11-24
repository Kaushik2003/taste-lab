#!/usr/bin/env python3
"""Build the literature review as one paper.

Reads the section drafts in "1 Literature review/", turns [[paper note]] links
into (Author Year) citations, builds the reference list from the frontmatter of
the notes in "2 Papers/", and writes:
  1 Literature review/Literature review - full paper.md
  1 Literature review/export/Literature review - full paper.html
With --office it also asks LibreOffice for .docx and .pdf.

Usage: python3 scripts/build_review.py [--office]
"""
import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REV = ROOT / "1 Literature review"
PAPERS = ROOT / "2 Papers"
ORDER = [
    "00-title-and-abstract.md", "01-introduction.md", "02-foundations.md",
    "03-monitoring.md", "03b-self-models-and-world-models.md",
    "04-evaluation-signals.md", "05-persistent-control.md", "06-limits.md",
    "07-taste-and-open-endedness.md", "08-synthesis.md", "09-conclusion.md",
]
OUT_NAME = "Literature review - full paper"

# Cited papers that have no note in "2 Papers/". Checked on arXiv on 2026-11-23/24.
EXTRA = {
    "Flavell 1979": dict(sur="Flavell", n=1, year="1979", authors="John H. Flavell",
        title="Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry",
        venue="American Psychologist 34(10), 906-911", url="https://doi.org/10.1037/0003-066X.34.10.906"),
    "Ha 2018": dict(sur="Ha", sur2="Schmidhuber", n=2, year="2018", authors="David Ha, Jürgen Schmidhuber",
        title="World Models", venue="arXiv preprint", url="https://arxiv.org/abs/1803.10122"),
    "Hafner 2023": dict(sur="Hafner", n=4, year="2023", authors="Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap",
        title="Mastering Diverse Domains through World Models", venue="arXiv preprint", url="https://arxiv.org/abs/2301.04104"),
    "Koh 2017": dict(sur="Koh", sur2="Liang", n=2, year="2017", authors="Pang Wei Koh, Percy Liang",
        title="Understanding Black-box Predictions via Influence Functions", venue="ICML 2017", url="https://arxiv.org/abs/1703.04730"),
    "Grosse 2023": dict(sur="Grosse", n=3, year="2023", authors="Roger Grosse et al.",
        title="Studying Large Language Model Generalization with Influence Functions", venue="arXiv preprint", url="https://arxiv.org/abs/2308.03296"),
    "Guo 2025": dict(sur="Guo", n=3, year="2025", authors="Jizhou Guo et al.",
        title="Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling", venue="arXiv preprint", url="https://arxiv.org/abs/2505.12225"),
    "Li 2024": dict(sur="Li", n=3, year="2024", authors="Kenneth Li et al.",
        title="Q-Probe: A Lightweight Approach to Reward Maximization for Language Models", venue="arXiv preprint", url="https://arxiv.org/abs/2402.14688"),
    "Bhatia 2025": dict(sur="Bhatia", n=3, year="2025", authors="Mehar Bhatia et al.",
        title="Value Drifts: Tracing Value Alignment During LLM Post-Training", venue="arXiv preprint", url="https://arxiv.org/abs/2510.26707"),
    "Zhu 2026": dict(sur="Zhu", n=3, year="2026", authors="Erkang Zhu et al.",
        title="Recursa: Toward Recursively Self-Improving Foundation Model Systems", venue="arXiv preprint", url="https://arxiv.org/abs/2611.04035"),
    "Lee 2026": dict(sur="Lee", n=3, year="2026", authors="Hyunin Lee et al.",
        title="Recursive Self-Improvement through Multi-Agent Self-Supervision", venue="arXiv preprint", url="https://arxiv.org/abs/2610.12176"),
    "Wang 2026": dict(sur="Wang", n=3, year="2026", authors="Haojin Wang et al.",
        title="ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?", venue="arXiv preprint", url="https://arxiv.org/abs/2610.34386"),
    "WangZ 2026": dict(sur="Wang", n=3, year="2026", authors="Zhaojia Wang et al.",
        title="Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming", venue="arXiv preprint", url="https://arxiv.org/abs/2611.17395"),
    "Liu 2026b": dict(sur="Liu", n=3, year="2026", authors="Mingda Liu, Zhenghan Zhu, Ze'an Miao, et al.",
        title="Norm Anchors Make Model Edits Last", venue="arXiv preprint", url="https://arxiv.org/abs/2602.02543"),
}


def front(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        text = text[m.end():]
    return meta, text


def clean_authors(a):
    a = re.sub(r"\[[^\]]*\]", "", a)
    a = re.sub(r"\([^)]*\)", "", a)
    return re.sub(r"\s+", " ", a).strip(" ,;")


def load_notes():
    notes = {}
    for p in PAPERS.glob("*.md"):
        m = re.search(r"\(([^()]+?) (\d{4})\)$", p.stem)
        if not m:
            continue
        meta, _ = front(p.read_text(errors="ignore"))
        authors = clean_authors(meta.get("authors", ""))
        parts = [x.strip() for x in re.split(r",|;| and ", authors) if x.strip()]
        etal = "et al" in authors
        parts = [x for x in parts if "et al" not in x]
        n = 3 if etal or len(parts) > 2 else max(len(parts), 1)
        sur2 = parts[1].split()[-1] if n == 2 and len(parts) == 2 else None
        url = meta.get("url", "")
        if re.match(r"^\d{4}\.\d{4,5}", meta.get("arxiv", "")):
            url = "https://arxiv.org/abs/" + meta["arxiv"].split()[0]
        authors = re.sub(r",\s*et al\.?", " et al.", authors)
        notes[p.stem] = dict(sur=m.group(1), sur2=sur2, n=n, year=m.group(2),
                             authors=authors or m.group(1), title=meta.get("title", "") or p.stem,
                             venue=meta.get("venue", ""), url=url)
    return notes


def main():
    notes = load_notes()
    body = []
    for name in ORDER:
        _, t = front((REV / name).read_text())
        t = re.split(r"\n## Log\n", t)[0].rstrip() + "\n"
        body.append(t)
    text = "\n".join(body)

    cited, problems = [], []

    def note_tok(m):
        stem = m.group(1).split("|")[0].strip()
        if stem in notes:
            if stem not in cited:
                cited.append(stem)
            return "\x00%s\x00" % stem
        return "\x01%s\x01" % stem

    text = re.sub(r"\[\[([^\]]+)\]\]", note_tok, text)

    def extra_tok(m):
        keys = [k.strip().lstrip("@") for k in m.group(1).split(";")]
        out = []
        for k in keys:
            if k not in EXTRA:
                problems.append("unknown extra reference: " + k)
                continue
            if k not in cited:
                cited.append(k)
            out.append("\x00%s\x00" % k)
        return "(" + "; ".join(out) + ")"

    text = re.sub(r"\[(@[^\]]+)\]", extra_tok, text)

    # links to non-paper notes: drop them when they stand alone in brackets, else keep the name
    text = re.sub(r"\s*\(\x01[^\x01]*\x01(?:,\s*\x01[^\x01]*\x01)*\)", "", text)
    text = re.sub(r"\x01([^\x01]*)\x01", lambda m: m.group(1), text)

    info = {k: (notes.get(k) or EXTRA[k]) for k in cited}
    groups = {}
    for k in cited:
        groups.setdefault((info[k]["sur"], info[k]["year"]), []).append(k)
    label, yearlab = {}, {}
    for (sur, year), ks in groups.items():
        for i, k in enumerate(ks):
            y = year + ("abcdefgh"[i] if len(ks) > 1 else "")
            d = info[k]
            who = sur if d["n"] == 1 else ("%s and %s" % (sur, d["sur2"]) if d["n"] == 2 and d.get("sur2") else sur + " et al.")
            label[k], yearlab[k] = "%s %s" % (who, y), y
    text = re.sub(r"\x00([^\x00]*)\x00", lambda m: label[m.group(1)], text)
    if "[[" in text or "\x00" in text or "\x01" in text:
        problems.append("leftover link markup")

    refs = []
    for k in sorted(cited, key=lambda k: (info[k]["sur"].lower(), yearlab[k])):
        d = info[k]
        line = "%s (%s). *%s*." % (d["authors"], yearlab[k], d["title"].rstrip("."))
        if d.get("venue"):
            line += " " + re.sub(r"\s*\[[^\]]*\]", "", d["venue"]).strip().rstrip(".") + "."
        if d.get("url"):
            line += " " + d["url"]
        refs.append("- " + line)
    text += "\n# References\n\n" + "\n".join(refs) + "\n"

    md = REV / (OUT_NAME + ".md")
    head = ('---\ntype: paper\nstatus: draft\ntags: [type/paper-draft, status/draft]\n'
            'links: ["[[outline]]", "[[TASKS]]"]\n---\n\n'
            '<!-- Built by scripts/build_review.py from the section files. Edit the section files, not this file. -->\n\n')
    md.write_text(head + text)
    exp = REV / "export"
    exp.mkdir(exist_ok=True)
    hp = exp / (OUT_NAME + ".html")
    hp.write_text(to_html(text))
    words = len(re.findall(r"\w+", text.split("# References")[0]))
    print("wrote", md.name, "| body words:", words, "| references:", len(refs), "| notes not cited:", len(notes) - sum(1 for k in cited if k in notes))
    for p in problems:
        print("PROBLEM:", p)
    if "--list-uncited" in sys.argv:
        for s in sorted(set(notes) - set(cited)):
            print("  uncited:", s)
    if "--office" in sys.argv:
        for fmt in ("docx:MS Word 2007 XML", "pdf:writer_web_pdf_Export"):
            subprocess.run(["libreoffice", "--headless", "--convert-to", fmt, "--outdir", str(exp), str(hp)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
        print("export:", ", ".join(sorted(p.name for p in exp.iterdir())))


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])", r"<i>\1</i>", s)
    s = re.sub(r"(https?://[^\s<]+[^\s<.,;)])", r'<a href="\1">\1</a>', s)
    return s


def to_html(text):
    out, lines, i = [], text.splitlines(), 0
    title = "Literature review"

    def close_list(stack):
        while stack:
            out.append("</%s>" % stack.pop())

    stack = []
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            close_list(stack); i += 1; continue
        m = re.match(r"^(#{1,4}) (.*)", ln)
        if m:
            close_list(stack)
            lvl = len(m.group(1))
            if lvl == 1 and title == "Literature review" and not re.match(r"\d", m.group(2)):
                title = m.group(2)
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2)), lvl)); i += 1; continue
        if ln.startswith("|"):
            close_list(stack)
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            out.append('<table border="1" cellspacing="0" cellpadding="5">')
            for r, row in enumerate(rows):
                if r == 1 and all(re.match(r"^:?-+:?$", c) for c in row):
                    continue
                tag = "th" if r == 0 else "td"
                out.append("<tr>" + "".join("<%s>%s</%s>" % (tag, inline(c), tag) for c in row) + "</tr>")
            out.append("</table>"); continue
        if ln.startswith("> "):
            close_list(stack)
            out.append("<blockquote><p>%s</p></blockquote>" % inline(ln[2:])); i += 1; continue
        m = re.match(r"^(\s*)([-*]|\d+\.) (.*)", ln)
        if m:
            kind = "ol" if m.group(2)[0].isdigit() else "ul"
            if not stack or stack[-1] != kind:
                close_list(stack); out.append("<%s>" % kind); stack.append(kind)
            out.append("<li>%s</li>" % inline(m.group(3))); i += 1; continue
        close_list(stack)
        if ln.startswith("<!--"):
            i += 1; continue
        out.append("<p>%s</p>" % inline(ln)); i += 1
    close_list(stack)
    css = ("body{font-family:'Liberation Serif',Georgia,serif;font-size:11pt;line-height:1.4;max-width:46em;margin:2em auto;padding:0 1em}"
           "h1{font-size:17pt;margin-top:1.6em}h2{font-size:13pt}h3{font-size:11.5pt}"
           "table{border-collapse:collapse;font-size:9.5pt;margin:1em 0}th{background:#eee;text-align:left}"
           "blockquote{border-left:3px solid #888;margin-left:0;padding-left:1em}")
    return ("<!doctype html><html><head><meta charset='utf-8'><title>%s</title><style>%s</style></head><body>\n%s\n</body></html>"
            % (html.escape(title), css, "\n".join(out)))


if __name__ == "__main__":
    main()
