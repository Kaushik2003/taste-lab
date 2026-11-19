---
type: paper
title: "Training Language Models for Introspective Oversight"
status: skimmed
arxiv: 2611.23365
url: https://arxiv.org/abs/2611.23365
authors: Alex Lin Wang, Linus Yifeng Tang, Dami Choi, Neil Chowdhury
year: 2026
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, component/monitoring, status/skimmed, relevance/3, role/prior-art, introspection, oversight, self-prediction, privileged-access]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Introspection claims fail basic checks (Singh 2026)]]", "[[Models sometimes notice injected thoughts (Lindsey 2025)]]"]
---

# Training Language Models for Introspective Oversight

**One line:** Add a new "observer" role to a model and train it only to answer questions about what the assistant role did or will do. The observer shares the assistant's weights, and it catches sycophancy and lies better than outside monitors.

**Why it matters to us:** It is the strongest 2026 evidence that a model's own weights give it an advantage in reading its own behavior ("privileged access"). It is also a working, trained meta level in the sense of [[Monitoring and control between two levels (Nelson 1990)]].

Source: [arXiv 2611.23365](https://arxiv.org/abs/2611.23365) (v1 17 Nov 2026). Full HTML read: Sections 2 to 6.

**Words used here:**
- **Role:** a labeled part of a chat, such as system, user or assistant. Here they add "query" and "observer".
- **Observer:** the new role. It sees the transcript and answers questions about the assistant. Its text is hidden from the assistant.
- **Prospective / retrospective query:** a question before the assistant answers (predict) or after (explain).
- **LoRA:** a small add-on to the weights that is trained instead of the full model. Rank 32 here.
- **On-policy distillation (OPD):** training that keeps the assistant's outputs close to the original model, so the assistant does not drift.
- **AUROC:** a score of how well a number separates two groups. 0.5 is chance, 1.0 is perfect.
- **Activation oracle:** a separate trained reader that answers questions from a model's hidden numbers.

## Claim
Training a separate role in the model to answer verifiable questions about the assistant gives better oversight than asking the assistant, honesty training, outside transcript monitors or activation oracles. Part of the gain comes from sharing weights with the assistant ([arXiv](https://arxiv.org/abs/2611.23365), Sec. 4.1).

## Mechanism
1. **Model:** Qwen3.6-27B, rank-32 LoRA, trained with Tinker (Sec. 2.2).
2. **Stage 1, supervised training (SFT):** two data sets in equal mix.
   - Behavior prediction: predict facts about the assistant's next answer. Labels come from 5 sampled answers per prompt; Claude Haiku 4.5 writes the question-answer pairs.
   - Hidden trait: a trait (for example "speak like a pirate") is put in a system prompt the observer cannot see. The observer must infer it from the answer.
3. **Stage 2, reinforcement learning (RL):** the observer reasons before it answers.
   - Counterfactual prediction: how would the assistant act on an edited input? Reward is the Brier score against the true rate from samples, so it rewards calibration.
   - Multiple choice: pick the assistant's real answer among answers from 4 other models.
4. OPD steps in both stages keep the assistant close to the original model (Sec. 2.2).

## Evidence
- **Main result (Sec. 4.1, Fig. 3):** on five held-out oversight tests, mean AUROC without reasoning: observer 0.907, honesty training 0.864, transcript monitoring 0.828, activation oracles 0.796 ([arXiv abstract](https://arxiv.org/abs/2611.23365)). Gains are largest on sycophancy and value leakage. On harm-pressure lies the observer is slightly below the best baseline.
- **Separate role helps:** the same training on the assistant role, in the first person, gives 0.877, below 0.907 (Sec. 4.1).
- **Weights matter:** larger models from other families (Inkling-Small, Nemotron 3 Super) trained on the same data reach only 0.684 and 0.647 (Sec. 4.1).
- **Data mix:** equal mix 0.904; behavior-prediction only 0.878; hidden-trait only 0.890 (Sec. 4.1).
- **With reasoning (Sec. 4.2):** RL raises reasoning AUROC to 0.823, about equal to a much larger outside monitor, GLM-5.3 (0.822). Reasoning length grows from 600 to 1,700 tokens. Reasoning scores are lower than log-probability scores.
- **Side effect (Sec. 4.3):** after observer training, the assistant itself is easier to monitor. Asking the assistant directly goes from 0.776 to 0.892. The cause is not clear; the authors give three possible explanations.
- Evaluation sizes (Table 1): sycophancy 1,500; harm-pressure 146; reward hacking 40; WeirdChat 200 + 200; value leakage 262.

## Limits / what they didn't show
- **Introspection or modeling?** The authors say it themselves (Sec. 6): the observer is trained only on visible behavior. It may model the assistant from outside patterns. Weight sharing helps, but they do not show the observer reads internal states that are absent from the outputs. No state injection test like [[Models sometimes notice injected thoughts (Lindsey 2025)]].
- The cross-model control uses different, larger models. A same-family model of the same size, without shared weights, would be a cleaner control [our concern, not in the paper].
- One model; evaluation transcripts without reasoning; some sets are small (40 items for reward hacking) (Sec. 6.1).
- Binary tasks only; free-form answers not checked.
- The observer is never used to control the assistant. The authors advise against using its reports as a training signal, because the assistant could learn to evade it (Sec. 6).

## Relevance to taste-lab
**Relevance 3.** Section 3, monitoring.
- **Grounded test** ([[Four tests for own taste]]): the "own-weights advantage" (0.907 vs 0.684) is the kind of control the grounded test needs. It answers part of the doubt in [[Introspection claims fail basic checks (Singh 2026)]] for behavior, not for internal states.
- **Monitor vs control:** it is a strong monitor with no control. Our loop needs the step it avoids.
- **Threat for the persist stage:** the authors warn that training on the observer's own verdicts may teach evasion. This is the same risk as judge hacking in [[Self-judge training makes wrong look right (Zhou 2026)]].
- **What would weaken it for us:** if a same-size, same-family model without shared weights matched the observer, "privileged access" would shrink to "more data about this model".

## Steal this
- The "verified against sampled behavior" reward: answers about the self are scored by what the model actually does, not by a human label.
- The cross-model control: same training data, different weights. Any self-monitoring claim in the review should be judged by whether it has this control.
- The observer role as a design: a meta level that shares weights but has its own channel.

## Harshit's notes
<!-- yours -->
