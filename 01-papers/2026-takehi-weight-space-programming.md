---
type: paper
title: "Weight-Space Programming (WSP)"
status: read
arxiv: (blog post, Nov 2 2026, "Sparks of Weight-Space Programming")
url: search "Sparks of Weight-Space Programming MIT CSAIL"
authors: Takehi, Teoh, Zhang, Khattab (MIT CSAIL)
year: 2026
venue: blog / preprint
relevance: 3
section: 5
tier: deep
tests: []
components: [consolidation]
tags: [type/paper, section/5, component/consolidation, status/read, relevance/3, weight-space-programming, gradient-free, model-repair]
links: ["[[landscape-persistent-control]]", "[[self-weight-updates]]"]
---

# Weight-Space Programming (WSP)

**One line:** A frontier LLM (GPT-6 Astra) reads another network's raw weights, reasons about what parts compute, and edits them directly. No gradients.

## Mechanism
Give the LLM the raw tensors plus a goal in plain English. It localizes a mechanism (e.g. a "loop direction")
and writes a targeted edit. For the anti-loop fix this was a rank-one edit to an MLP output matrix (see [[2026-fischetti-just-sort-it]]).

## Evidence
Qwen3.5-0.8B MATH-500 went from 7.9% to 48.1% (GSM8K 13.8% → 67.1%) after editing ~0.016% of weights to stop
repetitive reasoning loops. It also wrote small control-policy nets from scratch that beat a 100M-step PPO agent on 3 games.

## Limits
- Works on **localized** problems and struggles when the error is distributed across the network.
- It's an external, bigger model editing a smaller one, not self-editing.
- The ecosystem is moving fast: WeightBench (2611.18553) finds frontier agents can't yet reliably patch LMs.

## Relevance to taste-lab
Gradient-free consolidation for **localized** repairs. Also hints that an edit can bake a direction into the
weights. If steering vectors can be consolidated as rank-one edits, that's persistence without a training loop (→ T5).

## Steal this
The rank-one edit form W' = W + u vᵀ, plus the follow-up finding that v can be a simple sort over low-variance neurons.
