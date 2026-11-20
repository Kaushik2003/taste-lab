---
type: paper
title: "AI Models Collapse When Trained on Recursively Generated Data"
status: skimmed
url: https://www.nature.com/articles/s41586-024-07566-y
authors: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson (Oxford / Cambridge / Toronto et al.)
year: 2024
venue: Nature 631
relevance: 3
section: 6
tier: deep
tests: []
components: [consolidation]
tags: [type/paper, section/6, component/consolidation, status/skimmed, relevance/3, model-collapse, recursive-training, distribution-tails]
links: ["[[self-training-collapse-T3]]", "[[2026-srivastava-renyi-crossings]]", "[[2026-he-unsupervised-rlvr-limits]]"]
---

# Model Collapse (Shumailov et al., Nature 2024)

**One line:** Indiscriminate training on model-generated content causes irreversible defects: tails of the original distribution disappear first (early collapse), then convergence to a low-variance point estimate (late collapse). Shown in GMMs, VAEs and LLMs, with theory saying it is inevitable even with near-ideal learning conditions.

## Claim
Recursive training on generated data destroys the tails of the distribution, and access to genuine human-produced data becomes the scarce resource ([abs](https://www.nature.com/articles/s41586-024-07566-y)).

## Mechanism
Generational training where each model's output pollutes the next's training set; theoretical analysis of tail loss; early vs late collapse distinction.

## Evidence
Collapse demonstrated across GMMs, VAEs, LLMs; inevitability argued even without function-estimation error.

## Limits / what they didn't show
- Data-pollution collapse across model generations and scraped corpora, not single-model self-reward loops; the mechanism (distribution shift via mixing) differs from reward-driven sharpening.
- Measurement is distributional; see [[2026-srivastava-renyi-crossings]] for why single entropy orders mislead.

## Relevance to taste-lab
**The canonical collapse citation, and the reason the anchor must be external data, not just external reward.** For T3 ([[self-training-collapse-T3]]): self-training on valence-selected outputs is a milder version of recursive pollution - the novelty term and held-out human anchor in [[anti-collapse-anchor]] are directly motivated by this tail-loss result.
- Prior-art check: n/a (foundational risk result).

## Steal this
- Early vs late collapse as the staging language for T3's failure analysis.
- "Tails disappear first" as the measurable early-warning signal: track tail mass, not just mean quality.

## Kaushik's notes
<!-- yours -->
