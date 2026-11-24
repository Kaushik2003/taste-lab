---
type: paper
title: "Introspecting Alignment Shifts Beyond Behaviors Implanted Through Fine-Tuning"
status: skimmed
arxiv: 2608.04347
url: https://arxiv.org/abs/2608.04347
authors: Kotaro Yoshida, Laura Gomezjurado Gonzalez, Yukinori Yamamoto, Yuji Naraki, Ryotaro Shimizu, Wenya Wang
year: 2026
venue: arXiv preprint
relevance: 2
section: 3
tier: skim
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, component/monitoring, status/skimmed, relevance/2, role/prior-art, introspection, fine-tuning]
links: ["[[Field map - Models read their own state]]", "[[A trained adapter lets a model describe its weight change (Goel 2025)]]", "[[2026-11-23 gap check]]"]
---
# Introspecting alignment shifts (Yoshida 2026)

**One line:** Trained "introspection adapters" can make a fine-tuned model report alignment changes that came as side effects of fine-tuning, not only behaviors that were put in on purpose. The gains are modest and a simple probe is about as good at classification.

Read 2026-11-24: abstract, introduction, Sec. 5.2. Method details not read.

## Evidence
- Classification accuracy on three out-of-distribution settings: the new adapter 52.1, 52.3 and 41.3, against 51.9, 49.4 and 35.3 for a standard adapter (Sec. 5.2.1).
- A probe on activations is competitive and wins in one setting; the authors say classification alone shows no clear practical advantage for trained introspection (Sec. 5.2.1).
- For free-form reports, adding an adapter gives a large gain over asking the raw fine-tuned model directly, in all six settings (Sec. 5.2.2).

## Relevance to taste-lab
Second piece of evidence that a model does not describe its own weight change unless trained to. Side effects, the case closest to an unplanned preference shift, are harder to report than implanted behaviors.
