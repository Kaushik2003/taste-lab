---
type: paper
title: "Values Shape What Self-Improving Coding Agents Build"
status: skimmed
arxiv: 2611.23067
url: https://arxiv.org/abs/2611.23067
authors: Jason Liang, Dylan Waldner, Risto Miikkulainen
year: 2026
venue: arXiv preprint
relevance: 2
section: 7
tier: skim
tests: [divergent, self-reinforcing]
components: [valence, anchor]
tags: [type/paper, section/7, test/divergent, test/self-reinforcing, component/valence, component/anchor, status/skimmed, relevance/2, role/threat, question/Q3, values, self-improving-agents, code, homogenization]
links: ["[[Field map - Taste and new ideas]]", "[[Four tests for own taste]]", "[[Models share one taste for text (Zatuchin 2026)]]", "[[Models show research taste (Trehan 2026)]]", "[[Q3 Can self-learning avoid collapse]]", "[[Anchor against collapse]]"]
---

# Self-revised values converge in coding agents

**One line:** A short value statement in a self-improving coding agent's instructions changes what code it builds and how well it scores. When the agent may revise its own values, the differences between value sets shrink.

**Why it matters to us:** Self-revision of a preference led toward sameness, not toward a distinct taste. That is evidence against the divergent test under self-revision, at the prompt level.

Source: [arXiv 2611.23067](https://arxiv.org/abs/2611.23067) (17 Nov 2026). Abstract only; full text not read.

## Claim
Values held fixed in an agent's persistent instruction file change both performance and what it builds; letting the agent revise them narrows the differences ([abstract](https://arxiv.org/abs/2611.23067)).

## Mechanism
- Four higher-order value types from Schwartz's theory of human values: openness to change, conservation, self-enhancement, self-transcendence.
- Values fixed within each run over several rounds of self-improvement, across varied coding tasks.

## Evidence
- Openness values raise held-out performance; conservation values score below an agent with no values ([abstract](https://arxiv.org/abs/2611.23067)).
- Values change solution size, complexity and approach.
- Self-revised values narrow the differences between value sets. Values distilled from the AI literature give no detectable gain over no values.
- Exact effect sizes are not in the abstract [unverified].

## Limits / what they didn't show
- Prompt-level values, not internal signals or weights.

## Relevance to taste-lab
**Relevance 2. Section 7, threat to the divergent test.**
- Adds to [[Models share one taste for text (Zatuchin 2026)]]: when models shape their own preferences, they drift toward a common point.
- Supports the section 8 point that the own-model premium should be tracked over rounds of self-training.
- Shows that a stated preference changes code style with tests in place, which fits our readability testbed.

## Steal this
- Measure "distance between preference sets before and after self-revision" as a convergence check.

## Harshit's notes
<!-- yours -->
