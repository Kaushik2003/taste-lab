---
type: paper
status: skimmed
arxiv: 2604.07729
url: https://www.anthropic.com/research/emotion-concepts-function
authors: Anthropic Interpretability
year: 2026
venue: preprint
relevance: 3
tests: [grounded]
components: [valence]
tags: [functional-emotions, steering, preference]
---

# Emotion Concepts and Their Function in a Large Language Model

**One line:** Claude Sonnet 4.5 has linear emotion-concept representations (171 of them) that causally drive behavior and stated task preferences.

## Mechanism
Extract emotion vectors (activation directions), then monitor and steer along them.

## Evidence
- Emotion-vector activation predicts how much the model prefers an activity. Positive valence goes with stronger preference.
- Steering with an emotion vector while the model reads an option shifts its preference for that option. That's causal.
- Emotion vectors also steer reward hacking, blackmail, and sycophancy.
- Post-training shifts emotional activations (toward lower volatility).

## Limits
Frontier closed model. Says nothing about subjective experience. Whether this replicates in open 8–32B models is
not established, and see [[2026-ferrara-all-quiet-pain]] for reportability problems.

## Relevance to taste-lab
**This is the [[valence-readout]] substrate.** We don't need to build likes and dislikes. We need to read them and
connect them to learning. Also a safety flag: the same vectors drive misbehavior.

## Steal this
The extraction and steering methodology for valence vectors, and the preference-correlation analysis design.
