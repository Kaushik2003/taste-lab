---
type: question
title: "Q1. Does the model sense code quality?"
id: Q1
status: active
owner: harshit
created: 2026-11-19
updated: 2026-11-20
tags: [type/question, question/Q1, status/active]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# Q1. Does the model sense code quality?

## Hypothesis
On solutions to the same problem that all pass the tests, a valence readout from an open 8–32B model correlates
(Spearman ρ ≥ 0.4) with blind expert readability rankings. The correlation is not explained by length, familiarity (perplexity), or comment density.

## Why it matters
**Gating experiment.** If valence doesn't track quality, it can't be the evaluator, and Q2–Q5 change.

## Evidence for
- Emotion vectors predict and causally shift stated task preferences in Claude Sonnet 4.5 ([[Emotion directions drive choices in Claude (Anthropic 2026)]]).
- Emotion states are linearly decodable at 98–100% in open 7–32B models ([[Models do not report injected pain (Ferrara 2026)]]).
- A value axis in Qwen3-8B separates correct from corrupted code, including obfuscated names (d = 0.69) ([[Value axis - model knows it is on track (Jiang 2026)]]).
- Readability contrasts (comments, naming, branching) give separate, steerable directions in 13–14B code models ([[Steer code readability inside the model (Gao 2026)]]). Gao never rates real code against humans, so Q1 is not scooped.
- Valence held only in the KV cache shifts later choices in 5 of 7 open models ([[Hidden good-bad feeling changes choices (Berg 2026)]]).
- Hidden-state probes read self-correctness better than verbal reports ([[Models know when they are right (Zhang 2025)]], [[Few neurons predict right answers (Xu 2026)]]).

## Evidence against
- Same paper: open models can't *report* those states zero-shot. Readout must be probe-based, or trained.
- High value goes with fewer lines, comments and type hints, so valence may reward terseness ([[Value axis - model knows it is on track (Jiang 2026)]]). Gao's readability direction adds comments, so the two may point opposite ways on comment density ([[Steer code readability inside the model (Gao 2026)]]).
- Input-only (layer-0) probes match in-context self-reports; readability is visible in the text, so a layer-0 probe may match our readout ([[Introspection claims fail basic checks (Singh 2026)]]).
- Berg's valence effect is missing in Qwen3-32B and Gemma-3-27B, which puts the 32B scale-up at risk ([[Hidden good-bad feeling changes choices (Berg 2026)]]).
- Code confidence rewards drift toward short output ([[Self-reward on code collapses to short code (Jin 2026)]]).
- Valence may track familiarity/perplexity. Low-perplexity code is often the boilerplate-ish "slop" we want to avoid.

## What would kill this
ρ < 0.2 after controlling for perplexity and length, across two model families.

## Next action
Run [[1 Questions/Q1 experiment - read the signal/Plan|Q1 experiment - read the signal]] stage A on Qwen3.x-8B with ~50 problems × 8 passing solutions each.

## Log
- 2026-11-19: created. Pivot: the "grounded" test uses a probe readout first, with trained self-report as a later step.
- 2026-11-19: renamed from `T1-valence-tracks-quality` ("Does the model's internal valence track code quality?") in the metacognition recenter.
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change. Fixed the exp01 link to point at its spec.
- 2026-11-20: renamed from `does-the-models-internal-evaluation-signal-track-code-quality-T1` ("Does the model's internal evaluation signal track code quality? (Q1)") to an ASD-STE100-style name and title.
- 2026-11-20: prior-art update. Gao steers readability but never rates real code against humans; Q1 is not scooped. The bar is higher: valence must beat input-only, readability-direction and value-axis baselines, within-problem, anchors excluded.
- 2026-11-20: proposed (Claude, for Harshit to accept): new kill line. Within-problem partial ρ < 0.2 on natural passing solutions (anchors excluded) after length, perplexity and comment ratio, in two families; or valence adds < 0.05 ρ over a layer-0 probe plus a Gao-style readability direction; or ρ falls inside the 95th percentile of norm-matched random directions. Proposed cheap pre-check: valence vs a public human-rated readability set (Buse-Weimer or Scalabrino, Java) against a layer-0 probe, about one GPU afternoon, before the 2–3 days of rating. exp01 controls to add: layer-0 probe, Gao direction, Jiang value axis, Xu correctness probe, comment-stripped rerun, other-model and human solutions, rater reliability (≥5 blind raters, Krippendorff's alpha). Source: critic pass, see sources [2401.14936](https://arxiv.org/abs/2401.14936), [2404.13076](https://arxiv.org/abs/2404.13076), [2510.16579](https://arxiv.org/abs/2510.16579) [unverified numbers].
- 2026-11-20: renamed to a plain name (file "Q1 Does the model sense code quality"), so the name is clear at once. Old title: "Does the internal evaluation signal of the model show code quality? (Q1)". Codes T1 to T5 are now Q1 to Q5.
