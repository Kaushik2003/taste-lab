---
type: paper
title: "Eliciting Research Taste in LLMs through Future Research Direction Choice"
status: skimmed
arxiv: 2611.19794
url: https://arxiv.org/abs/2611.19794
authors: Dhruv Trehan, Paras Chopra (Lossfunk)
year: 2026
venue: preprint
relevance: 3
section: 7
tier: deep
tests: [divergent, stable]
components: [valence]
tags: [type/paper, section/7, test/divergent, test/stable, component/valence, status/skimmed, relevance/3, thread/T1, taste, research-taste, measurement, divergence, stability, position-bias]
links: ["[[four-taste-tests]]", "[[landscape-taste-open-endedness]]", "[[2026-zatuchin-shared-taste-model-text]]", "[[code-quality-signal-T1]]", "[[valence-readout]]"]
---

# Eliciting Research Taste in LLMs through Future Research Direction Choice

**One line:** A small pairwise test (author's next step vs. a plausible alternative, shown in both orders) separates a model's real preference from position noise, and finds that models prefer the non-author option consistently in 15 to 36% of cases, often in the same direction as other models.

## Claim
Research taste can be measured as a behavioral preference, without treating any answer as correct. When a model picks the non-author direction in both option orders, that is a "stable divergence": a content-level preference, not a position artifact. These divergences survive prompt changes and are partly shared across model families ([arXiv 2611.19794](https://arxiv.org/abs/2611.19794), abstract and Sec. 3).

## Mechanism
- **Items.** 19 ML papers from Dec 2025 to Feb 2026 (after the evaluated models' stated cutoffs). Claude Sonnet 4.5 extracts the research goal, tested hypotheses with key results, and the authors' stated future work, then rewrites each future-work item into a neutral one-sentence direction (Sec. 2).
- **Distractors.** Future-work items from the 5 most similar papers (text-embedding-3-small), length within 0.75 to 1.25x of the author option, filtered by an LLM judge for "distinct" and "plausible". 80 pairs survive.
- **Both orders.** Each pair is shown as A/B and B/A at temperature 0, one sample each (160 prompts per model).
- **Three outcomes per pair:**
  - *Author alignment:* picks the author option in both orders.
  - *Stable divergence:* picks the distractor in both orders.
  - *Unstable choice:* the pick follows position. Random baseline is 25 / 25 / 50%.
- **Robustness checks:** similarity control (author option is more context-similar in 80% of pairs), four prompt ablations (no role, no research goal, reframed task, "what would the authors pick?"), inter-model agreement over all 28 model pairs, and a five-category label on what the model moves toward (Sec. 3.3 to 3.5).

## Evidence
- 8 models (Claude Opus 4.5 and Haiku 4.5, Gemini 3 Pro and Flash, GPT-5.2 Pro, GPT-OSS-120B, Qwen3 Max Thinking, Llama 4 Maverick). Author alignment 45.0 to 67.5%, stable divergence 15.0 to 36.2%, unstable 12.5 to 28.7% (Table 2).
- 45 of 80 pairs produce stable divergence in at least one model, 24 in at least four models, 3 in all eight (Table 3). 169 divergence events in total.
- 76.9% of divergences happen where the author option was *more* similar to the context, so a similarity heuristic does not explain them (Table 4).
- Under the four prompt ablations, 66.9 to 80.5% of divergences are kept. When they break, they mostly become position-unstable (17.8 to 26.0%), and rarely flip to the author option (1.8 to 7.1%) (Table 5). Under "predict the authors' choice", 72.6% are kept and 7.0% flip (Table 7).
- Mean inter-model agreement 61.9%. GPT-5.2 Pro and GPT-OSS-120B share 26.2% stable divergence vs. a 15.6% mean (Table 9). So part of the "taste" is family-level.
- Divergences move mostly toward scaling/generalization, and trade infrastructure for method (55 of 128 cross-category events) (Sec. 3.5).
- Human pilot: 10 people, 108 responses on 23 pairs, 61.1% author choice. Humans saw one order only, so they are not directly comparable (Sec. 3.4).

## Limits / what they didn't show
- Only 80 pairs from 19 papers. Single sample per order at temperature 0, so "stable" means stable across two orders and four prompts, not across samples or temperatures (Sec. 2, Sec. 5).
- One model (Sonnet 4.5) does all extraction, rewriting and distractor judging, which can bias the item set (Sec. 5).
- No internal signal at all. They leave log-probabilities and interpretability to future work (Sec. 2).
- Nothing on whether the divergent preference is *better*, or whether the model would act on it in a real loop.
- Human baseline is small and uses a different protocol.

## Relevance to taste-lab
- **Divergent + Stable tests.** This is the most direct published operationalization of our tests 1 and 2 ([[four-taste-tests]]). The three-outcome split is cheap and fits code readability almost unchanged: two passing solutions to one problem, one preferred by human raters and one not, shown in both orders.
- **Threat to the word "own".** Divergence from humans is partly shared across models (Table 9). A divergent preference may be a shared model-family taste, not a self-originated one. We need the cross-model test from [[2026-zatuchin-shared-taste-model-text]] on top.
- **Gap we fill.** No grounding (test 3) and no self-reinforcement (test 4). Our probe-based readout in [[code-quality-signal-T1]] could ask: does the valence projection predict which pairs end up stable-divergent vs. unstable?
- **Prior-art check.** A: no (behavioral choice only, no internal signal, no steering). B: no.

## Steal this
- The **author alignment / stable divergence / unstable choice** triple, with both-order presentation. Code, items and all model responses: [github.com/Lossfunk/research-taste-eval-v1](https://github.com/Lossfunk/research-taste-eval-v1).
- The ablation ladder (no role, no goal, reframed task, "predict the humans") as our Stable-test battery, plus persona swaps.
- Report "became unstable" separately from "flipped to human": the paper shows these are different failure modes.

## Harshit's notes
<!-- yours -->
