---
type: thread
title: "Can a model change its own weights? (T4)"
id: T4
status: parked
owner: harshit
created: 2026-11-19
updated: 2026-11-19
tags: [type/thread, thread/T4, status/parked]
links: ["[[metacognition-monitor-control]]", "[[four-taste-tests]]"]
---

# Can a model change its own weights? (T4)

## Hypothesis
A model can localize and repair one of its own failure modes (e.g. looping) via WSP-style edits, matching an external frontier editor.

## Why parked
WeightBench (2611.18553): frontier agents can't yet reliably patch LMs, and a small model editing itself is harder still. Revisit after T5 shows whether rank-one consolidation works.

## Log
- 2026-11-19: created and parked.
- 2026-11-19: renamed from `T4-self-wsp` ("Can a model weight-space-program *itself*?") in the metacognition recenter.
- 2026-11-19: landscape sweep. Tree-Ising (2611.14210) and Exploring WSP (2611.09382) compute edits from forward passes with no frontier agent. Possible unpark path: the model runs that recipe on a direction from its own evaluation signal. Still parked. See [[landscape-persistent-control]].
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
- 2026-11-20: renamed from `can-a-model-edit-its-own-weights-T4` ("Can a model edit its own weights? (T4)") to an ASD-STE100-style name and title.
