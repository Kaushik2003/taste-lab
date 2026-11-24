---
type: draft
status: draft
section: 1
tags: [type/draft, section/1, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Four tests for own taste]]", "[[Metacognition - watch and control yourself]]", "[[Models that change their own weights]]"]
---

# 1. Introduction

Reasoning models now behave as if they know something about themselves. They hesitate, backtrack, write "wait", check their own steps, and sometimes decline to answer when unsure. This review asks what lies under that behavior and how far it could go. Can a language model monitor its own internal states, hold a model of itself, judge what it finds as good or bad, and use that judgment to control its reasoning and to change its own weights? And if a model keeps changing itself by its own judgment, could it develop preferences of its own, a taste, that its original weights did not contain?

One recent result makes the problem concrete. Removing a single direction from a model's weights stops the model from refusing requests. The same edit, in two model families, also made the models more optimistic on a task that had nothing to do with refusal, and nobody had chosen that change ([[One weight edit shifts a model's disposition (Fafuła 2026)]]). The study did not ask whether the edited models could tell that they had changed. A small change to the weights moved what the models chose, and the study could not say whether the models registered the change. Tools that let a model change its own weights now exist. The question of what such changes do to a model's preferences, and to its view of itself, has become practical.

The answer of this review, in brief, is as follows. Every part of a self-changing, self-judging model has prior work. Models carry readable signals about their own work. They carry internal good-or-bad signals that move their choices. Their weights can change after deployment, and one model has edited its own. The connections between the parts are missing. Open models cannot report a change to their own internal states. Where a model's own judgment decides which weight change stays, that judgment is its certainty or a verbal score, and loops on those signals drift; no method uses an evaluation signal read from the model's hidden states. No study changes a model's weights and then measures both its preferences and its self-monitoring.

The question draws on four literatures.

1. **Metacognition.** Psychology has studied how minds watch and steer themselves for decades ([[Monitoring and control between two levels (Nelson 1990)]]). Language models are the first artificial systems where researchers can measure the parts directly, because they can read the model's internal states. A Trends in Cognitive Sciences paper by Johnson, Bengio, Mitchell, Rahwan, Schölkopf, and others argues that AI has become smart without becoming wise, and that the missing part is metacognition ([[Wise machines need metacognition not just smarts (Johnson 2025)]]). A 2025 review treats metacognition and self-awareness in AI as measurable functions ([[AI awareness as a measurable capacity (Li 2025)]]).
2. **Self-models and world models.** A world model is a learned model that predicts what will happen when an agent acts, so the agent can plan before it acts. A self-model points the same idea inward: the system predicts its own behavior, its own success, and its own learning. A 20-author survey of world models finds that metacognition and motivation are their least-studied functions ([[World models miss motivation and metacognition (Rupprecht 2026)]]).
3. **Lasting change to the weights.** A deployed language model is static. Its weights do not change, and it loses what it learns in a conversation when the conversation ends. Two lines of work try to remove this limit. The first trains small parts of the model while it is in use ([[Titans - a memory that learns from surprise at test time (Behrouz 2025)]], [[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]). The second writes small, direct changes into the weights with no gradient training. This second line is called weight-space programming ([[WSP - a model reads and edits weights (Takehi 2026)]]). In late 2026 an open model applied it to itself: the model read its own hidden states, found a fault, and edited its own weights ([[A model rewrites its own weights (Fan 2026)]]).
4. **Preferences and taste.** Models make consistent choices between acceptable options, and researchers can now measure these choices ([[Model values form coherent utilities that can be steered (Mazeika 2025)]], [[Models show research taste (Trehan 2026)]]).

These literatures rarely cite each other. The metacognition papers stop at reading and reporting. The world-model papers rarely model the agent itself. The weight-change papers almost never ask who decides what a good change is, or what a change does to the model's preferences and to its view of itself.

**Contributions.** This review makes five contributions.

1. It places the four literatures in one frame, a loop of four steps (Section 1.1), and shows for each step what previous work has established and what is missing (Section 9.1).
2. It compares two routes to lasting weight change, learned memory and direct edits, which previous work treats separately, by who proposes a change and who decides whether it stays (Section 6.5).
3. It collects ten controls that a claim about a model's self-monitoring should pass (Section 3.7).
4. It proposes four tests for a taste of a model's own and names a previous instrument for each (Section 8.7).
5. It states the self-changing, self-judging model as an open agenda, lists nine problems with that agenda, and identifies one first question that no study has answered (Sections 9.4 and 9.6).

## 1.1 The frame: a loop with four steps

We organize the review around one loop. It extends the classic monitor-and-control model of metacognition with two steps.

- **Monitor:** what do the model's hidden states say about its own work, and can the model itself read them?
- **Evaluate:** is there an internal signal that judges a state or an output as good or bad?
- **Control:** how does that judgment change behavior, from choosing among outputs to steering hidden states?
- **Persist:** how does a change get written into the weights, so that what the model prefers now changes what it becomes?

A self-model sits across the loop: to choose a good change, a system must predict what the change will do to itself. An **anchor** sits under the loop: a loop that learns from its own signal can lock onto its own prior and collapse, so something must keep it honest.

Figure 1 shows the loop.

![Figure 1. The loop of this review. Solid arrows are the four steps. The self-model predicts the effect of a change before the model makes it. The anchor is a check outside the loop. For each step the figure names what previous work has shown (plain text) and what is missing (italic).](figures/loop.png)

Control can act at three levels, from temporary to lasting:
1. **Reasoning level:** pick, rank, or revise the model's own outputs.
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

- **Sources.** We collected papers between 19 and 24 November 2026 from four sources: daily arXiv searches with fixed queries on metacognition, introspection, self-reward, steering, model editing, and weight-space programming; targeted web searches on specific open points (stable preference, self-preference, self-referential networks, repeated weight edits, self-report after a weight change); the reading list of the largest survey of metacognition in language models ([[Survey of metacognition in language models (Liu 2026)]]), which supplied at least 32 of our papers; and backward citation from papers we read.
- **Inclusion.** We included a paper if it reports evidence or a framework on at least one step of the loop (monitor, evaluate, control, persist, anchor) in language models, or supplies a classic concept from cognitive science or earlier neural network research that the frame needs.
- **Exclusion.** We excluded pure application papers (for example weight-space programming applied to robot controllers or medical networks), and papers on general model performance with no link to self-monitoring, preference, or self-change.
- **Data extraction.** For each included paper we wrote a structured note with the same fields: claim, mechanism, evidence with numbers and their location in the paper, limits, and relevance to the loop.
- **Quality marking.** Each note records how much of the paper we read. We read 7 of the 137 papers in full or nearly in full, and skimmed the others: abstract, introduction, main results, and limitations. Some notes rest on the abstract only. The text marks claims from those notes with "abstract only".
- **The set.** 137 papers have notes. This review cites 134 of them, plus 35 further sources without notes: classic papers that we cite for lineage, and recent papers of which we checked the abstract. Table 1 shows their distribution. Among the skimmed papers, some notes rest on the abstract only, and the text marks each statement that comes from such a note. About two thirds of the 137 are preprints or blog posts that are not peer reviewed, and 21 appeared in November 2026, the month of writing. The central concept of Section 6.3, weight-space programming, comes from a blog post of 2 November 2026.

**Table 1.** The 137 papers by year of publication and by depth of reading.

| Year | Papers | | Depth of reading | Papers |
|---|---|---|---|---|
| 1990 to 2019 | 7 | | Read in full or nearly in full | 7 |
| 2022 to 2023 | 6 | | Skimmed: abstract, introduction, main results, and limitations, or less | 130 |
| 2024 | 17 | | | |
| 2025 | 40 | | | |
| 2026 | 67 | | | |

Section 9.5 lists the limits that follow from this method.

## 1.5 Plan of the review

Section 2 gives the foundations. Sections 3 to 8 each answer one research question. Section 9 assembles the loop, states the agenda and its problems, and names the first open question. Section 10 concludes.

## Log
- 2026-11-23: rewritten as a field map (metacognition, self-models, weight self-change, taste over time).
- 2026-11-24 (guides and critique): Figure 1; the corpus source and the share of preprints named in the method; the claim about who decides a weight change corrected.
- 2026-11-24 (later): style pass with the user's writing guides: main findings and contributions stated up front, a concrete opening example, a distribution table, active voice, serial commas.
- 2026-11-24: final pass after the user's "go". Two routes to lasting change (learned memory and direct edits), research questions, method section in the form asked by the writing guide, taste as a possibility.
