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

Totals (✓ only): Divergent 2, Stable 1, Grounded 8, Self-reinforcing 7.

## Reading the matrix

- **Stable is the least covered test.** Only [[2026-trehan-eliciting-research-taste]] measures it, with one model, 80 pairs and one sample per order. Divergent is close behind (2 papers, both behavioral). Neither has any internal-signal paper, so tests 1 and 2 rest on our own experiments.
- **T3 has the most threats (5):** He, Jin, Zhou, Berg and Zatuchin. Its only prior art for a working loop (Wu, Patel, SEAL) uses an external or frozen signal, never the model's own activations.
- **T5 has the most prior art (6 papers), which is why it was killed.** All six put a direction into weights; none take the direction from the model's own evaluation. That missing piece now sits in T3, not T5.
- **Grounded is well covered, but mostly by negative or method papers.** Singh, Ferrara and Arditi all show self-report does not follow the internal state. The positive grounded results (Anthropic, Berg, Jiang, Xu) are causal steering of choice, not self-report, which is the version of test 3 we should claim.
- **T1 is the most cited thread (prior art in 7 rows, threat in 3).** It is the gating experiment, and no paper tests an internal signal on passing-but-different code.
