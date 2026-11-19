---
type: question
title: "Q5 (stopped). Can we make steering permanent?"
id: Q5
status: killed
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/question, question/Q5, status/killed]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# Q5 (stopped). Can we make steering permanent?

## Hypothesis
If a valence/taste steering vector improves readability at inference time (Q2), then a rank-one weight edit
W' = W + u vᵀ (u = steering direction, v from low-variance neurons) reproduces most of that effect with no steering at inference time and no training loop.

## Why it matters
This is your "without a massive training loop" claim made concrete. WSP anti-loop edits already behave like a
constant bias along a direction ([[A simple sort replaces the anti-loop edit (Fischetti 2026)]]), so the same move could work for taste.

## Evidence for
Rank-one edits fixed looping in Qwen3.5-0.8B, and a simple sort-based v matched the LP version.

## Evidence against
Taste is probably more distributed than a loop direction. WSP is known to struggle with distributed errors.

## What would kill this
The rank-one edit recovers less than 30% of the inference-steering readability gain, or damages pass rate.

## Next action
Harshit: promote or kill. Depends on Q2.

## Log
- 2026-11-19: created (proposed by Claude).
- 2026-11-19: renamed from `T5-consolidate-steering-rank-one` ("Can a taste direction be made permanent by a rank-one edit?") in the metacognition recenter.
- 2026-11-19: killed (status set on the user's instruction in the prior-art update). Steering-as-weights is known: ThinkEdit [2503.22048](https://arxiv.org/abs/2503.22048) ([[ThinkEdit - edit weights to think longer (Sun 2025)]]), Steer2Edit [2602.09870](https://arxiv.org/abs/2602.09870) ([[Steer2Edit - steering into small weight edits (Sun 2026)]]).
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-a-steering-direction-be-made-permanent-with-one-small-weight-edit-T5` ("Can a steering direction be made permanent with one small weight edit? (Q5)") to an ASD-STE100-style name and title.
- 2026-11-20: paper notes added for both prior-art links ([[ThinkEdit - edit weights to think longer (Sun 2025)]], [[Steer2Edit - steering into small weight edits (Sun 2026)]]). Residual not covered by either: direction from the model's own valence readout, code readability with tests fixed, recovery ratio vs steering, repeated self-edits. Steer2Edit App. H puts reasoning-length edits mostly in MLP neurons, which supports "Evidence against".
- 2026-11-20: renamed to a plain name (file "Q5 (stopped) Make steering permanent"), so the name is clear at once. Old title: "Can one small weight change make a steering direction permanent? (Q5)". Codes T1 to T5 are now Q1 to Q5.
