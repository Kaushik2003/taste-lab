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
tags: [type/paper, section/5, test/self-reinforcing, component/consolidation, status/read, relevance/3, self-edit, weight-update, meta-learning]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[Four tests for own taste]]"]
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
Knowledge incorporation and few-shot ARC subset. ARC: self-edit success rate 72.5% vs 20% (self-edits without RL training), 0% (in-context learning) and 100% (oracle test-time training). Llama-3.2-1B-Instruct, 11 training tasks and 8 evaluation tasks, all filtered to be solvable by tuned test-time training; 5 self-edits per evaluation task ([arXiv 2506.10943](https://arxiv.org/abs/2506.10943), Sec. 4.1, Table 1). Checked 2026-11-20.

## Limits
- The reward is **external** (downstream task performance), so the model learns to learn, not what it likes.
- Each RL step needs an inner finetune, which is expensive. Catastrophic forgetting across many sequential edits is noted as an issue.

## Relevance to taste-lab
This is the consolidation mechanism for **distributed** taste (style). Our change: replace the external reward
with a [[Good-bad signal probe]] plus an [[Anchor against collapse]].

## Steal this
Code: https://jyopari.github.io/posts/seal. Reuse the self-edit generation and LoRA inner loop.
