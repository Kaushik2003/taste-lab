---
type: paper
title: "Metacognitive Reuse: Turning Recurring LLM Reasoning Into Concise Behaviors"
status: skimmed
arxiv: 2509.13237
url: https://arxiv.org/abs/2509.13237
authors: Aniket Didolkar, Nicolas Ballas, Sanjeev Arora, Anirudh Goyal
year: 2025
venue: arXiv preprint
relevance: 3
section: 5
tier: deep
tests: [stable]
components: [consolidation]
tags: [type/paper, section/5, test/stable, component/consolidation, status/skimmed, relevance/3, role/prior-art, metacognition, self-improvement, consolidation, skills]
links: ["[[Models name the skills a problem needs (Didolkar 2024)]]", "[[MoT - models improve by remembering their own good thinking (Li 2023)]]", "[[RISE - recursive introspection improves own answers (Qu 2024)]]"]
---

# Metacognitive Reuse: Turning Recurring Reasoning Into Concise Behaviors

**One line:** The model reads its own past reasoning traces, names the recurring fragments ("behaviors"), stores them in a handbook, and reuses them in-context or distills them into weights. Up to 46% fewer reasoning tokens at equal or better accuracy, and +10 points over critique-and-revise in self-improvement.

**Why it matters to us:** This is the consolidation rung of the ladder, done with metacognition doing the extraction: memory (MoT) -> reuse (this) -> weight edits (RISE, SFT). The behavior handbook is a persistent, inspectable self-state - the closest thing to an explicit skill-level self-model in current systems.

Source: [arXiv 2509.13237](https://arxiv.org/abs/2509.13237) (16 September 2025). Abstract-level note.

## Claim
Recurring reasoning fragments can be converted by the model's own metacognitive analysis into named, reusable behaviors; conditioning on or distilling these behaviors improves reasoning efficiency and accuracy ([abstract](https://arxiv.org/abs/2509.13237)).

## Mechanism
- Metacognitive analysis of prior traces extracts behavior = name + instruction.
- Behavior handbook: in-context supply at inference, or SFT distillation into parameters.
- Three regimes: behavior-conditioned inference, behavior-guided self-improvement (no weight updates), behavior-conditioned SFT.

## Evidence
- Up to 46% fewer reasoning tokens with matched or better accuracy ([abstract](https://arxiv.org/abs/2509.13237)).
- Self-improvement regime: up to 10% higher accuracy than naive critique-and-revise.
- Behavior-conditioned SFT beats conventional SFT on the same traces.

## Limits / what they didn't show
- Extraction quality depends on the model's own analysis of its traces; no check that the behaviors are what the model actually computes internally.
- Reasoning benchmarks (math-flavored); nothing on open-ended or evaluative tasks.
- The handbook grows by addition; no selection or forgetting mechanism.

## Relevance to taste-lab
**Relevance 3. Section 5.**
- Consolidation is where a taste would live: repeated good judgments -> named, reusable evaluative behaviors. The handbook format is directly adoptable for taste heuristics.
- The three-regime comparison (in-context vs self-improve vs distill) is the design space for how permanent an acquired preference should be.

## Steal this
- The behavior handbook (name + instruction, extracted from own traces) as the format for a taste handbook.
- Their three-regime experimental layout as the protocol for testing persistence levels.

## Kaushik's notes
<!-- yours -->
