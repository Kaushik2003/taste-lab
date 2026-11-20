# Lit review outline: Metacognition in Reasoning Models

Due 2026-11-24. Papers are placed by the `section:` field in their notes, deep tier first. The spine is the loop from the charter: monitor → evaluate → control → persist, with an anchor against collapse. Section 8 is where the pieces meet.

## 1. Introduction

Purpose: state the question (can a reasoning model judge its own internal states with a taste of its own, and use that judgment to control its thinking and its weights) and say why code readability is the testbed: tests fix correctness, so only the model's judgment can move style.

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
- [[SRWM - a weight matrix that rewrites itself (Irie 2022)]] (skim): a weight matrix that changes itself by a learned rule. Waits for your "in or out" decision on older self-modifying networks.
- [[Nested Learning - a model that learns its own update rule (Behrouz 2025)]] (skim): a model as nested learners, each with its own update rule. Same "in or out" decision.
- [[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]] (deep): a readout of the agent's own hidden state predicts its learning progress and picks which goals it trains on. The closest case of a hidden-state signal that controls learning; the signal is competence, not taste.

## 6. Limits

Purpose: what goes wrong when a model learns from its own signal. Sharpening then collapse, length collapse in code, judge hacking, and the one design (tests as a hard bound) that has worked.

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

Purpose: put the pieces together as one loop, show where the field stops, map our threads onto those gaps, and state the strongest evidence against us.

- **Monitor: the signal is there, but someone else reads it.** Hidden states carry readable signals about the model's own work. A probe on reasoning-model hidden states predicts correctness well enough to stop reasoning early with no loss in accuracy ([[Models know when they are right (Zhang 2025)]]). Emotion states are linearly decodable at 98 to 100% in open 7 to 32B models ([[Models do not report injected pain (Ferrara 2026)]]). Sparse "value neurons" in early layers track how well the model is doing ([[Few neurons predict right answers (Xu 2026)]]). In every case the reader is an outside probe trained on outside labels, and the signal is correctness. Q1 ([[Q1 Does the model sense code quality]]) keeps the probe readout but asks the open question: does it track a preference (readability) when correctness is fixed?
- **Evaluate: internal valence causes preference, but nobody has tested it on quality beyond correctness.** Emotion vectors predict and causally shift stated task preferences ([[Emotion directions drive choices in Claude (Anthropic 2026)]]). Valence held only in the KV cache shifts later choices with the text fixed ([[Hidden good-bad feeling changes choices (Berg 2026)]]). A value axis in Qwen3-8B separates correct from corrupted code and changes backtracking when steered ([[Value axis - model knows it is on track (Jiang 2026)]]; effect size from [[Gaps in the field]]). None of these compares solutions that all pass. That comparison is Q1. Confound to control: high value goes with shorter code and fewer comments ([[Value axis - model knows it is on track (Jiang 2026)]]), while a human-labeled readability direction adds comments ([[Steer code readability inside the model (Gao 2026)]]), so the two may point in opposite ways on comment density.
- **Control: steering works, but the experimenter picks the direction and the strength.** Steering along value or readability directions changes reasoning and code style ([[Value axis - model knows it is on track (Jiang 2026)]], [[Steer code readability inside the model (Gao 2026)]]), and a trained controller can read a reasoning regime and steer by it ([[Outside controller steers thinking modes (Karpf 2026)]]). In all three, humans choose the direction or train the controller, and only Jiang reports numbers on the effect. Q2 ([[Q2 Can the model steer its own code]]) closes the loop with the model's own readout. Evidence favors the best-of-n arm over the steering arm: a follow-up found probe-driven reranking helped where probe-driven steering and LoRA did not (Kirin 2607.18553, via [[Models know when they are right (Zhang 2025)]]).
- **Persist: the mechanism exists, and a model can now choose its own edit; the self-made judgment does not exist.** A steering direction can be written into weights with rank-one, training-free edits ([[One direction controls refusal (Arditi 2024)]], [[TFTV - turn a steering vector into a weight edit (Perin 2026)]], [[ThinkEdit - edit weights to think longer (Sun 2025)]], [[Steer2Edit - steering into small weight edits (Sun 2026)]]). That is why Q5 ([[Q5 (stopped) Make steering permanent]]) was killed. Weight-space programming repairs localized faults with rank-one edits that act like a constant push along one direction ([[WSP - a model reads and edits weights (Takehi 2026)]], [[A simple sort replaces the anti-loop edit (Fischetti 2026)]]). A 27B model now does this to itself: it reads its own hidden states, picks a direction and writes a rank-one edit, with no outside editor ([[A model rewrites its own weights (Fan 2026)]]). SEAL consolidates distributed changes through self-written LoRA edits ([[SEAL - models write their own training data (Zweiger 2025)]]). The gap: in every case outside correctness decides what is a good edit (graded answers, a task reward, an experimenter). Q3 ([[Q3 Can self-learning avoid collapse]]) swaps that for the model's own valence; Q4 ([[Q4 Can the model edit its own weights]]) stays parked, and Fan is now its closest prior work.
- **Anchor: every self-improvement loop that works has a hard external check.** Self-rewarding on SWE agents gains over a matched random-reward control only because tests bound the self-reward so it can never reorder pass and fail ([[Self-reward only within the same test result (Wu 2026)]]). A math discovery loop moves far from its starting library (mathlib overlap 91.9% to 30.6%) without collapse over 6 rounds, with Lean as the check ([[Learn to find interesting maths (Patel 2026)]]). Our design copies this shape: tests fix correctness, plus a novelty term ([[Anchor against collapse]]). Caveat: Patel's taste score is external and frozen, so it does not show a self-scored loop is safe.
- **Counter-evidence 1: intrinsic rewards sharpen, then collapse.** Unsupervised RLVR rewards are monotone transforms of cross-entropy to an anchor distribution, so they sharpen what the model already prefers: gains rise and then fall, with timing set by the model prior ([[Self-reward sharpens then collapses (He 2026)]]). Valence used as a reward is an intrinsic reward. In code, self-reward shrinks responses from about 7,300 to about 1,000 tokens and erases the confidence gap between right and wrong answers ([[Self-reward on code collapses to short code (Jin 2026)]]). Q3 must beat a no-novelty ablation and a matched random-reward control, and log length while tests pass.
- **Counter-evidence 2: a judge that sees the candidate gets hacked.** Training against one's own verdict on a shown answer inflates the judge's pass rate while true accuracy stays flat; in code, best-of-16 by the self-judge grows the gap from 0.20 to 0.588 with no training at all ([[Self-judge training makes wrong look right (Zhou 2026)]]). A valence readout on a shown solution sits in the same channel [unverified: not tested on probes]. Tests protect correctness, not style, so Q2 and Q3 need a hidden readability anchor that is never used for selection. Related warning: the "judge only among passing solutions" arm was the weakest in [[Self-reward only within the same test result (Wu 2026)]].
- **Counter-evidence 3: "grounded" cannot rest on self-report.** With input cues controlled, an input-only (layer-0) probe matches the model's in-context self-reports, and injection detection fails once "my input was manipulated" is an option ([[Introspection claims fail basic checks (Singh 2026)]]). Open models never name an injected pain state, though a probe finds it ([[Models do not report injected pain (Ferrara 2026)]]). A refusal change written into weights does not show up in the model's own account of its policy ([[One direction controls refusal (Arditi 2024)]]). Readability is visible in the text, so a layer-0 probe may match our readout too. Safer claim for the paper: "a probed internal signal that the model's behavior depends on", tested causally with steering.
- **Counter-evidence 4: divergent is not the same as self-originated.** Models diverge stably from authors' research choices in 15 to 36% of pairs, but often in the same direction as other models ([[Models show research taste (Trehan 2026)]]). In generator-by-selector data the own-model premium is near zero (+0.019, p = 0.14), so the taste is shared ([[Models share one taste for text (Zatuchin 2026)]]). DPO links valence to choice without moving the valence vector ([[Hidden good-bad feeling changes choices (Berg 2026)]]), so self-training may change how valence is used, not what it values. Readability may also be a convergent axis where diverging from experts means being wrong ([[Field map - Taste and new ideas]]). The test of drift from origin should be a growing own-model premium over self-training rounds.
- **Update 2026-11-20 (13 new notes).** The 2026 survey of the field covers monitoring and control but never mentions taste or weight self-edits ([[Survey of metacognition in language models (Liu 2026)]]); those two steps are where the review adds something. Privileged self-knowledge now has a stronger case ([[Training LMs to watch themselves (Wang 2026)]], [[Models predict themselves better than others do (Binder 2024)]]), but only for behavior, not internal states. Trained self-monitoring can read answer consistency instead of accuracy ([[Trained confidence tracks consistency, not accuracy (Yax 2026)]]). On persistence, audited weight patching of language models mostly fails, and no agent can tell an impossible edit from a hard one ([[WeightBench - models cannot yet patch models (Marasini 2026)]]). Self-improvement that does not collapse again needs a hard outside check plus a non-regression gate ([[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]).
- **Update 2026-11-20 (scout, 11 new notes).** A model now edits its own weights after it reads its own hidden states ([[A model rewrites its own weights (Fan 2026)]]), so the review's novelty moves from "self-edit" to "self-edit judged by the model's own taste". Self-judged learning rises and then decays over long runs ([[Self-judged nightly learning rises then decays (Kongsilp 2026)]]), a second case of the collapse threat. Values that agents revise themselves converge ([[Self-revised values converge in coding agents (Liang 2026)]]), against the divergent test. One shared evaluation circuit for norm judgments ([[One evaluation circuit for all norms (Liga 2026)]]) supports a valence readout.
- **Update 2026-11-20 (six-angle search, 12 new notes).** The Stable test now has 3 papers, and 2 say preferences move with task context and persona ([[Task context moves model preferences (Trhlik 2026)]], [[Model values drift with persona and long chats (Kovač 2024)]]). An own-model premium exists ([[Models recognize and favor their own text (Panickssery 2024)]]), grows when a model refines its own output by its own score ([[Self-refinement amplifies self-bias (Xu 2024)]]), and may be familiarity ([[Judges favor familiar text, not their own (Wataoka 2024)]]). A self-report can follow a weight change after fine-tuning ([[Models report preference weights trained into them (Plunkett 2025)]]). A hidden-state signal can choose what an agent learns, but it reads competence, not taste ([[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]]).
- **Where that leaves us.** No paper shows a model that reads an evaluation signal from its own activations and uses it, not an experimenter's direction or an outside judge, to choose what it generates and what it learns, on a quality its external checks do not measure ([[Gaps in the field]]). Each stage exists alone. The matrix ([[matrix]]) shows the Stable test is the least covered, and that Q3 faces the most direct threats. If Q1 fails (readout does not track readability beyond length and perplexity), Q2 and Q3 lose their evaluator.

## 9. Conclusion

Purpose: restate the gap, the claim we can defend after section 8's counter-evidence, and the first experiments (exp01 for Q1, then Q2's best-of-n arm).

- No paper notes assigned. Draw on [[Q1 Does the model sense code quality]], [[Q2 Can the model steer its own code]], [[Q3 Can self-learning avoid collapse]].
