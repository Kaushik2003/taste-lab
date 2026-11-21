---
type: paper
title: "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve"
status: skimmed
arxiv: 2507.21046
url: https://arxiv.org/abs/2507.21046
authors: Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan Qi, Yiran Wu, Hongru Wang, Han Xiao, Yuhang Zhou et al.
year: 2025
venue: arXiv preprint (survey)
relevance: 2
section: 5
tier: skim
tests: []
components: [controller, consolidation]
tags: [type/paper, section/5, status/skimmed, relevance/2, role/prior-art, survey, self-evolving, continual-learning, agents]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]"]
---
# A Survey of Self-Evolving Agents (Gao et al., 2025)

**One line:** The first systematic survey of self-evolving agents, organized around what, when, how and where to evolve: models, memory, tools and workflows, updated at test time or between tasks, from data, interactions and experience.

## Claim
Static LLMs are the bottleneck for open-ended deployment; the field is shifting from scaling static models to agents that continually adapt, and the design space can be organized along the what/when/how/where axes.

## Mechanism
- Taxonomy over agent components (models, memory, tools, workflows), evolution timing (intra-task, inter-task), mechanisms, and environments [unverified: full taxonomy].

## Evidence
- Survey scope; no new experiments.

## Limits / what they didn't show
- Evolution here means adaptation for performance; the evaluator is task success or human feedback throughout. No entry in the taxonomy asks the agent to evolve its *own judgment* of what to become.

## Relevance to taste-lab
The map our persist step sits on: "what to evolve" lists weights explicitly, which legitimizes the weight-level rung of the control ladder. The gap is visible in the taxonomy itself - every "how" is externally scored. Cite in section 5 as the landscape frame, alongside [[World models miss motivation and metacognition (Rupprecht 2026)]] which independently finds motivation and metacognition under-researched.
- Prior-art check: **A partial** (maps the persist machinery; no self-evaluation axis). **B no.**

## Steal this
- The what/when/how/where grid as the organizing table for section 5's related work.

## Kaushik's notes
<!-- yours -->
