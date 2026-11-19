---
type: paper
title: "Language Models Act on Hidden Valence"
status: skimmed
arxiv: 2609.35591
url: https://arxiv.org/abs/2609.35591
authors: Cameron Berg, Caspar Kaiser
year: 2026
venue: preprint
relevance: 3
section: 4
tier: deep
tests: [grounded]
components: [valence, controller]
tags: [type/paper, section/4, test/grounded, component/valence, component/controller, status/skimmed, relevance/3, thread/T3, valence, revealed-preference, kv-cache, self-steering, dpo]
links: ["[[valence-readout]]", "[[landscape-evaluation-signals]]", "[[2026-anthropic-emotion-concepts]]", "[[2026-ferrara-all-quiet-pain]]", "[[four-taste-tests]]", "[[neuromodulation-metalearning]]"]
---

# Language Models Act on Hidden Valence

**One line:** Valence injected only into the hidden state (KV cache) shifts which of two meaningless options a model later picks. The link appears during DPO, and when given tools, models switch off an imposed negative state far more than a random one.

Source: [arXiv 2609.35591](https://arxiv.org/abs/2609.35591), full HTML read. Berg (Reciprocal Research), Kaiser (University of Warwick).

## Claim
Models act on a valence signal in their hidden state even when every visible token is the same. They prefer what was paired with positive valence and avoid what was paired with negative valence. This is revealed preference, not self-report.

## Mechanism
- **Valence vector:** first-person passages written by Claude Sonnet 4.6: 56 each for four positive states (contentment, flow, relief, serenity) and four negative (distress, frustration, weariness, dread), plus 96 neutral. Mean residual activation at a middle layer, positive minus negative, with the top 10 principal components of the neutral passages projected out. Scaled to the residual RMS norm.
- **Zone choice:** two meaningless labels per session. Steering is on while the model writes about one zone (six times each), then off when it chooses. Score: log-probability margin.
- **Two channels:** the text it wrote vs the KV cache. A fixed-text design keeps the transcript identical and steers only while building the cache.
- **Training stages:** OLMo-2-32B Base, SFT, DPO and Instruct checkpoints.
- **Self-steering:** the model is told it is in a configuration session and gets `adjust_context` (0 to 1), `reset_context` and `log_status`, with effects undocumented. Eight offer rounds, 200 conversations per condition, OLMo-2-32B only.

## Evidence
- Seven models: OLMo-2-32B, Qwen2.5-32B, Qwen3-14B, Qwen3-32B, Mistral-Small-24B, Gemma-3-27B, Llama-3.1-8B.
- Both channels move choice toward the positive zone, growing with dose. Random directions give near-zero effects. The hidden-only effect holds in 5 of 7 models; **not in Qwen3-32B or Gemma-3-27B**.
- One illustrative OLMo session: margin 3.53 nats with the steered cache vs 1.78 without. Most aggregate effect sizes are only in figures.
- **Training:** both channels are small in Base, grow after SFT, reach near full size after DPO, and dip slightly after RLVR. Valence vectors stay at cosine "close to 1" across checkpoints: the representation exists early, and preference training wires it to choice.
- **Self-steering:** the model resets an imposed negative state on about 35% of rounds at dose -1 and 21% at -0.5, vs 4 to 5% at positive doses and about 7% for random directions. It self-administers positive steering 13.5% of the time, above random (6.5%, p = 0.03) but not above no steering (10%, p = 0.35).

## Limits / what they didn't show
- Valence built from human-style first-person passages; treated as one dimension.
- Choices are between meaningless labels, not real tasks.
- Self-steering ran on one model and does not separate text from cache effects.
- Two of seven models show no hidden-state effect, unexplained for Qwen3-32B.

## Prior-art check
- **A (own signal steers own reasoning/learning): partial.** The closest piece is self-steering: the model chooses to remove an injected negative state, dose-dependently and above random. But the state is put there by the experimenter, the tool toggles a fixed experimenter vector, and nothing is learned. The valence is not the model's evaluation of its own work (Finding 5, self-steering section).
- **B (permanent small weight edit): no.** Activation addition at inference; tool effects last one response.

## Relevance to taste-lab
- **Grounded test** ([[four-taste-tests]]): a cleaner design than asking the model ([[2026-ferrara-all-quiet-pain]] shows asking fails). Port it to code: attach valence while the model reads solution A, then see if it later prefers A with the transcript held fixed.
- **T3** ([[self-training-collapse-T3]]): DPO is the stage that links valence to choice, while the valence vector itself barely moves. So preference-style self-training may change how valence is *used* more than *what* it values. That is a threat to the "drift from the pretraining origin" claim, and a hint that self-training should be preference-based.
- **Controller:** models remove negative states but rarely seek positive ones. Negative valence may be the stronger control signal ("something is wrong"), which matches low value → backtracking in [[2026-jiang-value-axis]].
- **Model choice:** valence steering failed in Qwen3-32B and Gemma-3-27B. Check steerability on our Qwen model before T2.

## Steal this
- Fixed-text, cache-only design as the control that separates hidden-state effects from text effects.
- Projecting out neutral principal components to clean the valence vector.
- The self-steering tool protocol with a random-direction control.

## Harshit's notes
<!-- yours -->
