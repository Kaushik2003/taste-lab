---
type: paper
title: "Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories"
status: read
arxiv: 2606.03979
url: https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/
authors: Ali Behrouz, Farnoosh Hashemi, Adel Javanmard, Vahab Mirrokni
year: 2026
venue: arXiv preprint (2 June 2026); Google Research blog (27 October 2026)
relevance: 3
section: 5
tier: deep
tests: [self-reinforcing]
components: [consolidation, anchor]
tags: [type/paper, section/5, test/self-reinforcing, component/consolidation, status/read, relevance/3, role/prior-art, role/threat, continual-learning, self-modification, sleep]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[Nested Learning - a model that learns its own update rule (Behrouz 2025)]]", "[[Titans - a memory that learns from surprise at test time (Behrouz 2025)]]", "[[SEAL - models write their own training data (Zweiger 2025)]]", "[[Self-judged nightly learning rises then decays (Kongsilp 2026)]]", "[[2026-11-23 direction critique]]"]
---
# Language models need sleep (Behrouz 2026)

**One line:** A model alternates between a wake phase, where it takes in new information, and a sleep phase, where it distills that information into small new blocks of long-term weights and then fine-tunes on its own synthetic "dreams". It forgets less than the baselines and gains a few points over them. Every update is by gradients, and outside task scores decide which dreams count.

Read in full on 2026-11-24 at the user's request: arXiv HTML, Sections 1 to 5 and Appendices A and B ([arXiv 2606.03979](https://arxiv.org/abs/2606.03979)), plus the [Google Research blog post](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) of 27 October 2026. Numbers inside figures (class-incremental learning, translation, BABILong) are not in the text and are not checked. A title note says a version has been on OpenReview since September 2025.

**Words used here:**
- **Continuum memory system:** a chain of MLP blocks, each updated at its own rate. Fast blocks are short-term memory, slow blocks long-term (from [[Nested Learning - a model that learns its own update rule (Behrouz 2025)]]).
- **Low-rank expert:** a small added block of weights (two thin matrices), the same kind of object as a LoRA adapter.
- **Distillation:** training a student model to match a teacher model's outputs.

## Claim
A continual learner has no training time and test time, only a wake phase and a sleep phase. Sleep has two stages: memory consolidation, then "dreaming" for self-improvement (Sec. 1, Sec. 3.1).

## Mechanism
1. **Parameter expansion (Sec. 3.2).** Before a fast block is updated, a new low-rank expert is switched on in the next slower block. In practice the extra parameters exist from the start and are masked until used (Sec. 3.3, implementation note). The experiments use 5 added MLP blocks of dimension 64 (App. B).
2. **Knowledge seeding (Sec. 3.3).** The model before the update is the teacher; the model with the update and the new expert is the student. Only the new expert is trained, with on-policy distillation plus a reinforcement-learning reward for imitating the teacher's samples. The reward mixes a frozen semantic-similarity reward model and an edit-distance term (Eq. 3 and 4). Then the fast block's old experts are reset.
3. **Dreaming (Sec. 3.4).** Built on [[SEAL - models write their own training data (Zweiger 2025)]]. The model generates m dreams (synthetic data) with the task context; each expert router also picks one random expert. Dreams are ranked by a gradient-based importance score; the top k plus a few random ones are kept. For each kept dream, a copy of the model is fine-tuned with LoRA, and the dream gets reward 1 if the fine-tuned copy scores better on the downstream task measure, else 0 (Eq. 5).

## Evidence
- **Models:** Llama-3B and Llama3-8B (continual learning), Qwen3-1.7B and Qwen3-8B (math), Llama-3.2-1B (ARC). These are pre-trained models with the memory blocks added, not models trained from scratch (Sec. 4.1, App. B).
- **Math, Qwen3-8B, average of 16 runs (Table 2):** base 73.8 / 68.1 / 42.4 on AIME-24 / AIME-25 / HMMT-25; fine-tuning 75.5 / 66.4 / 43.7; GRPO 76.4 / 68.1 / 44.9; on-policy self-distillation 76.6 / 67.4 / 45.1; Sleep 79.2 / 69.0 / 46.1. Without parameter expansion: 78.2 / 67.9 / 44.9 (Table 1).
- **New facts, SQuAD without the passage in context (Table 3):** base 31.9; SEAL 46.7 (one passage) and 43.2 (200 passages); Sleep 48.9 and 46.2. Without dreaming: 35.7 and 36.2. So the SEAL-style dreaming stage carries most of this gain; consolidation adds about 2 to 3 points over SEAL.
- **Few-shot ARC (Table 4, App. B.3):** Sleep 80% against SEAL 72.5%, on 8 held-out tasks with 5 dreams each. That is 40 trials, so the gap is about 3 trials [our arithmetic].
- **Continual learning (Sec. 4.1, figures only):** consolidation alone beats in-context learning, EWC and an external-learner method on three class-incremental text datasets. In continual translation of two unseen languages, the three-stage variant nearly keeps its single-language score, while fine-tuning and Cartridges forget at least one language.
- **Long context (App. B.2):** fine-tuned small models stay stable up to 10M tokens on BABILong; without fine-tuning all small models, including this one, drop a lot.
- **Cost (App. B.5):** per training step, plain fine-tuning is 4 times cheaper. To reach the same math score, fine-tuning needs 3.6 to 4.8 times more wall-clock time.

## Limits / what they didn't show
- **All updates are by gradients:** distillation, reinforcement learning and LoRA fine-tuning. Nothing is a direct weight edit.
- **Outside signals decide.** The dream reward is improvement on a downstream task measure (Eq. 5); the consolidation reward uses a frozen reward model. The model's own judgment of good or bad is not used.
- **No long life shown.** "Continual" means two languages in sequence and class-incremental streams. There is no run over many sleep cycles, unlike the year-long test in [[Self-judged nightly learning rises then decays (Kongsilp 2026)]].
- **Capacity is fixed in advance.** The new experts are pre-allocated and masked, so the number of consolidations is bounded by what was allocated [our reading of Sec. 3.3 and App. B].
- **Small margins, no error bars in the text.** Most gains over the best baseline are 1 to 3 points. No seeds or intervals are given in the tables.
- **Method details are thin.** The gradient-based importance score is defined only as "the gradient of the objective" (Sec. 3.4).
- **The theory in the blog post is not in this arXiv version** [as far as we found].
- No measurement of the model's preferences or values across cycles, and no test of whether the model can report what changed.
- The authors cite work showing that self-distillation can collapse or can suppress a model's stated uncertainty, with out-of-distribution drops of up to 40% (App. A.4, citing Kim et al. 2026 and He et al. 2026). The Kim paper is now read: [[Self-distillation removes expressed doubt and hurts reasoning (Kim 2026)]]. Its teacher sees the correct solution; the Sleep teacher is the model's own earlier state, so the result does not transfer directly.

## Relevance to taste-lab
The main rival route to "a model that keeps changing its own weights after deployment". After the full read:
1. **It is closer to LoRA-style adaptation than the blog suggests.** Small added low-rank blocks are trained by distillation, then LoRA fine-tuning on synthetic data. It is what the user's idea wants to avoid (training), made forgetting-resistant by adding capacity.
2. **It does not yet show long-run evolution.** Two sequential tasks and narrow benchmarks. The "evolves over time" question is open on this route too, only less so than for direct edits.
3. **The evaluation step is external and open.** A model that picks its own dreams by its own judgment, a check of preference drift across sleep cycles, and self-report of the change are all absent.
4. **A lead for the metacognition side:** the cited result that self-distillation suppresses stated uncertainty links self-training to a loss of metacognitive report. See [[Self-distillation removes expressed doubt and hurts reasoning (Kim 2026)]].

## Steal this
- The compute, consolidate, update order: build the new state, distill into fresh capacity, and only then apply the change.
- Separate "store new knowledge safely" from "improve on it" as two stages with different risks.
- The ablation that removes dreaming, as a template for showing which stage carries a gain.

## Harshit's notes
<!-- yours -->

## Log
- 2026-11-24: first version from the blog post and abstract only. Same day: rewritten after a full read of the arXiv HTML. Corrections to the first version: the method runs on pre-trained models with added blocks (not a new architecture from scratch); no run over many sleep cycles is shown; gains over the best baselines are 1 to 3 points; per step it costs 4 times more than fine-tuning.
