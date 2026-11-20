---
type: paper
title: "Emergent Introspective Awareness in Large Language Models"
status: skimmed
arxiv: 2601.01828
url: https://arxiv.org/abs/2601.01828
authors: Jack Lindsey (Anthropic)
year: 2026
venue: preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/3, introspection, activation-injection, self-report, anthropic]
links: ["[[landscape-metacognitive-monitoring]]", "[[2026-singh-llm-introspection-reality-check]]", "[[2026-wang-introspective-oversight]]"]
---

# Emergent Introspective Awareness (Lindsey, Anthropic)

**One line:** Inject known concept vectors into a model's activations and test whether its self-reports track the injection: models can notice and identify injected concepts, recall prior internal representations and distinguish them from text inputs, and even tell their own outputs from artificial prefills by recalling prior intentions. Claude Opus 4/4.1 strongest; capacity real but highly unreliable and context-dependent.

## Claim
Current LMs possess some functional introspective awareness of their own internal states, demonstrated causally rather than through conversation ([abs](https://arxiv.org/abs/2601.01828)).

## Mechanism
- Concept injection into activations + measurement of influence on self-reported states: decouples genuine introspection from confabulation.
- Recall tests: prior internal representations vs raw text inputs; own outputs vs prefills via recalled intentions.
- Control tests: models modulate activations when instructed or incentivized to "think about" a concept.

## Evidence
- Opus 4 and 4.1 show the greatest introspective awareness among tested models; trends across models complex and sensitive to post-training strategy.

## Limits / what they didn't show
- Author's own caveat: highly unreliable, context-dependent; no error rates by condition extracted here [unverified until PDF read].
- Awareness of injected concepts and intentions, not of evaluations or preferences: no valence/taste self-report tested.

## Relevance to taste-lab
**The strongest causal evidence that monitoring exists, and the methods template for the grounded test.** Injection-and-report is exactly the design that separates "reads its own state" from "confabulates from text" - the layer-0 confound in [[gaps]]. Pairs with [[2026-singh-llm-introspection-reality-check]] (the skeptical bar) and [[2026-wang-introspective-oversight]] (trained report vs emergent report). Our valence readout is a probe version of what Lindsey tests verbally.
- Prior-art check: **A partial** (monitors its own states, sometimes; no evaluation-as-control, no loop). **B no.**

## Steal this
- Injection + self-report as the causal test battery for any "the model monitors X" claim.
- The own-output vs prefill distinction (recalling prior intentions) as a cheap grounded-test variant.

## Kaushik's notes
<!-- yours -->
