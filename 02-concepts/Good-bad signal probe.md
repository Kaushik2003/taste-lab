---
type: concept
tags: [type/concept, status/active, valence, emotion, preference]
links: ["[[Emotion directions drive choices in Claude (Anthropic 2026)]]", "[[Models do not report injected pain (Ferrara 2026)]]", "[[Four tests for own taste]]"]
---

# Valence readout

**Definition (plain):** A scalar "this is good / this is bad" signal read from the model's own activations,
usually by projecting onto emotion- or preference-related directions. It's the model's "likes and dislikes", made measurable.

**Why it matters for us:** It's the evaluator in the loop. If valence tracks *quality* (e.g. readability)
rather than familiarity, length or sycophancy, it can steer inference and gate learning.

**Two ways to read it:**
1. **Probe readout:** an external linear probe, wired back in as a control signal. Works today (98–100% decodable per [[Models do not report injected pain (Ferrara 2026)]]).
2. **Self-report:** the model says what it likes. Fails zero-shot in open models. A LoRA or observer role can be trained to report it (2611.23365).

**Open questions:**
- Does valence correlate with expert quality judgments, or just with familiarity? (→ Q1)
- Is a probe-based signal "the model's own" taste? Philosophically weaker, but mechanistically fine. Argue it in the paper.

**Related:** [[Metacognition - watch and control yourself]], [[Neuromodulators as learning settings]]
