---
type: paper
title: "The Metacognitive Monitoring Battery: A Cross-Domain Benchmark for LLM Self-Monitoring"
status: skimmed
arxiv: 2604.15702
url: https://arxiv.org/abs/2604.15702
authors: Jon-Paul Cacioli
year: 2026
venue: arXiv preprint
relevance: 2
section: 2
tier: skim
tests: [stable]
components: [monitoring, controller]
tags: [type/paper, section/2, test/stable, component/monitoring, component/controller, status/skimmed, relevance/2, metacognition, benchmark, nelson-narens, preregistered]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Monitoring and control between two levels (Nelson 1990)]]", "[[Confidence is a guess about your own decision (Fleming 2017)]]", "[[Models know when they know but do not act (Cao 2026)]]"]
---

# A test battery for self-monitoring

**One line:** A preregistered battery of 524 items from classic psychology tasks tests whether 20 frontier models withdraw wrong answers more often than right ones. Accuracy and metacognitive sensitivity rank almost in reverse.

**Why it matters to us:** It is a measurement tool grounded in Nelson and Narens, and it separates looking back (monitoring) from planning ahead (regulation). That split matters for section 2.

Source: [arXiv 2604.15702](https://arxiv.org/abs/2604.15702) (v2, 21 Apr 2026). Abstract only; full text not read.

## Claim
Standard benchmarks measure only object-level performance. A cross-domain battery can measure whether a model knows what it knows ([abstract](https://arxiv.org/abs/2604.15702)).

## Mechanism
- 524 items over six domains: learning, calibration, social cognition, attention, executive function, prospective regulation. Tasks 1 to 5 preregistered.
- After each answer, two probes adapted from Koriat and Goldsmith (1996): keep or withdraw, and bet or decline.
- Main metric: "withdraw delta", the difference in withdrawal rate between wrong and right items.

## Evidence
- 20 models, 10,480 evaluations. Three profiles: blanket confidence, blanket withdrawal, selective sensitivity ([abstract](https://arxiv.org/abs/2604.15702)).
- Accuracy rank and metacognitive sensitivity rank are largely inverted.
- Looking back and planning ahead look separable (correlation 0.17), but with only 20 models the interval is wide.

## Limits / what they didn't show
- Behavioral only; no internal states. Per-model numbers are not in the abstract.

## Relevance to taste-lab
**Relevance 2. Section 2 (foundations).**
- A ready citation for "metacognition in language models can be measured with human paradigms".
- The inverted ranking warns that a stronger model is not a better self-monitor.

## Steal this
- Withdraw delta as a simple behavioral measure of monitoring.

## Harshit's notes
<!-- yours -->
