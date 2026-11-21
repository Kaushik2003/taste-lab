---
type: paper
title: "Does It Make Sense to Speak of Introspection in Large Language Models?"
status: skimmed
arxiv: 2506.05068
url: https://arxiv.org/abs/2506.05068
authors: Iulia M. Comsa, Murray Shanahan
year: 2025
venue: arXiv preprint
relevance: 3
section: 2
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/2, test/grounded, status/skimmed, relevance/3, role/prior-art, metacognition, introspection, philosophy, self-report, causal-criterion]
links: ["[[Metacognition - watch and control yourself]]", "[[Introspection claims fail basic checks (Singh 2026)]]", "[[Models sometimes notice injected thoughts (Lindsey 2025)]]"]
---
# Does It Make Sense to Speak of Introspection in Large Language Models? (Comsa & Shanahan, 2025)

**One line:** A self-report counts as introspection only if a causal process links the internal state to the report. By that bar, Gemini's account of its own "creative process" is role play, but its correct inference of its own sampling temperature - read off its own outputs in context - is a minimal, legitimate case.

## Claim
A lightweight definition (no immediacy, no privileged access, no consciousness required): an LLM self-report is introspective when it accurately describes an internal state or mechanism *through a causal process* connecting that state to the report.

## Mechanism
- Two case studies on Gemini 1.0/1.5 (Oct-Dec 2024): (1) describe your creative process while writing a poem; (2) estimate whether your sampling temperature is high or low.
- Case 1 fails the bar: the six-step "process" is a fabrication patterned on human introspective reports in training data (the model even claims to have "read the poem aloud").
- Case 2 passes, minimally: temperature is set at inference time and absent from training data, so an accurate report must flow from the model's own current outputs in the context window - a real, if indirect, causal link.

## Evidence
- Gemini correctly infers low vs high temperature from its own recent outputs, when nudged to acknowledge it is an LLM with a temperature parameter [unverified: accuracy statistics].

## Limits / what they didn't show
- Two anecdotes, not a benchmark; no quantification, no controls across model families.
- The passing case reads internal state *through visible outputs*, which our grounded test would call the layer-0 confound - the report may need no hidden-state access at all.

## Relevance to taste-lab
This is the crisp criterion our grounded test formalizes: the report must be causally downstream of the internal state. Their temperature case is the weakest passing example (state read off own text), which marks exactly where our probe-based bar sits above theirs. Lindsey's injection-and-report result is the stronger case their definition anticipates.
- Prior-art check: **A partial** (the definition and the bar; no working readout beyond output-mediated inference). **B no.**

## Steal this
- The causal-link criterion as the one-sentence bar for any monitoring claim in the review.
- Self-reports-of-parameters as a confound-free test family: inference-time settings cannot be memorized from training data.

## Kaushik's notes
<!-- yours -->
