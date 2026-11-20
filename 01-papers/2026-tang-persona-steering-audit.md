---
type: paper
title: "Safety Side Effects of Preventative Persona Steering: An Empirical Audit"
status: skimmed
arxiv: 2611.17620
url: https://arxiv.org/abs/2611.17620
authors: Sabrina Tang, Nikolai Vo, Carson Murillo, Chira Sukumarnpiti, Sarah Wilson (UCI / Toledo / UCSD / BCC / Google)
year: 2026
venue: preprint
relevance: 2
section: 6
tier: skim
tests: []
components: [controller]
tags: [type/paper, section/6, component/controller, status/skimmed, relevance/2, steering, safety-audit, side-effects]
links: ["[[2025-chen-persona-vectors]]", "[[landscape-persistent-control]]"]
---

# Safety Side Effects of Preventative Persona Steering (audit)

**One line:** Independent audit of preventative persona steering ([[2025-chen-persona-vectors]]): the original validation measured capability (MMLU) alone; on three models with three safety benchmarks plus trait expression and coherence, preventative steering still changes refusal behavior, by an amount that depends on the trait. Not safety-neutral.

## Claim
Steering methods should be evaluated on several safety benchmarks, not capability alone; preventative steering's side effects are real and trait-dependent ([abs](https://arxiv.org/abs/2611.17620)).

## Mechanism
Empirical audit: preventative steering of sycophancy and hallucination vectors on three models; refusal behavior, trait expression, coherence, MMLU.

## Evidence
Refusal behavior changes under preventative steering; magnitude trait-dependent [unverified: effect sizes not extracted].

## Limits / what they didn't show
- Audit scope: three models, two traits; says nothing about whether side effects scale with vector norm or layer choice.

## Relevance to taste-lab
**The standing warning for any steering-based control we propose.** If we steer a valence direction (inference or training-time), the evaluation bar is multi-benchmark side-effect profiling, not just "did taste improve and MMLU survive". One line in Limits; also a design input for exp01's control battery.
- Prior-art check: n/a (audit).

## Steal this
- The audit battery (trait expression + coherence + safety benchmarks + refusal) as the default eval grid for steering experiments.

## Kaushik's notes
<!-- yours -->
