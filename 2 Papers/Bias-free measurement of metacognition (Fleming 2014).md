---
type: paper
title: "How to Measure Metacognition"
status: skimmed
url: https://doi.org/10.3389/fnhum.2014.00443
authors: Stephen M. Fleming, Hakwan C. Lau
year: 2014
venue: Frontiers in Human Neuroscience
relevance: 3
section: 3
tier: deep
tests: []
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/3, role/foundations, measurement, signal-detection, methodology]
links: ["[[A less accurate AI with better confidence wins decisions (Li 2025)]]", "[[Models act on their own confidence (Kumaran 2026)]]", "[[Monitoring and control between two levels (Nelson 1990)]]"]
---

# How to Measure Metacognition

**One line:** The measurement bible: plain confidence-accuracy correlations are contaminated by response bias; use signal-detection measures, and keep three quantities distinct - metacognitive bias, sensitivity, and efficiency.

**Why it matters to us:** This is the methodological floor for every confidence claim in the review, including our own Q1 readout. Li & Steyvers' "sensitivity" is exactly this paper's construct imported to AI; any taste readout we report must be bias-free in their sense or a reviewer will reject it on citation alone.

Source: [Frontiers in Human Neuroscience](https://doi.org/10.3389/fnhum.2014.00443) (2014). Abstract and article excerpts via search.

## Claim
The association between trial-by-trial accuracy and confidence is the quantitative measure of metacognition, but correlation-style measures are confounded by response bias; signal-detection-theory and ROC-based measures are bias-free and should replace them ([paper](https://doi.org/10.3389/fnhum.2014.00443)).

## Mechanism
- Distinguishes three quantities: metacognitive bias (confidence shifts at constant task performance), metacognitive sensitivity (distinguishing own correct from incorrect judgments), metacognitive efficiency (sensitivity relative to task performance).
- Recommends SDT/ROC measures (type-2 ROC, meta-d') over Pearson-style correlations.

## Evidence
- Methodological review; demonstrates the bias contamination of correlation measures and relates SDT quantities to calibration and discrimination in the probability-estimation literature ([abstract](https://doi.org/10.3389/fnhum.2014.00443)).

## Limits / what they didn't show
- Human perceptual/memory tasks; applying type-2 SDT to LLM confidence requires care about what a "trial" and a "criterion" are for a model.
- Assumes confidence is elicitable and stable; LLM verbal confidence fails both (Prasad, Barkan).

## Relevance to taste-lab
**Relevance 3. Section 3 (methodology).**
- The bias/sensitivity/efficiency trichotomy is the vocabulary the review's measurement claims should use.
- Metacognitive *bias* at constant performance is precisely what steering a valence signal would induce - giving a formal name to the effect Q1/Q2 would produce and must measure.

## Steal this
- The three-quantity split (bias / sensitivity / efficiency) as the mandatory reporting format for any confidence instrument.

## Kaushik's notes
<!-- yours -->
