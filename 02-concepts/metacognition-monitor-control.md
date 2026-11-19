---
type: concept
tags: [metacognition, introspection]
links: [[valence-readout]]
---

# Metacognition = monitoring + control

**Definition (plain):** Nelson & Narens (1990) split cognition into an object level (doing the task) and a
meta level that **monitors** it (reads its state) and **controls** it (changes what it does). Flavell (1979) coined the term.

**LLM evidence:**
- Monitoring: Ji-An et al. (NeurIPS 2025) show LLMs can report activation directions in-context, but only in a low-dimensional "metacognitive space". Lindsey (2026, concept injection) shows Claude Opus 4/4.1 sometimes detect and name injected concepts.
- Control: both papers show models can shift their own activations when asked. Effects are stronger in deeper layers and larger models.
- Against: [[2026-ferrara-all-quiet-pain]] and 2611.15267 show the states are decodable while self-report is at chance in open models.

**Why it matters:** Our loop is monitor (valence) → evaluate → control (steer/learn) → persist.

**Related:** [[valence-readout]], [[self-directed-weight-updates]]
