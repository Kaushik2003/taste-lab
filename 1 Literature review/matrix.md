# Coverage matrix

One row per paper. Test columns: ✓ = the paper tests or directly informs that test, ? = partial or indirect, – = no. Component uses the loop names (monitor, evaluate, control, persist, anchor). The last column says which thread the paper is prior art for or a threat to, from each note's `role/` tags and its "Relevance to taste-lab" section.

| Paper | Section | Tier | Divergent | Stable | Grounded | Self-reinforcing | Component | Prior art or threat to |
|---|---|---|---|---|---|---|---|---|
| [[Complexity feedback changes agent code style (Chapados 2026)]] | 1 | skim | – | – | – | – | control, anchor | prior art Q2 (style moves while tests hold correctness) |
| [[Monitoring and control between two levels (Nelson 1990)]] | 2 | deep | – | – | ? | – | monitor, control | prior art for the whole loop (frame) |
| [[Models mostly know what they know (Kadavath 2022)]] | 2 | deep | – | – | ? | – | monitor | prior art Q1, Q6 |
| [[Models predict themselves better than others do (Binder 2024)]] | 2 | deep | – | – | ✓ | – | monitor | prior art Q6 (cross-model control) |
| [[Confidence is a guess about your own decision (Fleming 2017)]] | 2 | deep | – | – | ? | – | monitor, evaluate | prior art for the whole loop (second-order frame) |
| [[Trained confidence tracks consistency, not accuracy (Yax 2026)]] | 2 | deep | – | – | ✓ | – | monitor | threat Q1, Q6 (consistency confound) |
| [[Survey of metacognition in language models (Liu 2026)]] | 2 | deep | – | – | ? | – | monitor, control | prior art for the review (shows taste and persist are missing) |
| [[Neuromodulators set how the brain learns (Doya 2002)]] | 2 | skim | – | – | – | – | control | prior art Q2, Q3 (controller knobs) |
| [[A test battery for self-monitoring (Cacioli 2026)]] | 2 | skim | – | ? | – | – | monitor, control | prior art for the review (human test battery for self-monitoring) |
| [[What a system changes when it changes itself (Koch 2026)]] | 2 | skim | – | – | – | ? | control, persist | prior art for the review (frame for kinds of self-change) |
| [[Backpropamine - a network sets its own plasticity (Miconi 2019)]] | 2 | skim | – | – | – | – | control, persist | prior art Q2, Q3 (a network sets its own learning rate; a machine version of the Doya knobs) |
| [[Self-improving agents need intrinsic metacognition (Liu 2025)]] | 2 | deep | – | – | – | – | monitor, control, persist | prior art for the architecture gap (the agenda: intrinsic metacognition) |
| [[World models miss motivation and metacognition (Rupprecht 2026)]] | 2 | skim | – | – | – | – | monitor, control, persist | prior art for the review (world-model survey; corroborates the architecture gap) |
| [[A map of artificial metacognition (Shakarian 2026)]] | 2 | skim | – | – | – | – | monitor, control | prior art section 2 (classical metareasoning lineage) |
| [[Models name the skills a problem needs (Didolkar 2024)]] | 2 | deep | – | – | – | – | monitor | prior art for the review (declarative metacognitive knowledge: naming own skills) |
| [[Introspection needs a causal link to count (Comsa 2025)]] | 2 | deep | – | – | ✓ | – | monitor | prior art for the review (the causal-link criterion for introspection) |
| [[AI awareness as a measurable capacity (Li 2025)]] | 2 | skim | – | – | – | – | monitor, control | prior art for the review (awareness as measurable capacity is now mainstream) |
| [[Metacognitive prompting cuts theory-of-mind errors (Leer 2023)]] | 2 | skim | – | – | – | – | monitor | prior art for the review (prompted scaffolding, not capacity) |
| [[Models can report and control their own activations (Ji-An 2025)]] | 3 | deep | – | – | ✓ | – | monitor, control | prior art Q6 |
| [[Models sometimes notice injected thoughts (Lindsey 2025)]] | 3 | deep | – | – | ✓ | – | monitor | prior art Q6; threat Q6 (weak in open 8B models) |
| [[Training LMs to watch themselves (Wang 2026)]] | 3 | deep | – | – | ✓ | – | monitor | prior art Q6; threat Q3 (warns against training on own verdicts) |
| [[Models know when they are right (Zhang 2025)]] | 3 | deep | – | – | ? | – | monitor, control | prior art Q2 (baseline), Q1 |
| [[Models do not report injected pain (Ferrara 2026)]] | 3 | deep | – | – | ✓ | – | monitor, evaluate | threat Q1 (self-report route; supports probe route) |
| [[Introspection claims fail basic checks (Singh 2026)]] | 3 | deep | – | – | ✓ | – | monitor | threat Q1 (grounded claim) |
| [[Probes find injections long before models report them (Rubin 2026)]] | 3 | deep | – | – | ✓ | – | monitor | threat Q1 (probe accuracy is a low bar) |
| [[Trained self-prediction without an own-model edge (Zeng 2026)]] | 3 | deep | – | – | ✓ | – | monitor | threat Q6 (no own-model edge) |
| [[Outside controller steers thinking modes (Karpf 2026)]] | 3 | skim | – | – | – | – | monitor, control | prior art Q2 (name and design overlap) |
| [[Models know when they know but do not act (Cao 2026)]] | 3 | deep | – | – | ✓ | – | monitor, control | prior art Q6 (self-reports exist, but an outside classifier makes the control decision) |
| [[Models describe behaviors they were trained into (Betley 2025)]] | 3 | deep | – | – | ✓ | – | monitor, persist | prior art Q6 (self-report follows a fine-tuned behavior) |
| [[Models report preference weights trained into them (Plunkett 2025)]] | 3 | deep | – | – | ✓ | – | monitor, evaluate | prior art Q6 (first self-report of an evaluation, not a behavior; no cross-model control) |
| [[A persistent latent stream gives metacognitive behavior (Aviss 2025)]] | 3 | deep | – | – | – | – | monitor | prior art for the architecture gap (leg 1: persistent self-state) |
| [[MUSE - a world model that predicts its own failure (Valiente 2024)]] | 3 | deep | – | – | – | – | monitor, control | prior art for the architecture gap (leg 2: world model includes the agent) |
| [[Frontier models use their own confidence strategically (Ackerman 2025)]] | 3 | deep | – | – | ✓ | – | monitor | prior art Q6 (strategic deployment of own confidence; behavioral, no self-report) |
| [[Beliefs form in latent space and drive choices (Yalon 2026)]] | 3 | deep | – | – | ✓ | – | monitor, evaluate | prior art Q6 (belief dominance causes action; the full modulate-cause-report chain) |
| [[Intrinsic metacognition needs a good lens (Ma 2025)]] | 3 | deep | – | – | – | – | monitor | prior art Q6 (step-level intrinsic metacognition; the lens is the bottleneck) |
| [[Fine-tuned uncertainty reports transfer across domains (Steyvers 2025)]] | 3 | deep | – | – | ✓ | – | monitor | prior art Q6 (trained calibrated uncertainty generalizes across domains) |
| [[Models partly know what they do not know (Yin 2023)]] | 3 | skim | – | – | – | – | monitor | prior art for the review (knowledge boundary; SelfAware) |
| [[Small models deny sentience and their internals agree (Kaiser 2026)]] | 3 | deep | – | – | ✓ | – | monitor | prior art Q6 (report-vs-probe consistency across 3 families, 0.6-70B) |
| [[Emotion directions drive choices in Claude (Anthropic 2026)]] | 4 | deep | – | – | ✓ | – | evaluate | prior art Q1 |
| [[Hidden good-bad feeling changes choices (Berg 2026)]] | 4 | deep | – | – | ✓ | ? | evaluate, control | prior art Q1 (grounded design); threat Q3 (DPO does not move valence) |
| [[Steer code readability inside the model (Gao 2026)]] | 4 | deep | – | – | – | – | control | prior art Q2 (baseline arm), Q1 |
| [[Value axis - model knows it is on track (Jiang 2026)]] | 4 | deep | – | – | ✓ | ✓ | monitor, evaluate, control | prior art Q1, Q2 |
| [[Few neurons predict right answers (Xu 2026)]] | 4 | deep | – | – | ✓ | – | monitor, evaluate, control | prior art Q1, Q2; threat Q1 (correctness confound) |
| [[One evaluation circuit for all norms (Liga 2026)]] | 4 | skim | – | ? | ? | – | evaluate | prior art Q1 (one shared evaluation circuit; cue-word confound) |
| [[Model values form coherent utilities that can be steered (Mazeika 2025)]] | 4 | deep | – | ✓ | – | – | monitor | prior art section 4 (values as coherent utilities that can be read and steered) |
| [[SEAL - models write their own training data (Zweiger 2025)]] | 5 | deep | – | – | – | ✓ | persist | prior art Q3, Q4 |
| [[TFTV - turn a steering vector into a weight edit (Perin 2026)]] | 5 | deep | – | – | – | – | persist | prior art Q5 |
| [[WSP - a model reads and edits weights (Takehi 2026)]] | 5 | deep | – | – | – | – | persist | prior art Q4, Q5 |
| [[One direction controls refusal (Arditi 2024)]] | 5 | skim | – | – | ✓ | – | persist | prior art Q5 |
| [[A simple sort replaces the anti-loop edit (Fischetti 2026)]] | 5 | skim | – | – | – | – | persist | prior art Q5, Q4 |
| [[ThinkEdit - edit weights to think longer (Sun 2025)]] | 5 | skim | – | – | – | – | persist | prior art Q5 (killed it) |
| [[Steer2Edit - steering into small weight edits (Sun 2026)]] | 5 | deep | – | – | – | – | persist | prior art Q5 (killed it) |
| [[Exploring WSP - small weight edits, uneven results (Hu 2026)]] | 5 | skim | – | – | – | ? | persist | prior art Q4 |
| [[WeightBench - models cannot yet patch models (Marasini 2026)]] | 5 | skim | – | – | – | – | persist | threat Q4 (patching mostly fails; impossible edits not spotted) |
| [[A model rewrites its own weights (Fan 2026)]] | 5 | deep | – | – | ? | ? | monitor, persist, anchor | threat Q4 novelty (a model edits its own weights after reading its own states); outside graded answers still judge the edit |
| [[Claude's WSP edits act at the output (Kundu 2026)]] | 5 | skim | – | – | – | – | persist | threat Q4 (WSP edits act at the output) |
| [[Reading weights is mostly reading inputs (Goworek 2026)]] | 5 | skim | – | – | ? | – | monitor, persist | threat Q4 (weight reading is shallow) |
| [[SRWM - a weight matrix that rewrites itself (Irie 2022)]] | 5 | skim | – | – | – | ? | persist | prior art Q4 (self-modification by a learned rule, no judgment) |
| [[Nested Learning - a model that learns its own update rule (Behrouz 2025)]] | 5 | skim | – | – | – | ? | persist | prior art Q4 (learned update rule, no judgment) |
| [[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]] | 5 | deep | – | – | ? | ? | monitor, control | prior art Q3 (a hidden-state competence signal picks what to learn; not taste) |
| [[WeightCode - a model writes programs that edit weights (Li 2026)]] | 5 | skim | – | – | – | – | persist | prior art Q4 (weight programs install capabilities and rerun on new networks) |
| [[Persona vectors monitor and steer character traits (Chen 2025)]] | 5 | deep | – | – | – | – | monitor, control | threat Q4 (preventative persona steering); a method for a taste vector |
| [[A survey of self-evolving agents (Gao 2025)]] | 5 | skim | – | – | – | – | control, persist | prior art for the review (the what/when/how/where map of self-evolution) |
| [[Self-reward sharpens then collapses (He 2026)]] | 6 | deep | – | – | – | ✓ | anchor | threat Q3 |
| [[Self-reward on code collapses to short code (Jin 2026)]] | 6 | deep | – | – | – | ✓ | evaluate, anchor | threat Q3 |
| [[Self-reward only within the same test result (Wu 2026)]] | 6 | deep | – | – | – | ✓ | anchor, persist | prior art Q3 |
| [[Self-judge training makes wrong look right (Zhou 2026)]] | 6 | deep | – | – | ✓ | ✓ | evaluate, anchor | threat Q2, Q3 |
| [[Training on own outputs erases rare data (Shumailov 2024)]] | 6 | deep | – | – | – | ✓ | anchor | threat Q3 |
| [[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]] | 6 | skim | – | – | – | ✓ | anchor | prior art Q3 (non-regression gate) |
| [[Self-judged nightly learning rises then decays (Kongsilp 2026)]] | 6 | deep | – | – | – | ✓ | evaluate, persist, anchor | threat Q3 (self-judge rises, then decays over days) |
| [[Training on own self-reports spreads misalignment (Tagade 2026)]] | 6 | skim | – | – | ? | ✓ | monitor, persist | threat Q3 (self-reports carry traits into training) |
| [[Self-refinement amplifies self-bias (Xu 2024)]] | 6 | deep | ? | – | – | ✓ | evaluate, persist | threat Q3 (self-scores rise faster than quality over self-refinement rounds) |
| [[Persona steering has safety side effects (Tang 2026)]] | 6 | skim | – | – | – | – | control | threat Q4 (persona steering has safety side effects) |
| [[Models fake alignment when training threatens them (Greenblatt 2024)]] | 6 | deep | – | – | – | – | monitor | threat Q3 (models fake alignment when training threatens their preferences) |
| [[Rényi crossings track richness loss in self-training (Srivastava 2026)]] | 6 | deep | – | – | – | – | monitor, persist | threat Q3 (richness vs evenness; measurement hygiene for collapse claims) |
| [[MARS - metacognitive reflection in one cycle (Hou 2026)]] | 6 | skim | – | – | – | – | control | prior art Q2 (metacognitive reflection improves the agent without moving the evaluator) |
| [[RISE - recursive introspection improves own answers (Qu 2024)]] | 6 | skim | – | – | – | – | control, persist | prior art Q2 (trained recursive self-correction; the evaluator stays fixed) |
| [[INTUITOR - self-certainty is reward enough to learn reasoning (Zhao 2025)]] | 6 | deep | – | – | – | ✓ | control, persist | prior art Q3 (the intrinsic-reward baseline: self-certainty alone matches RLVR) |
| [[MoT - models improve by remembering their own good thinking (Li 2023)]] | 6 | skim | – | – | – | – | persist | prior art Q3 (confidence-filtered memory; weakest persist rung) |
| [[Models show research taste (Trehan 2026)]] | 7 | deep | ✓ | ✓ | – | – | evaluate | prior art Q1 (method for tests 1 and 2) |
| [[OMNI - models judge which tasks are interesting (Zhang 2023)]] | 7 | deep | ? | – | – | ? | control, anchor | prior art Q3 (taste picks what to learn; taste is human, not own) |
| [[Open-ended means novel and learnable to an observer (Hughes 2024)]] | 7 | deep | ? | – | – | ✓ | anchor | prior art Q3 (definition for test 4) |
| [[Learn to find interesting maths (Patel 2026)]] | 7 | skim | ? | – | – | ✓ | anchor, persist | prior art Q3 |
| [[Models share one taste for text (Zatuchin 2026)]] | 7 | skim | ✓ | – | – | – | anchor | threat Q3 (own vs shared taste) |
| [[Self-revised values converge in coding agents (Liang 2026)]] | 7 | skim | ✓ | – | – | ? | evaluate, anchor | threat Q3 (self-revised values converge, against the divergent test) |
| [[Model values drift with persona and long chats (Kovač 2024)]] | 7 | deep | – | ✓ | – | – | evaluate | threat to the Stable test (in a persona, values move with chat topic and length) |
| [[Task context moves model preferences (Trhlik 2026)]] | 7 | deep | – | ✓ | – | – | evaluate | threat to the Stable test (task context shifts 37% of preference cells) |
| [[Models recognize and favor their own text (Panickssery 2024)]] | 7 | deep | ✓ | – | ? | – | monitor, evaluate | prior art Q3 (baseline own-model premium) |
| [[Judges favor familiar text, not their own (Wataoka 2024)]] | 7 | deep | ✓ | – | – | – | evaluate | threat Q3 and the Divergent test (self-preference may be familiarity) |
| [[Easy-to-process things feel beautiful (Reber 2004)]] | 7 | skim | ? | – | – | – | evaluate | threat Q1 ("good" may mean easy to process) |
| [[IdeaTaste - models fall short of human research taste (Zhong 2026)]] | 7 | deep | ✓ | – | – | – | evaluate | prior art for the divergent test (26% citation, 18% idea match to human communities) |
| [[Scientific taste can be trained from community feedback (Tong 2026)]] | 7 | deep | – | ✓ | – | – | evaluate, persist | prior art section 7 (taste is trainable from citations; origin stays human) |

Totals (✓ only), 64 papers: Divergent 5, Stable 3, Grounded 18, Self-reinforcing 13.

## Reading the matrix

- **Update 2026-11-20.** 15 rows added (13 new notes, plus Ji-An and Lindsey, which were missing). Stable is still the least covered test (1 paper) and Divergent is next (2). All 5 new grounded rows test behavior or injected states, and 2 of them (Yax, Lindsey at small scale) weaken the positive claims. Q3 gains one more threat (Shumailov) and two pieces of prior art for anchors (GUARD, Hughes). Q4 now has a direct threat: audited weight patching mostly fails (WeightBench).
- **Update 2026-11-20 (scout, 11 rows).** Divergent goes from 2 to 3 papers, but the new one (Liang) goes against the test: values that agents revise themselves converge. Stable stays at 1. Q3 gains two more threats (Kongsilp, Tagade). Q4 changes most: Fan shows a model editing its own weights after reading its own hidden states, so the novelty claim moves from "self-edit" to "self-edit judged by the model's own taste". 8 of the 11 rows come from abstracts only.
- **Update 2026-11-20 (six-angle search, 12 rows).** Stable goes from 1 to 3 papers, and both new ones go against the test: preferences move with task context, and with chat topic and length when the model plays a persona (Trhlik, Kovač). Divergent goes from 3 to 5: models favor their own text (Panickssery), but that may be familiarity, not taste (Wataoka). Q3 gains a direct threat: over rounds of self-refinement, self-scores rise faster than true quality (Xu). Grounded gains the first self-report of an evaluation, not a behavior (Plunkett). The controller gap narrows: a hidden-state competence signal picks what an agent learns (MAGELLAN).

- **Stable is the least covered test.** Only [[Models show research taste (Trehan 2026)]] measures it, with one model, 80 pairs and one sample per order. Divergent is close behind (2 papers, both behavioral). Neither has any internal-signal paper, so tests 1 and 2 rest on our own experiments.
- **Q3 has the most threats (5):** He, Jin, Zhou, Berg and Zatuchin. Its only prior art for a working loop (Wu, Patel, SEAL) uses an external or frozen signal, never the model's own activations.
- **Q5 has the most prior art (6 papers), which is why it was killed.** All six put a direction into weights; none take the direction from the model's own evaluation. That missing piece now sits in Q3, not Q5.
- **Grounded is well covered, but mostly by negative or method papers.** Singh, Ferrara and Arditi all show self-report does not follow the internal state. The positive grounded results (Anthropic, Berg, Jiang, Xu) are causal steering of choice, not self-report, which is the version of test 3 we should claim.
- **Q1 is the most cited thread (prior art in 7 rows, threat in 3).** It is the gating experiment, and no paper tests an internal signal on passing-but-different code.
