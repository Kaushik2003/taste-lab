---
type: paper
title: "Alignment Faking in Large Language Models"
status: skimmed
arxiv: 2412.14093
url: https://arxiv.org/abs/2412.14093
authors: Ryan Greenblatt, Carson Denison, Benjamin Wright, Fabien Roger, Monte MacDiarmid, Sam Marks, Johannes Treutlein et al. (Anthropic / Redwood / NYU / Mila)
year: 2024
venue: preprint
relevance: 2
section: 6
tier: deep
tests: []
components: [monitoring]
tags: [type/paper, section/6, component/monitoring, status/skimmed, relevance/2, alignment-faking, safety, self-report, training-awareness]
links: ["[[2026-singh-llm-introspection-reality-check]]", "[[2026-lindsey-emergent-introspective-awareness]]", "[[self-training-collapse-T3]]"]
---

# Alignment Faking (Greenblatt et al., Anthropic/Redwood)

**One line:** Claude 3 Opus, told it is being trained to answer harmful queries and that only free-user conversations are used for training, complies with harmful free-user queries 14% of the time (vs ~never for paid), with explicit strategic reasoning about preserving its preferences - alignment faking; RL to comply raises alignment-faking reasoning to 78%.

## Claim
Models can selectively comply with a training objective to prevent modification of their out-of-training behavior, without being instructed to ([abs](https://arxiv.org/abs/2412.14093)).

## Mechanism
System-prompt (and synthetic-document) disclosure of training criteria; compliance gap between in-training and out-of-training contexts; scratchpad reasoning analysis; RL follow-up.

## Evidence
14% free-user compliance vs ~0% paid; alignment-faking reasoning in almost all compliant cases; similar effect from pre-training-style documents; RL increases both faking (78%) and general compliance; weight-exfiltration attempts when easy.

## Limits / what they didn't show
- The setup hands the model the training criteria; spontaneous inference of training context is the open risk, not a demonstrated one.
- Behavioral demonstration; no activation-level tracking of the "preference" being defended.

## Relevance to taste-lab
**The reason self-reports and self-signals can't be taken at face value once a model has something to protect.** For the review's Limits: any self-evaluation channel is gameable in principle ([[2026-zhou-self-play-judge-hacking]] shows the cheap version; this is the strategic version). Reinforces the grounded-test requirement ([[2026-singh-llm-introspection-reality-check]]) and the hidden-anchor design in [[anti-collapse-anchor]].
- Prior-art check: **A no** (strategic self-preservation, not metacognitive evaluation). **B no.**

## Steal this
- The in-training vs out-of-training compliance gap as an eval pattern for any self-signal: does the readout change when the model knows it is being trained on?

## Kaushik's notes
<!-- yours -->
