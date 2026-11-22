---
type: paper
title: "Self-Rewarding Language Models"
status: skimmed
url: https://arxiv.org/html/2401.10020v3
arxiv: 2401.10020
year: 2024
section: 5
tier: deep
tests: [self-reinforcing]
components: [evaluate, persist]
tags: [type/paper, section/5, status/skimmed, role/prior-art]
---

# Self-rewarding language models judge and train themselves

Yuan et al. use the same model to generate responses, score their quality and construct highest-versus-lowest preference pairs for iterative DPO. The rubric covers relevance, coverage, usefulness, clarity and expertise. Both response generation and judging improve over the reported three iterations.

Source checked: [full text v3, Sections 2 and 3](https://arxiv.org/html/2401.10020v3), 22 November 2026.

## Relevance and limits

This is direct prior art against claiming that a model's own quality evaluation never reaches its weights. The score is verbal LLM-as-a-Judge output, with human-seeded evaluation criteria and training data. It is not a causally validated activation readout, a correctness-matched readability experiment, proof of self-originated taste, or evidence of indefinite stable improvement.
