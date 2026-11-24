---
type: draft
status: draft
section: 0
tags: [type/draft, status/draft]
links: ["[[outline]]", "[[01-introduction]]"]
---

# Can a language model judge and change itself? A review of metacognition, self-models, weight self-modification, and taste

**Authors:** [add names]

**Date:** 24 November 2026

## Abstract

Language models can now change their own weights after deployment, but no study has checked what such changes do to a model's preferences or to its view of itself. This review asks how far a language model can monitor its own internal states, hold a model of itself, judge what it finds as good or bad, and write the result into its own weights, and whether repeated self-change could give it preferences of its own. It organizes 137 papers, most from 2024 to 2026, around one loop of four steps (monitor, evaluate, control, persist), with a self-model across the loop and an anchor against collapse. Every step has prior work. Hidden states carry readable signals about a model's own work. Valence and value signals causally move choices. Weights can change after deployment through learned memory or through direct, gradient-free edits, and one open model has edited its own weights. The connections between the steps are weak. Open models cannot say whether their internal states were changed, the advantage of a model in predicting itself is disputed, and no model predicts the effect of a change to itself. Where a model's own judgment decides which weight change stays, that judgment is its certainty or a verbal score; no method uses an evaluation signal read from the model's hidden states, and outside scores decide every direct edit. Loops on a model's own signal sharpen, drift, or decay, and self-training can remove a model's expressed doubt. Measured taste is largely shared across models, and inherited values persist under self-modification. The review states the self-changing, self-judging model as an open agenda with nine problems, proposes four tests for a taste of a model's own, and identifies a first open question: when a model's weights change after deployment, do its preferences move, and does its self-monitoring change? A field that can change what a model does needs methods to check what the model has become.

**Keywords:** metacognition, introspection, self-models, world models, model editing, weight-space programming, continual learning, preferences, taste, self-improvement
