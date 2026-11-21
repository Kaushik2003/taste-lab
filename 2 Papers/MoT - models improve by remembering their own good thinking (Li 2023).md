---
type: paper
title: "MoT: Memory-of-Thought Enables ChatGPT to Self-Improve"
status: skimmed
arxiv:
url: https://aclanthology.org/2023.emnlp-main.392/
authors: Xiaonan Li, Xipeng Qiu
year: 2023
venue: EMNLP 2023
relevance: 2
section: 6
tier: skim
tests: []
components: [consolidation]
tags: [type/paper, section/6, status/skimmed, relevance/2, role/prior-art, self-improvement, memory, confidence-filtering, pre-rl]
links: ["[[Anchor against collapse]]", "[[INTUITOR - self-certainty is reward enough to learn reasoning (Zhao 2025)]]"]
---
# MoT: Memory-of-Thought Enables ChatGPT to Self-Improve (Li & Qiu, 2023)

**One line:** Before the test, the model pre-thinks over the unlabeled dataset and saves its high-confidence thoughts as external memory; at test time it recalls relevant memories to reason better. Self-improvement with no annotated data and no parameter updates.

## Claim
An LLM can improve itself through memory of its own thoughts: confidence-filtered self-generated reasoning, stored and retrieved, substitutes for fine-tuning.

## Mechanism
- Pre-think stage: sample thoughts on unlabeled data, keep the high-confidence ones as external memory.
- Test stage: retrieve relevant memories to condition reasoning.

## Evidence
- Significant improvements for ChatGPT on arithmetic and other reasoning tasks [unverified: margins].

## Limits / what they didn't show
- The filter is self-confidence, so the memory is the model's prior made explicit - the collapse risk (reinforcing its own biases) is one retrieval loop away.
- Improvements plateau with what the model already almost knows; no new capability enters.

## Relevance to taste-lab
The pre-RL point on the self-improvement axis: selection by confidence, storage outside the weights. It is the weakest form of persist (memory, not weights) and already shows the pattern the review tracks - self-selection by an internal signal. Pair with INTUITOR (same selection signal, but as RL reward into weights) to show the ladder: memory -> RL -> weight edits.
- Prior-art check: **A partial** (self-improvement by confidence-filtered memory; nothing reaches the weights). **B no.**

## Steal this
- Confidence-filtered memory as the cheap baseline any weight-level self-edit must beat.

## Kaushik's notes
<!-- yours -->
