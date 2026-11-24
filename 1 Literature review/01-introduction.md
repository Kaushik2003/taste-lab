---
type: draft
status: draft
section: 1
tags: [type/draft, section/1, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Four tests for own taste]]", "[[Metacognition - watch and control yourself]]", "[[Models that change their own weights]]"]
---

# 1. Introduction

Reasoning models now behave as if they know something about themselves. They hesitate, backtrack, write "wait", and sometimes decline to answer when unsure. This review asks how far that could go. Can a language model monitor its own internal states, judge what it finds as good or bad, and use that judgment to change its own weights? And if it keeps changing itself by its own judgment, could it develop preferences of its own, a taste, that its original weights did not contain?

One recent result makes the problem concrete. Removing a single direction from a model's weights stops the model from refusing requests. The same edit, in two model families, also made the models more optimistic on a task that had nothing to do with refusal, and nobody had chosen that change ([[One weight edit shifts a model's disposition (Fafuła 2026)]]). The study did not ask whether the edited models could tell that they had changed. Tools that let a model change its own weights now exist, so the question has become practical.

The answer of this review, in brief: every part of a self-changing, self-judging model has prior work, and the connections between the parts are missing. In particular, no study changes a model's weights and then measures both its preferences and its self-monitoring.

The question draws on four literatures that rarely cite each other. The first is metacognition, the study of how minds watch and steer themselves ([[Monitoring and control between two levels (Nelson 1990)]]); a recent position paper argues that it is what current AI lacks ([[Wise machines need metacognition not just smarts (Johnson 2025)]]). The second is world models, which rarely model the agent itself ([[World models miss motivation and metacognition (Rupprecht 2026)]]). The third is lasting weight change, by training small parts of a model while it is in use ([[Titans - a memory that learns from surprise at test time (Behrouz 2025)]], [[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]) or by small, direct edits with no gradient training, called weight-space programming ([[WSP - a model reads and edits weights (Takehi 2026)]]). In late 2026 an open model applied such an edit to itself ([[A model rewrites its own weights (Fan 2026)]]). The fourth measures the consistent choices that models make between acceptable options ([[Model values form coherent utilities that can be steered (Mazeika 2025)]], [[Models show research taste (Trehan 2026)]]). The weight-change papers almost never ask who decides what a good change is, or what a change does to the model's preferences.

This review makes five contributions.

1. One frame, a loop of four steps, with what previous work has established and what is missing at each step (Section 9.1).
2. A comparison of two routes to lasting weight change, learned memory and direct edits, by who proposes a change and who decides whether it stays (Section 6.4).
3. Ten controls that a claim about a model's self-monitoring should pass (Section 3.5).
4. Four tests for a taste of a model's own, with a previous instrument for each (Section 8.5).
5. The self-changing, self-judging model stated as an open agenda, with nine problems and one first question that no study has answered (Sections 9.2 and 9.4).

## 1.1 The frame: a loop with four steps

We organize the review around one loop (Figure 1). It extends the classic monitor-and-control model of metacognition with two steps, evaluate and persist.

- **Monitor:** what do the model's hidden states say about its own work, and can the model itself read them?
- **Evaluate:** is there an internal signal that judges a state or an output as good or bad?
- **Control:** how does that judgment change behavior?
- **Persist:** how does a change get written into the weights, so that what the model prefers now changes what it becomes?

A **self-model** sits across the loop: to choose a good change, a system must predict what the change will do to itself. An **anchor** sits under it: a loop that learns from its own signal can collapse onto its own prior, so something outside must keep it honest. Control can act at three levels: on the model's outputs (reasoning level), on its hidden states during a run (activation level), and on its weights.

![Figure 1. The loop of this review. Solid arrows are the four steps. The self-model predicts the effect of a change before the model makes it. The anchor is a check outside the loop. For each step the figure names what previous work has shown (plain text) and what is missing (italic).](figures/loop.png)

## 1.2 Taste and the four tests

By **taste** we mean a stable set of preferences that a model uses to judge its own work. We call a taste **self-originated** if it moves away from its origin in pretraining and human feedback because the model keeps selecting for it. This review does not claim that any model has such a taste. It treats the idea as a possibility and asks what evidence would be needed. We propose four tests, and each removes one cheaper explanation.

1. **Divergent:** the preference differs from the human and training preference distribution.
2. **Stable:** it holds when the question is reworded or the order of options changes; otherwise it could be noise.
3. **Grounded:** it matches an internal state that causally drives the choice; otherwise it could be a verbal habit.
4. **Self-reinforcing:** it sharpens over repeated self-change without collapse onto the model's prior.

## 1.3 Research questions and method

The review answers six questions, one per main section (Table 1).

**Table 1.** The six research questions and the sections that answer them.

| | Question | Section |
|---|---|---|
| RQ1 | What can a language model monitor about its own states, and does it act on what it monitors? | 3 |
| RQ2 | Can a model hold a model of itself and predict its own behavior and its own changes? | 4 |
| RQ3 | Which internal signals judge a state or an output as good or bad? | 5 |
| RQ4 | How can a model's weights change after deployment, and who decides the change? | 6 |
| RQ5 | What goes wrong when a model learns from its own signals? | 7 |
| RQ6 | How are a model's preferences measured, and does a measured taste belong to one model? | 8 |

This is a narrative review, not a systematic one. We collected papers between 19 and 24 November 2026 from arXiv searches with fixed queries, targeted web searches on open points, the reading list of the largest survey of metacognition in language models ([[Survey of metacognition in language models (Liu 2026)]]), and backward citation. We included a paper if it reports evidence or a framework on at least one step of the loop in language models, or supplies a classic concept that the frame needs, and we wrote a structured note on each: claim, mechanism, evidence, limits, and relevance.

The corpus has 137 notes. A longer version of this review cites 134 of them and 35 further sources; this version cites the 75 sources that carry the argument. Three facts limit the evidence. We read 7 of the 137 papers in full or nearly in full and skimmed the others; the text marks claims that rest on an abstract with "abstract only". About two thirds of the papers are preprints or blog posts that are not peer reviewed. And 21 appeared in November 2026, the month of writing; weight-space programming itself comes from a blog post of 2 November 2026. Section 9.3 lists the limits that follow.

## Log
- 2026-11-23: rewritten as a field map (metacognition, self-models, weight self-change, taste over time).
- 2026-11-24 (guides and critique): Figure 1; the corpus source and the share of preprints named in the method; the claim about who decides a weight change corrected.
- 2026-11-24 (later): style pass with the user's writing guides: main findings and contributions stated up front, a concrete opening example, a distribution table, active voice, serial commas.
- 2026-11-24: final pass after the user's "go". Two routes to lasting change (learned memory and direct edits), research questions, method section in the form asked by the writing guide, taste as a possibility.
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/01-introduction (long).md`.
