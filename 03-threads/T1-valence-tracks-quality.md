---
type: thread
id: T1
status: active
owner: harshit
created: 2026-11-19
updated: 2026-11-19
---

# T1: Does the model's internal valence track code quality?

## Hypothesis
On solutions to the same problem that all pass the tests, a valence readout from an open 8–32B model correlates
(Spearman ρ ≥ 0.4) with blind expert readability rankings. The correlation is not explained by length, familiarity (perplexity), or comment density.

## Why it matters
**Gating experiment.** If valence doesn't track quality, it can't be the evaluator, and T2–T5 change.

## Evidence for
- Emotion vectors predict and causally shift stated task preferences in Claude Sonnet 4.5 ([[2026-anthropic-emotion-concepts]]).
- Emotion states are linearly decodable at 98–100% in open 7–32B models ([[2026-ferrara-all-quiet-pain]]).

## Evidence against
- Same paper: open models can't *report* those states zero-shot. Readout must be probe-based, or trained.
- Valence may track familiarity/perplexity. Low-perplexity code is often the boilerplate-ish "slop" we want to avoid.

## What would kill this
ρ < 0.2 after controlling for perplexity and length, across two model families.

## Next action
Run [[exp01-valence-probe]] stage A on Qwen3.x-8B with ~50 problems × 8 passing solutions each.

## Log
- 2026-11-19: created. Pivot: the "grounded" test uses a probe readout first, with trained self-report as a later step.
