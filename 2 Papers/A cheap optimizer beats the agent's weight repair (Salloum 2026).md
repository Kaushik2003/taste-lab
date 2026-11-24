---
type: paper
title: "Tree-Ising: Repairing Language Models with Bit-Level Ising Edits"
status: skimmed
arxiv: 2611.14210
url: https://arxiv.org/abs/2611.14210
authors: Hadi Salloum, Ammar Ali, et al.
year: 2026
venue: arXiv preprint
relevance: 2
section: 5
tier: skim
tests: []
components: [consolidation]
tags: [type/paper, section/5, component/consolidation, status/skimmed, relevance/2, role/threat, weight-space-programming]
links: ["[[Field map - Changes that stay in the weights]]", "[[A simple sort replaces the anti-loop edit (Fischetti 2026)]]", "[[WSP - a model reads and edits weights (Takehi 2026)]]", "[[2026-11-23 gap check]]"]
---
# A cheap optimizer beats the agent's weight repair (Salloum 2026)

**One line:** The anti-loop repair that a frontier agent found by weight-space programming can be found better by a plain discrete optimizer, for about $0.90 of GPU time and no language-model tokens.

## Evidence (abstract)
- The agent repair used 158 turns, 89.7 million tokens and 50 forward-pass requests. Tree-Ising uses 4 forward-pass requests and zero LLM tokens.
- MATH-500 on the agent's two layers: 54.6% (Tree-Ising) vs 51.7% (agent edit); base 7.9%. Better on all five math benchmarks; significant on MATH-500 and GSM8K.
- 13 to 17% fewer weights changed. On Qwen3.5-2B, greedy GSM8K from 21.6% to 69.4%.

## Relevance to taste-lab
With [[A simple sort replaces the anti-loop edit (Fischetti 2026)]]: once the objective is known, an optimizer beats the agent. A self-editing model must add something an optimizer cannot: choosing *what* to change. That is the evaluation (taste) step, which supports framing the gap around the model's own judgment, not around the edit mechanics.
