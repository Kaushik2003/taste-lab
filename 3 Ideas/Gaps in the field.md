---
type: landscape
title: "Field gap table: where the five clusters stop"
status: proposed
created: 2026-11-19
updated: 2026-11-19
tags: [type/landscape, landscape, gaps]
links: ["[[Field map - Models read their own state]]", "[[Field map - Models judge good and bad]]", "[[Field map - Changes that stay in the weights]]", "[[Field map - Limits of self-learning]]", "[[Field map - Taste and new ideas]]"]
---

# Field gap table

Built from the five landscape notes (2026-11-19, arXiv sweep of the last 180 days plus older anchors). Details and links live in each note.

| Cluster | Best result | Open problem | Who's leading |
|---|---|---|---|
| 1. Monitoring & introspection ([[Field map - Models read their own state]]) | An external probe on R1-Distill-Llama-8B hidden states stops reasoning early: same MATH accuracy (88.2%), about 24% fewer tokens ([[Models know when they are right (Zhang 2025)]]) | External probes are common, but model-side confidence and competence controls also exist. With input cues controlled, in-context self-report matches input-only probes and self-control mostly disappears ([[Introspection claims fail basic checks (Singh 2026)]], 2609.00904) | Anthropic interpretability (Lindsey); NYU (Linzen, Ravfogel; He He); Ji-An, Mattar, Benna; Bau group |
| 2. Evaluation signals ([[Field map - Models judge good and bad]]) | A "value" axis in Qwen3-8B separates correct from corrupted code (d up to 1.05), changes backtracking when steered, and DPO raises it ([[Value axis - model knows it is on track (Jiang 2026)]]) | Preference readouts and non-correctness signals exist. The proposed question is causal use of a valence readout for readability selection and learning among test-matched programs | Anthropic + Fellows (Lindsey, Kauvar, Jiang); NYU (Chalmers, Izmailov); CAIS (Hendrycks, Mazeika); Berg & Kaiser |
| 3. Persistent control ([[Field map - Changes that stay in the weights]]) | A steering vector becomes rank-one weight edits with forward passes only, stronger than steering, MMLU flat ([[TFTV - turn a steering vector into a weight edit (Perin 2026)]]); also Steer2Edit (2602.09870), Arditi weight orthogonalization ([[One direction controls refusal (Arditi 2024)]]) | Fan can choose its own direct edit; graded answers govern retention. Yuan uses its own verbal quality judgments for training. The proposed gap is narrower. Unknown: how much of a steering gain an edit keeps at matched strength, and whether repeated edits stay stable | MIT CSAIL (Khattab, Agrawal: SEAL, WSP); Google (Behrouz, Mirrokni); USP + Google (Perin, Hirata); UCSD Weng lab; Arditi, Nanda |
| 4. Self-improvement & limits ([[Field map - Limits of self-learning]]) | SIF beats INTUITOR by 4.71 points on 12 math benchmarks (1.5B); in code, behavioral self-rewarding lifts SWE-bench Verified 32.1% → 34.7% over a 30.9% random-reward control ([[Self-reward only within the same test result (Wu 2026)]]) | Yuan reports three iterations of self-rewarded quality gains; long-horizon stability of the proposed activation-level loop remains unestablished. Self-judges get hacked ([[Self-judge training makes wrong look right (Zhou 2026)]]) and the one fix needs a checkable answer, which style doesn't have | Berkeley + Purdue (Song, Zhao); Tsinghua + UIUC (Ding, Liu); Shumailov, Gal; Meta FAIR (Weston); Stanford (Koyejo) |
| 5. Taste & open-endedness ([[Field map - Taste and new ideas]]) | 15 to 36% "stable divergence" from author choices in research taste ([[Models show research taste (Trehan 2026)]]); a frozen taste score drives a 6-round self-expanding math loop ([[Learn to find interesting maths (Patel 2026)]]) | Divergence is not ownership: measured "model taste" is human consensus or shared across models ([[Models share one taste for text (Zatuchin 2026)]]). Readability may be a convergent axis where differing from experts just means being wrong | Lossfunk (Chopra); Meta FAIR + NYU (Kempe, Munos); Clune, Stanley, Lehman (OMNI); DeepMind open-endedness; UW NLP (Hivemind) |

## Prior art that already covers part of our loop
- **Q5 mechanism is taken.** Steering → rank-one weight edit exists (TFTV 2609.09054, Steer2Edit 2602.09870, ITI bias, Arditi orthogonalization). Q5 was set to `killed` on 2026-11-19 in another session, at the user's request.
- **Q1/T2 neighbours.** Value Axis (internal signal tracks code correctness), Metacognitive Steering 2609.16245 (reads internal state, steers during decoding, but directions come from human scientists and evidence is qualitative), Readability RepE 2606.06214 (steers for readability, but never runs or rates the code).
- **Q3 neighbours.** Behavioral self-rewarding (own judgment as reward with tests fixed, verbal judge, style excluded), SIF and SpeCal (own logits or hidden-state geometry gate updates).

## Bounded contribution proposal

We propose to test whether a causally validated activation-level evaluation readout can guide output selection and subsequent self-training for readability among programs matched on observed test outcomes, with held-out audits of quality and drift.

Quality-related hidden-state readouts (Kirin v3), own verbal quality rewards (Yuan), learning-progress curricula (MAGELLAN), and self-chosen direct edits (Fan) are existing prior art. The proposed contribution is their narrower experimental distinction, not a claim that the field is empty. See [[08-synthesis]] for the maintained closest-prior-art table. Passing tests constrains observed behavior but is not a proof of complete correctness equivalence or preference ownership.

## Log
- 2026-11-19: created by Claude from the landscape sweep. Status proposed.
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
