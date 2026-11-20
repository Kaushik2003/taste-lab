---
type: paper
title: "Training Language Models for Introspective Oversight"
status: skimmed
arxiv: 2611.23365
url: https://arxiv.org/abs/2611.23365
authors: Alex Lin Wang, Linus Yifeng Tang, Dami Choi, Neil Chowdhury (Transluce / MATS / Thinking Machines)
year: 2026
venue: preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/3, introspection, oversight, self-report, observer]
links: ["[[landscape-metacognitive-monitoring]]", "[[2026-singh-llm-introspection-reality-check]]", "[[metacognition-monitor-control]]"]
---

# Training LMs for Introspective Oversight (Transluce)

**One line:** Train a third-person "observer" role inside the same weights (LoRA on Qwen3.6-27B) that answers arbitrary questions about the assistant, rewarded only for answers verified against the assistant's actual behavior: 0.907 mean AUROC across five held-out oversight evals, beating honesty training (0.864), transcript monitoring (0.828), activation oracles (0.796) and direct follow-ups (0.776).

## Claim
Oversight can be trained as a verifiable self-knowledge objective: a role sharing the assistant's weights and activations reports on it more accurately than any external monitor ([abs](https://arxiv.org/abs/2611.23365), [code](https://github.com/TransluceAI/introspective-oversight)).

## Mechanism
- New `query`/`observer` transcript roles; observer excluded from assistant context, so querying never changes assistant behavior. Prospective queries (what will it do) and retrospective queries (what did it do).
- Stage 1 SFT: behavior prediction + hidden-trait inference. Stage 2 RL on verifiable questions (counterfactual Brier-score calibration, multiple-choice against distractor responses from other models). On-policy distillation pins the assistant so the observer doesn't drift with training.
- Because observer and assistant share weights, the observer conditions on the full computation, not just the transcript - the privileged-access ablation (same data, external models) drops substantially.

## Evidence
- Five OOD evals: sycophancy (n=1500), harm-pressure lies (146), reward hacking on SWE-bench (40), WeirdChat fabricated code (200), WeirdChat denial of AI (200), value leakage (262).
- Third-person observer (0.907) beats first-person self-oversight training (0.877): role separation itself helps.
- RL triples observer reasoning length, lifts AUROC 0.719 -> 0.823, still below the non-reasoning 0.907.
- Side effect: introspective-oversight training makes the assistant easier to monitor by every baseline.

## Limits / what they didn't show
- The observer detects misbehavior categories (sycophancy, lies, hacking) - quality/taste questions ("was this response good by the model's own standards?") are untested.
- 40-item reward-hacking eval is thin; AUROC on detection, not on eliciting nuanced self-evaluation.
- Observer answers in natural language; no probe-level readout, so per [[2026-singh-llm-introspection-reality-check]] this is trained verbal report, not demonstrated second-order access.

## Relevance to taste-lab
**The strongest current answer to "models can't report on themselves."** For the grounded test: if an observer role can be trained to report verifiable behavioral facts, a valence/taste observer is the same architecture with a different verification signal. Also the cleanest evidence that separating monitor from actor (third person, own objective) beats asking the assistant - direct support for our external-probe design choice.
- Prior-art check: **A partial** (trained internal monitor of behavior, but the signal is external behavior verification, and it oversees misbehavior not taste). **B no.**

## Steal this
- The role-separation trick (observer excluded from assistant context) for any self-report experiment: zero interference, measurable.
- OPD anchoring as the concrete anti-drift mechanism when training a self-facing role.
- Their eval battery as a template for constructing verifiable self-knowledge questions.

## Kaushik's notes
<!-- yours -->
