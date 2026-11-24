---
type: draft
status: draft
section: 0
tags: [type/draft, status/draft]
links: ["[[outline]]", "[[01-introduction]]"]
---

# Can a language model judge and change itself? A review of metacognition, self-models, weight self-modification and taste

**Authors:** [add names]

**Date:** 24 November 2026

## Abstract

Reasoning models hesitate, check their own steps and sometimes decline to answer. We review what lies under this behavior and how far it could extend: whether a language model can monitor its own internal states, hold a model of itself, judge what it finds as good or bad, and write the result into its own weights, and whether repeated self-change could give it preferences of its own. We organize 137 papers, most from 2024 to 2026, around one loop (monitor, evaluate, control, persist) with a self-model across it and an anchor against collapse. We find that every step has prior art. Hidden states carry readable signals about a model's own work; valence and value signals causally move choices; weights can change after deployment through learned memory or through direct, gradient-free edits; and one open model has edited its own weights. The connections between the steps are weak. Models report their own states poorly below about 30 billion parameters, their self-predictions are generic, and no model predicts the effect of a change to itself. In every weight-changing method, a signal outside the model's own evaluation decides what is kept. Loops on a model's own signal sharpen, drift or decay, and self-training can remove a model's expressed doubt. Measured taste is shared across models, and inherited values persist under self-modification. We state the self-changing, self-judging model as an open agenda, list eight problems with it, propose four tests for a taste of a model's own with an existing instrument for each, and identify a first open question: when a model's weights change after deployment, do its preferences move, and does its self-monitoring change?

**Keywords:** metacognition, introspection, self-models, world models, model editing, weight-space programming, continual learning, preferences, taste, self-improvement
