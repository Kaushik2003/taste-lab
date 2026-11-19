---
type: paper
title: "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification"
status: skimmed
arxiv: 2504.05419
url: https://arxiv.org/abs/2504.05419
authors: Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, He He (NYU, NYU Shanghai)
year: 2025
venue: preprint (COLM 2025 [unverified])
relevance: 3
section: 3
tier: deep
tests: []
components: [monitoring, controller]
tags: [type/paper, role/prior-art, section/3, component/monitoring, component/controller, status/skimmed, relevance/3, thread/T2, thread/T1, probe, self-verification, early-exit, reasoning-models]
links: ["[[metacognition-monitor-control]]", "[[inference-time-steering-T2]]", "[[landscape-metacognitive-monitoring]]", "[[neuromodulation-metalearning]]"]
---

# Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification

**One line:** A small probe on a reasoning model's hidden states can tell whether each intermediate answer is right, well calibrated, and using it to stop reasoning early saves about a quarter of the tokens at no accuracy cost.

## Claim
Long chain-of-thought models encode whether their own intermediate answers are correct, even before the answer is written out, but they do not use that information, which is one cause of overthinking ([arXiv](https://arxiv.org/abs/2504.05419)).

## Mechanism
- **Segment** each reasoning trace at blank lines; keywords such as "wait", "double-check", "alternatively", "verify" start a new chunk. Chunks without an answer merge into the nearest chunk that has one.
- **Label** each chunk: Gemini 2.0 Flash extracts the intermediate answer and checks it against ground truth.
- **Probe**: input is the last-layer hidden state at the final token of the chunk. A 2-layer MLP (ReLU, sigmoid) trained with class-weighted BCE; grid search over hidden size {0, 16, 32}. Many probes end up linear (hidden size 0), so correctness looks linearly encoded. Max 1,000 training examples per dataset.
- **Early exit** (Section 5): during generation, stop at the first intermediate answer whose probe score is above a threshold.
- Models: DeepSeek-R1-Distill Llama-8B/70B, Qwen-1.5B/7B/32B, and QwQ-32B. Tasks: GSM8K, MATH, AIME, KnowLogic.

## Evidence
- In-distribution ROC-AUC above 0.7 for every probe; R1-Distill-Qwen-32B above 0.9 on AIME. R1-Distill-Llama-8B on MATH: AUC 0.84 (Table 2).
- ECE (Table 1) is mostly 0.01 to 0.10, but reaches 0.13 to 0.14 on some cells (Qwen-1.5B and Qwen-32B on AIME, QwQ-32B on MATH), so "ECE below 0.1" in the text is slightly generous.
- Correctness is readable **before** the answer appears, and gets stronger as the chunk approaches the answer.
- Transfer GSM8K ↔ MATH is reasonable; logic → math is weak.
- A non-reasoning model (Llama-3.1-8B-Instruct) gives clearly worse probes (Figure 3), which the authors attribute to long-CoT training.
- Early exit, R1-Distill-Llama-8B on MATH, 10K token cap (Figure 5): threshold 0.85 keeps accuracy at 88.2% (same as no exit) with about 24% fewer tokens; threshold 0.9 gives 88.6% with 19% fewer. Against stopping after a fixed number of chunks, up to 5 points more accuracy at similar cost.
- Class balance: most chunks are correct (for MATH, 68% to 84% positive, Table 4).

## Limits / what they didn't show
- **The probe is external.** The model never reads or uses the signal itself; the authors say models "encode a notion of correctness yet fail to exploit it".
- Labels come from an LLM judge; segmentation is a keyword heuristic.
- Early exit tested on one model and one dataset only. Math and logic only, no code.
- The in-distribution MATH entries are identical across Tables 2 and 11 to 15, which may be a copy error; check before citing exact AUCs.
- No code link in the paper [unverified whether code exists elsewhere].

## Relevance to taste-lab
- **The simplest working monitor → control loop** in the literature: read an internal evaluation signal, act on it at inference time. It is the template and the baseline for [[inference-time-steering-T2]].
- Prior-art check A: **partial**. The signal is internal (hidden states), and it changes the model's own reasoning (when to stop). But the reader is an external probe trained on externally graded labels, the signal is correctness not preference, and the only control is "stop".
- For our paper: correctness is held fixed by tests in our setup, so the open question is whether a similar probe can read a **preference** (readability) rather than correctness. That is [[code-quality-signal-T1]].
- Warning from a follow-up: [Kirin 2607.18553](https://arxiv.org/abs/2607.18553) finds a correctness probe on a looped model helps abstention and reranking of finished answers, but steering, branching and LoRA driven by the same probe gave no gain. Choosing among finished outputs (T2's best-of-n arm) is the use with evidence behind it.

## Steal this
- Chunk-level probing at reasoning boundaries ("wait", "alternatively") plus a threshold rule: a ready design for a T2 arm that reads valence per chunk instead of per final answer.
- Their calibration reporting (ROC-AUC + ECE + Brier per model × dataset) as the format for T1 results.
- The reasoning vs non-reasoning model contrast: run T1 on both a base/instruct and a reasoning checkpoint of the same family.

## Harshit's notes
<!-- yours -->
