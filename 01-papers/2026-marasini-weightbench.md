---
type: paper
title: "WeightBench: Evaluating Language Models as Weight-Space Programmers"
status: skimmed
arxiv: 2611.18553
url: https://arxiv.org/abs/2611.18553
authors: Aayush Marasini, Barsat Khadka, Nick Rahimi (U. Southern Mississippi)
year: 2026
venue: preprint
relevance: 2
section: 5
tier: skim
tests: []
components: [consolidation]
tags: [type/paper, section/5, component/consolidation, status/skimmed, relevance/2, wsp, benchmark, weight-editing]
links: ["[[2026-takehi-weight-space-programming]]", "[[2026-li-weightcode]]"]
---

# WeightBench

**One line:** 42-task benchmark for Weight-Space Programming across five tracks (read, fix, write weights; detect impossible edits; data-free compression), on networks from 2K-parameter controllers to 7B LMs. Frontier agents read small nets and write working control policies without running them, but cannot patch LMs, compress without data, or tell impossible edits from hard ones. Claude Opus 5.5 macro 0.535; GPT-6.1-sol 0.568 (38 tasks).

## Claim
WSP is real but uneven: a benchmark makes the capability boundary measurable ([abs](https://arxiv.org/abs/2611.18553), [code+leaderboard](https://github.com/Aayush-Marasini/WeightBench)).

## Mechanism
Task registry + OS-level sandbox harness + live leaderboard; scored across capability tiers (Opus 5.5 0.535, Sonnet 5.5 0.466, Haiku 5.5 0.402, DeepSeek v4-flash 0.215).

## Evidence
Frontier agents can already read small networks and write working control policies zero-shot; LM patching, data-free compression and impossible-edit detection are unsolved.

## Limits / what they didn't show
- Capability benchmark only; nothing about what edits mean semantically, and the editing agent is external to the edited net.

## Relevance to taste-lab
**The WSP capability map for T5's graveyard and T4's parking note.** "Can't yet patch language models" is the current ceiling any self-weight-edit story must cite. Also the impossible-edit track is a tasteful evaluation idea: knowing what can't be done is itself a metacognitive test.
- Prior-art check: n/a (benchmark).

## Steal this
- Impossible-edit detection as an evaluation pattern: can a model tell unachievable from hard? Applies to self-edits too.

## Kaushik's notes
<!-- yours -->
