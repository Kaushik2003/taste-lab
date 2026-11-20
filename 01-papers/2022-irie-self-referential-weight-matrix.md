---
type: paper
title: "A Modern Self-Referential Weight Matrix That Learns to Modify Itself"
status: skimmed
arxiv: 2202.05780
url: https://arxiv.org/abs/2202.05780
authors: Kazuki Irie, Imanol Schlag, Róbert Csordás, Jürgen Schmidhuber (KAUST / IDSIA)
year: 2022
venue: ICML 2022
relevance: 2
section: 5
tier: skim
tests: []
components: [consolidation]
tags: [type/paper, section/5, component/consolidation, status/skimmed, relevance/2, self-referential, fast-weights, self-modification, meta-learning]
links: ["[[self-weight-updates]]", "[[2025-zweiger-seal]]", "[[2025-behrouz-nested-learning]]"]
---

# Self-Referential Weight Matrix (Irie et al., ICML 2022)

**One line:** A scalable weight matrix that keeps modifying ALL of itself at runtime via learned outer-product/delta-rule updates - the 90s Schmidhuber self-referential dream made practical with fast-weight-programmer machinery; works on few-shot learning and multi-task RL.

## Claim
A neural net can treat its own weight matrix as its program and learn to rewrite it continually, a step toward recursive self-improvement in principle ([abs](https://arxiv.org/abs/2202.05780)).

## Mechanism
Self-referential WM producing its own delta updates (outer products, delta rule), building on fast weight programmers and linear Transformers.

## Evidence
Competitive few-shot and multi-task RL performance in procedurally generated environments [unverified: baseline margins].

## Limits / what they didn't show
- Small scale; the self-modification is a learned dynamics mechanism, not evaluation-driven: no signal decides WHAT to change based on how the model is doing.
- No stability analysis of unbounded self-modification.

## Relevance to taste-lab
**The deepest architectural ancestor of T4.** If T4 ([[self-weight-change-T4]]) is ever unparked, this is the lineage: self-referential weights -> SEAL ([[2025-zweiger-seal]]) -> Hope ([[2025-behrouz-nested-learning]]). All three modify self without an internal evaluation signal choosing the edit; that missing signal is the gap.
- Prior-art check: **B partial** (the model's own machinery rewrites its weights, but edits are driven by task input dynamics, not by self-evaluation).

## Steal this
- The "weight matrix as program" framing for the persist section's opening.
- Delta-rule self-update as the concrete mechanism class a self-chosen edit would need.

## Kaushik's notes
<!-- yours -->
