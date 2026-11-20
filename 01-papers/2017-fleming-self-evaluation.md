---
type: paper
title: "Self-evaluation of decision-making: A general Bayesian framework for metacognitive computation"
status: skimmed
arxiv:
url: https://doi.org/10.1037/rev0000045
authors: Stephen M. Fleming, Nathaniel D. Daw
year: 2017
venue: Psychological Review 124(1), 91-114
relevance: 3
section: 2
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/2, test/grounded, component/monitoring, status/skimmed, relevance/3, metacognition, second-order, foundations]
links: ["[[metacognition-monitor-control]]", "[[landscape-metacognitive-monitoring]]", "[[four-taste-tests]]"]
---

# Self-evaluation of decision-making (Fleming & Daw, 2017)

**One line:** Self-evaluation is a second-order inference: a monitoring system infers how well a coupled but separate decision system did, the same computation as judging another agent.

## Claim
One Bayesian model covers both confidence and error detection, and explains why metacognition can be better or worse than task performance.

## Mechanism
Second-order inference works when the states behind the decision and the states behind confidence are separated in space or time. First-order models, where one internal state drives both the decision and the confidence, cannot produce genuine self-evaluation. PMC: [PMC5178868](https://pmc.ncbi.nlm.nih.gov/articles/PMC5178868/).

## Relevance to taste-lab
- A ready-made account of the probe-vs-report gap in LLMs: if generation and self-evaluation run on partly separate states, the verbal report can come apart from the decodable state ([[2026-ferrara-all-quiet-pain]], [[2026-singh-llm-introspection-reality-check]]) without either being broken.
- Singh et al.'s "second-order computation" requirement for introspection tests is the same distinction, so we cite both together for the grounded test ([[four-taste-tests]]).
- Predicts that a system's own actions feed into its self-evaluation, which matters for T2's best-of-n arm judged on the model's own outputs.

## Kaushik's notes
<!-- yours -->
