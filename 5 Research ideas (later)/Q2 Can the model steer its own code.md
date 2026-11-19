---
type: question
title: "Q2. Can the model steer its own code?"
id: Q2
status: parked
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/question, question/Q2, status/parked]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# Q2. Can the model steer its own code?

> **In short**
> - **Question:** Can the model use its own good-or-bad signal to make its code easier to read, with no change to its weights?
> - **Where it stands:** Parked while we write the literature review (from 2026-11-20). It needs the first result of Question 1 (does the model sense code quality?).
> - **Next step:** When stage A of Question 1 passes, plan this experiment. Picking the best of several answers looks more likely to work than steering.

**Words used here**
- **Valence:** the model's inner good-or-bad feeling about something. We read it with a probe (a small classifier on the model's hidden numbers).
- **Best-of-n:** the model writes n answers, and we keep the one with the best score. Here the score is the model's own valence.
- **Reranking:** putting finished answers in a new order by a score. Best-of-n is one type of reranking.
- **Valence direction:** a fixed pattern in the hidden numbers that goes with "good" feeling.
- **Steering:** adding a direction to the hidden numbers while the model writes, to push its output one way.
- **Inference time:** when the model runs and writes, not when it trains.
- **Weights:** the stored numbers that the model learns in training.
- **LoRA:** a cheap way to train a model. It changes only a small add-on set of weights.
- **Pass rate:** the part of solutions that pass all tests.
- **Length-matched random baseline:** we pick answers at random, but with the same lengths as the chosen ones. This shows if the gain only comes from length.
- **Self-judge gap:** how much the model's own judge likes the answer it picked, minus how good that answer really is. A big gap means the judge is fooled.

## Hypothesis
*What we think is true.*

The model can improve its code in one of two ways, or both:
- **Pick:** it writes n solutions and picks the one with the best valence (best-of-n).
- **Push:** it adds the valence direction to its hidden numbers while it writes (steering).

We expect blind raters (people who do not know our goal) to rate this code as more readable than a randomly picked solution.
We expect the test pass rate to stay the same.

## Why it matters
*Why this result is useful.*

This is taste with zero weight changes.
It is the cheapest proof that the signal *does* something.
It is also the "steer its own thinking" half of our main claim.

## Evidence for
*Results from other papers that make this likely.*

- Kirin (2607.18553) found that reranking gave a gain, so best-of-n has support.
- Gao steers a model toward readable code ([[Steer code readability inside the model (Gao 2026)]]). But Gao never runs the code or rates it.
- The closest earlier work is Karpf ([[Outside controller steers thinking modes (Karpf 2026)]]). It uses the same name and the same loop shape. But humans pick the directions, and the evidence is only examples, not numbers.

## Evidence against
*Results that make this less likely, or harder to prove.*

- Kirin (2607.18553) found that steering driven by a probe, and LoRA, gave no gain. This is a risk for the "push" arm.
- Zhou found that in code, the self-judge gap gets bigger as n gets bigger: from 0.20 to 0.588 at n = 16 ([[Self-judge training makes wrong look right (Zhou 2026)]]). We must measure this gap.
- The baseline to beat: Zhang uses a probe to stop the model early when it is probably right ([[Models know when they are right (Zhang 2025)]]).

## What would kill this
*The result that makes us stop.*

We stop if one of these is true:
- The code is no more readable than with a length-matched random baseline.
- All of the gain comes from shorter or longer code.

## Next action
*What to do next.*

Wait. This depends on stage A of Question 1 (does the model sense code quality?).

## Log
- 2026-11-19: created.
- 2026-11-19: renamed from `T2-inference-time-taste` ("Does steering with valence at inference time make code more readable?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Closest prior art: [[Outside controller steers thinking modes (Karpf 2026)]] (same name and loop shape; directions come from human scientists, evidence qualitative) and [[Steer code readability inside the model (Gao 2026)]] (steers for readability but never runs or rates the code). Baseline to beat: probe-driven early exit in [[Models know when they are right (Zhang 2025)]]. Against the steering arm: Kirin 2607.18553 found probe-driven steering and LoRA gave no gain, while reranking did, so best-of-n has more support. Self-judge gap widens with n in code (0.20 to 0.588 at n=16, [[Self-judge training makes wrong look right (Zhou 2026)]]): measure it. See [[Gaps in the field]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-metacognitive-steering-at-inference-time-improve-code-T2` ("Can metacognitive steering at inference time improve code? (Q2)") to an ASD-STE100-style name and title.
- 2026-11-20: renamed to a plain name (file "Q2 Can the model steer its own code"), so the name is clear at once. Old title: "Can metacognitive steering during inference improve code? (Q2)". Codes T1 to T5 are now Q1 to Q5.
- 2026-11-20: rewritten in plain English (same facts).
- 2026-11-20: parked on the user's instruction. The current goal is the literature review, not experiments.
