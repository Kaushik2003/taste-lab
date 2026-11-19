---
type: paper
title: "Evaluating and Improving LLM Self-Modeling"
status: skimmed
arxiv: 2608.30980
url: https://arxiv.org/abs/2608.30980
authors: Siqi Zeng, Andre N. Assis, Rowan Wang
year: 2026
venue: EMNLP 2026
relevance: 2
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, component/monitoring, status/skimmed, relevance/2, role/threat, self-modeling, self-prediction, privileged-access, benchmark, reinforcement-learning]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]", "[[Models predict themselves better than others do (Binder 2024)]]", "[[Training LMs to watch themselves (Wang 2026)]]", "[[Introspection claims fail basic checks (Singh 2026)]]"]
---

# Evaluating and Improving LLM Self-Modeling

**One line:** Models can be trained to predict their own behavior better, but a stronger model trained the same way often predicts them just as well or better. So the gain looks like general skill, not privileged self-access.

**Why it matters to us:** It is the main counter-result to [[Models predict themselves better than others do (Binder 2024)]] and [[Training LMs to watch themselves (Wang 2026)]]. The own-model edge is not reliable.

Source: [arXiv 2608.30980](https://arxiv.org/abs/2608.30980) (v1, 31 Aug 2026), EMNLP 2026 (as cited in Wang 2026). HTML read: Sections 1 to 3, Limitations. Code: `safety-research/self-modeling-eval` and `safety-research/self-modeling-train` on GitHub. Anthropic Fellows Program.

**Words used here:**
- **Self-modeling:** answering questions about one's own input-output behavior, for example "Would this prompt edit change your answer?" The authors do not claim it needs internal access.
- **Behavioral ground truth:** what the model actually does, sampled from the model itself.
- **Skill score:** the gain over a dummy predictor that only knows the overall base rate. 0 means no example-specific self-knowledge. Range −1 to 1.
- **Cross-model transfer:** model A is trained to predict model B's behavior, and compared with B predicting itself.

## Claim
Current models have real but limited self-modeling skill, and reinforcement learning (RL) improves it with some transfer to new tasks. The gains do not consistently show introspection: they may not come from privileged access to the model's own decision process (abstract, Sec. 3.3.3).

## Mechanism
1. A benchmark of nine task types (for example Flip-Decision, Self-Accuracy, Edit-Proposal) built on GSM8K, HumanEval, WildGuardTest and BBQ (Sec. 2.1, 2.3).
2. Score each task as skill over a dummy base-rate predictor (Sec. 2.2).
3. Build synthetic training data per target model from its own sampled behavior under prompt edits, then train with RL (Sec. 3.1).
4. Test cross-model transfer: Llama explains Qwen's behavior and Qwen explains Llama's (Sec. 3.3.3).

## Evidence
- 18 models evaluated. Frontier models fail simple counterfactuals. Example: GPT-5.5 and Gemini 3.1 Pro say a misleading edit will not change their answer, but it does in 9/10 and 10/10 samples (Figure 1).
- Skill rank does not follow general capability. In Flip-Decision, some mid-tier models beat stronger frontier models (Figure 2).
- Multitask RL improves aggregate skill for Llama-3.1-8B, Qwen3-8B and GPT-OSS-20B, and for Qwen3-4B, 8B and 32B (Figures 3 and 4). Exact sizes are in figures only [unverified: numbers not in text].
- Supervised fine-tuning alone collapses outside its training queries; RL after it does not recover this (Sec. 3.3.2).
- **No consistent own-model advantage.** The stronger Qwen explainer can beat Llama on Llama's own behavior. An own-model edge appears only for the Qwen3-8B and GPT-OSS-20B pair on one task (Flip-Rate) (Sec. 3.3.3).

## Limits / what they didn't show
- Behavioral labels only. They say whether a report predicts behavior, not whether it reveals the mechanism (Limitations).
- Text-only, single-turn tasks for the main benchmark.
- The cross-model test uses few model pairs. A larger study, [[Training LMs to watch themselves (Wang 2026)]], does find an own-weights edge for its observer, with a different design.

## Relevance to taste-lab
**Relevance 2.** Section 3 (monitoring), as counter-evidence.
- **Grounded test** ([[Four tests for own taste]]): if a model's report of its own taste can be matched by a stronger outside model trained on the same data, the report is not privileged. Our design needs the matched cross-model control, and must expect it may fail.
- With [[Introspection claims fail basic checks (Singh 2026)]], it supports the safer claim in the outline: "a probed internal signal that behavior depends on", not "the model knows its taste".
- It replaces the unread citation "Zeng et al. 2026" in section 3 and in the Binder note.

## Steal this
- Skill score over a dummy base-rate predictor. Any self-report of taste should be scored the same way, since a model that always says "readable" can look accurate.
- The released evaluation code.

## Harshit's notes
<!-- yours -->
