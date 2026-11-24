---
type: paper
title: "Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States"
status: skimmed
arxiv: 2605.07579
url: https://arxiv.org/abs/2605.07579
authors: Yunho Choi, et al.
year: 2026
venue: arXiv preprint
relevance: 2
section: 4
tier: skim
tests: [grounded]
components: [evaluation, control]
tags: [type/paper, section/4, test/grounded, component/evaluation, status/skimmed, relevance/2, role/prior-art, hidden-state-reward, rl]
links: ["[[Field map - Models judge good and bad]]", "[[Good-bad signal probe]]", "[[2026-11-23 gap check]]"]
---
# A hidden-state probe as critic in RL (Choi 2026), POISE

**One line:** A small probe reads the policy's own internal states to predict the expected reward, and serves as the value baseline in reinforcement learning, replacing a separate critic model.

## Evidence (abstract)
- Probe trained online with the policy; a cross-rollout construction keeps gradients unbiased.
- Qwen3-4B and OLMo3-7B-Instruct-DPO on a six-domain verifiable-reward corpus: beats other RLVR baselines [unverified: margins].

## Limits
The probe predicts an outside verifiable reward; the update is by gradients.

## Relevance to taste-lab
Prior art for gap point 2: internal states already serve as a learned value signal inside training. Related: SWIFT (arXiv 2505.12225, a hidden-state reward for best-of-N) and Q-Probe (arXiv 2402.14688, a linear probe that reweights candidates). None gates a direct weight edit, and all are trained to match an outside reward or preference labels.
