---
description: Turn a paper/post into a structured note. Usage /ingest <arxiv-id | url>
argument-hint: <arxiv-id | url>
---

Ingest $ARGUMENTS:

1. Dedupe against `2 Papers/`.
2. Fetch the abstract page, and the full text (HTML/PDF) if available. Read the method and results sections, not just the abstract.
3. Create `2 Papers/<what the paper shows, 8 words or fewer> (<First author> <Year>).md` (see the naming rule in CLAUDE.md) from `9 Claude files/Templates/paper.md`. Fill every section, paraphrased,
   with concrete numbers in Evidence. "Steal this" must name something reusable (code link, metric, dataset).
   Set `section` (lit review section 1-9, names in `dashboard.json`) and `tier` (`deep` if relevance is 3, else `skim`).
4. Create or update the relevant `3 Ideas/` notes and add wikilinks both ways.
5. If it affects a thread in `1 Questions/`, add a dated line to that thread's Log and to Evidence for/against.
6. Report: one-line summary, relevance score, and which threads it touched.
