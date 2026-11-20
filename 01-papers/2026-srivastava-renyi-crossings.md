---
type: paper
title: "Richness Is Not Evenness: Ordered Rényi Crossings under Self-Training"
status: skimmed
arxiv: 2611.08892
url: https://arxiv.org/abs/2611.08892
authors: Pranjal Srivastava (U. Michigan)
year: 2026
venue: preprint
relevance: 3
section: 6
tier: deep
tests: []
components: [monitoring, consolidation]
tags: [type/paper, section/6, component/monitoring, component/consolidation, status/skimmed, relevance/3, model-collapse, entropy, self-training, measurement]
links: ["[[self-training-collapse-T3]]", "[[2026-he-unsupervised-rlvr-limits]]", "[[anti-collapse-anchor]]"]
---

# Ordered Rényi Crossings under Self-Training

**One line:** Nine generations of GPT-2 self-training: Rényi entropies don't move together - min-entropy flips from loss to gain first as training temperature rises, then collision, Shannon, and observed richness last. At T=1, generation 9 has 24% fewer word types but 0.91 bits HIGHER collision entropy. "Collapse" depends on which order of entropy you measure.

## Claim
Self-training's distributional effect is not a single decline: entropy orders cross in a persistent sequence, so richness and evenness can move in opposite directions ([abs](https://arxiv.org/abs/2611.08892)).

## Mechanism
Recursive fine-tuning on own output at varied training temperatures, one fixed measurement sampler; Rényi spectrum (min, collision, Shannon, richness) tracked per generation; robustness across grids, samplers, budgets, seeds, Hindi, 12/13 measurements under 8 representations; next-token and categorical-simulation controls.

## Evidence
Ordered crossings replicate across settings; fine-tuning on human text can produce the same split while likelihood improves; no single order's sign identifies worse likelihood.

## Limits / what they didn't show
- GPT-2 scale, English/Hindi text only; nothing about reasoning, code, or whether the crossings survive instruction tuning.
- Measurement paper: it tells you collapse metrics can mislead, not how to prevent collapse.

## Relevance to taste-lab
**A measurement-hygiene warning aimed straight at T3.** If we report "vocabulary shrank" as collapse evidence, a reviewer cites this: at T=1 types fall while collision entropy rises. The drift metric for [[self-training-collapse-T3]] must be a stated-budget entropy PROFILE plus an independent quality measure (their recommendation), plus our gamma statistic - not any single diversity number.
- Prior-art check: n/a (measurement).

## Steal this
- Entropy profiles at stated budgets + independent quality measure as the required reporting format for self-training experiments.
- The ordered-crossing phenomenon itself as a diagnostic: where in the order a given training regime sits.

## Kaushik's notes
<!-- yours -->
