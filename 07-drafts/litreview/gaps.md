# Gaps & patterns (2026-11-21)

Output of a `/gaps` pass over the vault: 27 paper notes, 11 concept notes, 5 threads, the coverage matrix and the section drafts. Ordered by how much each gap blocks the paper.

## Gaps that block the claim

- **G1 · No monitor reads a quality beyond correctness.** Every working readout ([[2025-zhang-reasoning-models-know-when-right]], [[2026-xu-sparse-reward-subsystem]], [[2026-jiang-value-axis]]) is trained or validated on correctness labels. The only style-adjacent signal ([[2026-gao-readability-repe]]) is measured through the model's own answer probabilities, never executed or human-rated code. This is the gap exp01 attacks; it is also the one a reviewer hits first.
- **G2 · Ownership of taste is unmeasured in every internal-signal paper.** Behavioral work shows measured taste is largely shared across models ([[2026-zatuchin-shared-taste-model-text]], [[2026-trehan-eliciting-research-taste]]). No probe or steering paper asks whether the signal is the model's own or the shared machine prior. The gamma statistic exists and has never been run on activations.
- **G3 · The steering-to-edit recovery ratio is unreported anywhere.** Four papers write directions into weights ([[2024-arditi-refusal-direction]], [[2025-sun-thinkedit]], [[2026-sun-steer2edit]], [[2026-perin-training-free-task-vectors]]); none measures how much of the inference-time steering gain survives at matched strength. Cheap to compute, needed before any persist claim.
- **G5 · No architecture is built so metacognition can develop.** The pieces exist as separate papers: persistent self-state ([[2025-aviss-state-stream-transformer]], state stream, metacognitive-like behaviors with frozen weights), self included in a world model ([[2024-valiente-muse]], competence prediction gating strategy choice), and the agenda ([[2025-liu-intrinsic-metacognitive-learning]], intrinsic over extrinsic metacognition). Nobody has combined persistent self-state + learned selection of what to keep + world-model simulation of self. That combination is the paper's contribution claim.
- **G4 · No self-scored loop has run long enough to fail.** The working loops use frozen external signals ([[2026-patel-interesting-mathematics]], 6 rounds) or bounded self-judgment ([[2026-wu-behavioral-self-rewarding]], a few hundred steps). The collapsing loops use unbounded self-signals ([[2026-he-unsupervised-rlvr-limits]], [[2026-jin-intrinsic-rewards-code]]). The middle cell - a live internal signal, hard external check, many rounds - is empty.

## Confounds the drafts must keep visible

- **Grounded test, layer-0 confound.** Readability is visible in the text, so an input-only probe may match any valence readout ([[2026-singh-llm-introspection-reality-check]]). The claim must be "probed internal signal the behavior depends on", tested causally, not "the model monitors its taste".
- **Terseness confound.** High value goes with shorter, comment-free code ([[2026-jiang-value-axis]]); the readability direction adds comments ([[2026-gao-readability-repe]]); self-reward collapses length ([[2026-jin-intrinsic-rewards-code]]). Length and comment density are load-bearing controls, not niceties.
- **Judge-hacking channel.** A valence readout on a shown candidate is candidate-conditioned, the exact channel that gets hacked ([[2026-zhou-self-play-judge-hacking]]). Best-of-n by valence needs gap@k against a hidden anchor from day one.

## Patterns worth exploiting

- **Negative valence is the working control signal.** Models remove imposed negative states and rarely seek positive ones ([[2026-berg-hidden-valence]]); low value triggers backtracking ([[2026-jiang-value-axis]]). Design the controller around "something is wrong" before "this is good".
- **Preference training wires evaluation to choice without moving the representation** (DPO in [[2026-berg-hidden-valence]] and [[2026-jiang-value-axis]]). Self-training may change how taste is used, not what it values - plan the drift metric (gamma over rounds) accordingly.
- **Sparse is enough.** Value and regime signals live in <1% of coordinates or ten neurons ([[2026-xu-sparse-reward-subsystem]], [[2026-karpf-metacognitive-steering]]). A valence readout can be cheap.
- **WSP is a crowd, not a moat.** Two framework papers in one month plus 8+ follow-ups. Position as taste + self-direction; cite [[2026-takehi-weight-space-programming]] and [[2026-li-weightcode]] as mechanism, never as novelty.

## Coverage holes (from the matrix)

- Stable test: one paper, behavioral only, 80 pairs, one model family deep. Needs an internal-signal replication and more samples per order.
- Section 2 foundations now have notes ([[1990-nelson-metamemory]], [[2002-doya-metalearning-neuromodulation]], [[2017-fleming-self-evaluation]]); details flagged [unverified] need PDF verification.
- Reading queue "Next" holds ~10 papers not yet ingested (introspective oversight, GUARD, WeightBench, persona vectors, INTUITOR). Several likely move threat counts in the matrix.
- The two 2026 surveys are ingested: [[2026-liu-metacognition-survey]] (citation backbone for sections 1-2; its GitHub paper list doubles as a loop backfill source) and [[2026-rupprecht-world-models-survey]] (20-author CAT survey concluding motivation + metacognition are the under-researched world-model functions - independent corroboration of G5).
