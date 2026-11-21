---
type: paper
title: "Violation of Expectation via Metacognitive Prompting Reduces Theory of Mind Prediction Error in Large Language Models"
status: skimmed
arxiv: 2310.06983
url: https://arxiv.org/abs/2310.06983
authors: Leer et al. [unverified: full author list]
year: 2023
venue: arXiv preprint
relevance: 1
section: 2
tier: skim
tests: []
components: [monitoring]
tags: [type/paper, section/2, status/skimmed, relevance/1, role/prior-art, metacognition, prompting, theory-of-mind]
links: ["[[Metacognition - watch and control yourself]]"]
---
# Violation of Expectation via Metacognitive Prompting Reduces Theory of Mind Prediction Error in LLMs (Leer et al., 2023)

**One line:** Prompting a model through a violation-of-expectation procedure - predict, observe, compare - reduces its theory-of-mind prediction errors [unverified: tasks and effect sizes].

## Claim
Metacognitive prompting structured as expectation-violation (a paradigm from developmental psychology) improves LLM theory-of-mind accuracy.

## Mechanism
- The prompt walks the model through predicting an agent's belief, observing the outcome, and comparing prediction to outcome before answering.

## Evidence
- Reduced ToM prediction error under the metacognitive prompt [unverified: models, margins].

## Limits / what they didn't show
- Prompting only: the metacognition is in the script, not the model. No internal state is read or used.
- 2023-era models.

## Relevance to taste-lab
Section 2 framing material: the difference between metacognitive *scaffolding* (this paper) and metacognitive *capacity* (the rest of the review). A reviewer will cite prompt-based metacognition against us; the answer is that a prompt script is an external controller, the same object as the outside probes in section 3.
- Prior-art check: **A no. B no.**

## Steal this
- Predict-observe-compare as a minimal loop structure to cite when defining the monitor step for a general audience.

## Kaushik's notes
<!-- yours -->
