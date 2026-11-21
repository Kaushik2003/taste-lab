---
type: paper
title: "Causal Evidence that Language Models use Confidence to Drive Behavior"
status: skimmed
arxiv: 2603.22161
url: https://arxiv.org/abs/2603.22161
authors: Dharshan Kumaran, Nathaniel Daw, Simon Osindero, Petar Velickovic, Viorica Patraucean
year: 2026
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, controller]
tags: [type/paper, section/3, test/grounded, component/monitoring, component/controller, status/skimmed, relevance/3, role/prior-art, question/Q6, metacognition, confidence, abstention, activation-steering]
links: ["[[Models know when they know but do not act (Cao 2026)]]", "[[Introspection needs a causal link to count (Comsa 2025)]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Q6 Can the model read and use its own signal]]"]
---

# Causal Evidence that Language Models use Confidence to Drive Behavior

**One line:** Models do not just carry confidence signals, they act on them. Activation steering that boosts or suppresses the confidence direction moves abstention rates in the predicted direction.

**Why it matters to us:** This clears the causal bar that Comsa and Shanahan set for real introspection, in the cleanest case so far: confidence used for abstention. It is the strongest existing evidence that monitoring feeds control inside a model, which is the link our G5 architecture claim needs.

Source: [arXiv 2603.22161](https://arxiv.org/abs/2603.22161) (23 March 2026). Abstract-level note.

## Claim
LLMs apply an implicit threshold to an internal confidence signal when deciding whether to answer or abstain, and this is causal, not correlational: steering the signal changes the decision ([abstract](https://arxiv.org/abs/2603.22161)).

## Mechanism
- Four phases. (1) Baseline confidence with no abstain option. (2) Add abstention: an implicit threshold on internal confidence appears, with confidence effect sizes about an order of magnitude larger than alternative mechanisms. (3) Activation steering: boosting confidence lowers abstention, suppressing it raises abstention. (4) Varying the instructed threshold shows models deploy the signal to implement an abstention policy.
- Verbal confidence predicts abstention independently of log-probability confidence, even though it discriminates correctness worse. Both are lossy readouts of a richer internal representation decoded at the last pre-answer token.

## Evidence
- Causal steering result across phases 3 and 4 ([abstract](https://arxiv.org/abs/2603.22161)).
- Confidence effect sizes ~10x larger than alternative mechanisms in phase 2.

## Limits / what they didn't show
- Abstention is a narrow control decision. No evidence yet that the same signal steers what the model says, only whether it says anything.
- The internal representation is richer than both readouts, so verbal and log-prob confidence are each partial.
- No persistent state: each decision is local to one question.

## Relevance to taste-lab
**Relevance 3. Section 3, and Question 6 (can the model read and use its own signal?).**
- The missing causal rung for the monitoring-to-control ladder: signal exists (Kadavath, Zhang), signal is readable (Cao), and here the signal is *used* causally.
- A template for the taste version: steer the "this is good" direction and see whether selection behavior moves. That is the Q1/Q6 experiment design.
- Pairs with [[Introspection needs a causal link to count (Comsa 2025)]]: this paper meets that bar.

## Steal this
- The four-phase paradigm (baseline -> abstain option -> steering -> instructed threshold) as a protocol for testing whether any internal signal drives behavior.
- Verbal + log-prob + probe as three readouts of one latent state; report all three.

## Kaushik's notes
<!-- yours -->
