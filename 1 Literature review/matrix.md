# Coverage matrix

One row per paper. Test columns: ✓ = the paper tests or directly informs that test, ? = partial or indirect, – = no. Component uses the loop names (monitor, evaluate, control, persist, anchor). The last column says which thread the paper is prior art for or a threat to, from each note's `role/` tags and its "Relevance to taste-lab" section.

| Paper | Section | Tier | Divergent | Stable | Grounded | Self-reinforcing | Component | Prior art or threat to |
|---|---|---|---|---|---|---|---|---|
| [[Monitoring and control between two levels (Nelson 1990)]] | 2 | deep | – | – | ? | – | monitor, control | prior art for the whole loop (frame) |
| [[Models mostly know what they know (Kadavath 2022)]] | 2 | deep | – | – | ? | – | monitor | prior art Q1, Q6 |
| [[Models predict themselves better than others do (Binder 2024)]] | 2 | deep | – | – | ✓ | – | monitor | prior art Q6 (cross-model control) |
| [[Confidence is a guess about your own decision (Fleming 2017)]] | 2 | deep | – | – | ? | – | monitor, evaluate | prior art for the whole loop (second-order frame) |
| [[Trained confidence tracks consistency, not accuracy (Yax 2026)]] | 2 | deep | – | – | ✓ | – | monitor | threat Q1, Q6 (consistency confound) |
| [[Survey of metacognition in language models (Liu 2026)]] | 2 | deep | – | – | ? | – | monitor, control | prior art for the review (shows taste and persist are missing) |
| [[Neuromodulators set how the brain learns (Doya 2002)]] | 2 | skim | – | – | – | – | control | prior art Q2, Q3 (controller knobs) |
| [[Models can report and control their own activations (Ji-An 2025)]] | 3 | deep | – | – | ✓ | – | monitor, control | prior art Q6 |
| [[Models sometimes notice injected thoughts (Lindsey 2025)]] | 3 | deep | – | – | ✓ | – | monitor | prior art Q6; threat Q6 (weak in open 8B models) |
| [[Training LMs to watch themselves (Wang 2026)]] | 3 | deep | – | – | ✓ | – | monitor | prior art Q6; threat Q3 (warns against training on own verdicts) |
| [[Models know when they are right (Zhang 2025)]] | 3 | deep | – | – | ? | – | monitor, control | prior art Q2 (baseline), Q1 |
| [[Models do not report injected pain (Ferrara 2026)]] | 3 | deep | – | – | ✓ | – | monitor, evaluate | threat Q1 (self-report route; supports probe route) |
| [[Introspection claims fail basic checks (Singh 2026)]] | 3 | deep | – | – | ✓ | – | monitor | threat Q1 (grounded claim) |
| [[Probes find injections long before models report them (Rubin 2026)]] | 3 | deep | – | – | ✓ | – | monitor | threat Q1 (probe accuracy is a low bar) |
| [[Trained self-prediction without an own-model edge (Zeng 2026)]] | 3 | deep | – | – | ✓ | – | monitor | threat Q6 (no own-model edge) |
| [[Outside controller steers thinking modes (Karpf 2026)]] | 3 | skim | – | – | – | – | monitor, control | prior art Q2 (name and design overlap) |
| [[Emotion directions drive choices in Claude (Anthropic 2026)]] | 4 | deep | – | – | ✓ | – | evaluate | prior art Q1 |
| [[Hidden good-bad feeling changes choices (Berg 2026)]] | 4 | deep | – | – | ✓ | ? | evaluate, control | prior art Q1 (grounded design); threat Q3 (DPO does not move valence) |
| [[Steer code readability inside the model (Gao 2026)]] | 4 | deep | – | – | – | – | control | prior art Q2 (baseline arm), Q1 |
| [[Value axis - model knows it is on track (Jiang 2026)]] | 4 | deep | – | – | ✓ | ✓ | monitor, evaluate, control | prior art Q1, Q2 |
| [[Few neurons predict right answers (Xu 2026)]] | 4 | deep | – | – | ✓ | – | monitor, evaluate, control | prior art Q1, Q2; threat Q1 (correctness confound) |
| [[SEAL - models write their own training data (Zweiger 2025)]] | 5 | deep | – | – | – | ✓ | persist | prior art Q3, Q4 |
| [[TFTV - turn a steering vector into a weight edit (Perin 2026)]] | 5 | deep | – | – | – | – | persist | prior art Q5 |
| [[WSP - a model reads and edits weights (Takehi 2026)]] | 5 | deep | – | – | – | – | persist | prior art Q4, Q5 |
| [[One direction controls refusal (Arditi 2024)]] | 5 | skim | – | – | ✓ | – | persist | prior art Q5 |
| [[A simple sort replaces the anti-loop edit (Fischetti 2026)]] | 5 | skim | – | – | – | – | persist | prior art Q5, Q4 |
| [[ThinkEdit - edit weights to think longer (Sun 2025)]] | 5 | skim | – | – | – | – | persist | prior art Q5 (killed it) |
| [[Steer2Edit - steering into small weight edits (Sun 2026)]] | 5 | deep | – | – | – | – | persist | prior art Q5 (killed it) |
| [[Exploring WSP - small weight edits, uneven results (Hu 2026)]] | 5 | skim | – | – | – | ? | persist | prior art Q4 |
| [[WeightBench - models cannot yet patch models (Marasini 2026)]] | 5 | skim | – | – | – | – | persist | threat Q4 (patching mostly fails; impossible edits not spotted) |
| [[Self-reward sharpens then collapses (He 2026)]] | 6 | deep | – | – | – | ✓ | anchor | threat Q3 |
| [[Self-reward on code collapses to short code (Jin 2026)]] | 6 | deep | – | – | – | ✓ | evaluate, anchor | threat Q3 |
| [[Self-reward only within the same test result (Wu 2026)]] | 6 | deep | – | – | – | ✓ | anchor, persist | prior art Q3 |
| [[Self-judge training makes wrong look right (Zhou 2026)]] | 6 | deep | – | – | ✓ | ✓ | evaluate, anchor | threat Q2, Q3 |
| [[Training on own outputs erases rare data (Shumailov 2024)]] | 6 | deep | – | – | – | ✓ | anchor | threat Q3 |
| [[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]] | 6 | skim | – | – | – | ✓ | anchor | prior art Q3 (non-regression gate) |
| [[Models show research taste (Trehan 2026)]] | 7 | deep | ✓ | ✓ | – | – | evaluate | prior art Q1 (method for tests 1 and 2) |
| [[OMNI - models judge which tasks are interesting (Zhang 2023)]] | 7 | deep | ? | – | – | ? | control, anchor | prior art Q3 (taste picks what to learn; taste is human, not own) |
| [[Open-ended means novel and learnable to an observer (Hughes 2024)]] | 7 | deep | ? | – | – | ✓ | anchor | prior art Q3 (definition for test 4) |
| [[Learn to find interesting maths (Patel 2026)]] | 7 | skim | ? | – | – | ✓ | anchor, persist | prior art Q3 |
| [[Models share one taste for text (Zatuchin 2026)]] | 7 | skim | ✓ | – | – | – | anchor | threat Q3 (own vs shared taste) |

Totals (✓ only), 38 papers: Divergent 2, Stable 1, Grounded 13, Self-reinforcing 10.

## Reading the matrix

- **Update 2026-11-20.** 15 rows added (13 new notes, plus Ji-An and Lindsey, which were missing). Stable is still the least covered test (1 paper) and Divergent is next (2). All 5 new grounded rows test behavior or injected states, and 2 of them (Yax, Lindsey at small scale) weaken the positive claims. Q3 gains one more threat (Shumailov) and two pieces of prior art for anchors (GUARD, Hughes). Q4 now has a direct threat: audited weight patching mostly fails (WeightBench).

- **Stable is the least covered test.** Only [[Models show research taste (Trehan 2026)]] measures it, with one model, 80 pairs and one sample per order. Divergent is close behind (2 papers, both behavioral). Neither has any internal-signal paper, so tests 1 and 2 rest on our own experiments.
- **Q3 has the most threats (5):** He, Jin, Zhou, Berg and Zatuchin. Its only prior art for a working loop (Wu, Patel, SEAL) uses an external or frozen signal, never the model's own activations.
- **Q5 has the most prior art (6 papers), which is why it was killed.** All six put a direction into weights; none take the direction from the model's own evaluation. That missing piece now sits in Q3, not Q5.
- **Grounded is well covered, but mostly by negative or method papers.** Singh, Ferrara and Arditi all show self-report does not follow the internal state. The positive grounded results (Anthropic, Berg, Jiang, Xu) are causal steering of choice, not self-report, which is the version of test 3 we should claim.
- **Q1 is the most cited thread (prior art in 7 rows, threat in 3).** It is the gating experiment, and no paper tests an internal signal on passing-but-different code.
