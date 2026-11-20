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

Drafted in full at [[08-synthesis]] (`07-drafts/litreview/08-synthesis.md`). Keep this outline section to purpose and status only.

Purpose: put the pieces together as one loop, show where the field stops, map our threads onto those gaps, and state the strongest evidence against us.

## 9. Conclusion

Purpose: restate the gap, the claim we can defend after section 8's counter-evidence, and the first experiments (exp01 for T1, then T2's best-of-n arm).

- No paper notes assigned. Draw on [[code-quality-signal-T1]], [[inference-time-steering-T2]], [[self-training-collapse-T3]].
