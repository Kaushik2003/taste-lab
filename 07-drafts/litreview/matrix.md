# Coverage matrix

One row per paper. Test columns: ✓ = the paper tests or directly informs that test, ? = partial or indirect, – = no. Component uses the loop names (monitor, evaluate, control, persist, anchor). The last column says which thread the paper is prior art for or a threat to, from each note's `role/` tags and its "Relevance to taste-lab" section.

| Paper | Section | Tier | Divergent | Stable | Grounded | Self-reinforcing | Component | Prior art or threat to |
|---|---|---|---|---|---|---|---|---|
| [[2025-zhang-reasoning-models-know-when-right]] | 3 | deep | – | – | ? | – | monitor, control | prior art T2 (baseline), T1 |
| [[2026-ferrara-all-quiet-pain]] | 3 | deep | – | – | ✓ | – | monitor, evaluate | threat T1 (self-report route; supports probe route) |
| [[2026-singh-llm-introspection-reality-check]] | 3 | deep | – | – | ✓ | – | monitor | threat T1 (grounded claim) |
| [[2026-karpf-metacognitive-steering]] | 3 | skim | – | – | – | – | monitor, control | prior art T2 (name and design overlap) |
| [[2026-anthropic-emotion-concepts]] | 4 | deep | – | – | ✓ | – | evaluate | prior art T1 |
| [[2026-berg-hidden-valence]] | 4 | deep | – | – | ✓ | ? | evaluate, control | prior art T1 (grounded design); threat T3 (DPO does not move valence) |
| [[2026-gao-readability-repe]] | 4 | deep | – | – | – | – | control | prior art T2 (baseline arm), T1 |
| [[2026-jiang-value-axis]] | 4 | deep | – | – | ✓ | ✓ | monitor, evaluate, control | prior art T1, T2 |
| [[2026-xu-sparse-reward-subsystem]] | 4 | deep | – | – | ✓ | – | monitor, evaluate, control | prior art T1, T2; threat T1 (correctness confound) |
| [[2025-zweiger-seal]] | 5 | deep | – | – | – | ✓ | persist | prior art T3, T4 |
| [[2026-perin-training-free-task-vectors]] | 5 | deep | – | – | – | – | persist | prior art T5 |
| [[2026-takehi-weight-space-programming]] | 5 | deep | – | – | – | – | persist | prior art T4, T5 |
| [[2024-arditi-refusal-direction]] | 5 | skim | – | – | ✓ | – | persist | prior art T5 |
| [[2026-fischetti-just-sort-it]] | 5 | skim | – | – | – | – | persist | prior art T5, T4 |
| [[2025-sun-thinkedit]] | 5 | skim | – | – | – | – | persist | prior art T5 (killed it) |
| [[2026-sun-steer2edit]] | 5 | deep | – | – | – | – | persist | prior art T5 (killed it) |
| [[2026-he-unsupervised-rlvr-limits]] | 6 | deep | – | – | – | ✓ | anchor | threat T3 |
| [[2026-jin-intrinsic-rewards-code]] | 6 | deep | – | – | – | ✓ | evaluate, anchor | threat T3 |
| [[2026-wu-behavioral-self-rewarding]] | 6 | deep | – | – | – | ✓ | anchor, persist | prior art T3 |
| [[2026-zhou-self-play-judge-hacking]] | 6 | deep | – | – | ✓ | ✓ | evaluate, anchor | threat T2, T3 |
| [[2026-trehan-eliciting-research-taste]] | 7 | deep | ✓ | ✓ | – | – | evaluate | prior art T1 (method for tests 1 and 2) |
| [[2026-patel-interesting-mathematics]] | 7 | skim | ? | – | – | ✓ | anchor, persist | prior art T3 |
| [[2026-zatuchin-shared-taste-model-text]] | 7 | skim | ✓ | – | – | – | anchor | threat T3 (own vs shared taste) |

| [[2026-li-weightcode]] | 5 | deep | – | – | – | – | persist | prior art T4, T5 |
| [[1990-nelson-metamemory]] | 2 | deep | – | – | – | – | monitor, control | framework (monitor/control split) |
| [[2002-doya-metalearning-neuromodulation]] | 2 | deep | – | – | – | – | monitor, control | framework (neuromodulatory evaluation signals) |
| [[2017-fleming-self-evaluation]] | 2 | deep | – | – | ? | – | monitor | framework (second-order computation bar) |
| [[2025-aviss-state-stream-transformer]] | 3 | deep | – | – | ? | – | monitor | architecture gap (persistent self-state) |
| [[2024-valiente-muse]] | 3 | deep | – | – | ? | – | monitor, control | architecture gap (self in world model) |
| [[2025-liu-intrinsic-metacognitive-learning]] | 2 | deep | – | – | – | – | monitor, control, persist | agenda citation (intrinsic vs extrinsic) |
| [[2026-liu-metacognition-survey]] | 2 | skim | – | – | – | – | monitor, control | citation baseline sections 1-2 |
| [[2026-rupprecht-world-models-survey]] | 2 | skim | – | – | – | – | monitor, control, persist | corroborates G5 (world-model side) |
| [[2026-wang-introspective-oversight]] | 3 | deep | – | – | ✓ | – | monitor | threat T1 (trained self-report works); supports probe route |
| [[2026-lindsey-emergent-introspective-awareness]] | 3 | deep | – | – | ✓ | – | monitor | threat T1 (emergent self-report, unreliable); methods template |
| [[2025-jian-metacognitive-neurofeedback]] | 3 | deep | – | – | ✓ | – | monitor, control | ceiling on T1 (metacognitive space) |
| [[2026-zhang-guard]] | 6 | deep | – | – | – | ✓ | control, anchor | prior art T3 (harness-regime stability) |
| [[2026-marasini-weightbench]] | 5 | skim | – | – | – | – | persist | capability bound T4 |
| [[2026-hu-wsp-scope]] | 5 | skim | – | – | – | – | persist | prior art T4, T5; locality evidence |
| [[2025-chen-persona-vectors]] | 5 | deep | – | – | ? | ? | monitor, control, persist | threat T4 (preventative steering); method for taste vector |
| [[2026-tang-persona-steering-audit]] | 6 | skim | – | – | – | – | control | constraint on steering-based persist |
| [[2025-zhao-intuitor]] | 4 | deep | – | – | – | ✓ | evaluate, persist | threat T3 (the intrinsic-reward baseline) |
| [[2026-tong-scientific-taste]] | 7 | deep | ? | ? | – | ✓ | evaluate, persist | prior art (taste trainable from feedback) |
| [[2026-zhong-ideataste]] | 7 | deep | ? | ? | – | – | evaluate | threat (26%/18% of human taste level) |
| [[2025-gao-self-evolving-agents-survey]] | 6 | skim | – | – | – | – | control, persist | field map (what/when/how) |
| [[2025-mazeika-utility-engineering]] | 4 | deep | – | ? | – | – | evaluate | supports Stable (coherent value systems) |
| [[2023-zhang-omni]] | 7 | deep | – | – | – | ✓ | monitor, control | prior art (external taste as auto-curriculum) |
| [[2024-greenblatt-alignment-faking]] | 6 | deep | – | – | ? | – | monitor | threat (self-signals gameable) |
| [[2026-srivastava-renyi-crossings]] | 6 | deep | – | – | – | ✓ | monitor, anchor | threat T3 (measurement hygiene) |
| [[2024-shumailov-model-collapse]] | 6 | deep | – | – | – | ✓ | anchor | threat T3 (canonical collapse) |
| [[2022-irie-self-referential-weight-matrix]] | 5 | skim | – | – | – | – | persist | prior art T4 (partial: machinery without evaluator) |
| [[2025-behrouz-nested-learning]] | 5 | skim | – | – | – | – | persist | prior art T4 (partial: learned self-modification) |

Totals (✓ only): Divergent 2, Stable 1, Grounded 11, Self-reinforcing 10. (51 rows, 2026-11-21 re-pass.)

## Reading the matrix

- **Stable is the least covered test.** Only [[2026-trehan-eliciting-research-taste]] measures it, with one model, 80 pairs and one sample per order. Divergent is close behind (2 papers, both behavioral). Neither has any internal-signal paper, so tests 1 and 2 rest on our own experiments.
- **T3 has the most threats (8+):** He, Jin, Zhou, Berg, Zatuchin, plus INTUITOR (the baseline to beat), Shumailov (canonical collapse) and Srivastava (measurement hygiene). Its working prior art (Wu, Patel, SEAL, GUARD) uses an external or frozen signal, or edits only the harness - never the model's own activations.
- **T4's prior art hardened in the 2026-11-21 re-pass:** preventative persona steering ([[2025-chen-persona-vectors]]) controls what training writes into weights, externally; Irie and Hope supply learned self-modification machinery without an evaluator. T4's remaining novelty is exactly the self-directed, evaluation-triggered edit.
- **T5 has the most prior art (6 papers), which is why it was killed.** All six put a direction into weights; none take the direction from the model's own evaluation. That missing piece now sits in T3, not T5.
- **Grounded now has positive causal self-report evidence.** Lindsey (injection-and-report) and the trained observer (0.907 AUROC) pass or approach the privileged-access bar, while Singh, Ferrara and Arditi show untrained self-report does not follow the internal state. Ji-An's metacognitive space is the ceiling: reportable directions are few, interpretable and high-variance. The claim to make remains causal: "a probed internal signal the behavior depends on".
- **T1 is the most cited thread (prior art in 7 rows, threat in 3).** It is the gating experiment, and no paper tests an internal signal on passing-but-different code.
