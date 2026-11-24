#!/usr/bin/env python3
"""Build the literature review as an IEEE journal paper (IEEEtran class).

Reads the same section files as build_review.py and writes, in
"1 Literature review/export/ieee/":
  review.tex, references.bib, IEEEtran.cls, IEEEtran.bst, loop.png
Then it runs Tectonic (a self-contained LaTeX engine) and copies the result to
  1 Literature review/export/Literature review - full paper (IEEE).pdf

What changes against the plain build, because the IEEE style needs it:
  - numbered citations [n] in order of first use, references set by IEEEtran.bst
  - section numbers I, II, ... and A, B, ...; cross-references follow them
  - every table has a number and a caption above it; tables float
  - headings, title, and table captions in title case
The wording of the review comes from the section files.

Usage: python3 scripts/build_review_ieee.py [--no-pdf]
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_review as b  # noqa: E402

ROOT = b.ROOT
REV = b.REV
OUT = REV / "export" / "ieee"
IEEE = ROOT / "IEEEtran"
PDF_NAME = "Literature review - full paper (IEEE).pdf"

L = r">{\raggedright\arraybackslash}X"


def P(w):
    return r">{\raggedright\arraybackslash}p{%s}" % w


# One entry per table, in order of appearance. "head" is a header cell used to
# check that the entry still matches the table. "num" is the number the table
# has in the section files; its caption is the "**Table N.** ..." line above it.
TABLES = [
    dict(head="Question", num="1", wide=False, cols=["l", L, "c"]),
    dict(head="What this review adds", num="2", wide=True, cols=[P(r"0.20\textwidth"), L, L]),
    dict(head="Simpler explanation it removes", num="3", wide=True,
         cols=[P(r"0.27\textwidth"), L, P(r"0.25\textwidth")]),
    dict(head="Who proposes the change", num="4", wide=True, cols=[P(r"0.25\textwidth"), L, L, "l"]),
    dict(head="Previous instrument", num="5", wide=True, cols=["l", L, P(r"0.20\textwidth"), L]),
    dict(head="Strongest evidence", num="6", wide=True, cols=["l", L, L, L]),
    dict(head="It does not", num="7", wide=False, cols=[P(r"0.20\columnwidth"), L, L]),
]

# Venue strings in the notes that need a hand-made IEEE form.
VENUE_FIX = {
    "The Psychology of Learning and Motivation, Vol. 26":
        r"in \emph{The Psychology of Learning and Motivation}, vol. 26, G. H. Bower, Ed. Academic Press, {YEAR}, pp. 125--173",
    "Transformer Circuits Thread": r"\emph{Transformer Circuits Thread}, 2025",
    "alphaXiv": "alphaXiv preprint, Nov. 2026",
    "ACL Findings 2023": r"in \emph{Findings of ACL}, 2023",
    "NeurIPS 2026 (poster": "NeurIPS poster, 2026",
}

ACCENT = {"ö": '{\\"o}', "é": "{\\'e}", "ł": "{\\l}", "ü": '{\\"u}', "č": "{\\v{c}}", "í": "{\\'i}",
          "ä": '{\\"a}', "ó": "{\\'o}", "á": "{\\'a}", "Ş": "{\\c{S}}", "Ż": "{\\.Z}", "π": "$\\pi$",
          "’": "'", "–": "--"}

SMALL = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "of", "on", "in", "to",
         "at", "by", "as", "per", "via", "vs"}

problems = []


def esc(s):
    """Escape LaTeX special characters in plain text."""
    s = s.replace("\\", r"\textbackslash{}")
    for ch in "&%$#_{}":
        s = s.replace(ch, "\\" + ch) if ch not in "{}" else s
    s = s.replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}")
    return s


def quotes(s):
    out = []
    for i, ch in enumerate(s):
        if ch == '"':
            prev = s[i - 1] if i else " "
            out.append("``" if prev in " \t\n([{-/*|" else "''")
        else:
            out.append(ch)
    return "".join(out)


def cap(word):
    for i, ch in enumerate(word):
        if ch.isalpha():
            return word[:i] + ch.upper() + word[i + 1:]
    return word


def titlecase(s):
    words = s.split(" ")
    out, new_start = [], True
    last = len(words) - 1
    for i, w in enumerate(words):
        parts = w.split("-")
        done = []
        for j, p in enumerate(parts):
            core = re.sub(r"[^A-Za-z']", "", p)
            if re.search(r"[A-Z]", p[1:] if p[:1].isalpha() else p.lstrip('"(')[1:]):
                done.append(p)                      # keeps INTUITOR, SEAL, "I"
            elif core.lower() in SMALL and not (j == 0 and (new_start or i == last)):
                done.append(p)
            else:
                done.append(cap(p))
        out.append("-".join(done))
        new_start = w.endswith((":", "?", ".")) and not w.endswith("vs.")
    return " ".join(out)


def bibkey(who, yearlab):
    import unicodedata
    s = unicodedata.normalize("NFKD", who.replace("ł", "l").replace("Ż", "Z"))
    s = "".join(c for c in s if c.isascii() and c.isalnum())
    return s + yearlab


def for_bib(s):
    s = esc(s.replace('\\"', '"'))
    s = quotes(s)
    for k, v in ACCENT.items():
        s = s.replace(k, v)
    bad = sorted(set(c for c in s if ord(c) > 127))
    if bad:
        problems.append("non-ASCII character in a reference: %s in %s" % (bad, s[:60]))
    return s


def bib_authors(a):
    a = re.sub(r"\([^)]*\)", "", a)
    etal = "et al" in a
    a = re.sub(r",?\s*et al\.?", "", a)
    parts = [p.strip() for p in re.split(r",|;|\band\b", a) if p.strip()]
    parts = [re.sub(r"\.(?=\w)", ". ", p) for p in parts]
    if etal:
        parts.append("others")
    return " and ".join(parts)


def bib_venue(d):
    """Return (howpublished, url) in IEEE reference form."""
    raw = d.get("venue", "") or ""
    year = d["year"]
    url = d.get("url", "") or ""
    m = re.search(r"arxiv\.org/abs/([\w./-]+)", url)
    arx = m.group(1) if m else None
    for k, v in VENUE_FIX.items():
        if raw.startswith(k):
            how = v.replace("{YEAR}", year)
            return (how + (", arXiv:" + arx if arx and "arXiv" not in raw[:5] and "Circuits" not in k else ""),
                    "" if arx else url)
    v = re.sub(r"\s*\[[^\]]*\]", "", raw)
    v = re.sub(r"\s+\([^)]*\)", "", v).strip().rstrip(".,; ")
    generic = (not v) or v.lower().startswith(("arxiv preprint", "preprint"))
    if generic:
        if arx:
            return "%s, arXiv:%s" % (year, arx), ""
        return "%s" % year, url
    jm = re.match(r"^(.+?) (\d+)(?:\(([\d-]+)\))?, (\d+)-(\d+)$", v)
    if jm:
        how = r"\emph{%s}, vol. %s" % (for_bib(jm.group(1)), jm.group(2))
        if jm.group(3):
            how += ", no. %s" % jm.group(3).replace("-", "--")
        how += ", pp. %s--%s, %s" % (jm.group(4), jm.group(5), year)
    elif v.startswith("Blog post"):
        how = for_bib(v)
    elif v.startswith("Proceedings"):
        how = r"in \emph{%s}, %s" % (for_bib(v.replace("Proceedings of the", "Proc.")), year)
    else:
        cm = re.match(r"^(.*?)\s+((?:19|20)\d\d)(\s+[Ww]orkshop)?$", v)
        if cm and not cm.group(1).startswith("PLOS"):
            name = cm.group(1) + (" Workshop" if cm.group(3) else "")
            how = r"in \emph{Proc. %s}, %s" % (for_bib(name), cm.group(2))
        elif cm:
            how = r"\emph{%s}, %s" % (for_bib(cm.group(1)), cm.group(2))
        else:
            how = r"\emph{%s}, %s" % (for_bib(v), year)
    if arx:
        return how + ", arXiv:" + arx, ""
    return how, url


def main():
    notes = b.load_notes()
    body = []
    for name in b.ORDER:
        _, t = b.front((REV / name).read_text())
        body.append(re.split(r"\n## Log\n", t)[0].rstrip() + "\n")
    text = "\n".join(body)

    # lead-in sentences for the tables that have no number in the section files
    for t in TABLES:
        if "replace" in t:
            old, new = t["replace"]
        elif "after" in t:
            old, new = t["after"], t["after"] + t["add"]
        else:
            continue
        if text.count(old) != 1:
            problems.append("lead-in text for table '%s' found %d times" % (t["label"], text.count(old)))
        text = text.replace(old, new, 1)

    # ---- citations: turn links into numbered tokens
    cited = []

    def tok(k):
        if k not in cited:
            cited.append(k)
        return "\x00%d\x00" % cited.index(k)

    def note_tok(m):
        stem = m.group(1).split("|")[0].strip()
        return tok(stem) if stem in notes else "\x01%s\x01" % stem

    text = re.sub(r"\[\[([^\]]+)\]\]", note_tok, text)

    def extra_tok(m):
        out = []
        for k in [k.strip().lstrip("@") for k in m.group(1).split(";")]:
            if k not in b.EXTRA:
                problems.append("unknown extra reference: " + k)
                continue
            out.append(tok(k))
        return "(" + "; ".join(out) + ")"

    text = re.sub(r"\[(@[^\]]+)\]", extra_tok, text)
    text = re.sub(r"\s*\(\x01[^\x01]*\x01(?:,\s*\x01[^\x01]*\x01)*\)", "", text)
    text = re.sub(r"\x01([^\x01]*)\x01", lambda m: m.group(1), text)

    info = {k: (notes.get(k) or b.EXTRA[k]) for k in cited}
    groups = {}
    for k in cited:
        groups.setdefault((info[k]["sur"], info[k]["year"]), []).append(k)
    who, key = {}, {}
    for (sur, year), ks in groups.items():
        for i, k in enumerate(ks):
            d = info[k]
            who[k] = sur if d["n"] == 1 else ("%s and %s" % (sur, d["sur2"]) if d["n"] == 2 and d.get("sur2") else sur + " et al.")
            key[k] = bibkey(sur, year + ("abcdefgh"[i] if len(ks) > 1 else ""))
    if len(set(key.values())) != len(key):
        problems.append("duplicate reference keys")

    T = r"\x00(\d+)\x00"

    def keys_of(s):
        return ",".join(key[cited[int(i)]] for i in re.findall(T, s))

    def cites(s):
        def group(m):
            g = m.group(1)
            lead = re.match(r"^((?:\x00\d+\x00(?:[;,]\s*)?)+)(.*)$", g, re.S)
            if lead:
                rest = lead.group(2).strip()
                c = r"\cite{%s}" % keys_of(lead.group(1))
                return c if not rest else "%s (%s)" % (c, rest)
            g = re.sub(r"(?:\x00\d+\x00(?:[;,]\s*)?)+", lambda mm: r"\cite{%s}" % keys_of(mm.group(0)) +
                       (" " if mm.group(0)[-1] in " " else ""), g)
            return "(" + g + ")"

        s = re.sub(r"\(([^()]*\x00[^()]*)\)", group, s)
        s = re.sub(T, lambda m: r"%s~\cite{%s}" % (who[cited[int(m.group(1))]], key[cited[int(m.group(1))]]), s)
        while True:
            s2 = re.sub(r"\\cite\{([^}]*)\}\s*\\cite\{([^}]*)\}", r"\\cite{\1,\2}", s)
            if s2 == s:
                break
            s = s2
        return re.sub(r" (\\cite\{)", r"~\1", s)

    # ---- labels
    sec_labels = set(re.findall(r"^#{1,3} (\d+(?:\.\d+)?)\.? ", text, re.M))
    tab_label = {t["num"]: "tab:" + t["num"] for t in TABLES if "num" in t}

    def refs(s):
        def sec(m):
            word, rest = m.group(1), m.group(2)
            items = re.split(r"(,\s*(?:and\s+|or\s+)?|\s+(?:and|to|or)\s+)", rest)
            out, used = "", 0
            for i in range(0, len(items), 2):
                if items[i] not in sec_labels:
                    break
                out += (items[i - 1] if i else "") + r"\ref{sec:%s}" % items[i]
                used = i + 1
            if not used:
                return m.group(0)
            return "%s~%s%s" % (word, out, "".join(items[used:]))

        s = re.sub(r"\b(Sections?)\s+(\d+(?:\.\d+)?(?:(?:,\s*(?:and\s+|or\s+)?|\s+(?:and|to|or)\s+)\d+(?:\.\d+)?)*)", sec, s)

        def tab(m):
            if m.group(1) not in tab_label:
                problems.append("reference to unknown table " + m.group(1))
                return m.group(0)
            return r"Table~\ref{%s}" % tab_label[m.group(1)]

        s = re.sub(r"\bTable (\d+)", tab, s)
        s = re.sub(r"\bFigure (\d+)", r"Fig.~\\ref{fig:\1}", s)
        s = re.sub(r"\x02(\w+)\x02", r"Table~\\ref{tab:\1}", s)
        return s

    def tex(s):
        s = esc(s)
        s = re.sub(r"`([^`]+)`", r"\\texttt{\1}", s)
        s = quotes(s)
        s = re.sub(r"(?<=\w)''([,.])", r"\1''", s)   # IEEE style: comma and period inside the quotes
        s = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", s)
        s = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])", r"\\emph{\1}", s)
        s = re.sub(r"(https?://[^\s<]+[^\s<.,;)])", lambda m: r"\url{%s}" % m.group(1).replace("\\", ""), s)
        return cites(refs(s))

    # ---- title block
    lines = text.splitlines()
    title = authors = date = keywords = ""
    abstract = []
    i = 0
    while i < len(lines) and not re.match(r"^# \d", lines[i]):
        ln = lines[i].strip()
        if ln.startswith("# "):
            title = ln[2:]
        elif ln.startswith("**Authors:**"):
            authors = ln.split("**", 2)[2].strip()
        elif ln.startswith("**Date:**"):
            date = ln.split("**", 2)[2].strip()
        elif ln.startswith("**Keywords:**"):
            keywords = ln.split("**", 2)[2].strip()
        elif ln and not ln.startswith(("## Abstract", "<!--")):
            abstract.append(ln)
        i += 1
    if authors in ("", "[add names]"):
        authors = "[Author names to be added]"
    kw = sorted((k.strip() for k in keywords.split(",")), key=str.lower)
    kw = ", ".join(kw)
    kw = kw[:1].upper() + kw[1:] + "."

    out = []
    tab_i = 0
    pending_caption = None
    first_par = False
    stack = []

    def close_list():
        while stack:
            out.append(r"\end{%s}" % stack.pop())

    while i < len(lines):
        ln = lines[i]
        if not ln.strip() or ln.startswith("<!--"):
            close_list()
            i += 1
            continue
        m = re.match(r"^(#{1,3}) (.*)", ln)
        if m:
            close_list()
            lvl, head = len(m.group(1)), m.group(2).strip()
            nm = re.match(r"^(\d+(?:\.\d+)?)\.? (.*)", head)
            cmd = ["section", "subsection", "subsubsection"][lvl - 1]
            if nm:
                out.append("\n\\%s{%s}\\label{sec:%s}" % (cmd, tex(titlecase(nm.group(2))), nm.group(1)))
                first_par = nm.group(1) == "1"
            else:
                out.append("\n\\%s*{%s}" % (cmd, tex(titlecase(head))))
            i += 1
            continue
        m = re.match(r"^\*\*Table (\d+)\.\*\*\s*(.*)$", ln)
        if m:
            close_list()
            pending_caption = (m.group(1), m.group(2).strip().rstrip("."))
            i += 1
            continue
        if ln.startswith("|"):
            close_list()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            rows = [r for n, r in enumerate(rows) if not (n == 1 and all(re.match(r"^:?-+:?$", c) for c in r))]
            keep = [c for c in range(len(rows[0])) if any(r[c] for r in rows if c < len(r))]
            rows = [[r[c] if c < len(r) else "" for c in keep] for r in rows]
            spec = TABLES[tab_i] if tab_i < len(TABLES) else None
            tab_i += 1
            if not spec or spec["head"] not in rows[0] or len(spec["cols"]) != len(rows[0]):
                problems.append("table %d does not match its entry in TABLES: %s" % (tab_i, rows[0]))
                continue
            if "num" in spec:
                if not pending_caption or pending_caption[0] != spec["num"]:
                    problems.append("caption missing for Table " + spec["num"])
                    continue
                caption, label = pending_caption[1], "tab:" + spec["num"]
            else:
                caption, label = spec["caption"], "tab:" + spec["label"]
            pending_caption = None
            sec_col = rows[0].index("Section") if "Section" in rows[0] else None
            env = "table*" if spec["wide"] else "table"
            width = r"\textwidth" if spec["wide"] else r"\columnwidth"
            out.append("\n\\begin{%s}[!t]" % env)
            out.append("\\caption{%s}\\label{%s}" % (tex(titlecase(caption)), label))
            out.append("\\centering\\footnotesize\\renewcommand{\\arraystretch}{1.15}")
            out.append("\\begin{tabularx}{%s}{@{}%s@{}}" % (width, "".join(spec["cols"])))
            out.append("\\toprule")
            for n, r in enumerate(rows):
                cells = []
                for c, cell in enumerate(r):
                    if n and c == sec_col and cell in sec_labels:
                        cells.append(r"\ref{sec:%s}" % cell)
                    elif n == 0:
                        cells.append(r"\textbf{%s}" % tex(cell) if cell else "")
                    else:
                        cells.append(tex(cell))
                out.append(" & ".join(cells) + r" \\")
                if n == 0:
                    out.append("\\midrule")
            out.append("\\bottomrule")
            out.append("\\end{tabularx}")
            out.append("\\end{%s}\n" % env)
            continue
        m = re.match(r"^!\[Figure (\d+)\.\s*(.*)\]\((.+)\)$", ln)
        if m:
            close_list()
            src = REV / m.group(3)
            shutil.copy(src, OUT / src.name)
            out.append("\n\\begin{figure*}[!t]\n\\centering")
            out.append("\\includegraphics[width=0.82\\textwidth]{%s}" % src.name)
            out.append("\\caption{%s}\\label{fig:%s}" % (tex(m.group(2)), m.group(1)))
            out.append("\\end{figure*}\n")
            i += 1
            continue
        if ln.startswith("> "):
            close_list()
            out.append("\\begin{quote}\n%s\n\\end{quote}" % tex(ln[2:]))
            i += 1
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.) (.*)", ln)
        if m:
            kind = "enumerate" if m.group(2)[0].isdigit() else "itemize"
            if not stack or stack[-1] != kind:
                close_list()
                out.append("\\begin{%s}" % kind)
                stack.append(kind)
                if kind == "enumerate" and m.group(2) != "1.":
                    out.append("\\setcounter{enumi}{%d}" % (int(m.group(2)[:-1]) - 1))
            out.append("\\item %s" % tex(m.group(3)))
            i += 1
            continue
        close_list()
        par = tex(ln)
        if first_par:
            fm = re.match(r"^([A-Za-z])(\w*)", par)
            if fm:
                par = "\\IEEEPARstart{%s}{%s}%s" % (fm.group(1), fm.group(2), par[fm.end():])
            first_par = False
        out.append("\n" + par)
        i += 1
    close_list()
    if tab_i != len(TABLES):
        problems.append("found %d tables, TABLES has %d entries" % (tab_i, len(TABLES)))

    body_tex = "\n".join(out)
    if "\x00" in body_tex or "\x01" in body_tex or "\x02" in body_tex or "[[" in body_tex:
        problems.append("leftover link markup")
    for lab in re.findall(r"\\ref\{sec:([^}]+)\}", body_tex):
        if lab not in sec_labels:
            problems.append("reference to unknown section " + lab)

    # ---- references
    bib = []
    for k in cited:
        d = info[k]
        how, url = bib_venue(d)
        e = ["@misc{%s," % key[k],
             "  author = {%s}," % for_bib(bib_authors(d["authors"])),
             "  title = {{%s}}," % for_bib(d["title"].rstrip(".")),
             "  howpublished = {%s}," % how]
        if url:
            e.append("  url = {%s}," % url)
        e.append("}")
        bib.append("\n".join(e))

    font = "[Extension=.otf,UprightFont=*-regular,BoldFont=*-bold,ItalicFont=*-italic,BoldItalicFont=*-bolditalic%s]"
    doc = r"""%% Built by scripts/build_review_ieee.py from the section files.
%% Edit the section files, not this file.
\documentclass[journal]{IEEEtran}
\usepackage{fontspec}
\setmainfont{texgyretermes}%s
\setsansfont{texgyreheros}%s
\setmonofont{texgyrecursor}%s
\usepackage{cite}
\usepackage{graphicx}
\usepackage{array,booktabs,tabularx}
\usepackage{url}
\usepackage[hidelinks]{hyperref}
\usepackage{flushend}
\frenchspacing
\emergencystretch=1.5em
\hyphenation{meta-cog-ni-tion meta-cog-ni-tive}

\begin{document}

\title{%s}
\author{%s%%
\thanks{Draft of %s.}}
\markboth{Draft of %s}{Draft of %s}
\maketitle

\begin{abstract}
%s
\end{abstract}

\begin{IEEEkeywords}
%s
\end{IEEEkeywords}
%s

\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
""" % (font % ",Ligatures=TeX", font % ",Ligatures=TeX,Scale=MatchLowercase", font % ",Scale=MatchLowercase",
       tex(titlecase(title)), tex(authors), tex(date), tex(date), tex(date),
       " ".join(tex(a) for a in abstract), tex(kw), body_tex)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "review.tex").write_text(doc)
    (OUT / "references.bib").write_text("\n\n".join(bib) + "\n")
    shutil.copy(IEEE / "IEEEtran.cls", OUT / "IEEEtran.cls")
    shutil.copy(IEEE / "bibtex" / "IEEEtran.bst", OUT / "IEEEtran.bst")
    words = len(re.findall(r"\w+", " ".join(abstract)))
    print("wrote review.tex | references:", len(bib), "| tables:", tab_i, "| abstract words:", words)
    for p in problems:
        print("PROBLEM:", p)
    if "--no-pdf" in sys.argv:
        return
    r = subprocess.run(["tectonic", "--keep-logs", "review.tex"], cwd=OUT, capture_output=True, text=True)
    tail = [x for x in (r.stdout + r.stderr).splitlines() if x.strip()]
    for x in tail:
        if re.search(r"error|undefined|Overfull|multiply|Missing", x, re.I):
            print("  tex:", x[:200])
    if r.returncode != 0:
        print("Tectonic failed. Last lines:")
        print("\n".join(tail[-25:]))
        sys.exit(1)
    shutil.copy(OUT / "review.pdf", REV / "export" / PDF_NAME)
    for junk in ("review.log", "review.blg"):
        (OUT / junk).unlink(missing_ok=True)
    print("wrote", "export/" + PDF_NAME)


if __name__ == "__main__":
    main()
