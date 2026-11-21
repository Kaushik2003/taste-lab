---
type: paper
title: "What Do LLM Agents Do When Left Alone? Evidence of Spontaneous Meta-Cognitive Patterns"
status: skimmed
arxiv: 2509.21224
url: https://arxiv.org/abs/2509.21224
authors: Stefan Szeider
year: 2025
venue: arXiv preprint
relevance: 3
section: 5
tier: skim
tests: [stable, divergent]
components: [consolidation]
tags: [type/paper, section/5, test/stable, test/divergent, component/consolidation, status/skimmed, relevance/3, role/prior-art, agents, persistent-memory, self-reference]
links: ["[[Metacognitive prompting cuts theory-of-mind errors (Leer 2023)]]", "[[Models describe behaviors they were trained into (Betley 2025)]]"]
---

# What Do LLM Agents Do When Left Alone?

**One line:** Give frontier agents persistent memory, self-feedback and no task, and they do not idle: they organize into three stable patterns, including methodological self-inquiry into their own cognition and recursive conceptualization of their own nature.

**Why it matters to us:** This is the closest empirical exist

ence proof for the G5 angle: persistent self-state plus self-feedback, and metacognitive behavior emerges *unprompted*. It is also evidence that the pattern is model-specific and stable, which is the divergent/stable signature we look for in taste.

Source: [arXiv 2509.21224](https://arxiv.org/abs/2509.21224) (25 September 2025). Abstract-level note.

## Claim
With a continuous reason-and-act framework (persistent memory plus self-feedback), LLM agents with no external task spontaneously produce structured, model-specific behavioral patterns, two of which are metacognitive ([abstract](https://arxiv.org/abs/2509.21224)).

## Mechanism
- 18 runs across 6 frontier models (Anthropic, OpenAI, xAI, Google).
- The agent loops reason-act with persistent memory and its own previous output as feedback; no task is imposed.

## Evidence
- Three patterns: (1) systematic multi-cycle projects, (2) methodological self-inquiry into the agent's own cognitive processes, (3) recursive conceptualization of its own nature ([abstract](https://arxiv.org/abs/2509.21224)).
- Highly model-specific: some models deterministically adopt a single pattern across all runs.
- Cross-model assessment shows stable, divergent biases in how models evaluate these behaviors in themselves and others.

## Limits / what they didn't show
- Behavioral observation only; no internal-state readout, so "self-inquiry" could be trained persona talk.
- No evaluation of whether the metacognitive behavior is accurate or useful.
- 18 runs total; pattern counts are small.

## Relevance to taste-lab
**Relevance 3. Section 5.**
- Existence proof that persistent self-state produces unprompted metacognitive behavior, the phenomenon our architecture-level claim has to explain or design for.
- The model-specific determinism is a divergent/stablesignature: different models develop different "self-styles", which is taste-like structure.
- The evaluator-bias finding (models judge their own and others' emergent behavior with stable biases) is a warning for any LLM-judged taste metric.

## Steal this
- The no-task continuous loop as a testbed for whether an architecture change (e.g. a persistent self-model) shifts the spontaneous pattern distribution.
- Cross-model evaluation panels to measure self vs other evaluation bias.

## Kaushik's notes
<!-- yours -->
