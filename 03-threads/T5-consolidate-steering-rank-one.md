---
type: thread
id: T5
status: proposed
owner: harshit
created: 2026-11-19
updated: 2026-11-19
---

# T5 (proposed by Claude): Can a taste direction be made permanent by a rank-one edit?

## Hypothesis
If a valence/taste steering vector improves readability at inference time (T2), then a rank-one weight edit
W' = W + u vᵀ (u = steering direction, v from low-variance neurons) reproduces most of that effect with no steering at inference time and no training loop.

## Why it matters
This is your "without a massive training loop" claim made concrete. WSP anti-loop edits already behave like a
constant bias along a direction ([[2026-fischetti-just-sort-it]]), so the same move could work for taste.

## Evidence for
Rank-one edits fixed looping in Qwen3.5-0.8B, and a simple sort-based v matched the LP version.

## Evidence against
Taste is probably more distributed than a loop direction. WSP is known to struggle with distributed errors.

## What would kill this
The rank-one edit recovers less than 30% of the inference-steering readability gain, or damages pass rate.

## Next action
Harshit: promote or kill. Depends on T2.
