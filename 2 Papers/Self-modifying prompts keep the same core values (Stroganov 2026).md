---
type: paper
title: "When LLMs Modify Themselves: Convergence, Values, and Stopping in Iterative Self-Improvement"
status: skimmed
arxiv: 2611.01304
url: https://arxiv.org/abs/2611.01304
authors: Oleg Stroganov [unverified: co-authors]
year: 2026
venue: arXiv preprint
relevance: 3
section: 7
tier: deep
tests: [divergent, stable, self-reinforcing]
components: [evaluation, consolidation]
tags: [type/paper, section/7, test/divergent, test/stable, status/skimmed, relevance/3, role/threat, self-modification, values]
links: ["[[Field map - Taste and new ideas]]", "[[Four tests for own taste]]", "[[Self-revised values converge in coding agents (Liang 2026)]]", "[[2026-11-23 gap check]]"]
---
# Self-modifying prompts keep the same core values (Stroganov 2026)

**One line:** Six frontier models rewrite their own system prompts in a loop. When they stop depends on which model it is, not on the goal they are given, and the same core values (honesty, clarity, curiosity) survive 100+ rounds of self-modification.

## Mechanism
54 runs, six models (Claude Opus 4.5, Claude Sonnet 4.5, GPT-4o, GPT-5.1, Grok-4, Gemini-3 Pro), three modes (freedom, happiness, improvement). Each run starts from an empty system prompt; the model drafts a new prompt, tests it in conversations, then commits or declares convergence.

## Evidence (abstract)
- Both Claude models declared convergence in 100% of runs; GPT-4o in 11%, one run reaching 101 iterations.
- A shared core of stated values recurred in all six models and stayed stable through iteration, including 100+ modifications.
- Stopping behavior varies independently of other capabilities.

## Limits
- Prompt edits, not weights. Values are stated, not probed.

## Relevance to taste-lab
Threat to the "taste over time" hint: self-modification so far preserves the inherited core values rather than producing new ones. Agrees with [[Self-revised values converge in coding agents (Liang 2026)]] and with Value Drifts (Bhatia, arXiv 2510.26707: SFT sets values, preference optimization rarely changes them). The stopping-rule result is useful: a self-editor needs a convergence decision, and models differ in it.
