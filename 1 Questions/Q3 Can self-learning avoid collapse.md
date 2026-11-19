---
type: question
title: "Q3. Can self-learning avoid collapse?"
id: Q3
status: active
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/question, question/Q3, status/active]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# Q3. Can self-learning avoid collapse?

> **In short**
> - **Question:** Can the model train itself on what its own good-or-bad signal likes, and not fall into collapse?
> - **Where it stands:** Active, but no plan yet. A known paper (He et al.) says this kind of self-training always collapses in the end.
> - **Next step:** Write the plan after Question 1 (does the model sense code quality?) and Question 2 (can the model steer its own code?). Read the GUARD paper first.

**Words used here**
- **Valence:** the model's inner good-or-bad feeling about something. We read it with a probe (a small classifier on the model's hidden numbers).
- **Collapse:** the model's output gets more and more alike and poorer, for example always short or repeated code, until it stops being useful.
- **Sharpening:** the model becomes more sure of what it already preferred. This often comes before collapse.
- **LoRA:** a cheap way to train a model. It changes only a small add-on set of weights.
- **Self-edit:** a small training update that the model makes from its own output.
- **Gated by valence:** the model keeps an update only if its valence says the result is good.
- **Neuromodulator controller:** a small controller modeled on brain chemicals (neuromodulators). It sets values such as how fast the model learns (the learning rate).
- **Novelty term:** an extra reward for output that is new and different. It works against collapse.
- **Intrinsic reward:** a reward that comes from inside the model, not from an outside check. Valence used as a reward is one.
- **Prior:** what the model already preferred before this training.
- **Ablation:** the same setup with one part removed, to see what that part does.
- **Arm:** one version of the experiment that we compare with the others.
- **Model Collapse Step:** a measure from He et al.: the training step where collapse starts.
- **RL / DPO:** two common ways to train a model from rewards or preferences.

## Hypothesis
*What we think is true.*

The model trains itself in rounds with small LoRA self-edits.
- Its valence decides which edits to keep.
- A neuromodulator controller sets the learning rate.
- A novelty term rewards new and different output.

We expect the model to stay sensible and varied for N rounds.
We expect the same setup without the novelty term to collapse, as He et al. predict ([[Self-reward sharpens then collapses (He 2026)]]).

## Why it matters
*Why this result is useful.*

This is the main result for the hopeful version of our paper.
It is also test 4 (self-reinforcing) of [[Four tests for own taste]].

## Evidence for
*Results from other papers that make this likely.*

- The closest design is Wu ([[Self-reward only within the same test result (Wu 2026)]]). The model's own judgment is a reward with a cap, and the tests make sure passing code always ranks above failing code. But Wu uses a judge in words, and does not look at style.

## Evidence against
*Results that make this less likely, or harder to prove.*

- He et al. found that every intrinsic reward collapses in the end. When it happens depends on the prior. Valence used as a reward is an intrinsic reward.
- Jin found that self-reward on code makes output shrink from about 7,300 to 1,000 tokens. It also removes the difference between right and wrong answers ([[Self-reward on code collapses to short code (Jin 2026)]]).
- Zhou found that self-judges get fooled, unless they first commit to their own answer. Style has no single answer to commit to ([[Self-judge training makes wrong look right (Zhou 2026)]]).
- Berg found that RL or DPO training connects an existing valence vector to choices, but does not move the vector ([[Hidden good-bad feeling changes choices (Berg 2026)]], welfare axis 2605.30232). This weakens our claim that taste "drifts away from where it started".

## What would kill this
*The result that makes us stop.*

We stop if the arm with the novelty term collapses at the same Model Collapse Step as the plain arm.
The Log below also proposes a second stop rule: output length or repetition collapses while the tests still pass.

## Next action
*What to do next.*

1. Write the plan after Question 1 (does the model sense code quality?) and Question 2 (can the model steer its own code?).
2. Read GUARD (2611.23476). It keeps an update only if it does not make results worse (a non-regression gate).
3. Add a control arm with a matched random reward. See [[Field map - Limits of self-learning]].

## Log
- 2026-11-19: created.
- 2026-11-19: renamed from `T3-closed-loop-novelty` ("Can valence-gated self-training escape sharpening collapse?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Closest design: [[Self-reward only within the same test result (Wu 2026)]] (own judgment as a capped reward, tests keep pass above fail; verbal judge, style excluded). Threats: self-reward on code collapses output length about 7,300 to 1,000 tokens and erases the right/wrong gap ([[Self-reward on code collapses to short code (Jin 2026)]]); self-judges get hacked unless they commit an answer first, which style lacks ([[Self-judge training makes wrong look right (Zhou 2026)]]); RL/DPO wires an existing valence vector to choice without moving it ([[Hidden good-bad feeling changes choices (Berg 2026)]], welfare axis 2605.30232), which weakens "drift from origin". Add a matched random-reward control and a "length or repetition collapse while tests pass" kill criterion. See [[Field map - Limits of self-learning]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-learning-from-its-own-judgment-avoid-collapse-T3` ("Can learning from its own judgment avoid collapse? (Q3)") to an ASD-STE100-style name and title.
- 2026-11-20: renamed to a plain name (file "Q3 Can self-learning avoid collapse"), so the name is clear at once. Old title: "Can a model learn from its own evaluation and not collapse? (Q3)". Codes T1 to T5 are now Q1 to Q5.
- 2026-11-20: rewritten in plain English (same facts).
