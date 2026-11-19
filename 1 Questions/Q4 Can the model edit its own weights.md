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

## Hypothesis
A model can localize and repair one of its own failure modes (e.g. looping) via WSP-style edits, matching an external frontier editor.

## Why parked
WeightBench (2611.18553): frontier agents can't yet reliably patch LMs, and a small model editing itself is harder still. Revisit after Q5 shows whether rank-one consolidation works.

## Log
- 2026-11-19: created and parked.
- 2026-11-19: renamed from `T4-self-wsp` ("Can a model weight-space-program *itself*?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Tree-Ising (2611.14210) and Exploring WSP (2611.09382) compute edits from forward passes with no frontier agent. Possible unpark path: the model runs that recipe on a direction from its own evaluation signal. Still parked. See [[Field map - Changes that stay in the weights]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-a-model-edit-its-own-weights-T4` ("Can a model edit its own weights? (Q4)") to an ASD-STE100-style name and title.
- 2026-11-20: renamed to a plain name (file "Q4 Can the model edit its own weights"), so the name is clear at once. Old title: "Can a model change its own weights? (Q4)". Codes T1 to T5 are now Q1 to Q5.
