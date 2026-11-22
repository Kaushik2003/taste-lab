---
type: paper
title: "Reading Human Preference from Looped Transformer Internal States"
status: skimmed
url: https://arxiv.org/abs/2604.09870v3
arxiv: 2604.09870
authors: Jan Kirin
year: 2026
section: 4
tier: deep
tests: [grounded]
components: [monitor, evaluate]
tags: [type/paper, section/4, status/skimmed, role/prior-art]
---

# Human preference is weakly readable from hidden states

Corrected v3 (18 November 2026) studies human-preference readouts from Ouro-2.6B-Thinking hidden states on HH-RLHF. Linear pairwise accuracy is about 61%; the nonlinear evaluator reaches about 65%. These results exceed simple length-based rules but are far below the original headline results.

Source checked: [corrected v3](https://arxiv.org/abs/2604.09870v3), introduction, Sections 3 and 4 and correction summary, 22 November 2026. Versions 1 and 2 had a different title. Do not reuse the superseded 95.2% evaluator or 84.5% linear-probe results, or the withdrawn relational-encoding conclusion.

## Relevance and limits

Human quality-related preference is already readable, weakly, from hidden states. This refutes a broad absence claim, not the proposed test-matched readability loop. The readouts are researcher-trained on human preference labels. This single-model preprint does not demonstrate causal endogenous evaluation, autonomous readout use, readability-specific validity, longitudinal self-training or preference ownership. A decodable preference is not sufficient evidence of metacognition.
