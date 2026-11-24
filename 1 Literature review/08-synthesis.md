---
type: draft
status: draft
section: 8
tags: [type/draft, section/8, status/draft]
links: ["[[gaps]]", "[[outline]]", "[[matrix]]", "[[2026-11-23 gap check]]", "[[2026-11-23 direction critique]]", "[[Parked - old synthesis and study protocol]]"]
---

# 9. Synthesis and open problems

## 9.1 The loop, step by step

Table 6 shows where each step of the loop stands.

**Table 6.** The loop, step by step: what exists and what is missing.

| Step | What exists | Strongest evidence | What is missing |
|---|---|---|---|
| **Monitor** | Hidden states carry signals about the model's own work. Probes read them well. | Correctness probes; the model acts on its own confidence when it abstains ([[Models act on their own confidence (Kumaran 2026)]]) | The model's own verbal access. Reports of internal changes are at chance in open models ([[Models cannot tell a real internal change from a fake one (Ferrara 2026)]]) |
| **Self-model** | Trained prediction of one's own behavior; an estimate of one's own learning progress | [[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]]; [[Models predict themselves better than others do (Binder 2024)]] | An undisputed advantage of self over an outside model; prediction of what a change to oneself will do |
| **Evaluate** | Valence, emotion, and value signals that causally move choices | [[Hidden good-bad feeling changes choices (Berg 2026)]]; [[Value axis - model knows it is on track (Jiang 2026)]] | A signal that judges quality beyond correctness and is the model's own |
| **Control** | Meta-level control of reasoning; steering of hidden states | Engineered meta levels (Section 3.4) | Control driven by the model's own evaluation signal |
| **Persist** | Two routes: learned memory with gradients; direct edits without | [[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]; [[A model rewrites its own weights (Fan 2026)]] | A hidden-state evaluation signal deciding what stays; edits that build on earlier edits; a check of what the change did to the model |
| **Anchor** | Outside checks that protect stated limits | Sealed audits and proof checkers (Section 7.4) | A check that protects the monitor itself, and a long run of any direct-edit loop |

Every step has prior art, and previous work connects several pairs of steps: a monitor that drives control (abstention), a self-estimate that drives learning (learning progress), a self-written example that drives a weight update (SEAL, Sleep), a self-found direction that drives a weight edit (self-editing), and a certainty signal that drives training (INTUITOR).

A finding of the form "no system does all of these together" is weak, because a conjunction of four steps is almost always open. The finding of this review does not rest on the conjunction. It rests on three single links that no study has tested:

1. **From a hidden-state evaluation signal to a weight change.** Valence and value signals move choices (Section 5), and certainty and verbal scores drive training (Section 6.4). No study uses a valence or value signal to choose or keep a change to the weights.
2. **From a weight change to the model's preferences.** One study measured one disposition after one edit (Section 6.2). No study measures a broad set of preferences before and after a change, on either route.
3. **From a direct weight change to the model's untrained self-report.** Models describe changes that long training put into them (Section 3.3). One anecdote and one adapter study bear on direct edits (Section 4.2).

## 9.2 The open agenda and its problems

Put together, the literature describes most of the parts of a system that it has not built: a model that keeps changing its own weights after deployment, where the model's own evaluation proposes and judges each change, a model of itself predicts each change, an outside check can veto damage, and an observer watches for drift in its preferences. Position papers ask for something close to this from different sides ([[Self-improving agents need intrinsic metacognition (Liu 2025)]], [[Wise machines need metacognition not just smarts (Johnson 2025)]]). We present it as an agenda, not as a claim that it will work, and a self-originated taste would be its long-term outcome. The agenda has nine serious problems.

1. **It stacks four contested abilities.** Self-monitoring, a self-model, self-directed weight change, and a taste of one's own are each unsettled, and a system that needs all four fails if any one fails.
2. **Direct edits fit local faults; taste is probably spread out.** The clearest gains from weight-space programming are repairs of one fault, mostly reasoning loops (Section 6.3).
3. **The editing step is not where the value lies.** Once the goal of an edit is known, a plain optimizer finds a better edit than the agent, at far lower cost. What an optimizer cannot supply is the choice of goal, which is the evaluation step.
4. **The cost comparison is mixed.** Learned memory with small trained blocks is a strong alternative (Section 6.5).
5. **The value of a self-model is disputed.** Four studies find no advantage of a model over others in predicting itself or its own edits, and one finds an advantage in frontier models (Sections 3.3 and 4.2).
6. **Evidence points away from a taste that drifts.** Inherited values persist under self-modification, and measured taste is shared (Sections 8.3 and 8.4).
7. **Self-judged loops decay and can remove self-monitoring** (Section 7), and repeated direct edits collapse models (Section 6.5).
8. **"Taste" is hard to falsify.** If preferences drift, a critic can call it decay; if they do not, a critic can call them inherited.
9. **The safety literature treats a change in an agent's own criterion as a hazard** (Section 7.5). A research program that hopes to see preferences drift must say why the drift would be good and how anyone would stop a bad one. This review has no answer beyond the outside check of Section 7.4.

## 9.3 Limits of this review

We read seven of the 137 papers in full; most claims rest on abstracts, introductions, main results, and limitations, and claims marked "abstract only" need a check against the full paper. Most 2026 sources are not peer reviewed, and several key results (self-editing, weight-space programming, Sleep, the introspection re-checks) rest on one paper each. The text does not grade sources by venue, sample size, or replication. Positive introspection results come mostly from closed frontier models and negative ones from open models of 32B and below, and studies have rarely tested the two groups with the same method. The loop, the ten controls, the observation about model size, and the four tests are our constructions, and a gap defined across a new frame is easy to find; Section 9.1 therefore states the three single links that carry the finding. Finally, a language model searched for the papers, wrote the notes, and drafted the text under the authors' direction (see the statement at the end), and errors of summary that a specialist reader would catch may remain.

## 9.4 Open problems, and a first question

Six open problems follow from the review. (1) Does a model's description of itself follow a direct edit to its weights, without training to report? (2) Does a weight change move a broad set of a model's preferences? (3) Can a signal read from the model's own hidden states choose which change to keep, and does it agree with outside checks? (4) Can a model make edits that build on its earlier edits without collapse? (5) Can a model, or an outside predictor, say what an edit will do before the model makes it? (6) Over repeated change, does a model's preference for its own output grow beyond the taste all models share?

Problems 1 and 2 come first, because the others depend on them. If weight changes do not carry preferences, there is nothing for a self-originated taste to live in. If a model cannot tell what it has become, it cannot steer its own development. They combine into one question:

> **When a model's weights change after deployment, do its preferences move, and does its self-monitoring change?**

The question applies to both routes of Section 6. The instruments reviewed here can measure each part: preference batteries under controlled context (Section 8.2), expressed doubt (Section 7.2), and stated against behavioral preferences (Section 3.3). The question has four possible outcomes, and each is informative (Table 7). We found no study that changes a model's weights and then measures both its preferences and its self-monitoring.

**Table 7.** The four possible outcomes of the first question.

| | The model's self-monitoring registers the change | It does not |
|---|---|---|
| **Preferences move** | The conditions for self-steered development exist | Silent drift: the model changes and cannot tell |
| **Preferences do not move** | Self-reports of change cannot be trusted | Small weight changes do not carry taste; taste needs another mechanism |

## Log
- 2026-11-20 to 22: earlier versions built around a code-readability study. That text, with its study protocol, is kept in [[Parked - old synthesis and study protocol]].
- 2026-11-24 (guides and critique): the finding now rests on three single untested links, not on a four-way conjunction; the claim about who decides a weight change is corrected; a ninth problem (the safety view of preference change) and four limits (ungraded evidence, circular tests, frame-shaped finding, AI drafting) added.
- 2026-11-24: rewritten after the user's decisions: the full idea as an open agenda, its problems stated, taste as a possibility, and one closing question. Sources for the decisions: [[2026-11-23 gap check]], [[2026-11-23 direction critique]].
- 2026-11-24 (IEEE build): removed a blank line before problem 9, so the list of nine problems no longer restarts at 1.
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/08-synthesis (long).md`.
