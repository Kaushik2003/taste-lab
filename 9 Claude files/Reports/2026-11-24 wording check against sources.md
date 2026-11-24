---
type: report
status: active
tags: [type/report, plagiarism-check, literature-review]
links: ["[[Literature review - full paper]]", "[[2026-11-24 independent critique of the review]]", "[[2026-11-24 response to the critique]]", "[[TASKS]]"]
---

# Wording check of the review against its sources, 2026-11-24

**Result: no copied passages found.** The review shares very little wording with the papers it cites.

## Method
- Text checked: the body of [[Literature review - full paper]] (about 19,300 words), without the reference list.
- Compared with 158 source texts: the full text of 141 cited arXiv papers (arXiv HTML), the abstract of 5 more, and 12 cited web pages (blog posts, project pages, conference pages).
- Measure: word sequences of 8 and of 6 words that appear in both the review and a source, after lower-casing and removing punctuation.
- Scripts: `scripts/review_checks/fetch_sources.py` and `scripts/review_checks/overlap.py`.

## Numbers
| Measure | Result |
|---|---|
| 8-word sequences shared with any source | 15 of 19,267 (0.08%) |
| 6-word sequences shared with any source | about 100 of 19,269 (0.5%) |
| Review words inside a shared 6-word sequence | about 2% |

## What the shared sequences are
- **Two marked quotations**, each inside quotation marks with its source: "requires at least one deployment-acceptance signal outside the agent's control" (Guo 2026) and "encode a notion of correctness yet fail to exploit it" (Zhang 2025).
- **Citation strings** that the source also contains, such as "Ha and Schmidhuber 2018; Hafner et al. 2023".
- **Reported numbers**, such as "from 10.8% to 63.8%" or "from 7.9% to 48.1%". These must match the source.
- **Technical terms and short common phrases**, such as "feelings of knowing, judgments of learning" or "model trained on the same data".
- Two short phrases followed a source closely and were reworded on 2026-11-24 (Stroganov 2026, Szeider 2025).

The longest shared passage outside quotation marks is 8 words.

## Limits of this check
- It compares the review only with the sources it cites. It does not search the wider web or student-paper databases. A service such as the university's Turnitin does that.
- 11 cited sources could not be fetched (paywalled journals, PDFs, one page that refused the request), among them Nelson and Narens 1990, Doya 2002, Reber 2004, Fleming and Lau 2014, Nisbett and Wilson 1977.
- It finds copied wording. It does not find a paraphrase that follows a source's structure with different words.
- It says nothing about who wrote the text. That is covered by the statement on AI use in the review.
