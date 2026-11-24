---
type: paper
title: "The Butterfly Effect of Model Editing: Few Edits Can Trigger Large Language Models Collapse"
status: skimmed
arxiv: 2402.09656
url: https://arxiv.org/abs/2402.09656
authors: Wanli Yang, Fei Sun, Xinyu Ma, Xun Liu, et al.
year: 2024
venue: arXiv preprint [unverified: later venue]
relevance: 2
section: 6
tier: skim
tests: [self-reinforcing]
components: [consolidation, anchor]
tags: [type/paper, section/6, test/self-reinforcing, component/anchor, status/skimmed, relevance/2, role/threat, model-editing, collapse]
links: ["[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]", "[[Many sequential weight edits cause sudden forgetting (Gupta 2024)]]", "[[2026-11-23 gap check]]"]
---
# A few edits can collapse a model (Yang 2024)

**One line:** Even one weight edit can make a model collapse on many benchmarks, and almost all editing methods collapse after only a few sequential edits on hard cases. Perplexity is a cheap warning signal.

## Evidence (abstract)
- A single edit can trigger large drops across benchmark tasks.
- Change in perplexity after an edit correlates strongly with downstream performance, so it can replace full benchmarking after each edit.
- In sequential editing on hard cases, nearly all tested methods collapse after few edits. Releases a HardEdit dataset.

## Limits
Fact-editing methods and datasets; numbers not checked in the full text.

## Relevance to taste-lab
For gap point 1: a self-editing loop must check its own health after each edit. Perplexity is a candidate anchor signal that needs no outside labels.
