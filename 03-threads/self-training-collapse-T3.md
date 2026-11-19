---
type: thread
title: "Can a model learn from its own evaluation and not collapse? (T3)"
id: T3
status: active
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/thread, thread/T3, status/active]
links: ["[[metacognition-monitor-control]]", "[[four-taste-tests]]"]
---

# Can a model learn from its own evaluation and not collapse? (T3)

## Hypothesis
LoRA self-edits gated by valence, with the learning rate set by a neuromodulator controller, plus a novelty term,
stay coherent and diverse for N rounds. The no-novelty ablation collapses (as [[2026-he-unsupervised-rlvr-limits]] predicts).

## Why it matters
This is the headline result for the optimistic paper, and test 4 of [[four-taste-tests]].

## Evidence against
He et al.: every intrinsic reward eventually collapses, and timing depends on the prior. Valence-as-reward is an intrinsic reward.

## What would kill this
The novelty arm collapses at the same Model Collapse Step as the plain arm.

## Next action
Spec after T1/T2. Read GUARD (2611.23476) for non-regression gating.

## Log
- 2026-11-19: created.
- 2026-11-19: renamed from `T3-closed-loop-novelty` ("Can valence-gated self-training escape sharpening collapse?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Closest design: [[2026-wu-behavioral-self-rewarding]] (own judgment as a capped reward, tests keep pass above fail; verbal judge, style excluded). Threats: self-reward on code collapses output length about 7,300 to 1,000 tokens and erases the right/wrong gap ([[2026-jin-intrinsic-rewards-code]]); self-judges get hacked unless they commit an answer first, which style lacks ([[2026-zhou-self-play-judge-hacking]]); RL/DPO wires an existing valence vector to choice without moving it ([[2026-berg-hidden-valence]], welfare axis 2605.30232), which weakens "drift from origin". Add a matched random-reward control and a "length or repetition collapse while tests pass" kill criterion. See [[landscape-self-improvement-limits]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-learning-from-its-own-judgment-avoid-collapse-T3` ("Can learning from its own judgment avoid collapse? (T3)") to an ASD-STE100-style name and title.
