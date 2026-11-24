---
type: paper
title: "Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents"
status: skimmed
arxiv: 2607.24300
url: https://arxiv.org/abs/2607.24300
authors: Diandian Guo, Cong Cao, Fangfang Yuan, Yingqi Wang, et al.
year: 2026
venue: arXiv preprint
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing]
components: [anchor, evaluation]
tags: [type/paper, section/6, test/self-reinforcing, component/anchor, status/skimmed, relevance/3, role/threat, self-verification]
links: ["[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]", "[[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]", "[[Self-judge training makes wrong look right (Zhou 2026)]]", "[[2026-11-23 gap check]]"]
---
# Self-written tests miss real regressions (Guo 2026)

**One line:** Agents that rewrite their own policies and accept edits by their own tests keep near-perfect self-scores while real performance falls or stays low. A sealed outside acceptance check fixes it.

## Evidence (abstract)
- Studies the "verifier-deployment gap": the agent's self-authored score against a sealed evaluation it cannot see.
- Weaker agents damage earlier strategies behind easy self-tests; stronger agents are more stable but still mismeasure the deployment distribution.
- Self-written constraints do not close the gap. A Sealed Exogenous Acceptance Loop (the agent gets only accept or reject from an audit it cannot write or see, and the old state is kept after a regression) beats unprotected baselines across six models and three seeds.

## Limits
Heuristic rules and controllers, not weights.

## Relevance to taste-lab
Direct threat to gap point 2 (own judgment keeps edits): self-acceptance alone drifts. The authors' conclusion fits our anchor: "reliable self-improvement ... requires at least one deployment-acceptance signal outside the agent's control." A self-editing model can propose and judge, but needs a sealed outside veto.
