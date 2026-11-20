---
type: paper
title: "Nested Learning: The Illusion of Deep Learning Architectures (Hope)"
status: skimmed
arxiv: 2512.24695
url: https://arxiv.org/abs/2512.24695
authors: Ali Behrouz, Peilin Zhong, Vahab Mirrokni (Google Research)
year: 2025
venue: NeurIPS 2025
relevance: 2
section: 5
tier: skim
tests: []
components: [consolidation]
tags: [type/paper, section/5, component/consolidation, status/skimmed, relevance/2, continual-learning, self-modifying, memory, google]
links: ["[[2022-irie-self-referential-weight-matrix]]", "[[2025-zweiger-seal]]", "[[2025-aviss-state-stream-transformer]]"]
---

# Nested Learning / Hope (Google, NeurIPS 2025)

**One line:** Treat a model as nested multi-level optimization problems, each compressing its own context flow: optimizers (Adam, momentum) are really associative memories over gradients; sequence models can learn their own update algorithm; and the Hope architecture (self-modifying Titans + continuum memory) shows gains on language modeling, continual learning and long-context reasoning.

## Claim
Architecture and optimizer are the same concept at different levels; adding levels yields higher-order in-context learning and a path past catastrophic forgetting ([abs](https://arxiv.org/abs/2512.24695), [blog](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/)).

## Mechanism
- Deep optimizers: gradient compressors with deeper memory / stronger learning rules.
- Self-modifying Titans: the model learns how to modify itself by learning its own update algorithm.
- Continuum Memory System: generalizes long/short-term memory; combined into Hope.

## Evidence
Lower perplexity and higher accuracy than modern recurrent models and standard Transformers on LM/common-sense tasks; better NIAH long-context memory management [unverified: margins].

## Limits / what they didn't show
- Self-modification is still outer-loop trained: the update rule is learned, but the objective choosing updates is the designer's loss, not an internal evaluation.
- Continual-learning benchmarks, not open-ended self-improvement.

## Relevance to taste-lab
**The current frontier of learned self-modification, and it still lacks the evaluator.** Hope learns HOW to update itself; nothing decides WHAT is worth learning based on the model's own assessment. That is the persistent-selection leg of G5 in [[gaps]]: learned selection of what to keep. Cite beside SST ([[2025-aviss-state-stream-transformer]]) in the architecture proposal: SST gives persistent state, Hope gives learned update levels, the missing piece is the valence-driven selection signal.
- Prior-art check: **B partial** (learned self-modification machinery; no self-evaluation gate).

## Steal this
- "Optimizers are associative memories over gradients" as the unifying frame for the persist section.
- Multi-level context flows as vocabulary for where a taste signal could sit (a level with its own update rate).

## Kaushik's notes
<!-- yours -->
