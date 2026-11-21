---
type: paper
title: "Evidence for Limited Metacognition in LLMs"
status: skimmed
arxiv: 2509.21545
url: https://arxiv.org/abs/2509.21545
authors: Christopher Ackerman
year: 2025
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, status/skimmed, relevance/3, role/prior-art, metacognition, behavioral-test, animal-metacognition, confidence]
links: ["[[Metacognition - watch and control yourself]]", "[[Field map - Models read their own state]]", "[[Models mostly know what they know (Kadavath 2022)]]"]
---
# Evidence for Limited Metacognition in LLMs (Ackerman, 2025)

**One line:** Borrow the animal-metacognition playbook: skip self-reports entirely and test whether models *strategically deploy* knowledge of their internal states. Frontier models since early 2024 show increasingly strong evidence they can use their own confidence and anticipate their own answers.

## Claim
Metacognition in LLMs should be measured by behavior under strategic incentives, not by what the model says about itself. Judged that way, recent frontier models pass real metacognitive tests, though the abilities are still narrow.

## Mechanism
- Two paradigms adapted from nonhuman-animal research [unverified: paradigm details]: models must use their confidence in their own answers to make strategic choices, and must anticipate what answer they would give and use that anticipation appropriately.
- Self-reports are eschewed by design; the readout is a behavioral choice that only pays off if the model's estimate of its own state is accurate.
- Behavioral results are buttressed with a token-probability analysis.

## Evidence
- Frontier LLMs introduced since early 2024 show increasingly strong evidence of assessing and utilizing their own confidence on factual and reasoning questions [unverified: effect sizes].
- A capability trend over time: newer models do better [unverified: which models].

## Limits / what they didn't show
- Single-author study; paradigms cover confidence and answer anticipation only - no evaluation of quality beyond correctness, no taste.
- Behavioral deployment shows the signal is *usable*, not where it lives; no internal-state localization.

## Relevance to taste-lab
The strongest behavioral evidence on the monitor side, and a design template: our grounded test can borrow the "strategic deployment" framing so the readout has to be *used*, not just reported. Complements [[Introspection claims fail basic checks (Singh 2026)]]: self-report fails checks, but strategic use can still pass. If a taste signal exists, this is how you prove the model can act on it.
- Prior-art check: **A partial** (monitors and uses confidence; no evaluation of good vs bad, no weights). **B no.**

## Steal this
- Animal-paradigm strategic tasks as the behavioral arm of the grounded test.
- The trend-over-model-generations analysis as a framing for "metacognition is arriving now".

## Kaushik's notes
<!-- yours -->
