---
type: landscape
status: draft
cluster: 3
section: 5
tags: [type/landscape, section/5, landscape, persistent-control, self-modification, weight-editing, steering-to-weights, fast-weights, neuromodulation]
links: ["[[TFTV - turn a steering vector into a weight edit (Perin 2026)]]", "[[One direction controls refusal (Arditi 2024)]]", "[[SEAL - models write their own training data (Zweiger 2025)]]", "[[WSP - a model reads and edits weights (Takehi 2026)]]", "[[A simple sort replaces the anti-loop edit (Fischetti 2026)]]", "[[Models that change their own weights]]", "[[Neuromodulators as learning settings]]", "[[Q4 Can the model edit its own weights]]", "[[Q5 (stopped) Make steering permanent]]", "[[Gaps in the field]]"]
---

# Landscape 3: Persistent metacognitive control: self-modification of weights

**Guiding question:** Can a model turn a judgment about its own behavior into a lasting change in its own weights, cheaply, without breaking anything else?

## Timeline
- 1992-93 · [Schmidhuber: fast-weight memories, self-referential weight matrix](https://arxiv.org/abs/2202.05780) (cited there: Neural Computation 4(1), ICANN 1993) · a slow net learns to write a fast net's weights, then a net that can in principle rewrite its own weight-change rule.
- 2002 · [[Neuromodulators as learning settings]] ([Doya, Neural Networks 15(4-6)](https://doi.org/10.1016/S0893-6080(02)00044-8)) · neuromodulators map to learning meta-parameters (acetylcholine to learning rate): our controller blueprint.
- 2022 · [ROME](https://arxiv.org/abs/2202.05262) · a closed-form rank-one edit to one mid-layer MLP rewrites one stored fact.
- 2022 · [Modern self-referential weight matrix](https://arxiv.org/abs/2202.05780) · a weight matrix that updates itself at runtime with outer products and a delta rule, tested on few-shot learning and multi-task RL.
- 2023 · [Inference-Time Intervention](https://arxiv.org/abs/2306.03341) · a per-layer truthfulness shift is constant, so it can be baked into the attention output bias offline. Earliest "steering made permanent" we found.
- 2024 · [[One direction controls refusal (Arditi 2024)]] · one direction controls refusal in 13 chat models; projecting it out of every residual-writing matrix makes the ablation permanent and exact.
- 2025 · [[SEAL - models write their own training data (Zweiger 2025)]] · the model writes its own finetuning data; RL on the downstream score teaches it which self-edits help.
- 2025 · [Contrastive weight steering](https://arxiv.org/abs/2511.05408) · subtract two small opposite finetunes to get a behavior direction in weight space; it generalizes further out of distribution than activation steering.
- 2025 · [Nested Learning](https://arxiv.org/abs/2512.24695) · a model as nested optimizers updating at different rates (Hope): multi-timescale memory built into the architecture.
- 2026-02 · [Steer2Edit](https://arxiv.org/abs/2602.09870) · steering vector to sparse rank-one edits per attention head and MLP neuron; safety sits in a few heads, reasoning length in dense MLP edits across many layers.
- 2026-09 · [[TFTV - turn a steering vector into a weight edit (Perin 2026)]] · rank-one edits on attention outputs across a layer band, built from forward passes only, control traits more strongly than the steering vector they came from.
- 2026-10 · [Select-TTT](https://arxiv.org/abs/2610.36794) · the model's own output head scores each context chunk's relevance, and that score sets the learning rate of its fast-weight writes.
- 2026-11 · [[WSP - a model reads and edits weights (Takehi 2026)]], [Exploring WSP](https://arxiv.org/abs/2611.09382), [WeightBench](https://arxiv.org/abs/2611.18553) · a frontier agent edits a small LM; one 1,023-value edit adds 29.45 points on MATH-500, yet agents cannot reliably patch LMs.
- 2026-11 · [Tree-Ising](https://arxiv.org/abs/2611.14210) · a fixed recipe (contrastive directions from forward passes, then sparse bit-level edits) beats the agent's loop repair for about $0.90 instead of about $312.

## Current best result
Steering to weights: [[TFTV - turn a steering vector into a weight edit (Perin 2026)]]. On Llama-3.1-8B, rank-one edits on attention outputs in layers 14 to 19 raise the "evil" trait score from 0 to 63.3 (the steering vector alone: 14.1), and subtracting the edits cuts hallucination from 97.5 to 1.9 (steering: 79.1), with MMLU within 0.2 points of base ([Tables 1-2](https://arxiv.org/html/2609.09054)).
Search-based repair: [Tree-Ising](https://arxiv.org/abs/2611.14210) gets Qwen3.5-0.8B to 55.1% on MATH-500 (base 7.9%, WSP agent 51.7%).

## Biggest open problem
In most working methods someone else picks the direction: experimenter prompts plus an external judge (TFTV, Steer2Edit, Arditi) or a frontier agent (WSP). One 27B model now picks a direction from its own hidden states and writes it into its own weights, but graded answers decide which edits to keep ([[A model rewrites its own weights (Fan 2026)]]). No paper shows a model choosing the direction from its own evaluation signal and then writing it into its weights. Also missing: what fraction of a fixed steering gain a weight edit keeps at matched strength, and whether repeated edits stay stable ([Schessl 2026](https://arxiv.org/abs/2607.24805): stacked closed-form edits end 61 to 71% of the edit size away from one-shot composition).

## Leading groups
- MIT CSAIL (Takehi, Khattab; Zweiger, Pari, Agrawal, Kim): [[WSP - a model reads and edits weights (Takehi 2026)]], [[SEAL - models write their own training data (Zweiger 2025)]].
- Google Research (Behrouz, Mirrokni): [Nested Learning](https://arxiv.org/abs/2512.24695), [Language Models Need Sleep](https://arxiv.org/abs/2606.03979) (Sleep paper affiliation [unverified]).
- University of São Paulo with Google and Google DeepMind (Perin, Hirata, Boscaini, Araujo): [[TFTV - turn a steering vector into a weight edit (Perin 2026)]].
- UC San Diego, Weng lab (Sun, Yan, Wang, Weng): [Steer2Edit](https://arxiv.org/abs/2602.09870).
- Steering and ablation interpretability (Arditi, Obeso, Nanda; Fierro and Roger): [[One direction controls refusal (Arditi 2024)]], [Contrastive weight steering](https://arxiv.org/abs/2511.05408). Mixed affiliations; Nanda, Fierro and Roger [unverified].
- IDSIA, Schmidhuber group (Irie, Schlag, Csordás): [Modern SRWM](https://arxiv.org/abs/2202.05780) [unverified affiliation].

## Closest to taste-lab
- **Q5's mechanism is prior art.** TFTV and Steer2Edit already turn a steering vector into rank-one weight edits with no training, and ITI and Arditi (App. I.1) note that a constant steering shift is just a bias edit. So the bridge in [[A simple sort replaces the anti-loop edit (Fischetti 2026)]] is known. Still ours in [[Q5 (stopped) Make steering permanent]]: a direction from the model's own [[Good-bad signal probe]], code readability with tests fixed, and the "fraction of steering gain kept" measure that nobody reports.
- **"One small edit" may be too small for taste.** TFTV edits 6 to 17 layers (the widest band for hallucination), and Steer2Edit puts most of its reasoning-length edits in MLP neurons ([[Steer2Edit - steering into small weight edits (Sun 2026)]], App. H). Style is probably that kind of behavior, which supports Q5's "Evidence against".
- **Q4 looks more feasible.** Tree-Ising and the Exploring-WSP edit show the useful part of a WSP repair is a contrastive direction plus a sparse write, computed from forward passes with no frontier agent. A small model could run that recipe on itself ([[Q4 Can the model edit its own weights]]). The open part is choosing the direction.
- **Controller prior art is partial.** Select-TTT sets learning rates from the model's own output head, and [AutoHebb](https://arxiv.org/abs/2610.40757) gates Hebbian plasticity with a signal from its last hidden layer plus external right/wrong feedback. Neither uses valence. [Surprise as a Signal](https://arxiv.org/abs/2606.31495) finds an external surprise detector (AUROC 0.966) beats the model's own verbal confidence (0.618), so read the gate from activations, not self-report.
- **Grounded-test risk after consolidation.** Arditi's edited model still describes its old refusal policy when asked (App. L.3). A taste written into weights may not reach self-report, so check test 3 of [[Four tests for own taste]] after the edit too.

## Reading order for Harshit
1. **must-read** [[TFTV - turn a steering vector into a weight edit (Perin 2026)]] · closest prior art to Q5. Read §3.2-3.3 (the construction, one page), §5.2 (edit vs steering at the same layer), App. B (how layers and α were tuned).
2. **must-read** [[One direction controls refusal (Arditi 2024)]] · the cleanest case of a direction intervention becoming an exact weight edit. Read §2.4, §4.1, App. E, App. I.1 (bias trick for addition), App. L.3 (self-report not updated).
3. **skim** [Steer2Edit](https://arxiv.org/abs/2602.09870) · §3.5 for the rank-one rule, §4.2 for which behaviors are sparse and which are distributed.
4. **skim** [Exploring WSP](https://arxiv.org/abs/2611.09382) · the "Math (Primary)" edit: one rank-one column edit with reversed-direction and random-direction controls, a ready control design for Q5.
5. **skim** [Tree-Ising](https://arxiv.org/abs/2611.14210) · §3.2-3.3: directions from forward passes turned into a sparse edit, the recipe a model could run on itself (Q4).
6. **skim** [Forgetting Is Not a Fix](https://arxiv.org/abs/2607.24805) · the four findings on stacked closed-form edits. Read before planning repeated self-edits (Q3, Q5).

## Log
- 2026-11-20: added self-rewriting ([[A model rewrites its own weights (Fan 2026)]]) to the open problem. The gap is now the judgment, not the choice of edit.
