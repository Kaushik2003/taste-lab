---
type: thread
title: "Can metacognitive steering during inference improve code? (T2)"
id: T2
status: active
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/thread, thread/T2, status/active]
links: ["[[metacognition-monitor-control]]", "[[four-taste-tests]]"]
---

# Can metacognitive steering during inference improve code? (T2)

## Hypothesis
Best-of-n selection by the model's own valence, and/or adding the valence direction during generation, raises
blind readability ratings vs. random selection, with test pass rate unchanged.

## Why it matters
Taste with zero weight changes. It's the cheapest proof that the signal *does* something, and it's the "steer its own thinking" half of the claim.

## What would kill this
No readability gain over a length-matched random baseline, or gains that come entirely from shorter or longer code.

## Next action
Blocked on T1 stage A.

## Log
- 2026-11-19: created.
- 2026-11-19: renamed from `T2-inference-time-taste` ("Does steering with valence at inference time make code more readable?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Closest prior art: [[2026-karpf-metacognitive-steering]] (same name and loop shape; directions come from human scientists, evidence qualitative) and [[2026-gao-readability-repe]] (steers for readability but never runs or rates the code). Baseline to beat: probe-driven early exit in [[2025-zhang-reasoning-models-know-when-right]]. Against the steering arm: Kirin 2607.18553 found probe-driven steering and LoRA gave no gain, while reranking did, so best-of-n has more support. Self-judge gap widens with n in code (0.20 to 0.588 at n=16, [[2026-zhou-self-play-judge-hacking]]): measure it. See [[landscape-gap-table]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-metacognitive-steering-at-inference-time-improve-code-T2` ("Can metacognitive steering at inference time improve code? (T2)") to an ASD-STE100-style name and title.
