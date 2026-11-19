---
type: question
title: "Q3. Can self-learning avoid collapse?"
id: Q3
status: active
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/question, question/Q3, status/active]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# Q3. Can self-learning avoid collapse?

## Hypothesis
LoRA self-edits gated by valence, with the learning rate set by a neuromodulator controller, plus a novelty term,
stay coherent and diverse for N rounds. The no-novelty ablation collapses (as [[Self-reward sharpens then collapses (He 2026)]] predicts).

## Why it matters
This is the headline result for the optimistic paper, and test 4 of [[Four tests for own taste]].

## Evidence against
He et al.: every intrinsic reward eventually collapses, and timing depends on the prior. Valence-as-reward is an intrinsic reward.

## What would kill this
The novelty arm collapses at the same Model Collapse Step as the plain arm.

## Next action
Spec after Q1/T2. Read GUARD (2611.23476) for non-regression gating.

## Log
- 2026-11-19: created.
- 2026-11-19: renamed from `T3-closed-loop-novelty` ("Can valence-gated self-training escape sharpening collapse?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Closest design: [[Self-reward only within the same test result (Wu 2026)]] (own judgment as a capped reward, tests keep pass above fail; verbal judge, style excluded). Threats: self-reward on code collapses output length about 7,300 to 1,000 tokens and erases the right/wrong gap ([[Self-reward on code collapses to short code (Jin 2026)]]); self-judges get hacked unless they commit an answer first, which style lacks ([[Self-judge training makes wrong look right (Zhou 2026)]]); RL/DPO wires an existing valence vector to choice without moving it ([[Hidden good-bad feeling changes choices (Berg 2026)]], welfare axis 2605.30232), which weakens "drift from origin". Add a matched random-reward control and a "length or repetition collapse while tests pass" kill criterion. See [[Field map - Limits of self-learning]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-learning-from-its-own-judgment-avoid-collapse-T3` ("Can learning from its own judgment avoid collapse? (Q3)") to an ASD-STE100-style name and title.
- 2026-11-20: renamed to a plain name (file "Q3 Can self-learning avoid collapse"), so the name is clear at once. Old title: "Can a model learn from its own evaluation and not collapse? (Q3)". Codes T1 to T5 are now Q1 to Q5.
