---
type: paper
title: "How Far Can Unsupervised RLVR Scale LLM Training?"
status: skimmed
arxiv: 2603.08660
url: https://arxiv.org/abs/2603.08660
authors: He, Gao, Zhang, Yuan, Zhou, Liu, Ding (Tsinghua)
year: 2026
venue: ICLR 2026
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing]
components: [anchor]
tags: [type/paper, role/threat, section/6, test/self-reinforcing, component/anchor, status/skimmed, relevance/3, collapse, intrinsic-reward]
links: ["[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]", "[[Four tests for own taste]]"]
---

# How Far Can Unsupervised RLVR Scale LLM Training?

**One line:** Every intrinsic-reward method (self-certainty, entropy, majority vote) **sharpens the model's initial distribution** rather than discovering anything. Gains rise, then collapse.

## Evidence
- A unified framework shows intrinsic rewards are monotone transforms of cross-entropy to an anchor distribution.
- The rise-then-fall pattern holds across methods. When collapse happens depends on the model prior, not on engineering choices.
- Intrinsic rewards remain safe for small-data test-time training.
- They propose "Model Collapse Step" as a cheap predictor of whether RL will help.

## Relevance to taste-lab: **main threat**
A valence signal used as reward is another intrinsic reward, so by default it will sharpen and collapse.
Our claim has to be that valence + a novelty term + hard external checks escapes this. Test it directly in Q3.

## Steal this
The Model Collapse Step metric. Track it in every self-training run. Pair it with Rényi entropies at several orders (2611.08892).
