---
type: paper
title: "CoRE: Enhancing Metacognition with Label-free Self-evaluation in LRMs"
status: skimmed
arxiv: 2507.06087
url: https://arxiv.org/abs/2507.06087
authors: Haoxi Li, Sikai Bai, Jie Zhang, Song Guo
year: 2025
venue: arXiv preprint
relevance: 3
section: 4
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/4, test/grounded, component/monitoring, status/skimmed, relevance/3, role/prior-art, metacognition, self-evaluation, label-free, interpretability]
links: ["[[Models act on their own confidence (Kumaran 2026)]]", "[[Models track and can be steered in thinking length (Eisenstadt 2025)]]", "[[INTUITOR - self-certainty is reward enough to learn reasoning (Zhao 2025)]]"]
---

# CoRE: Label-free Self-evaluation from Hidden-state Geometry

**One line:** The geometry of a model's hidden states across a reasoning chain tells you when it is going in circles: redundant reasoning shows up as cyclical fluctuations, and cutting the chain there keeps accuracy while slashing tokens.

**Why it matters to us:** A self-evaluation signal read off internal state with no labels and no training - this is the intrinsic evaluation signal our architecture needs, shown working for a process property (overthinking). Pairs with INTUITOR (self-certainty as reward) as the second concrete candidate signal.

Source: [arXiv 2507.06087](https://arxiv.org/abs/2507.06087) (8 July 2025). Abstract-level note.

## Claim
Intermediate reasoning steps carry a readable signal of redundancy in their hidden-state trajectories: cyclical fluctuation corresponds to repetitive, unconscious reflection, and detecting it enables label-free early exit ([abstract](https://arxiv.org/abs/2507.06087)).

## Mechanism
- CoRE: chain-of-reasoning embedding = the series of hidden states across reasoning steps.
- CoRE-Eval: training-free, label-free detector over the trajectory's geometric properties; terminates reasoning when cyclical patterns appear.

## Evidence
- GSM8K, MATH-500, AIME across 7B-32B models: large token reductions from early exit ([abstract](https://arxiv.org/abs/2507.06087)).
- The cyclical-fluctuation <-> redundancy correspondence is shown geometrically, not just empirically tuned.

## Limits / what they didn't show
- Detects *redundancy*, not *incorrectness*: a fluently wrong chain is not flagged.
- Mathematical reasoning only; open-ended generation has no analogous "cycle".
- Threshold for what counts as cyclical is presumably tuned per setup.

## Relevance to taste-lab
**Relevance 3. Section 4 (evaluation signals).**
- Second intrinsic candidate signal after INTUITOR's self-certainty: trajectory geometry. The review's signal taxonomy (certainty, geometry, probes) now has a concrete member per family.
- Grounded: reads hidden states, not self-report, so it survives the faithfulness objections to verbal confidence.

## Steal this
- Trajectory-shape features (cycle detectors) as cheap monitors for any iterative generation loop.
- Label-free + training-free as the bar for a deployable internal monitor.

## Kaushik's notes
<!-- yours -->
