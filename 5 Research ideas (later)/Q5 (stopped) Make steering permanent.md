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

> **In short**
> - **Question:** Can we turn a steering push into one small, permanent change to the weights?
> - **Where it stands:** Stopped on 2026-11-19, on Harshit's instruction. Two earlier papers already show that steering can be written into weights: [[ThinkEdit - edit weights to think longer (Sun 2025)|ThinkEdit (Sun 2025)]] and [[Steer2Edit - steering into small weight edits (Sun 2026)|Steer2Edit (Sun 2026)]]. So the main idea is not new.
> - **Next step:** None. Some parts are still not covered by those papers (see the last part of the Log). They may come back inside other questions.

**Words used here**
- **Steering:** adding a fixed direction to the model's hidden numbers while it writes, to push its output one way.
- **Steering vector:** the direction that we add.
- **Valence / taste:** the model's inner good-or-bad feeling about something.
- **Inference time:** when the model runs and writes, not when it trains.
- **Weights:** the stored numbers that the model learns in training.
- **Rank-one edit:** the simplest possible weight change. It adds one direction to a weight matrix. In symbols: W' = W + u vᵀ.
  - u is the steering direction (what to add).
  - v chooses where to add it. It comes from neurons whose values change little (low-variance neurons).
- **WSP (weight-space programming):** a method where an agent reads a model's weights and edits them by hand.
- **Looping:** the model repeats the same text without end.
- **LP (linear program):** a standard math method to find the best value under limits. Here it chose v.
- **Pass rate:** the part of solutions that pass all tests.

## Hypothesis
*What we thought was true.*

Suppose a valence or taste steering vector makes code more readable at inference time.
This is Question 2 (can the model steer its own code?).
Then a rank-one weight edit, W' = W + u vᵀ, gives most of the same gain.
- u is the steering direction.
- v comes from low-variance neurons.

It needs no steering at inference time and no training loop.

## Why it matters
*Why this result was useful.*

It makes our claim "without a massive training loop" concrete.
WSP edits that stop looping already act like a constant push along one direction ([[A simple sort replaces the anti-loop edit (Fischetti 2026)]]).
So the same move could work for taste.

## Evidence for
*Results from other papers that made this likely.*

Rank-one edits fixed looping in Qwen3.5-0.8B.
A simple v, found by sorting, worked as well as the v from the LP method.

## Evidence against
*Results that made this less likely.*

Taste is probably spread over many parts of the model, more than a loop direction is.
WSP is known to have problems with errors that are spread out like this.

## What would kill this
*The result that would make us stop.*

We would stop if one of these is true:
- The rank-one edit keeps less than 30% of the readability gain from steering at inference time.
- The edit lowers the pass rate.

## Next action
*What to do next.*

None. The question is stopped (see "In short").
The old next action was: "Harshit: promote or kill. Depends on Question 2." Harshit chose to stop it.

## Log
- 2026-11-19: created (proposed by Claude).
- 2026-11-19: renamed from `T5-consolidate-steering-rank-one` ("Can a taste direction be made permanent by a rank-one edit?") in the metacognition recenter.
- 2026-11-19: killed (status set on the user's instruction in the prior-art update). Steering-as-weights is known: ThinkEdit [2503.22048](https://arxiv.org/abs/2503.22048) ([[ThinkEdit - edit weights to think longer (Sun 2025)]]), Steer2Edit [2602.09870](https://arxiv.org/abs/2602.09870) ([[Steer2Edit - steering into small weight edits (Sun 2026)]]).
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-a-steering-direction-be-made-permanent-with-one-small-weight-edit-T5` ("Can a steering direction be made permanent with one small weight edit? (Q5)") to an ASD-STE100-style name and title.
- 2026-11-20: paper notes added for both prior-art links ([[ThinkEdit - edit weights to think longer (Sun 2025)]], [[Steer2Edit - steering into small weight edits (Sun 2026)]]). Residual not covered by either: direction from the model's own valence readout, code readability with tests fixed, recovery ratio vs steering, repeated self-edits. Steer2Edit App. H puts reasoning-length edits mostly in MLP neurons, which supports "Evidence against".
- 2026-11-20: renamed to a plain name (file "Q5 (stopped) Make steering permanent"), so the name is clear at once. Old title: "Can one small weight change make a steering direction permanent? (Q5)". Codes T1 to T5 are now Q1 to Q5.
- 2026-11-20: rewritten in plain English (same facts).
