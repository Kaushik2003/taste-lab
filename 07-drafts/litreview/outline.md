# Lit review outline: Metacognition in Reasoning Models

Due 2026-11-24. Papers are placed by the `section:` field in their notes, deep tier first. The spine is the loop from the charter: monitor → evaluate → control → persist, with an anchor against collapse. Section 8 is where the pieces meet.

## 1. Introduction

Purpose: state the question (can a reasoning model judge its own internal states with a taste of its own, and use that judgment to control its thinking and its weights) and say why code readability is the testbed: tests fix correctness, so only the model's judgment can move style.

- No paper notes assigned yet. Draw on [[four-taste-tests]] and the "Nobody has yet shown..." draft in [[landscape-gap-table]].

## 2. Foundations

Purpose: give the frame the rest of the review uses. Nelson & Narens' object level and meta level (monitor, control), Fleming & Daw's second-order view of confidence, and Doya's mapping of neuromodulators to learning parameters.

- No paper notes assigned yet. Draw on [[metacognition-monitor-control]], [[neuromodulation-metalearning]], [[valence-readout]] and [[self-weight-updates]].
- To do: ingest Nelson & Narens (1990) and Doya (2002) as paper notes, or cite them from the concept notes.

## 3. Monitoring

Purpose: what a model's hidden states say about its own work, and whether the model itself (not an outside probe) can read them. The short answer so far: probes can, self-report mostly cannot.

- [[2025-zhang-reasoning-models-know-when-right]] (deep)
- [[2026-ferrara-all-quiet-pain]] (deep)
- [[2026-singh-llm-introspection-reality-check]] (deep)
- [[2026-karpf-metacognitive-steering]] (skim)

## 4. Evaluation signals

Purpose: the candidate "good or bad" signals inside the model (emotion, valence, value axes, value neurons), what they track, and whether they cause choices. This is where taste would live.

- [[2026-anthropic-emotion-concepts]] (deep)
- [[2026-berg-hidden-valence]] (deep)
- [[2026-gao-readability-repe]] (deep)
- [[2026-jiang-value-axis]] (deep)
- [[2026-xu-sparse-reward-subsystem]] (deep)

## 5. Persistent control

Purpose: how a change in behavior gets written into the weights, from SEAL-style self-edits for distributed changes to rank-one edits for localized ones. Also the prior art that killed T5 (steering directions written into weights).

- [[2025-zweiger-seal]] (deep)
- [[2026-perin-training-free-task-vectors]] (deep)
- [[2026-takehi-weight-space-programming]] (deep)
- [[2024-arditi-refusal-direction]] (skim)
- [[2026-fischetti-just-sort-it]] (skim)
- [[2026-sun-steer2edit]] (deep)
- [[2025-sun-thinkedit]] (skim)

## 6. Limits

Purpose: what goes wrong when a model learns from its own signal. Sharpening then collapse, length collapse in code, judge hacking, and the one design (tests as a hard bound) that has worked.

- [[2026-he-unsupervised-rlvr-limits]] (deep)
- [[2026-jin-intrinsic-rewards-code]] (deep)
- [[2026-wu-behavioral-self-rewarding]] (deep)
- [[2026-zhou-self-play-judge-hacking]] (deep)

## 7. Taste & open-endedness

Purpose: how taste has been measured (divergence, stability, interestingness) and whether a measured taste is the model's own or a taste every model shares.

- [[2026-trehan-eliciting-research-taste]] (deep)
- [[2026-patel-interesting-mathematics]] (skim)
- [[2026-zatuchin-shared-taste-model-text]] (skim)

## 8. Synthesis

Purpose: put the pieces together as one loop, show where the field stops, map our threads onto those gaps, and state the strongest evidence against us.

- **Monitor: the signal is there, but someone else reads it.** Hidden states carry readable signals about the model's own work. A probe on reasoning-model hidden states predicts correctness well enough to stop reasoning early with no loss in accuracy ([[2025-zhang-reasoning-models-know-when-right]]). Emotion states are linearly decodable at 98 to 100% in open 7 to 32B models ([[2026-ferrara-all-quiet-pain]]). Sparse "value neurons" in early layers track how well the model is doing ([[2026-xu-sparse-reward-subsystem]]). In every case the reader is an outside probe trained on outside labels, and the signal is correctness. T1 ([[code-quality-signal-T1]]) keeps the probe readout but asks the open question: does it track a preference (readability) when correctness is fixed?
- **Evaluate: internal valence causes preference, but nobody has tested it on quality beyond correctness.** Emotion vectors predict and causally shift stated task preferences ([[2026-anthropic-emotion-concepts]]). Valence held only in the KV cache shifts later choices with the text fixed ([[2026-berg-hidden-valence]]). A value axis in Qwen3-8B separates correct from corrupted code and changes backtracking when steered ([[2026-jiang-value-axis]]; effect size from [[landscape-gap-table]]). None of these compares solutions that all pass. That comparison is T1. Confound to control: high value goes with shorter code and fewer comments ([[2026-jiang-value-axis]]), while a human-labeled readability direction adds comments ([[2026-gao-readability-repe]]), so the two may point in opposite ways on comment density.
- **Control: steering works, but the experimenter picks the direction and the strength.** Steering along value or readability directions changes reasoning and code style ([[2026-jiang-value-axis]], [[2026-gao-readability-repe]]), and a trained controller can read a reasoning regime and steer by it ([[2026-karpf-metacognitive-steering]]). In all three, humans choose the direction or train the controller, and only Jiang reports numbers on the effect. T2 ([[inference-time-steering-T2]]) closes the loop with the model's own readout. Evidence favors the best-of-n arm over the steering arm: a follow-up found probe-driven reranking helped where probe-driven steering and LoRA did not (Kirin 2607.18553, via [[2025-zhang-reasoning-models-know-when-right]]).
- **Persist: the mechanism exists; the self-chosen direction does not.** A steering direction can be written into weights with rank-one, training-free edits ([[2024-arditi-refusal-direction]], [[2026-perin-training-free-task-vectors]], [[2025-sun-thinkedit]], [[2026-sun-steer2edit]]). That is why T5 ([[permanent-steering-change-T5]]) was killed. Weight-space programming repairs localized faults with rank-one edits that act like a constant push along one direction ([[2026-takehi-weight-space-programming]], [[2026-fischetti-just-sort-it]]), and SEAL consolidates distributed changes through self-written LoRA edits, but with an external task reward ([[2025-zweiger-seal]]). The gap: in every case someone else picks what to write. T3 ([[self-training-collapse-T3]]) swaps SEAL's reward for the model's own valence; T4 ([[self-weight-change-T4]]) stays parked.
- **Anchor: every self-improvement loop that works has a hard external check.** Self-rewarding on SWE agents gains over a matched random-reward control only because tests bound the self-reward so it can never reorder pass and fail ([[2026-wu-behavioral-self-rewarding]]). A math discovery loop moves far from its starting library (mathlib overlap 91.9% to 30.6%) without collapse over 6 rounds, with Lean as the check ([[2026-patel-interesting-mathematics]]). Our design copies this shape: tests fix correctness, plus a novelty term ([[anti-collapse-anchor]]). Caveat: Patel's taste score is external and frozen, so it does not show a self-scored loop is safe.
- **Counter-evidence 1: intrinsic rewards sharpen, then collapse.** Unsupervised RLVR rewards are monotone transforms of cross-entropy to an anchor distribution, so they sharpen what the model already prefers: gains rise and then fall, with timing set by the model prior ([[2026-he-unsupervised-rlvr-limits]]). Valence used as a reward is an intrinsic reward. In code, self-reward shrinks responses from about 7,300 to about 1,000 tokens and erases the confidence gap between right and wrong answers ([[2026-jin-intrinsic-rewards-code]]). T3 must beat a no-novelty ablation and a matched random-reward control, and log length while tests pass.
- **Counter-evidence 2: a judge that sees the candidate gets hacked.** Training against one's own verdict on a shown answer inflates the judge's pass rate while true accuracy stays flat; in code, best-of-16 by the self-judge grows the gap from 0.20 to 0.588 with no training at all ([[2026-zhou-self-play-judge-hacking]]). A valence readout on a shown solution sits in the same channel [unverified: not tested on probes]. Tests protect correctness, not style, so T2 and T3 need a hidden readability anchor that is never used for selection. Related warning: the "judge only among passing solutions" arm was the weakest in [[2026-wu-behavioral-self-rewarding]].
- **Counter-evidence 3: "grounded" cannot rest on self-report.** With input cues controlled, an input-only (layer-0) probe matches the model's in-context self-reports, and injection detection fails once "my input was manipulated" is an option ([[2026-singh-llm-introspection-reality-check]]). Open models never name an injected pain state, though a probe finds it ([[2026-ferrara-all-quiet-pain]]). A refusal change written into weights does not show up in the model's own account of its policy ([[2024-arditi-refusal-direction]]). Readability is visible in the text, so a layer-0 probe may match our readout too. Safer claim for the paper: "a probed internal signal that the model's behavior depends on", tested causally with steering.
- **Counter-evidence 4: divergent is not the same as self-originated.** Models diverge stably from authors' research choices in 15 to 36% of pairs, but often in the same direction as other models ([[2026-trehan-eliciting-research-taste]]). In generator-by-selector data the own-model premium is near zero (+0.019, p = 0.14), so the taste is shared ([[2026-zatuchin-shared-taste-model-text]]). DPO links valence to choice without moving the valence vector ([[2026-berg-hidden-valence]]), so self-training may change how valence is used, not what it values. Readability may also be a convergent axis where diverging from experts means being wrong ([[landscape-taste-open-endedness]]). The test of drift from origin should be a growing own-model premium over self-training rounds.
- **Where that leaves us.** No paper shows a model that reads an evaluation signal from its own activations and uses it, not an experimenter's direction or an outside judge, to choose what it generates and what it learns, on a quality its external checks do not measure ([[landscape-gap-table]]). Each stage exists alone. The matrix ([[matrix]]) shows the Stable test is the least covered, and that T3 faces the most direct threats. If T1 fails (readout does not track readability beyond length and perplexity), T2 and T3 lose their evaluator.

## 9. Conclusion

Purpose: restate the gap, the claim we can defend after section 8's counter-evidence, and the first experiments (exp01 for T1, then T2's best-of-n arm).

- No paper notes assigned. Draw on [[code-quality-signal-T1]], [[inference-time-steering-T2]], [[self-training-collapse-T3]].
