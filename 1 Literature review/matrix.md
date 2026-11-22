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
| [[Reasoning models show habits of mind (Dong 2025)]] | 2 | skim | ✓ | – | – | – | monitor | prior art for the review (habit profiles as family signatures) |
| [[Wise machines need metacognition not just smarts (Johnson 2025)]] | 2 | skim | – | – | – | – | monitor, control | prior art for the review (TiCS position: metacognition is the bottleneck) |
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
| [[Models act on their own confidence (Kumaran 2026)]] | 3 | deep | – | – | ✓ | – | monitor, control | prior art Q6 (causal steering of confidence moves abstention) |
| [[Both sides of a debate think they will win (Prasad 2025)]] | 3 | skim | – | – | – | – | monitor | prior art for the review (confidence escalates under opposition) |
| [[Medical models cannot say what they do not know (Griot 2025)]] | 3 | skim | – | – | – | – | monitor | motivation for the review (clinical monitoring gap) |
| [[Models are overconfident about their own abilities (Barkan 2025)]] | 3 | skim | – | – | – | – | monitor, control | prior art for the review (monitoring fails, control rule fine) |
| [[Models track and can be steered in thinking length (Eisenstadt 2025)]] | 3 | skim | – | – | ✓ | – | monitor, control | prior art Q6 (decode-then-steer progress signal) |
| [[A metacognitive coach lets a fast model beat a reasoner (Khandelwal 2025)]] | 3 | skim | – | – | – | – | monitor, control | prior art for the review (external monitor substitutes for capability) |
| [[AI advice inflates confidence in the AI and in oneself (Colombatto 2025)]] | 3 | skim | – | – | – | – | monitor | prior art for the review (advice exposure causally inflates confidence) |
| [[A less accurate AI with better confidence wins decisions (Li 2025)]] | 3 | deep | – | – | – | – | monitor | prior art Q6 (sensitivity priced as a first-class objective) |
| [[People over-trust what models know (Steyvers 2025)]] | 3 | deep | – | – | – | – | monitor | prior art for the review (the calibration gap, internal vs perceived) |
| [[LLM judgments of learning do not predict memory (Huff 2025)]] | 3 | skim | – | – | – | – | monitor | prior art for the review (standard JOL paradigm fails in LLMs) |
| [[Do models know how much they know (Prato 2024)]] | 3 | skim | – | – | – | – | monitor | prior art for the review (knowledge-scope awareness benchmark) |
| [[Bias-free measurement of metacognition (Fleming 2014)]] | 3 | deep | – | – | – | – | monitor | foundations (bias / sensitivity / efficiency trichotomy) |
| [[Meta-d-prime - sensitivity relative to task performance (Maniscalco 2012)]] | 3 | deep | – | – | – | – | monitor | foundations (sensitivity is identifiable only relative to task performance) |
| [[Emotion directions drive choices in Claude (Anthropic 2026)]] | 4 | deep | – | – | ✓ | – | evaluate | prior art Q1 |
| [[Hidden good-bad feeling changes choices (Berg 2026)]] | 4 | deep | – | – | ✓ | ? | evaluate, control | prior art Q1 (grounded design); threat Q3 (DPO does not move valence) |
| [[Steer code readability inside the model (Gao 2026)]] | 4 | deep | – | – | – | – | control | prior art Q2 (baseline arm), Q1 |
| [[Value axis - model knows it is on track (Jiang 2026)]] | 4 | deep | – | – | ✓ | ✓ | monitor, evaluate, control | prior art Q1, Q2 |
| [[Few neurons predict right answers (Xu 2026)]] | 4 | deep | – | – | ✓ | – | monitor, evaluate, control | prior art Q1, Q2; threat Q1 (correctness confound) |
| [[One evaluation circuit for all norms (Liga 2026)]] | 4 | skim | – | ? | ? | – | evaluate | prior art Q1 (one shared evaluation circuit; cue-word confound) |
| [[Model values form coherent utilities that can be steered (Mazeika 2025)]] | 4 | deep | – | ✓ | – | – | monitor | prior art section 4 (values as coherent utilities that can be read and steered) |
| [[Hidden-state geometry flags redundant reasoning (Li 2025)]] | 4 | deep | – | – | ✓ | – | monitor | prior art Q1 (label-free internal signal for self-evaluation) |
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
| [[Agents left alone study themselves (Szeider 2025)]] | 5 | skim | ✓ | ✓ | – | – | consolidation | prior art G5 (persistent self-state yields unprompted self-inquiry) |
| [[Reusable behaviors distilled from own traces (Didolkar 2025)]] | 5 | deep | – | ✓ | – | – | consolidation | prior art Q3 (own traces -> behavior handbook -> SFT) |
| [[An explicit meta-level makes reasoning controllable (Dong 2025)]] | 5 | skim | – | – | – | – | monitor, control | prior art G5 (engineered object/meta split) |
| [[Decoupled reasoning and control beats entangled thinking (Ha 2025)]] | 5 | skim | – | – | – | – | control | prior art G5 (control trained separately via CSPO) |
| [[Two agents learn to think about thinking (Wan 2025)]] | 5 | deep | – | – | – | – | control | prior art G5 (MARL meta-agent learns oversight) |
| [[Metacognitive knowledge guards against forgetting (Zhang 2026)]] | 5 | skim | – | – | – | – | consolidation | prior art for the review (forgetting guard for the persist leg) |
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
| [[Metacognitive myopia as a frame for model bias (Scholten 2024)]] | 6 | skim | – | – | – | – | monitor, control | prior art for the review (bias as missing metacognition) |
| [[Train reasoning and calibration together or lose both (Yeom 2026)]] | 6 | skim | – | – | – | – | monitor | prior art for the review (self-training eats calibration; joint objective fixes) |
| [[Honest non-signals bypass epistemic vigilance (Maynard 2026)]] | 6 | skim | – | – | – | – | anchor | prior art for the review (fluency as a counterfeit trust signal) |
| [[AI use flattens Dunning-Kruger and breaks self-assessment (Fernandes 2025)]] | 6 | skim | – | – | – | – | monitor | prior art for the review (human monitor degrades with AI use) |
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
| [[Self-rewarding language models judge and train themselves (Yuan 2024)]] | 5 | deep | – | – | – | ? | evaluate, persist | prior art for self-judged quality training; verbal rubric, not activation-level taste |
| [[Human preference is weakly readable from hidden states (Kirin 2026)]] | 4 | deep | – | – | ? | – | monitor, evaluate | prior art for quality-related activation readouts; corrected v3 only, not causal self-use |

Totals (✓ only), 120 papers: Divergent 8, Stable 7, Grounded 26, Self-reinforcing 14.

## Reading the matrix

Reconciled 22 November 2026. There were 118 paper rows before this pass and 120 after adding Yuan and corrected Kirin. Counts above are computed from the current rows, not inherited from an earlier search batch. A checkmark means the paper tests or informs a criterion, not that the full criterion has been satisfied; partial entries are excluded from checkmark totals.

- Stability is thinly covered, but not by only one paper. Several rows concern persona/context changes or reusable behaviors rather than readability stability itself.
- MAGELLAN is an explicit precedent for hidden-state-informed learning control. Its competence/progress signal must not be erased by a claim that internal monitoring never guides learning.
- Fan chooses a direct edit from its own hidden states; graded answers evaluate retention. Edit proposal is not edit evaluation.
- Yuan is prior art for own verbal quality judgments driving training. Kirin v3 is prior art for preference readout, with correction and non-causal limits.
- Irie and Nested Learning have source-linked skimmed notes with selected full-text checks. Runtime learned updates are distinct from self-evaluated persistent quality changes.
- The bounded contribution and closest-prior-art comparison are maintained in [[08-synthesis]]. Paper counts do not establish novelty, and no combination of checkmarks proves self-originated taste.
