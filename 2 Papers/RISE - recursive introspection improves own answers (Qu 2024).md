---
type: paper
title: "Recursive Introspection: Teaching Language Model Agents How to Self-Improve (RISE)"
status: skimmed
arxiv: 2407.18219
url: https://arxiv.org/abs/2407.18219
authors: Yuxiao Qu, Tianjun Zhang, Naman Garg, Aviral Kumar
year: 2024
venue: ICML 2024 Workshop
relevance: 2
section: 6
tier: skim
tests: []
components: [controller, consolidation]
tags: [type/paper, section/6, component/controller, component/consolidation, status/skimmed, relevance/2, self-improvement, fine-tuning, error-correction, role/prior-art]
links: ["[[MARS - metacognitive reflection in one cycle (Hou 2026)]]", "[[Self-improving agents need intrinsic metacognition (Liu 2025)]]", "[[Q3 Can self-learning avoid collapse]]"]
---

# RISE: Recursive Introspection

**One line:** Fine-tune LLMs so that more turns actually help: pose single-turn problem solving as a multi-turn MDP and train on iterative correction data; Llama2/3 and Mistral then keep improving their own answers over turns, beating single-turn strategies at equal compute, scaling with model capability.

## Claim
Sequential self-improvement is trainable even though base models barely show it ([abs](https://arxiv.org/abs/2407.18219), [project](https://cohenqu.github.io/rise.github.io/)).

## Mechanism
Multi-turn MDP with prompt as initial state; online imitation / RL-inspired data collection teaching the model to alter responses after unsuccessful attempts, optionally with environment feedback.

## Evidence
Math reasoning gains with more turns; outperforms single-turn sampling at matched inference compute; larger benefits on more capable models; one-turn ability preserved [unverified: exact numbers].

## Limits / what they didn't show
- Correction target is the correct answer: environment or answer feedback defines the direction. No internal evaluation signal, no taste.
- Math only; multi-turn gains in open-ended domains untested.

## Relevance to taste-lab
**Trained self-correction without a self-evaluator.** RISE teaches the control move (revise after failure) while an external signal marks failure. Pair with MARS ([[MARS - metacognitive reflection in one cycle (Hou 2026)]]) in section 6 as the two trained-reflection baselines; both stop where our question starts.
- Prior-art check: **A no. B no.**

## Steal this
- Multi-turn MDP framing for the control stage of the loop.
- "More turns help only if trained" as a caution for inference-time control experiments.

## Kaushik's notes
<!-- yours -->
