---
type: paper
title: "SEAL: Self-Adapting Language Models"
status: read
arxiv: 2506.10943
url: https://arxiv.org/abs/2506.10943
authors: Zweiger, Pari, Guo, Akyürek, Kim, Agrawal (MIT)
year: 2025
venue: NeurIPS 2025
relevance: 3
section: 5
tier: deep
tests: [self-reinforcing]
components: [consolidation]
tags: [self-edit, weight-update, meta-learning]
---

# SEAL: Self-Adapting Language Models

**One line:** The model writes its own finetuning data and hyperparameters ("self-edits"). RL teaches it which self-edits actually help after the update.

## Claim
LLMs can learn to direct their own persistent weight updates.

## Mechanism
Two nested loops. Inner loop: given context C, the model generates a self-edit (restated facts, synthetic QA,
augmentation and optimizer settings), then an SFT/LoRA update is applied. Outer loop: RL (ReST-style filtering)
rewards the self-edits whose updated model does better on a downstream eval τ.

## Evidence
Knowledge incorporation and few-shot ARC subset. Reported ARC jump of roughly 20% → 72% on a Llama-3.2-1B setup (selected tasks) [check the paper for the exact protocol].

## Limits
- The reward is **external** (downstream task performance), so the model learns to learn, not what it likes.
- Each RL step needs an inner finetune, which is expensive. Catastrophic forgetting across many sequential edits is noted as an issue.

## Relevance to taste-lab
This is the consolidation mechanism for **distributed** taste (style). Our change: replace the external reward
with a [[valence-readout]] plus an [[anti-collapse-anchor]].

## Steal this
Code: https://jyopari.github.io/posts/seal. Reuse the self-edit generation and LoRA inner loop.
