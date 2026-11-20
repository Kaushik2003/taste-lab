---
type: paper
title: "IdeaTaste: Do LLMs Share the Research Taste of Human Researchers?"
status: skimmed
arxiv: 2611.03424
url: https://arxiv.org/abs/2611.03424
authors: Shanshan Zhong, Chen Xu, Jingjie Ning, Zhengzhong Liu, Aviral Kumar, Chenyan Xiong
year: 2026
venue: arXiv preprint
relevance: 3
section: 7
tier: deep
tests: [divergent]
components: [evaluation]
tags: [type/paper, section/7, test/divergent, status/skimmed, relevance/3, role/prior-art, taste, benchmark, research-ideas, ideation, evaluation]
links: ["[[Models show research taste (Trehan 2026)]]", "[[Models share one taste for text (Zatuchin 2026)]]", "[[Field map - Taste and new ideas]]"]
---
# IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (Zhong et al., 2026)

**One line:** Freeze the literature at 2025, ask LLM agents to write research proposals, and score them against what human communities actually published in 2026: models reach about 26% of the human level on citation matching and only 18% on idea matching.

## Claim
Research taste - judging what to read, which problems to pursue, which methods to try - is measurable as a benchmark, and current LLMs fall well short of human research communities.

## Mechanism
- IdeaTaste benchmark: proposals written from a literature snapshot frozen at 2025, scored against the work the same communities published in 2026.
- Six contemporary LLMs, four research areas from established to emerging, over 90,000 proposals.

## Evidence
- ~26% of human level on citation matching, ~18% on idea matching.
- Model populations can cite as *diversely* as a community and adopt its tasks and methods, but rarely arrive at its concrete approaches and research plans.

## Limits / what they didn't show
- The ground truth is the community's revealed choice, so "human level" conflates taste with access to 2026 information; a model with different-but-good ideas scores low.
- Research-level taste only; says nothing about token-level or code-level judgment.

## Relevance to taste-lab
The hard benchmark version of our divergent test at the research level, and a counterweight to [[Models share one taste for text (Zatuchin 2026)]]: models *share* a text taste but *lack* the community's research taste. The divergence they measure is a deficit, not a self-originated taste - our divergent test asks for drift that is *better* by some external standard, not just different. Feeds section 7's measurement story next to [[Models show research taste (Trehan 2026)]].
- Prior-art check: **A no. B partial** (measures divergence of model taste from human communities at scale).

## Steal this
- The frozen-snapshot benchmark design: freeze at time T, score against T+1 publications - directly reusable to test whether a self-trained taste anticipates human judgment.

## Kaushik's notes
<!-- yours -->
