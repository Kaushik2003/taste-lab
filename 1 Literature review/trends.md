# Trend analysis (2026-11-21)

Qualitative trends from the paper notes, candidate feeds and coverage matrix. The cluster counts below are a historical 21 November snapshot, not current totals; [[matrix]] now has 120 paper rows after the 22 November reconciliation.

## Velocity by cluster

| Cluster | Notes in vault | Newest item | Movement |
|---|---|---|---|
| Monitoring & introspection | 4 | 2026-11 (Ferrara) | Steady; methods turning adversarial (controls, layer-0 baselines) |
| Evaluation signals | 5 | 2026-09 to 11 | Fast; Anthropic + fellows driving valence/value work |
| Persistent control | 8 | 2026-11-19 (WeightCode) | **Fastest.** Two WSP framework papers in one month, 8+ follow-ups in two weeks |
| Self-improvement limits | 4 | 2026-10 | Test-anchored safeguards are useful; not a universal requirement |
| Taste & open-endedness | 3 | 2026-11 (Trehan) | Emerging; measurement papers appearing monthly |

## Direction of travel

- **From "does the signal exist" to "can we trust the readout".** 2024-2025: correctness is decodable (Zhang). 2026: introspection claims are being dismantled with controls (Singh, Ferrara), and the positive results are all probe-based. Expect the next wave to be trained reportability (observer roles, LoRA reporters) - 2611.23365 is the first.
- **Steering-to-weights is commoditizing.** Arditi (2024) -> ThinkEdit (2025-03) -> Steer2Edit / TFTV (2026) -> WSP frameworks (2026-11). Each step needs less training and less compute. Within a year "write a direction into weights" will be a library call. Fan already picks its own direction. The proposed distinction concerns the evaluator, target quality and audited learning loop (see [[08-synthesis]]).
- **Self-improvement results are bifurcating.** Probability-derived self-rewards can collapse (He, Jin), while test-anchored self-judgment works in particular settings (Wu, Patel). Yuan also reports short-run own-quality-reward gains without a hard correctness verifier. These results motivate scoped safeguards, not a universal solved architecture.
- **Taste is becoming a measured quantity.** Divergence/stability operationalized (Trehan, Nov 2026), ownership statistics (Zatuchin, Oct 2026), aesthetic agreement across models (K-pop paper, Oct 2026). "Machine taste" as a phrase is spreading outside ML venues. The shared-vs-own question is the live one.
- **Architecture-level metacognition is the newest thread.** Persistent latent state with emergent self-monitoring (State Stream Transformer, 2501.18356), world models that model the agent itself (MUSE, 2411.13537), intrinsic metacognitive learning as a requirement for self-improvement (2506.05109). Now ingested: [[A persistent latent stream gives metacognitive behavior (Aviss 2025)]], [[MUSE - a world model that predicts its own failure (Valiente 2024)]], [[Self-improving agents need intrinsic metacognition (Liu 2025)]]. This is the direction the review's architecture gap points at, and where the loop widens next.

## What to watch (next 30 days)

- WSP follow-ups hitting language-model behaviors (so far vision/SCAN/BabyAI only).
- Whether the value-axis/valence line (Jiang, Berg, Anthropic) publishes a closed-loop version - that would be the scoop risk for Q2.
- Collapse metrics standardizing (Model Collapse Step, Rényi crossings) - adopt early, cite as method.
