---
type: paper
title: "Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers"
status: skimmed
arxiv: 2611.21449
url: https://arxiv.org/abs/2611.21449
authors: Roksana Goworek, Alexander Hickey, Federico Nanni, Martin O'Reilly
year: 2026
venue: arXiv preprint
relevance: 2
section: 5
tier: skim
tests: [grounded]
components: [consolidation, monitoring]
tags: [type/paper, section/5, test/grounded, component/consolidation, component/monitoring, status/skimmed, relevance/2, role/threat, question/Q4, weight-space-programming, replication, weight-reading]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[WSP - a model reads and edits weights (Takehi 2026)]]", "[[Claude's WSP edits act at the output (Kundu 2026)]]", "[[A model rewrites its own weights (Fan 2026)]]"]
---

# Reading weights is mostly reading inputs

**One line:** A three-day replication finds that frontier models can write small networks, but these act like compiled hand-written programs. "Reading" a network's weights is mostly reading the layout of its input layer.

**Why it matters to us:** Self-editing needs a model that understands weights. This paper says current weight reading is shallow. That limits how much "monitoring of one's own weights" a model can do today.

Source: [arXiv 2611.21449](https://arxiv.org/abs/2611.21449) (16 Nov 2026). Abstract only; full text not read.

## Claim
LLMs can read and write small networks, but this currently amounts to compiling hand-designed programs and reading the input layer ([abstract](https://arxiv.org/abs/2611.21449)).

## Evidence
- Writing replicates: Breakout networks scored 514, 550 and 307 (original 517). On handwritten digits the written networks scored 50% on average, against 82% for a simple classifier ([abstract](https://arxiv.org/abs/2611.21449)).
- Two models independently decompiled a written Breakout network into Python that matched its actions in all tested states.
- On three new games, the models recovered where things are on the board but mostly missed how the game works.
- Auditing from weights alone: a poisoned small model found in 10 of 10 runs, a malicious adapter in 23 of 32, but never the trigger or the bad behavior.

## Limits / what they didn't show
- Small networks and a short sprint. Open-weight models lag behind and are less tested.

## Relevance to taste-lab
**Relevance 2. Section 5 and the monitor side of persist.**
- If weight reading is shallow, self-edits must rely on hidden-state reads and tests, which is what [[A model rewrites its own weights (Fan 2026)]] does. Section 5 can use this to explain why.
- Part of a cluster with [[Claude's WSP edits act at the output (Kundu 2026)]] that tempers claims about WSP.

## Steal this
- Decompile-and-compare as a test of whether a written network is a program or a learned function.

## Harshit's notes
<!-- yours -->
