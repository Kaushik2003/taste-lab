---
type: paper
title: "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?"
status: read
arxiv: 2603.24472
url: https://arxiv.org/abs/2603.24472
authors: Jeonghye Kim, Xufang Luo, Minbeom Kim, Sangmook Lee, Dohyung Kim, Jiwon Jeon, Dongsheng Li, Yuqing Yang
year: 2026
venue: arXiv preprint, 25 March 2026 (Microsoft Research, KAIST, SK hynix, Seoul National University)
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing, grounded]
components: [monitoring, anchor]
tags: [type/paper, section/6, test/self-reinforcing, component/monitoring, component/anchor, status/read, relevance/3, role/threat, self-distillation, uncertainty, metacognition]
links: ["[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]", "[[Metacognition - watch and control yourself]]", "[[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]", "[[Self-reward sharpens then collapses (He 2026)]]", "[[One weight edit shifts a model's disposition (Fafuła 2026)]]", "[[Reasoning models show habits of mind (Dong 2025)]]"]
---
# Why does self-distillation (sometimes) degrade reasoning? (Kim 2026)

**One line:** When a model is trained to copy a version of itself that was shown the answer, it stops saying "wait", "hmm" and "maybe" while it reasons. Its answers get shorter and more confident, and on new maths problems it gets much worse.

Read 2026-11-24 at the user's request: Sections 1 to 7 and Appendices F, G, H, I, part of B. Not read: Appendices C, D, E, J, K. Numbers inside figures are quoted only where the text states them.

**Words used here:**
- **Self-distillation:** two copies of one model. The teacher copy sees extra information (here the correct solution). The student copy is trained to match the teacher's next-word predictions.
- **Epistemic verbalization:** the model writes its doubt into its reasoning. The paper counts 10 marker words: wait, hmm, perhaps, maybe, actually, alternatively, seems, might, likely, check (Sec. 3).
- **GRPO:** a standard reinforcement-learning method that rewards correct final answers.
- **SDPO:** an on-policy self-distillation method (Hübotter et al. 2026).
- **OOD (out of distribution):** test problems unlike the training problems.

## Claim
Self-distillation suppresses expressed doubt. That helps when the training tasks are few and similar, and hurts when the model must handle new kinds of problems (Abstract, Sec. 6).

## Mechanism
1. The more the teacher knows, the less doubt it writes. Same model, 100 problems: with no help, 13,054 tokens and 182.5 doubt words per answer; with the full solution in context, 1,873 tokens and 8.8 doubt words (Table 1).
2. The student copies this confident style, but at test time it does not have the solution. So it commits early and cannot recover (Sec. 2, Sec. 4).
3. The teacher disagrees with the student most at exactly the doubt words: 1.9 to 6.8 times the average divergence (App. F).

## Evidence
- **Fine-tuning on correct answers only (Table 2, DeepSeek-R1-Distill-Qwen-7B).** Trained on 800 correct answers written without help: AIME24 stays near the base (54.79 to 51.04). Trained on 800 correct answers written with the solution in view: AIME24 falls from 54.79 to 20.21, AIME25 from 37.92 to 12.71, AMC23 from 89.06 to 57.03, MATH500 from 92.19 to 65.52.
- **On-policy self-distillation (Sec. 5.1).** GRPO gives small gains (AIME24 54.7 to 56.0). SDPO with the full solution loses about 40% on AIME24 and about 15% on AMC23. With a weaker hint the loss is smaller but the model stays below base.
- **Qwen3-8B (Sec. 5.2, 5.3).** Same direction: SDPO removes more doubt words than GRPO and ends below the base model on AIME24.
- **Causal test (Sec. 5.4).** Penalizing only the 10 doubt words during GRPO gives shorter answers and lower scores, a weaker copy of the SDPO effect.
- **Feedback loop (Sec. 5.5).** If the teacher is updated during training, even slowly, the loss of doubt and of accuracy grows: a more confident student becomes a more confident teacher.
- **Internal uncertainty also falls (App. G).** Token-level entropy is 0.385 without help and 0.218 with the solution. After training: base 0.378, GRPO 0.401, SDPO 0.248. Doubt words sit at positions with about 3.5 times the average entropy.
- **A prompt does not fix it (App. H).** Telling the teacher to show its uncertainty raises doubt words from 8.8 to 31.4, still far below 182.5, and the performance loss stays.
- **Task coverage (Sec. 6).** With 1 to 128 training questions, SDPO learns fast and cuts length up to 8 times. At 512 questions it falls behind GRPO. On new benchmarks SDPO is below base at every size.

## Limits / what they didn't show
- Maths only. In chemistry, tool use and coding (other authors' results), the same method helps; the authors explain this by narrow task coverage, tested only on maths (Sec. 6.1).
- Models of 1.7B to 8B.
- "Doubt" is 10 marker words, checked against a language-model annotator. It is expressed doubt, not a full measure of metacognition.
- Internal uncertainty is token entropy, not a probe of hidden states.
- The teacher always sees a correct solution. The teacher in [[Sleep - a model consolidates memories into its weights (Behrouz 2026)]] is the model's own earlier state with no solution, so this result does not transfer to Sleep directly [our reading].

## Relevance to taste-lab
1. **Self-training can remove metacognitive behavior without touching the objective.** The loss function only asks for correct reasoning; the monitoring habit ("wait, is this right?") disappears as a side effect, and nothing in standard training penalizes its loss (Sec. 1). This is direct evidence for the review's claim that a self-improvement loop needs a check on the monitor itself.
2. **Expressed doubt is a cheap, countable metacognition readout.** It needs no probe and it predicts robustness here. It can serve as one measure of "did the model's self-monitoring change after a weight change".
3. **Two papers now show a weight change that thins doubt vocabulary:** this one by training, and [[One weight edit shifts a model's disposition (Fafuła 2026)]] by a direct edit [the link is our reading].
4. **The feedback loop is a warning for any repeated self-change:** each round's more confident model becomes the next round's standard. Same shape as [[Self-reward sharpens then collapses (He 2026)]].
5. Here expressed and internal uncertainty fall together (App. G). In Fafuła they come apart (stated doubt changes, behavior does not). So both must be measured.

## Steal this
- Count doubt words and token entropy before and after any weight change.
- The two-dataset design of Sec. 4: same model, both sets fully correct, only the amount of expressed doubt differs.
- The task-coverage sweep (1 to 512 questions) to show when a shortcut stops paying.

## Harshit's notes
<!-- yours -->
