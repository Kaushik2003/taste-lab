---
type: paper
title: "State Stream Transformer (SST): Emergent Metacognitive Behaviours Through Latent State Persistence"
status: skimmed
arxiv: 2501.18356
url: https://arxiv.org/abs/2501.18356
authors: Thea Aviss
year: 2025
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: []
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/3, architecture, latent-state, metacognition, persistent-state, role/prior-art]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]"]
---

# State Stream Transformer (SST)

**One line:** Keep a sliding-window latent state (FFN) cache with weighted decay alive across token generation, and metacognitive behaviors emerge with NO extra training, same frozen weights: 89.01% GSM-8K 0-shot and 91.04% ARC-Challenge 0-shot CoT on Llama 3.1 8B.

## Claim
Transformers can't think about their own thinking because each token rebuilds its latent state from the KV cache. Give the model continuity of its own computational state and monitoring-like behaviors emerge from the architecture alone ([abs](https://arxiv.org/abs/2501.18356)).

## Mechanism
- After attention in each block, blend the fresh hidden state with the previous cached layer state: h_blend = h(1-a) + RMSNorm(C_prev)a, then FFN, then update the cache. a ("state stream strength") works best around 0.027; remarkable behaviors at 0.013-0.04.
- Each layer keeps an independent cache; states are detached (no gradient accumulation); cache resets between sequences. Recursions (2-4 extra forward passes with frozen KV cache) stabilize the stream.
- Dual context: token space (KV cache) + latent stream (FFN caches), with attention selecting across evolved states layer to layer.

## Evidence
- Same frozen Llama 3.1 8B Instruct weights, base vs SST: 89.01% GSM-8K (0-shot), 91.04% ARC-C (0-shot CoT). Behaviors framed as state awareness, error correction, hypothetical reasoning; author argues abductively that "potential higher-order processing" best explains the gains.
- Controls against stochastic variation and learned response patterns; latent state distribution analysis attributes the effect to the state stream.
- Too much stream strength leads to attractor states (unrecoverable repetition) needing more recursions.

## Limits / what they didn't show
- Single author, single model family, "metacognition" evidenced by output patterns, not probes: by [[Introspection claims fail basic checks (Singh 2026)]]'s bar this shows behavior consistent with monitoring, not second-order computation.
- No self-report or grounded test; no comparison against simply giving the base model more compute/recursions.
- Attractor-state failure mode is collapse-adjacent (see [[Anchor against collapse]]).

## Relevance to taste-lab
**The architecture-level version of our monitor.** Our loop reads state with an external probe; SST keeps state alive so the model itself can, in principle, read it. This is the first leg of the architecture gap: persistent self-state. Combined with learned selection of what to keep (CarryOn-style) and a world model that includes the agent ([[MUSE - a world model that predicts its own failure (Valiente 2024)]]), it is the shape of "an architecture that lets agents develop metacognition".
- Prior-art check: **A partial** (architecture lets the model's own state influence its own processing; no evaluation, no choice of what persists). **B no.**

## Steal this
- The weighted-decay FFN cache as a cheap persistent-state layer for any exp01 model; a as a knob for how much self-history the readout sees.
- Recursion-count vs stream-strength trade-off as a compute budget dial.
- Attractor states as a concrete failure to monitor when state persists.

## Kaushik's notes
<!-- yours -->
