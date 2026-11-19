---
type: landscape
title: "Field gap table: where the five clusters stop"
status: proposed
created: 2026-11-19
updated: 2026-11-19
tags: [type/landscape, landscape, gaps]
links: ["[[landscape-metacognitive-monitoring]]", "[[landscape-evaluation-signals]]", "[[landscape-persistent-control]]", "[[landscape-self-improvement-limits]]", "[[landscape-taste-open-endedness]]"]
---

# Field gap table

Built from the five landscape notes (2026-11-19, arXiv sweep of the last 180 days plus older anchors). Details and links live in each note.

| Cluster | Best result | Open problem | Who's leading |
|---|---|---|---|
| 1. Monitoring & introspection ([[landscape-metacognitive-monitoring]]) | An external probe on R1-Distill-Llama-8B hidden states stops reasoning early: same MATH accuracy (88.2%), about 24% fewer tokens ([[2025-zhang-reasoning-models-know-when-right]]) | Every working loop puts the reader outside the model. With input cues controlled, in-context self-report matches input-only probes and self-control mostly disappears ([[2026-singh-llm-introspection-reality-check]], 2609.00904) | Anthropic interpretability (Lindsey); NYU (Linzen, Ravfogel; He He); Ji-An, Mattar, Benna; Bau group |
| 2. Evaluation signals ([[landscape-evaluation-signals]]) | A "value" axis in Qwen3-8B separates correct from corrupted code (d up to 1.05), changes backtracking when steered, and DPO raises it ([[2026-jiang-value-axis]]) | Nobody closes the loop: a human reads the signal and injects it at a fixed strength. Untested whether it tracks quality beyond correctness, e.g. readability among passing solutions | Anthropic + Fellows (Lindsey, Kauvar, Jiang); NYU (Chalmers, Izmailov); CAIS (Hendrycks, Mazeika); Berg & Kaiser |
| 3. Persistent control ([[landscape-persistent-control]]) | A steering vector becomes rank-one weight edits with forward passes only, stronger than steering, MMLU flat ([[2026-perin-training-free-task-vectors]]); also Steer2Edit (2602.09870), Arditi weight orthogonalization ([[2024-arditi-refusal-direction]]) | Someone else always picks the direction (experimenter + judge, or a frontier agent). Unknown: how much of a steering gain an edit keeps at matched strength, and whether repeated edits stay stable | MIT CSAIL (Khattab, Agrawal: SEAL, WSP); Google (Behrouz, Mirrokni); USP + Google (Perin, Hirata); UCSD Weng lab; Arditi, Nanda |
| 4. Self-improvement & limits ([[landscape-self-improvement-limits]]) | SIF beats INTUITOR by 4.71 points on 12 math benchmarks (1.5B); in code, behavioral self-rewarding lifts SWE-bench Verified 32.1% → 34.7% over a 30.9% random-reward control ([[2026-wu-behavioral-self-rewarding]]) | No self-signal keeps improving a quality the external check does not measure, over many rounds. Self-judges get hacked ([[2026-zhou-self-play-judge-hacking]]) and the one fix needs a checkable answer, which style doesn't have | Berkeley + Purdue (Song, Zhao); Tsinghua + UIUC (Ding, Liu); Shumailov, Gal; Meta FAIR (Weston); Stanford (Koyejo) |
| 5. Taste & open-endedness ([[landscape-taste-open-endedness]]) | 15 to 36% "stable divergence" from author choices in research taste ([[2026-trehan-eliciting-research-taste]]); a frozen taste score drives a 6-round self-expanding math loop ([[2026-patel-interesting-mathematics]]) | Divergence is not ownership: measured "model taste" is human consensus or shared across models ([[2026-zatuchin-shared-taste-model-text]]). Readability may be a convergent axis where differing from experts just means being wrong | Lossfunk (Chopra); Meta FAIR + NYU (Kempe, Munos); Clune, Stanley, Lehman (OMNI); DeepMind open-endedness; UW NLP (Hivemind) |

## Prior art that already covers part of our loop
- **T5 mechanism is taken.** Steering → rank-one weight edit exists (TFTV 2609.09054, Steer2Edit 2602.09870, ITI bias, Arditi orthogonalization). T5 was set to `killed` on 2026-11-19 in another session, at the user's request.
- **T1/T2 neighbours.** Value Axis (internal signal tracks code correctness), Metacognitive Steering 2609.16245 (reads internal state, steers during decoding, but directions come from human scientists and evidence is qualitative), Readability RepE 2606.06214 (steers for readability, but never runs or rates the code).
- **T3 neighbours.** Behavioral self-rewarding (own judgment as reward with tests fixed, verbal judge, style excluded), SIF and SpeCal (own logits or hidden-state geometry gate updates).

## Draft: "Nobody has yet shown…" (proposed, for Harshit to rewrite)
Nobody has yet shown a model that reads an evaluation signal from its own activations, uses that signal (not an experimenter's direction or an external judge) to choose what it generates and what it learns, and does this on a quality its external checks don't measure. Each piece exists on its own: internal value and valence axes track correctness, probes on hidden states can stop reasoning early, steering vectors can be written into weights with rank-one edits, and self-rewarding can improve code when tests anchor correctness. But the reader is always outside the model, the direction is always picked by someone else, and every self-reward that improves quality leans on a checkable answer. Code readability among solutions that all pass the tests is a clean place to close the loop, because correctness is fixed and only the model's own judgment can move style. The open question is whether that judgment is the model's own, or just the consensus every model shares.

## Log
- 2026-11-19: created by Claude from the landscape sweep. Status proposed.
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change.
