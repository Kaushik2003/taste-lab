---
type: paper
title: "Sparse Reward Subsystem in Large Language Models"
status: unread
arxiv: 2602.00986
url: https://arxiv.org/abs/2602.00986
authors: Guowei Xu, Mert Yuksekgonul, James Zou
year: 2026
venue: NeurIPS 2026
relevance: 2
section: 4
tier: deep
tests: [grounded]
components: [valence, controller, monitoring]
tags: [type/paper, section/4, test/grounded, component/valence, component/controller, component/monitoring, status/unread, relevance/2, thread/T3, thread/T2, thread/T1, value-neurons, dopamine, td-error, reward-prediction-error, sparse-probe, process-reward-model, confidence, neuron-ablation]
links: ["[[valence-readout]]", "[[neuromodulation-metalearning]]", "[[metacognition-monitor-control]]", "[[landscape-evaluation-signals]]", "[[2026-jiang-value-axis]]", "[[2025-zhang-reasoning-models-know-when-right]]", "[[2026-ferrara-all-quiet-pain]]", "[[code-quality-signal-T1]]", "[[inference-time-steering-T2]]", "[[self-training-collapse-T3]]", "[[four-taste-tests]]"]
---

# Sparse Reward Subsystem in Large Language Models

**One line:** Fewer than 1% of hidden-state coordinates in 0.8B to 14B models are enough to predict whether the model will get a problem right ("value neurons"). A second sparse set tracks step-by-step surprise ("dopamine neurons") and works as a process reward model for search. Both readouts are probes trained on correctness labels.

Source: [arXiv 2602.00986](https://arxiv.org/abs/2602.00986) (v3, Nov 2026), full HTML read including appendices. Tsinghua and Stanford. Code: [zou-group/reward_subsystem](https://github.com/zou-group/reward_subsystem) (MIT).

## Claim
Reward-related information in LLM hidden states is not spread across the whole vector. It sits in a small subset of coordinates: some encode the expected value of the current state, others encode the step-level temporal difference (TD) error. The authors call this a "reward subsystem", by analogy with value and dopamine neurons in the brain. The analogy is about computational role only (App. N).

## Mechanism
- **Setup:** treat the LLM as a policy. Terminal reward r is 1 if the final answer is correct, 0 otherwise. State value V(s_t) = probability of ending correct from partial output s_t.
- **Value probe (Sec. 3.1):** a two-layer MLP (hidden size 1024) on the hidden state of one layer, trained with TD learning (gamma = 1 - 1e-5) on the model's own sampled responses, not by direct regression on the final reward. AdamW, lr 1e-4, 100 epochs, 80/20 split (App. A).
- **Finding the "neurons" (Sec. 3.2):** rank input coordinates by the L1 norm of their first-layer probe weights, drop the weakest fraction p, and re-evaluate. Main metric: AUC of the value predicted at the last prompt token (before any answer tokens) against final correctness. If AUC stays flat as p goes to 0.99, the surviving coordinates are "value neurons". Here "neuron" means a residual-stream coordinate, not an MLP unit.
- **Dopamine probe (Sec. 4):** split each response into paragraphs. At each paragraph boundary, estimate V by Monte Carlo rollouts (K completions; K is not stated in the text [unverified]). Target = TD error between consecutive boundaries. Input = hidden states z-scored per neuron within the response, then averaged over the paragraph's tokens (App. E). MLP hidden size 32. Only steps with |TD error| > 0.3 are kept for training and evaluation. Same L1 pruning to find "dopamine neurons", scored by Spearman correlation.
- **Interventions (Sec. 3.4):** zero the top 1% value neurons in one layer and measure task accuracy, against several neuron-selection baselines.
- **Applications (Sec. 5):** (1) value readout at the prompt as a confidence predictor; (2) dopamine readout as a process reward model: at each paragraph boundary sample K = 4 candidate next paragraphs and keep the one the probe scores highest.

## Evidence
- **Models:** Qwen-2.5-7B and 14B SimpleRL-Zoo (RLVR-tuned), Qwen2.5-7B-PPO-Zero, base Qwen-2.5-7B, Llama-3.1-8B-Instruct, Phi-3.5-mini-instruct, Gemma-3-4B, Qwen3.5-0.8B. Largest is 14B. Data: GSM8K, MATH500, ARC, Minerva Math, plus MBPP+ (code) and IFEval as existence checks only (App. C.1, curves with no numbers in the text).
- **Sparsity:** value AUC at the prompt stays flat down to about 1% of coordinates in layers 2 to 4 (Fig. 2). Absolute AUC at the prompt is moderate; at the last response token it stays above 0.8 for 4 models on Minerva Math (App. I).
- **Ablation (Table 1, Qwen-2.5-7B-SimpleRL-Zoo, MATH500, baseline 75.2%):** zeroing the top 1% value neurons in a single layer drops accuracy to 20.3% on average over layers 2 to 5 (1.2% at layer 5). Same-size controls: random 74.6%, neurons from a next-token-prediction probe 76.4%, weight magnitude 71.6%, Wanda 65.8%. Value and NTP neuron sets overlap 0.7% (random 0.5%).
- **Specificity (Table 2, layer 2):** reasoning drops (MATH500 -38.2, GSM8K -40.2, ARC -16.0 points), factual recall barely moves (PopQA +3.6, EntityQuestions -3.0). Extra controls (Table 8): massive activations, super weights and attention sinks cost at most 2 points; "rogue dimensions" cost up to 11.4.
- **Present before RL (Table 12):** value-neuron sets in base Qwen-2.5-7B and its two RL-tuned versions overlap far above chance (IoU 0.28 to 0.29 at p = 0.99 vs 0.005 random).
- **Confidence (Table 3, 4 models x MATH500/ARC):** mean AUC 0.67 for value neurons vs 0.62 question length, 0.60 full-hidden-state linear probe (LCD), 0.52 verbal confidence, 0.48 token confidence. Question length beats value neurons on Qwen3.5-0.8B on both datasets.
- **Dopamine signal:** mean Spearman rho = 0.28 between probe output and MC TD error at the chosen threshold (Table 11, Qwen-2.5-7B, averaged over layers and 3 seeds). Qualitative traces of one neuron (index 1517, layer 5) peak at key steps and dip at errors (Fig. 4, App. F).
- **Process reward search (Table 4, MATH500, 3 seeds):** mean accuracy 72.3% with the dopamine probe vs 67.3% P(true), 66.2% min logprob, 66.1% random candidate, 63.5% implicit PRM, 61.3% greedy. Per model: 79.6% (7B), 82.7% (14B), 54.6% (Llama-3.1-8B). Transfer MATH500 to GSM8K on Llama-3.1-8B: 94.4% vs 92.8% implicit PRM and 90.7% greedy (App. K).

## Limits / what they didn't show
- **Needs a verifiable reward.** Both probes are trained against answer correctness. The authors say it is untested on open-ended tasks without such a signal (App. O). Readability is exactly that kind of task.
- **The ablation may show general damage, not reward specificity.** Zeroing 1% of residual coordinates in layers 2 to 5 takes MATH500 to 1.2%. Long multi-step reasoning is likely more fragile to any damage than short-answer factual recall, so the specificity contrast is confounded by task length and format. The authors call these interventions "preliminary" and flag overlap with large-magnitude coordinates as an open confound.
- **No steering.** They never push on the value or dopamine coordinates to see whether confidence, backtracking or accuracy shift in a graded way. Steering is listed as future work (App. N).
- **The prompt-position signal may be mostly problem difficulty.** AUC 0.67 vs 0.62 for plain question length. That is a readout of "is this problem hard for me", not clearly an evaluation of the model's own ongoing state.
- **Dopamine evidence is weak.** Average rho 0.28, and the clearest pictures come from one selected neuron.
- **PRM baselines are self-signals only** (logprob, P(true), implicit PRM). No trained external PRM is compared. Probes are trained and searched on MATH500; whether search used only the held-out 20% is not stated [unverified].
- **Probes are policy-specific.** The authors note probes may need refitting when the policy changes substantially.
- Scale tops out at 14B. An independent pre-registered replication (Nell Watson) is acknowledged, but its results are not reported and I could not find them [unverified].

## Relevance to taste-lab
**Relevance 2.** Strong on the monitor and controller components, but the signal is about correctness, which our testbed holds fixed.
- **Monitor ([[valence-readout]]):** a cheap, sparse readout of "how am I doing" from early layers. It is a concrete alternative to emotion-direction readouts and to the dense value direction in [[2026-jiang-value-axis]] (layer 21 of Qwen3-8B, difference of means). Open question: are Jiang's axis and these early-layer coordinates the same signal?
- **Controller ([[neuromodulation-metalearning]]):** "dopamine neurons" are a readable reward prediction error, which is exactly the dopamine slot in the Doya mapping. A TD-error readout could set the per-step learning rate or decide which experiences are worth learning from in T3.
- **T1 control, and a threat ([[code-quality-signal-T1]]):** on solutions that all pass the tests, a correctness-value readout should have little to track. Run a value-neuron probe next to our valence readout. If our readout ranks readability and the value probe does not, that is evidence our signal carries more than "will this be right". If both move together, our "taste" may just be a correctness-confidence signal leaking through style cues.
- **T2 template ([[inference-time-steering-T2]]):** step-level search guided by an internal probe beats random selection by about 6 points. It is reasoning-level control by an internal signal, but with a probe trained on external labels, not the model's own evaluation.
- **T3 warning ([[self-training-collapse-T3]]):** a probe fitted to the starting policy goes stale as the policy changes. In a self-training loop, staleness and real "drift away from the pretraining origin" look the same unless we refit a reference probe each round.
- **Grounded test:** internal value beats verbal confidence (0.67 vs 0.52 AUC), which fits [[2026-ferrara-all-quiet-pain]]: internal state carries more than self-report.

## Steal this
- Released code (MIT): TD-trained MLP probe, L1-norm input pruning to find a sparse coordinate set, and bootstrap AUC curves.
- Paragraph-level z-scored activations as the input for any step-level signal.
- The ablation control set: random, next-token-probe coordinates, weight magnitude, Wanda, massive activations, super weights, rogue dimensions, attention sink. Use it before claiming any of our valence coordinates is causal.
- K = 4 per-paragraph search as a cheap T2 arm next to whole-solution best-of-n.

## Harshit's notes
<!-- yours -->
