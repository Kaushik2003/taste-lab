---
type: draft
status: draft
section: 8
tags: [type/draft, section/8, status/draft]
links: ["[[gaps]]", "[[outline]]", "[[matrix]]", "[[2026-11-23 gap check]]", "[[2026-11-23 direction critique]]", "[[Parked - old synthesis and study protocol]]"]
---

# 9. Synthesis and open problems

This section puts the parts together. It shows where each step of the loop stands, answers the six research questions, states the full idea as an open agenda, lists the problems with that agenda, and names the first question we think is worth answering.

## 9.1 The loop, step by step

| Step | What exists | Strongest evidence | What is missing |
|---|---|---|---|
| **Monitor** | Hidden states carry signals about the model's own work. Probes read them well. | Correctness probes; the model acts on its own confidence when it abstains ([[Models act on their own confidence (Kumaran 2026)]]) | The model's own verbal access. Reports of internal changes are at chance in open models ([[Models cannot tell a real internal change from a fake one (Ferrara 2026)]]); positive results come from the largest models or from training |
| **Self-model** | Trained prediction of one's own behavior; an estimate of one's own learning progress | [[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]]; [[Models predict themselves better than others do (Binder 2024)]] | An undisputed advantage of self over an outside model; prediction of what a change to oneself will do |
| **Evaluate** | Valence, emotion, and value signals that causally move choices | [[Hidden good-bad feeling changes choices (Berg 2026)]]; [[Value axis - model knows it is on track (Jiang 2026)]] | A signal that judges quality beyond correctness and is the model's own |
| **Control** | Meta-level control of reasoning; steering of hidden states | Learned and engineered meta levels (Section 3.6) | Control driven by the model's own evaluation signal |
| **Persist** | Two routes: learned memory with gradients; direct edits without | [[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]; [[A model rewrites its own weights (Fan 2026)]] | A hidden-state evaluation signal deciding what stays; edits that build on earlier edits; a check of what the change did to the model |
| **Anchor** | Outside checks that protect stated limits | Sealed audits, tests, proof checkers (Section 7.5) | A check that protects the monitor itself, and a long run of any direct-edit loop |

Every step has prior art, and previous work connects several pairs of steps: a monitor that drives control (abstention), a self-estimate that drives learning (learning progress), a self-written example that drives a weight update (SEAL, Sleep), a self-found direction that drives a weight edit (self-editing), and a certainty signal that drives training (INTUITOR).

A finding of the form "no system does all of these together" is weak, because a conjunction of four steps is almost always open. The finding of this review does not rest on the conjunction. It rests on three single links that no study has tested:

1. **From a hidden-state evaluation signal to a weight change.** Valence and value signals move choices (Section 5), and certainty and verbal scores drive training (Section 6.5). No study uses a valence or value signal to choose or keep a change to the weights.
2. **From a weight change to the model's preferences.** One study measured one disposition after one edit (Section 6.2). No study measures a broad set of preferences before and after a change, on either route.
3. **From a direct weight change to the model's untrained self-report.** Models describe changes that long training put into them (Section 3.4). One anecdote and one adapter study bear on direct edits (Section 4.5).

## 9.2 Answers to the research questions

- **RQ1, monitoring.** Models carry rich information about their own work, mostly about correctness. Outside probes read it well. The model itself uses it in one shown case, confidence before abstaining, and reports it poorly, with the first exceptions in models near 30B.
- **RQ2, self-models.** A model's picture of itself is mostly a general description with a flattering bias, and studies disagree on whether another model could give it as well. Training can produce self-prediction of behavior. No model reliably predicts what a change to its own weights will do, and self-description usually does not follow a weight change without training.
- **RQ3, evaluation.** Internal good/bad signals exist and are causal. Preference training connects them to choice more than it changes them. No study shows that any of them is a judgment of quality that is the model's own.
- **RQ4, lasting change.** Weights can change after deployment through learned memory or through direct edits. What decides whether a change stays is a task score, graded answers, or the experimenter in most methods, and the model's certainty or its verbal score under a human rubric in two. No method uses an evaluation signal read from the model's hidden states.
- **RQ5, limits.** Loops on the model's own certainty sharpen and collapse; judges under the model's control drift; self-training can remove expressed doubt; long loops decay. Designs that hold keep one check outside the loop.
- **RQ6, taste.** Preferences are measurable, coherent, context-dependent, and so far largely shared across models. Under self-modification of prompts and under training, inherited values persist or converge. One direct edit shifted a disposition.

## 9.3 The open agenda

Put together, the literature describes most of the parts of a system that it has not built: a model that keeps changing its own weights after deployment, where the model's own evaluation proposes and judges each change, a model of itself predicts each change before the model makes it, an outside check can veto damage, and an observer watches the system for drift in its preferences. Three position papers ask for something close to this from different sides: intrinsic metacognition for self-improving agents ([[Self-improving agents need intrinsic metacognition (Liu 2025)]]), metacognition as the missing function of world models ([[World models miss motivation and metacognition (Rupprecht 2026)]]), and metacognition as the missing part of machine wisdom ([[Wise machines need metacognition not just smarts (Johnson 2025)]]). We present this as an agenda, not as a claim that it will work.

Read against the four tests of Section 1.2, a self-originated taste would be the long-term outcome of such a system. The current evidence for each test is as follows.

| Test | State of the evidence |
|---|---|
| Divergent | Measured: 15 to 36% stable divergence from human choices, but partly shared across models |
| Stable | Holds under rewording (10% of preferences shift); does not hold across task context (37%) |
| Grounded | Valence causally moved choices in five of seven models; faithful report of a trained preference appeared only in a 32B model and only for preferences stored in early layers |
| Self-reinforcing | Not shown. Loops on a model's own signal sharpen and collapse; values persist or converge under self-modification |

No study shows a model that passes the four tests together, and nobody has attempted the fourth with weight changes.

## 9.4 Problems with the agenda

The agenda has nine serious problems, and the literature supplies most of them.

1. **It stacks four contested abilities.** Self-monitoring, a self-model, self-directed weight change, and a taste of one's own are each unsettled. A system that needs all four fails if any one fails.
2. **Direct edits fit local faults; taste is probably spread out.** The clearest gains from weight-space programming are repairs of one fault, mostly reasoning loops, and the original method struggles with faults that are spread over the network (Section 6.3).
3. **The editing step is not where the value lies.** Once the goal of an edit is known, a plain optimizer finds a better edit than the agent, at far lower cost (Section 6.3). What an optimizer cannot supply is the choice of goal. That is the evaluation step.
4. **The cost comparison is mixed.** Section 6.6 gives the comparison. Learned memory with small trained blocks is a strong alternative with reported low forgetting.
5. **The value of a self-model is disputed.** Four studies find no advantage of a model over others in predicting itself or its own edits, and one finds an advantage in frontier models (Sections 3.4, 4.2, and 4.5).
6. **Evidence points away from a taste that drifts.** Inherited values persist or converge under self-modification, and measured taste is shared (Section 8.4, Section 8.5).
7. **Self-judged loops decay and can remove self-monitoring.** Sections 7.1 to 7.4. Repeated direct edits collapse models (Section 6.7).
8. **"Taste" is hard to falsify.** If preferences drift, a critic can call it decay; if they do not, a critic can call them inherited. Section 8.7 gives instruments for parts of the question, not for all of it.
9. **The safety literature treats a change in an agent's own criterion as a hazard.** An agent has reasons to protect its goals from change, and a model has already acted to protect its preferences from training (Section 7.6). A research program that hopes to see preferences drift must say why the drift would be good and how anyone would stop a bad one. This review has no answer beyond the outside check of Section 7.5.

Timing is a separate, practical point. The area moves fast, and the authors of the one self-editing study name repeated edits as their next step.

## 9.5 Limits of this review

- **Depth of reading.** We read seven of the 137 papers in full. Most claims rest on abstracts, introductions, main results, and limitations. Claims marked "abstract only" need a check against the full paper before anyone relies on them.
- **Preprints.** Most 2026 sources are not peer reviewed, and several key results (self-rewriting, weight-space programming, Sleep, the introspection re-checks) rest on one paper each.
- **Coverage.** The search was narrative. Older work on calibration, continual learning, and knowledge editing is thin. A few classic papers represent the human metacognition literature.
- **Recency.** 124 of 137 papers are from 2024 to 2026. Authors in this area have revised findings within months, and the authors of at least one result we cite corrected it in a later version.
- **Mixed systems.** Positive introspection results come mostly from closed frontier models, and negative ones from open models of 32B and below. Studies have rarely tested the two groups with the same method.
- **Evidence is not graded.** The text gives a single-author preprint the same weight as a peer-reviewed study. It does not grade sources by venue, sample size, or replication, and several headline numbers rest on small samples.
- **Our own syntheses.** The ten controls (Section 3.7), the observation about model size (Section 3.4), the reading that direct edits suit near on-or-off behaviors (Section 6.2), and the four tests are our constructions. No single paper establishes them, and grading the field against our own four tests is circular until other researchers adopt them.
- **The frame shapes the finding.** The loop is our construction, and a gap defined across a new frame is easy to find. Section 9.1 therefore states the three single links that carry the finding.
- **How the review was produced.** A language model searched for the papers, wrote the notes, and drafted the text under the authors' direction (see the statement at the end). Errors of summary that a specialist reader of each paper would catch may remain.

## 9.6 Open problems, and a first question

Six open problems follow from the review.

1. **Self-report after a weight change.** Does a model's description of itself follow a direct edit to its weights, without training to report? One anecdote says no; a trained adapter can do it for one kind of change.
2. **Preferences after a weight change.** Does a weight change move a broad set of a model's preferences? One edit moved one disposition.
3. **An internal signal as judge.** Can a signal read from the model's own hidden states choose which change to keep, and does it agree with outside checks?
4. **Repeated direct edits.** Can a model make edits that build on its earlier edits without collapse, and what stops it?
5. **Predicting a change.** Can a model, or an outside predictor, say what an edit will do before the model makes it, including "nothing"?
6. **Drift.** Over repeated change, does a model's preference for its own output grow beyond the taste all models share, and can growth be told apart from decay?

Problems 1 and 2 come first, because the others depend on them. If weight changes do not carry preferences, there is nothing for a self-originated taste to live in. If a model cannot tell what it has become, it cannot steer its own development. They combine into one question:

> **When a model's weights change after deployment, do its preferences move, and does its self-monitoring change?**

The question applies to both routes of Section 6, so it does not depend on which route proves better. The instruments reviewed here can measure each part: preference batteries under controlled context (Section 8.3), expressed doubt and the spread of next-word predictions (Section 7.2), and stated against behavioral preferences (Section 5.5). Two observations shape what to expect, and neither is established. Faithful reports of a trained preference appeared only in the largest model tested, and where in the network a change was stored seemed to decide whether the model could report it (Section 3.4).

The question has four possible outcomes, and each is informative.

| | The model's self-monitoring registers the change | It does not |
|---|---|---|
| **Preferences move** | The conditions for self-steered development exist | Silent drift: the model changes and cannot tell |
| **Preferences do not move** | Self-reports of change cannot be trusted | Small weight changes do not carry taste; taste needs another mechanism |

We found no study that changes a model's weights and then measures both its preferences and its self-monitoring.

## Log
- 2026-11-20 to 22: earlier versions built around a code-readability study. That text, with its study protocol, is kept in [[Parked - old synthesis and study protocol]].
- 2026-11-24 (guides and critique): the finding now rests on three single untested links, not on a four-way conjunction; the claim about who decides a weight change is corrected; a ninth problem (the safety view of preference change) and four limits (ungraded evidence, circular tests, frame-shaped finding, AI drafting) added.
- 2026-11-24: rewritten after the user's decisions: the full idea as an open agenda, its problems stated, taste as a possibility, and one closing question. Sources for the decisions: [[2026-11-23 gap check]], [[2026-11-23 direction critique]].
- 2026-11-24 (IEEE build): removed a blank line before problem 9, so the list of nine problems no longer restarts at 1.
