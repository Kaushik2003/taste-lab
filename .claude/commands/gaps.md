---
description: Find gaps and patterns across the papers, print them, and save them to 07-drafts/litreview/gaps.md. Usage /gaps
---

Map what the literature covers for the metacognition lit review, what it leaves open, and what keeps coming up.

1. **Read** every note in `01-papers/` (frontmatter, Evidence, Limits, and `## Harshit's notes`), the threads in
   `03-questions/`, the section names in `dashboard.json`, and, if they exist, `07-drafts/litreview/outline.md`,
   `07-drafts/litreview/gaps.md` (the previous run) and `03-questions/Gaps in the field.md`. Read `06-patterns/` for
   what Harshit finds interesting. Never write there. Weight read papers and Harshit's notes above skimmed ones.
2. **Write** the output in this order. The dashboard's Overview panel shows only the start of the file, so the gap
   table goes first:
   - `# Gaps & patterns`, then a line: `Updated YYYY-MM-DD · N papers, M read`.
   - `## Gaps`: table `Gap | Loop stage | Test | Closest work | Why it matters`. One row per thing no paper has shown
     yet. Loop stage is monitor, evaluate, control or persist. Test is one of the four tests, or `none`.
   - `## Patterns`: 3 to 6 bullets. Each is a finding that repeats across at least 2 papers, with the papers linked.
   - `## Tensions`: papers that disagree with each other, and places where Harshit's notes disagree with a paper.
   - `## Coverage by section`: table `Section | Papers | Read | Note`. Flag sections with fewer than 2 papers.
   - `## Fill next`: up to 5 searches or papers that would close the biggest gaps.
   Cite papers as `[[file-name]]` (no `|alias` inside tables, because the pipe breaks the table). Mark anything you're
   not sure of `[unverified]`. Be adversarial: a gap that kills one of our threads matters more than a flattering one.
3. **Save** to `07-drafts/litreview/gaps.md`, overwriting the old file (create the folder if needed). No frontmatter:
   the dashboard shows this file as-is and would print it as text. Stick to headings, bullets, tables, bold, `code`
   and links, which is all the dashboard renders.
4. **Print** the same content in chat, then one line on what changed since the previous run.
