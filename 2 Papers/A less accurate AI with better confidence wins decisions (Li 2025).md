---
type: paper
title: "Beyond Accuracy: How AI Metacognitive Sensitivity Improves AI-Assisted Decision Making"
status: skimmed
arxiv: 2507.22365
url: https://arxiv.org/abs/2507.22365
authors: ZhaoBin Li, Mark Steyvers
year: 2025
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: []
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/3, role/prior-art, human-ai, calibration, metacognitive-sensitivity]
links: ["[[People over-trust what models know (Steyvers 2025)]]", "[[Medical models cannot say what they do not know (Griot 2025)]]", "[[Models mostly know what they know (Kadavath 2022)]]"]
---

# Beyond Accuracy: AI Metacognitive Sensitivity in Decision Making

**One line:** A formal framework plus a behavioral experiment showing an AI with lower accuracy but better confidence discrimination (metacognitive sensitivity) can improve human decisions more than a more accurate but worse-calibrated AI.

**Why it matters to us:** This is the deployable-value argument for monitoring, quantified: sensitivity is a separable design target from accuracy, and it can dominate. It gives the review a theorem-shaped reason to build the internal evaluation signal, not just a philosophical one.

Source: [arXiv 2507.22365](https://arxiv.org/abs/2507.22365) (30 July 2025). Abstract-level note.

## Claim
In hybrid human-AI decision making, overall performance depends jointly on AI accuracy and AI metacognitive sensitivity; there are conditions where higher sensitivity beats higher accuracy ([abstract](https://arxiv.org/abs/2507.22365)).

## Mechanism
- Theoretical framework for the joint impact of predictive accuracy and confidence discrimination on hybrid decision accuracy.
- Behavioral experiment confirming that greater AI sensitivity improves human decision performance.

## Evidence
- Identified conditions where a lower-accuracy, higher-sensitivity AI enhances human decision accuracy ([abstract](https://arxiv.org/abs/2507.22365)).
- Experiment: human decision performance rises with AI metacognitive sensitivity.

## Limits / what they didn't show
- Binary-style decision tasks with ground truth; taste-like open-ended judgments are out of scope.
- Sensitivity is supplied to the human as visible confidence scores; how to elicit honest scores from the model is assumed, not solved.

## Relevance to taste-lab
**Relevance 3. Section 3.**
- The formal hook for "monitoring is a first-class objective": sensitivity is named, measured and shown to pay off independently of accuracy.
- Connects to Griot: medicine is the case where sensitivity failure is most expensive; this paper prices that failure.

## Steal this
- Accuracy x sensitivity as a 2x2 evaluation grid for any assistant system; report both, always.

## Kaushik's notes
<!-- yours -->
