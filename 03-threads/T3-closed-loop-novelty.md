---
type: thread
id: T3
status: active
owner: harshit
created: 2026-11-19
updated: 2026-11-19
---

# T3: Can valence-gated self-training escape sharpening collapse?

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
