---
type: paper
title: "AI Can Learn Scientific Taste"
status: skimmed
arxiv: 2603.14473
url: https://arxiv.org/abs/2603.14473
authors: Jingqi Tong, Mingzhe Li, Hangcheng Li, Yongzhuo Yang, Yurong Mou, Weijie Ma, Hongji Chen, Xiaoran Liu, Qinyuan Cheng, Ming Zhang, Qiguang Chen, Weifeng Ge, Qipeng Guo et al.
year: 2026
venue: arXiv preprint
relevance: 3
section: 7
tier: deep
tests: [stable]
components: [evaluation, consolidation]
tags: [type/paper, section/7, test/stable, status/skimmed, relevance/3, role/prior-art, taste, rlcf, community-feedback, scientific-judge, training]
links: ["[[Models show research taste (Trehan 2026)]]", "[[IdeaTaste - models fall short of human research taste (Zhong 2026)]]", "[[Field map - Taste and new ideas]]"]
---
# AI Can Learn Scientific Taste (Tong et al., 2026)

**One line:** Train a Scientific Judge on community feedback (citations) with Reinforcement Learning from Community Feedback (RLCF), and the learned judgment generalizes to future-year papers, other community metrics and unseen fields; a paired Scientific Thinker learns to propose high-potential ideas.

## Claim
Scientific taste - judging and proposing research with long-term impact potential - is learnable by AI from community signals.

## Mechanism
- RLCF: reinforcement learning where the reward is community feedback such as citations.
- Scientific Judge: learns to judge research quality/impact. Scientific Thinker: learns to propose ideas with high potential impact.

## Evidence
- Scientific Judge outperforms strong LLM baselines; learned judgment generalizes to future-year papers, other community metrics, and unseen fields [unverified: margins].

## Limits / what they didn't show
- The taste is **borrowed by construction**: the reward is the human community's revealed preference, so this is distillation of human taste, not a self-originated one. Under our definition the divergent test is failed on day one.
- Citation feedback rewards what communities reward - including their fashions and blind spots.

## Relevance to taste-lab
Half of the taste-trainability tension in section 7: taste *is* trainable (Tong) but models still fall short of communities (IdeaTaste). For the thesis: RLCF is the clearest example of evaluation that never becomes self-originated - the loop's reward stays outside the model. Our claim needs the opposite direction: a taste that starts human and drifts while staying good.
- Prior-art check: **A no. B partial** (trained taste that generalizes; origin stays human).

## Steal this
- Future-year generalization as the test that separates learned judgment from memorized judgment.
- The Judge/Thinker split as the evaluate/generate pair in our own loop.

## Kaushik's notes
<!-- yours -->
