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

Language models can now change their own weights after deployment, but no study has checked what such changes do to a model's preferences or to its view of itself. This review asks how far a language model can monitor its own internal states, hold a model of itself, judge what it finds as good or bad, and write the result into its own weights, and whether repeated self-change could give it preferences of its own. It organizes the literature, mostly from 2024 to 2026, around one loop of four steps (monitor, evaluate, control, persist), with a self-model across the loop and an anchor against collapse. Every step has prior work: hidden states carry readable signals about a model's own work, valence and value signals causally move choices, and weights can change through learned memory or through direct, gradient-free edits. The connections between the steps are weak. Open models cannot say whether their internal states were changed, and no model predicts the effect of a change to itself. Where a model's own judgment decides which weight change stays, that judgment is its certainty or a verbal score, and loops on such signals sharpen, drift, or decay. Measured taste is largely shared across models. The review states the self-changing, self-judging model as an open agenda with nine problems, proposes four tests for a taste of a model's own, and identifies a first open question: when a model's weights change after deployment, do its preferences move, and does its self-monitoring change?

**Keywords:** metacognition, introspection, self-models, world models, model editing, weight-space programming, continual learning, preferences, taste, self-improvement

## Log
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/00-title-and-abstract (long).md`.
