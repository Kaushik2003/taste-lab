---
type: paper
title: "EpiCaR: Knowing What You Don't Know Matters for Better Reasoning in LLMs"
status: skimmed
arxiv: 2601.06786
url: https://arxiv.org/abs/2601.06786
authors: Jewon Yeom, Jaewon Sok, Seonghyeon Park, Jeongjae Park, Taesup Kim
year: 2026
venue: arXiv preprint
relevance: 2
section: 6
tier: skim
tests: []
components: [monitoring]
tags: [type/paper, section/6, component/monitoring, status/skimmed, relevance/2, role/prior-art, metacognition, calibration, self-training, collapse]
links: ["[[Self-reward sharpens then collapses (He 2026)]]", "[[Models are overconfident about their own abilities (Barkan 2025)]]", "[[Models mostly know what they know (Kadavath 2022)]]"]
---

# EpiCaR: Epistemically-calibrated Reasoning

**One line:** Standard self-training on model-generated reasoning quietly destroys calibration - distributions collapse toward overconfident point estimates - and a joint objective that optimizes reasoning *and* calibration together Pareto-dominates the usual recipe.

**Why it matters to us:** The training-dynamics version of He's self-reward collapse: any loop where a model learns from its own output must protect the uncertainty representation, or the monitor degrades exactly as the reasoner improves. Directly constrains how a self-improving taste loop could be trained safely.

Source: [arXiv 2601.06786](https://arxiv.org/abs/2601.06786) (11 January 2026). Abstract-level note.

## Claim
Iterative self-training reinforces successful reasoning paths at a substantial calibration cost (a form of model collapse); reframing reasoning training as joint epistemic learning - how to reason and when to be trusted - recovers both ([abstract](https://arxiv.org/abs/2601.06786)).

## Mechanism
- EpiCaR objective: jointly optimize reasoning performance and calibration within iterative SFT, using explicit self-evaluation signals.

## Evidence
- Pareto-superior accuracy and calibration over standard baselines on Llama-3 and Qwen-3 families, especially 3B+ ([abstract](https://arxiv.org/abs/2601.06786)).
- Generalizes OOD to GSM8K and MBPP.

## Limits / what they didn't show
- Needs explicit self-evaluation signals in the training data; where those come from at scale is open.
- Calibration measured on tasks with ground truth; taste-like judgments have none.
- The effect is weak below ~3B.

## Relevance to taste-lab
**Relevance 2. Section 6 (limits/failure modes).**
- The second collapse result after He 2026: self-referential training loops eat the uncertainty signal. Any persistent-self-state training must carry a calibration-preservation term.
- Gives the fix, not just the failure: joint objective. Useful as the constructive half of the collapse story.

## Steal this
- Pareto-front reporting (accuracy vs calibration) as the honest way to evaluate any self-training scheme.
- "Reinforce successes = collapse pressure" as a standing warning for the taste-training loop design.

## Kaushik's notes
<!-- yours -->
