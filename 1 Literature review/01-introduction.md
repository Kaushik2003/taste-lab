---
type: draft
status: draft
section: 1
tags: [type/draft, section/1, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Four tests for own taste]]", "[[Metacognition - watch and control yourself]]", "[[Models that change their own weights]]"]
---

# 1. Introduction

Reasoning models now behave, from the outside, as if they know something about themselves. They hesitate, backtrack, write "wait", check their own steps and sometimes decline to answer when unsure. This review asks what lies under that behavior, and how far it could go. Can a language model **monitor** its own internal states, hold a **model of itself**, **judge** what it finds as good or bad, and use that judgment to **control** its reasoning and, in the end, to **change its own weights**? And if a model keeps changing itself by its own judgment, could it develop preferences of its own, a **taste**, that its original weights did not contain?

The question has four parts, and each part has its own literature.

1. **Metacognition.** Psychology has studied how minds watch and steer themselves for decades ([[Monitoring and control between two levels (Nelson 1990)]]). Language models are the first artificial systems where the parts can be measured directly, because their internal states can be read. A Trends in Cognitive Sciences paper by Johnson, Bengio, Mitchell, Rahwan, Schölkopf and others argues that AI has become smart without becoming wise, and that the missing part is metacognition ([[Wise machines need metacognition not just smarts (Johnson 2025)]]). A 2025 review treats metacognition and self-awareness in AI as measurable functions ([[AI awareness as a measurable capacity (Li 2025)]]).
2. **Self-models and world models.** A world model is a learned model that predicts what will happen when an agent acts, so the agent can plan before it acts. A self-model points the same idea inward: the system predicts its own behavior, its own success and its own learning. A 20-author survey of world models finds that metacognition and motivation are their least-studied functions ([[World models miss motivation and metacognition (Rupprecht 2026)]]).
3. **Lasting change to the weights.** A deployed language model is static. Its weights do not change, and what it learns in a conversation is lost when the conversation ends. Two lines of work try to remove this limit. The first trains small parts of the model while it is in use, inside architectures built for that purpose ([[Titans - a memory that learns from surprise at test time (Behrouz 2025)]], [[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]). The second writes small, direct changes into the weights with no gradient training at all. This is **weight-space programming (WSP)** ([[WSP - a model reads and edits weights (Takehi 2026)]]). In late 2026 an open model used it on itself: it read its own hidden states, found a fault, and edited its own weights ([[A model rewrites its own weights (Fan 2026)]]).
4. **Preferences and taste.** Models make consistent choices between acceptable options, and these choices can now be measured ([[Model values form coherent utilities that can be steered (Mazeika 2025)]], [[Models show research taste (Trehan 2026)]]).

These literatures rarely cite each other. The metacognition papers stop at reading and reporting. The world-model papers rarely model the agent itself. The weight-change papers almost never ask who decides what a good change is, or what a change does to the model's preferences and to its view of itself. This review puts them in one frame, so that it is clear which parts of a self-changing, self-judging model exist today and which do not.

## 1.1 The frame: a loop with four steps

We organize the review around one loop. It extends the classic monitor-and-control model of metacognition with two steps.

- **Monitor:** what do the model's hidden states say about its own work, and can the model itself read them?
- **Evaluate:** is there an internal signal that judges a state or an output as good or bad?
- **Control:** how does that judgment change behavior, from choosing among outputs to steering hidden states?
- **Persist:** how does a change get written into the weights, so that what the model prefers now changes what it becomes?

A self-model sits across the loop: to choose a good change, a system must predict what the change will do to itself. An **anchor** sits under the loop: a loop that learns from its own signal can lock onto its own prior and collapse, so something must keep it honest.

Control can act at three levels, from temporary to lasting:
1. **Reasoning level:** pick, rank or revise the model's own outputs.
2. **Activation level:** steer the model's hidden states while it generates.
3. **Weight level:** write the change into the weights.

## 1.2 What we mean by taste

By **taste** we mean a stable set of preferences that a model uses to judge its own work. Most of a model's preferences come from pretraining and human feedback. We call a taste **self-originated** if it moves away from that origin because the model keeps selecting for it. This review does not claim that any model has such a taste, or that one will appear. It treats the idea as a possibility and asks what evidence would be needed. We use four tests, proposed by us and applied in Section 9:
1. **Divergent:** the preference differs from the human and training preference distribution.
2. **Stable:** it holds when the question is reworded or the order of options changes.
3. **Grounded:** it matches an internal state that can be read and that causally drives the choice, not only a verbal self-report.
4. **Self-reinforcing:** it sharpens over repeated self-change without collapse.

## 1.3 Research questions

The review answers six questions, one per main section.

| | Question | Section |
|---|---|---|
| RQ1 | What can a language model monitor about its own states, and does it act on what it monitors? | 3 |
| RQ2 | Can a model hold a model of itself and predict its own behavior and its own changes? | 4 |
| RQ3 | Which internal signals judge a state or an output as good or bad? | 5 |
| RQ4 | How can a model's weights change after deployment, and who decides the change? | 6 |
| RQ5 | What goes wrong when a model learns from its own signals? | 7 |
| RQ6 | How are a model's preferences measured, and does a measured taste belong to one model? | 8 |

## 1.4 Method

This is a narrative review, not a full systematic review. We did not run exhaustive search strings over all digital libraries or count every excluded record. We state what we did so that a reader can judge the coverage.

- **Sources.** We collected papers between 19 and 24 November 2026 from four sources: daily arXiv searches with fixed queries on metacognition, introspection, self-reward, steering, model editing and weight-space programming; targeted web searches on specific open points (stable preference, self-preference, self-referential networks, repeated weight edits, self-report after a weight change); the reading list of a public survey of metacognition in language models; and backward citation from papers we read.
- **Inclusion.** We included a paper if it reports evidence or a framework on at least one step of the loop (monitor, evaluate, control, persist, anchor) in language models, or supplies a classic concept from cognitive science or earlier neural network research that the frame needs.
- **Exclusion.** We excluded pure application papers (for example weight-space programming applied to robot controllers or medical networks), and papers on general model performance with no link to self-monitoring, preference or self-change.
- **Data extraction.** For each included paper we wrote a structured note with the same fields: claim, mechanism, evidence with numbers and their location in the paper, limits, and relevance to the loop.
- **Quality marking.** Each note records how much of the paper was read. Of the 137 papers, 7 were read in full or nearly in full, and the others were skimmed: abstract, introduction, main results and limitations. Several notes rest on the abstract only. We mark such claims in the text with "abstract only".
- **The set.** 137 papers have notes, and this review cites 134 of them, plus 13 further sources that we checked but did not write notes for. Of the 137, 124 are from 2024 to 2026, and 67 from 2026 alone. Seven classic papers from 1990 to 2019 supply the frame. Many 2026 papers are preprints that are not yet peer reviewed.

Section 9.5 lists the limits that follow from this method.

## 1.5 Plan of the review

Section 2 gives the foundations: the monitor-and-control model, how metacognition is measured, and a mapping from brain chemistry to learning settings. Section 3 covers monitoring and the control of reasoning. Section 4 covers self-models and world models. Section 5 covers internal evaluation signals. Section 6 covers changes that persist in the weights, by learned memory and by direct edits. Section 7 covers the limits of learning from one's own signal. Section 8 covers how preferences and taste are measured. Section 9 assembles the loop, states what is missing, lists the problems with the full idea, and names the first open question. Section 10 concludes.

## Log
- 2026-11-23: rewritten as a field map (metacognition, self-models, weight self-change, taste over time).
- 2026-11-24: final pass after the user's "go". Two routes to lasting change (learned memory and direct edits), research questions, method section in the form asked by the writing guide, taste as a possibility.
