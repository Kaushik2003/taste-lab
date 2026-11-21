---
type: paper
title: "Large Language Models Lack Essential Metacognition for Reliable Medical Reasoning"
status: skimmed
url: https://doi.org/10.1038/s41467-024-55628-6
authors: Maxime Griot, Coralie Hemptinne, Jean Vanderdonckt, Demet Yuksel
year: 2025
venue: Nature Communications
relevance: 2
section: 3
tier: skim
tests: []
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/2, role/prior-art, metacognition, calibration, medical, benchmark]
links: ["[[Models mostly know what they know (Kadavath 2022)]]", "[[Models know when they know but do not act (Cao 2026)]]"]
---

# Large Language Models Lack Essential Metacognition for Reliable Medical Reasoning

**One line:** Twelve models ace medical multiple-choice but fail the metacognitive layer: they cannot recognize the limits of their knowledge, stay confident when the correct option is absent, and cannot say when a question is unanswerable.

**Why it matters to us:** The domain where monitoring failure costs the most. MetaMedQA's "missing answer recall" and "unknown recall" are evaluation-signal designs worth stealing for the taste setting, where "none of my candidates is good" is the analogous judgment.

Source: [Nature Communications](https://doi.org/10.1038/s41467-024-55628-6) (14 January 2025). Abstract-level note.

## Claim
High task accuracy and metacognitive reliability come apart in medicine: across twelve models, confidence-based accuracy, missing-answer recall and unknown recall are all poor despite expert-level multiple-choice scores ([paper](https://doi.org/10.1038/s41467-024-55628-6)).

## Mechanism
- MetaMedQA: medical multiple-choice questions augmented with confidence scores and metacognitive tasks.
- Metrics: confidence-based accuracy, missing answer recall (does the model notice the correct option is absent), unknown recall (does it flag unanswerable questions).

## Evidence
- All twelve tested models show "significant metacognitive deficiencies"; they give confident answers when the correct option is absent and fail to flag insufficient-information questions ([abstract](https://doi.org/10.1038/s41467-024-55628-6)).

## Limits / what they didn't show
- Medical MCQ format only; "unknown" is well-defined here in a way it is not in open-ended generation.
- Verbal confidence elicitation; no internal readouts.
- No intervention: shows the gap, not how to close it.

## Relevance to taste-lab
**Relevance 2. Section 3 (and intro motivation).**
- Concrete high-stakes case that monitoring is the bottleneck, not knowledge.
- The "missing answer recall" metric is the exact analog of the taste judgment "none of these options is good", a candidate eval for the internal evaluation signal.

## Steal this
- MetaMedQA's three-part metric split (confidence-based accuracy, missing answer recall, unknown recall) as a template for a taste-evaluation battery.

## Kaushik's notes
<!-- yours -->
