---
type: paper
title: "Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement"
status: skimmed
arxiv: 2402.11436
url: https://arxiv.org/abs/2402.11436
authors: Wenda Xu, Guanglei Zhu, Xuandong Zhao, Liangming Pan, Lei Li, William Yang Wang
year: 2024
venue: ACL 2024
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing, divergent]
components: [anchor, valence]
tags: [type/paper, section/6, test/self-reinforcing, test/divergent, component/anchor, component/valence, status/skimmed, relevance/3, question/Q3, role/threat, self-bias, self-refine, self-rewarding, fluency, external-feedback]
links: ["[[Field map - Limits of self-learning]]", "[[Four tests for own taste]]", "[[Anchor against collapse]]", "[[Self-judge training makes wrong look right (Zhou 2026)]]", "[[Models recognize and favor their own text (Panickssery 2024)]]", "[[Judges favor familiar text, not their own (Wataoka 2024)]]", "[[Q3 Can self-learning avoid collapse]]"]
---

# Pride and Prejudice: self-refinement amplifies self-bias

**One line:** When a model critiques and rewrites its own output in a loop, its self-scores rise faster than true quality, so its bias toward its own work grows each round. The text gets more fluent, not better. Larger models and accurate outside feedback reduce the effect.

Source: [arXiv 2402.11436](https://arxiv.org/abs/2402.11436), [ACL 2024](https://aclanthology.org/2024.acl-long.826). Full HTML of v2 read for Sections 3 to 5.

**Words used here:**
- **Self-refine:** the model writes an answer, gives itself feedback, and rewrites. A rewrite is kept only if the self-score goes up (Sec. 3.1).
- **Self-bias (their bias statistic):** the average gap between the model's score for its own output and the true quality score. Positive means the model overrates itself (Sec. 3.2).
- **Distance skewness:** how one-sided the gaps are, from 0 (symmetric) to 1 (all on one side) (Sec. 3.3).

## Claim
Self-bias exists in all six tested models, and self-refinement amplifies it. The loop optimizes for false positive "improvements" rather than true quality ([arXiv](https://arxiv.org/abs/2402.11436), Sec. 1, Sec. 4).

## Mechanism
1. Run self-refine for up to 10 rounds on translation (four low-resource pairs from Flores-200), constrained generation (CommonGen Hard) and math (MATH), 100 examples each (Sec. 4.1).
2. Compare the model's self-score with an outside quality score (BLEURT mapped to an error scale, and human ratings).
3. Track bias and skewness over rounds, and over candidate pool size in a self-rewarding (pick the best of k by self-score) setup (Sec. 4.2, 4.4).
4. Test fixes: an outside feedback model (InstructScore) and larger model size (Sec. 5).

## Evidence
- Models: GPT-4, GPT-3.5-Turbo, Gemini, LLaMA2-7B, Mixtral 8x7B, DeepSeekMoE 16B (Sec. 4.1).
- Over 10 rounds with human evaluation, GPT-4's bias rises from 8.06 to 14.6 (skewness 0.452 to 0.692). Gemini rises from 9.62 to 17.6 (Sec. 4.2, Table 1).
- In the best-of-k setup, DeepSeekMoE's bias rises from 14.8 at k = 1 to 18.5 at k = 32 (Sec. 4.4, Table 3). Picking the top candidate by self-score amplifies the bias.
- Fluency and understandability rise across rounds, but quality does not (Sec. 4.3).
- After models paraphrase text, all of them favor their own paraphrases more (Sec. 4.3). The bias follows the model's own style.
- Outside feedback lowers bias and gives real quality gains. A 70B model's bias stops growing after round 5, while 7B and 13B models keep growing (Sec. 5). Exact values are only in figures.

## Limits / what they didn't show
- 100 examples per task, and translation dominates the numbers.
- No weight updates: the loop runs at inference only, so it shows amplification at the reasoning level, not after training.
- The authors leave open whether models also favor models that share their training data or family (Limitations section).

## Relevance to taste-lab
**Relevance 3. Section 6, limits. Threat to the Self-reinforcing test and to Question 3, can self-learning avoid collapse ([[Q3 Can self-learning avoid collapse]]).**
- This is the reasoning-level version of sharpen-then-collapse. Selecting by one's own score inflates that score and moves outputs toward one's own style.
- Our loop's control step at the reasoning level (best-of-n by own evaluation) is exactly the setup that amplifies bias here (best-of-k).
- **The style result matters most.** Self-bias grows toward the model's own style, and readability is a style. A rising own-model premium could be this bias, not taste.
- **Support for the anchor:** outside feedback that is accurate stops the growth ([[Anchor against collapse]]). This fits the pattern that every working loop has a hard outside check.

## Steal this
- The bias and distance-skewness pair, tracked per round.
- Measure bias against pool size k in best-of-k selection.
- The paraphrase test: rewrite the same content in the model's style and check if the score moves.
- Code and data: [github.com/xu1998hz/llm_self_bias](https://github.com/xu1998hz/llm_self_bias) [link from search results, not opened].

## Harshit's notes
<!-- yours -->
