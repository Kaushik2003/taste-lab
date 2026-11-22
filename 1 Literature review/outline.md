# Lit review outline: Metacognition in Reasoning Models

Due 2026-11-24. Papers are placed by the `section:` field in their notes, deep tier first. The spine is the loop from the charter: monitor → evaluate → control → persist, with an anchor against collapse. Section 8 is where the pieces meet.

## 1. Introduction

Purpose: state the question (can a reasoning model judge its own internal states with a taste of its own, and use that judgment to control its thinking and its weights) and say why code readability is the testbed: programs can be matched on observed test outcomes while readability varies; passing tests does not establish complete equivalence.

- [[Complexity feedback changes agent code style (Chapados 2026)]] (skim): agent code style moves while tests hold correctness. Supports code readability as the testbed. Abstract only.
- Draw on [[Four tests for own taste]] and the "Nobody has yet shown..." draft in [[Gaps in the field]].

## 2. Foundations

Purpose: give the frame the rest of the review uses. Nelson & Narens' object level and meta level (monitor, control), Fleming & Daw's second-order view of confidence, and Doya's mapping of neuromodulators to learning parameters.

- [[Monitoring and control between two levels (Nelson 1990)]] (deep): the object level and meta level, monitoring up and control down.
- [[Models mostly know what they know (Kadavath 2022)]] (deep): calibration, P(True) and P(IK), the classic self-knowledge result.
- [[Models predict themselves better than others do (Binder 2024)]] (deep): the cross-model control for privileged self-knowledge.
- [[Trained confidence tracks consistency, not accuracy (Yax 2026)]] (deep): trained self-monitoring reads answer consistency away from the training data. A threat to monitoring claims.
- [[Survey of metacognition in language models (Liu 2026)]] (deep): the survey to position against. It has monitor and control, but no taste and no weight self-edits.
- [[Neuromodulators set how the brain learns (Doya 2002)]] (skim): the four learning knobs for the controller. Abstract only; no open full text found.
- Concept notes to draw on: [[Metacognition - watch and control yourself]], [[Neuromodulators as learning settings]], [[Good-bad signal probe]], [[Models that change their own weights]].
- [[Confidence is a guess about your own decision (Fleming 2017)]] (deep): confidence as a second-order inference about one's own decision, so it can come apart from performance. Added 2026-11-20.
- [[A test battery for self-monitoring (Cacioli 2026)]] (skim): human metacognition tests applied to language models. Abstract only.
- [[What a system changes when it changes itself (Koch 2026)]] (skim): a frame for kinds of self-change, from settings to rules. Abstract only.
- [[Backpropamine - a network sets its own plasticity (Miconi 2019)]] (skim): a network outputs its own "dopamine" signal, which sets how fast its plastic weights change. A machine version of the Doya learning-rate knob.

## 3. Monitoring

Purpose: what a model's hidden states say about its own work, and whether the model itself (not an outside probe) can read them. The short answer so far: probes can, self-report mostly cannot.

- [[Models can report and control their own activations (Ji-An 2025)]] (deep)
- [[Models sometimes notice injected thoughts (Lindsey 2025)]] (deep)
- [[Training LMs to watch themselves (Wang 2026)]] (deep)
- [[Models know when they are right (Zhang 2025)]] (deep)
- [[Models do not report injected pain (Ferrara 2026)]] (deep)
- [[Introspection claims fail basic checks (Singh 2026)]] (deep)
- [[Probes find injections long before models report them (Rubin 2026)]] (deep): a probe finds injections long before the model reports them; decodable even in random networks. Added 2026-11-20.
- [[Trained self-prediction without an own-model edge (Zeng 2026)]] (deep): trained self-prediction improves, but with no consistent own-model edge. Added 2026-11-20.
- [[Outside controller steers thinking modes (Karpf 2026)]] (skim)
- [[Models know when they know but do not act (Cao 2026)]] (deep): the model's own reports carry the signal, but a classifier trained on outside labels makes the retry decision.
- [[Models describe behaviors they were trained into (Betley 2025)]] (deep): after fine-tuning, models can describe the new behavior, though training never named it. The report is noisy. Self-report follows a weight change.
- [[Models report preference weights trained into them (Plunkett 2025)]] (deep): models state the preference weights trained into them (correlation about 0.5, about 0.75 after training on correct reports). The first self-report of an evaluation; no cross-model control.

## 4. Evaluation signals

Purpose: the candidate "good or bad" signals inside the model (emotion, valence, value axes, value neurons), what they track, and whether they cause choices. This is where taste would live.

- [[Emotion directions drive choices in Claude (Anthropic 2026)]] (deep)
- [[Hidden good-bad feeling changes choices (Berg 2026)]] (deep)
- [[Steer code readability inside the model (Gao 2026)]] (deep)
- [[Value axis - model knows it is on track (Jiang 2026)]] (deep)
- [[Few neurons predict right answers (Xu 2026)]] (deep)
- [[One evaluation circuit for all norms (Liga 2026)]] (skim): one shared evaluation circuit for moral, aesthetic and other norm judgments in 14 models; features may track a cue word. Abstract only.

## 5. Persistent control

Purpose: how a change in behavior gets written into the weights, from SEAL-style self-edits for distributed changes to rank-one edits for localized ones. Also the prior art that killed Q5 (steering directions written into weights).

- [[SEAL - models write their own training data (Zweiger 2025)]] (deep)
- [[TFTV - turn a steering vector into a weight edit (Perin 2026)]] (deep)
- [[WSP - a model reads and edits weights (Takehi 2026)]] (deep)
- [[One direction controls refusal (Arditi 2024)]] (skim)
- [[A simple sort replaces the anti-loop edit (Fischetti 2026)]] (skim)
- [[Steer2Edit - steering into small weight edits (Sun 2026)]] (deep)
- [[ThinkEdit - edit weights to think longer (Sun 2025)]] (skim)
- [[Exploring WSP - small weight edits, uneven results (Hu 2026)]] (skim)
- [[WeightBench - models cannot yet patch models (Marasini 2026)]] (skim)
- [[A model rewrites its own weights (Fan 2026)]] (deep): a 27B model edits its own weights after it reads its own hidden states. Graded answers decide which edits to keep. Only the largest model can do it.
- [[Claude's WSP edits act at the output (Kundu 2026)]] (skim): weight-space edits that act like sampling changes. Abstract only.
- [[Reading weights is mostly reading inputs (Goworek 2026)]] (skim): weight reading is mostly reading the input layer. Abstract only.
- [[SRWM - a weight matrix that rewrites itself (Irie 2022)]] (skim): a weight matrix that changes itself by a learned rule. Source-linked skimmed note exists; inclusion is an editorial decision, not a verification blocker.
- [[Nested Learning - a model that learns its own update rule (Behrouz 2025)]] (skim): a model as nested learners, each with its own update rule. Source-linked skimmed note exists; inclusion is an editorial decision.
- [[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]] (deep): a readout of the agent's own hidden state predicts its learning progress and picks which goals it trains on. The closest case of a hidden-state signal that controls learning; the signal is competence, not taste.

## 6. Limits

Purpose: what goes wrong when a model learns from its own signal. Sharpening then collapse, length collapse in code, judge hacking, and test-anchored safeguards and their scope limits, alongside self-rewarding quality gains without a hard verifier.

- [[Self-reward sharpens then collapses (He 2026)]] (deep)
- [[Self-reward on code collapses to short code (Jin 2026)]] (deep)
- [[Self-reward only within the same test result (Wu 2026)]] (deep)
- [[Self-judge training makes wrong look right (Zhou 2026)]] (deep)
- [[Training on own outputs erases rare data (Shumailov 2024)]] (deep)
- [[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]] (skim)
- [[Self-judged nightly learning rises then decays (Kongsilp 2026)]] (deep): a self-judged nightly loop rises for a week, then decays below its start over a year.
- [[Training on own self-reports spreads misalignment (Tagade 2026)]] (skim): training on a model's self-reports passes on misalignment. Abstract and blog summary only.
- [[Self-refinement amplifies self-bias (Xu 2024)]] (deep): when a model critiques and rewrites its own output in a loop, its self-scores rise faster than true quality, so its self-bias grows each round. The text gets more fluent, not better.

## 7. Taste & open-endedness

Purpose: how taste has been measured (divergence, stability, interestingness) and whether a measured taste is the model's own or a taste every model shares.

- [[Models show research taste (Trehan 2026)]] (deep)
- [[OMNI - models judge which tasks are interesting (Zhang 2023)]] (deep)
- [[Open-ended means novel and learnable to an observer (Hughes 2024)]] (deep)
- [[Learn to find interesting maths (Patel 2026)]] (skim)
- [[Models share one taste for text (Zatuchin 2026)]] (skim)
- [[Self-revised values converge in coding agents (Liang 2026)]] (skim): agents that revise their own values end up with the same values. Against the divergent test. Abstract only.
- [[Model values drift with persona and long chats (Kovač 2024)]] (deep): when the model plays a persona, its stated values change with the topic of the chat and drift as the chat gets longer. Without a persona they are more stable. Against the Stable test.
- [[Task context moves model preferences (Trhlik 2026)]] (deep): task context shifts 37% of preference cells; paraphrase 10%, temperature 5%. The coarse order holds, the fine order moves. Against the Stable test as now defined.
- [[Models recognize and favor their own text (Panickssery 2024)]] (deep): judges recognize and favor their own text, and the bias grows with self-recognition. Baseline for the own-model premium.
- [[Judges favor familiar text, not their own (Wataoka 2024)]] (deep): self-preference follows low perplexity (familiar text), not authorship. Own taste may be familiarity.
- [[Easy-to-process things feel beautiful (Reber 2004)]] (skim): in people, easy-to-process things feel beautiful. Warning that a "good" signal may mean "typical".

## 8. Synthesis

Purpose: distinguish existing quality readouts, self-judged training, model-side learning control and direct self-editing from the proposed experiment. The maintained synthesis and closest-prior-art table live in [[08-synthesis]]; this outline does not duplicate their paragraphs.

**Bounded contribution.** We propose to test whether a causally validated activation-level evaluation readout can guide output selection and subsequent self-training for readability among programs matched on observed test outcomes, with held-out audits of quality and drift.

- Yuan 2024: own verbal quality scores already supply iterative DPO preferences.
- Kirin 2026: corrected v3 already reads human preference from hidden states, weakly; superseded large results are withdrawn.
- MAGELLAN: hidden-state competence and learning progress already choose what to learn.
- Fan: the model chooses its own direct edit; graded answers decide retention.
- Irie and Nested Learning: source-linked skimmed notes exist; learned update machinery is prior art, not missing verification.
- G5: longer-term architecture agenda, not a demonstrated contribution of the readability experiment.
- Q1 gates this candidate evaluator; Q2 precedes Q3. Tests constrain observed functional behavior rather than proving full correctness equivalence.
- Section 8.1 specifies the proposed Q1 protocol: blind five-rater rankings, problem-held-out baselines, fixed-text matched-strength causal checks and separate support/negative/inconclusive outcomes. Experiments remain parked; design cutoffs still need review.

## 9. Conclusion

Purpose: restate the gap, the claim we can defend after section 8's counter-evidence, and the first experiments (exp01 for Q1, then Q2's best-of-n arm).

- No paper notes assigned. Draw on [[Q1 Does the model sense code quality]], [[Q2 Can the model steer its own code]], [[Q3 Can self-learning avoid collapse]].
