---
type: question
title: "Q2. Can the model steer its own code?"
id: Q2
status: active
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/question, question/Q2, status/active]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# Q2. Can the model steer its own code?

## Hypothesis
Best-of-n selection by the model's own valence, and/or adding the valence direction during generation, raises
blind readability ratings vs. random selection, with test pass rate unchanged.

## Why it matters
Taste with zero weight changes. It's the cheapest proof that the signal *does* something, and it's the "steer its own thinking" half of the claim.

## What would kill this
No readability gain over a length-matched random baseline, or gains that come entirely from shorter or longer code.

## Next action
Blocked on Q1 stage A.

## Log
- 2026-11-19: created.
- 2026-11-19: renamed from `T2-inference-time-taste` ("Does steering with valence at inference time make code more readable?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Closest prior art: [[Outside controller steers thinking modes (Karpf 2026)]] (same name and loop shape; directions come from human scientists, evidence qualitative) and [[Steer code readability inside the model (Gao 2026)]] (steers for readability but never runs or rates the code). Baseline to beat: probe-driven early exit in [[Models know when they are right (Zhang 2025)]]. Against the steering arm: Kirin 2607.18553 found probe-driven steering and LoRA gave no gain, while reranking did, so best-of-n has more support. Self-judge gap widens with n in code (0.20 to 0.588 at n=16, [[Self-judge training makes wrong look right (Zhou 2026)]]): measure it. See [[Gaps in the field]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-metacognitive-steering-at-inference-time-improve-code-T2` ("Can metacognitive steering at inference time improve code? (Q2)") to an ASD-STE100-style name and title.
- 2026-11-20: renamed to a plain name (file "Q2 Can the model steer its own code"), so the name is clear at once. Old title: "Can metacognitive steering during inference improve code? (Q2)". Codes T1 to T5 are now Q1 to Q5.
