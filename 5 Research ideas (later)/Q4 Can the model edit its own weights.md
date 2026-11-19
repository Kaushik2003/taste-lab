---
type: question
title: "Q4. Can the model edit its own weights?"
id: Q4
status: parked
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/question, question/Q4, status/parked]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# Q4. Can the model edit its own weights?

> **In short**
> - **Question:** Can a model find one of its own faults and fix it by changing its own weights directly?
> - **Where it stands:** Parked (on hold). Even the strongest AI agents cannot yet do this well for other models.
> - **Next step:** None for now. A possible way back: two new methods (Tree-Ising and Exploring WSP) make weight edits from normal model runs, with no outside agent. The model could use them on a direction from its own good-or-bad signal. The question stays parked until Harshit decides.

**Words used here**
- **Weights:** the stored numbers that the model learns in training.
- **Failure mode:** a type of mistake that the model makes again and again, for example looping (it repeats the same text without end).
- **WSP (weight-space programming):** a method where an agent reads a model's weights and edits them by hand, like code ([[Field map - Changes that stay in the weights]]).
- **Frontier agent / frontier editor:** a top AI model that does this editing from the outside.
- **LM:** language model.
- **Rank-one edit:** the simplest possible weight change. It adds one direction to a weight matrix.
- **Forward pass:** one normal run of the model on an input, with no training.
- **Parked:** on hold. We do not work on it now, but we may come back.

## Hypothesis
*What we think is true.*

A model can find where one of its own failure modes lives in its weights (for example looping).
It can then fix it with WSP-style edits.
We expect it to do this as well as an outside frontier editor.

## Why parked
*Why we stopped for now.*

WeightBench (2611.18553) found that frontier agents cannot yet fix language models reliably.
A small model that edits itself has an even harder task.
We planned to come back after Question 5 (can we make steering permanent?) showed if rank-one edits that make a change permanent work. Question 5 is now stopped.

## Log
- 2026-11-19: created and parked.
- 2026-11-19: renamed from `T4-self-wsp` ("Can a model weight-space-program *itself*?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Tree-Ising (2611.14210) and Exploring WSP (2611.09382) compute edits from forward passes with no frontier agent. Possible unpark path: the model runs that recipe on a direction from its own evaluation signal. Still parked. See [[Field map - Changes that stay in the weights]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-a-model-edit-its-own-weights-T4` ("Can a model edit its own weights? (Q4)") to an ASD-STE100-style name and title.
- 2026-11-20: renamed to a plain name (file "Q4 Can the model edit its own weights"), so the name is clear at once. Old title: "Can a model change its own weights? (Q4)". Codes T1 to T5 are now Q1 to Q5.
- 2026-11-20: rewritten in plain English (same facts).
