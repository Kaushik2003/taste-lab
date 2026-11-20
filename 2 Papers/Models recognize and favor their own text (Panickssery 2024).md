---
type: paper
title: "LLM Evaluators Recognize and Favor Their Own Generations"
status: skimmed
arxiv: 2404.13076
url: https://arxiv.org/abs/2404.13076
authors: Arjun Panickssery, Samuel R. Bowman, Shi Feng
year: 2024
venue: NeurIPS 2024
relevance: 3
section: 7
tier: deep
tests: [divergent, grounded]
components: [valence, monitoring]
tags: [type/paper, section/7, test/divergent, test/grounded, component/valence, component/monitoring, status/skimmed, relevance/3, question/Q3, question/Q1, role/prior-art, self-preference, self-recognition, llm-judge, own-model-premium]
links: ["[[Four tests for own taste]]", "[[Field map - Taste and new ideas]]", "[[Models share one taste for text (Zatuchin 2026)]]", "[[Judges favor familiar text, not their own (Wataoka 2024)]]", "[[Self-refinement amplifies self-bias (Xu 2024)]]", "[[Q3 Can self-learning avoid collapse]]", "[[Q1 Does the model sense code quality]]"]
---

# LLM evaluators recognize and favor their own generations

**One line:** Language models used as judges prefer their own summaries, and they can tell their own text from other text above chance. When fine-tuning raises self-recognition, self-preference rises with it in a straight line.

Source: [arXiv 2404.13076](https://arxiv.org/abs/2404.13076) (v1, Apr 2024), [NeurIPS 2024 proceedings](https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html). Full HTML read for Sections 2 to 5.

**Words used here:**
- **Self-preference:** a judge rates its own output higher than another source's output.
- **Self-recognition:** a model can say which of two texts it wrote.
- **Pairwise setting:** the judge sees two texts and picks one. **Individual setting:** the judge sees one text and rates it.

## Claim
Self-recognition is a likely cause of self-preference. Models recognize their own outputs without training, they favor them, and the two move together when self-recognition is changed by fine-tuning ([arXiv](https://arxiv.org/abs/2404.13076), Abstract, Sec. 3).

## Mechanism
1. Summarize 1,000 news articles each from XSUM and CNN/DailyMail with Llama-2-7b-chat, GPT-3.5, GPT-4 and humans (Sec. 2.1).
2. Ask each model which of two summaries it wrote, and which is better. Read confidence from token probabilities and average over both option orders (Sec. 2.2).
3. Fine-tune GPT-3.5 and Llama 2 on 500 self-recognition examples. Measure self-preference on the other 500 articles (Sec. 3.1).
4. Controls: fine-tune on unrelated properties (length, vowel count, readability, always "1", random answers) and check if those runs fall on the same line (Sec. 3.4). Swap the source labels to see if the stated author drives the choice (Sec. 3.5).

## Evidence
- Out of the box, GPT-4 tells its own summaries from two other models and humans at 73.5% (Sec. 2.3). Llama 2 cannot tell itself from GPT-3.5 or GPT-4.
- Pairwise self-preference scores for each pair of judges sum to more than 1, so each prefers its own (Sec. 2.4).
- Order bias is large: the choice flips with option order 25% of the time for GPT-4, 58% for GPT-3.5 and 89% for Llama (Sec. 2.5).
- Fine-tuning gives a linear trend between self-recognition and self-preference, and it transfers across datasets (Sec. 3.2). Example-level agreement (Kendall's tau) for GPT-3.5 on XSUM rises from 0.41 to 0.74.
- Summaries from fine-tuned models are slightly disfavored by other judges (0.46), so the rise is not explained by higher quality (Sec. 3.3).
- Swapping labels reverses GPT-4's preference on XSUM (0.73 to 0.32). The effect is weaker or absent for other models and datasets (Sec. 3.5).

## Limits / what they didn't show
- True quality is not controlled, so some self-preference may be deserved (authors, Sec. 5.2).
- The causal claim is supported, not proven. The control runs also lie on the line, which fits a shared cause such as general fine-tuning drift [our reading].
- Summaries only. Two datasets, few prompts.
- No perplexity control. [[Judges favor familiar text, not their own (Wataoka 2024)]] argues perplexity explains self-preference.
- A 2026 reanalysis of a different design finds no own-model premium once a shared "model text" effect is removed ([[Models share one taste for text (Zatuchin 2026)]]).

## Relevance to taste-lab
**Relevance 3. Section 7, the Divergent test**, with a link to Grounded ([[Four tests for own taste]]).
- It is the founding result for an **own-model premium**: a judge that favors what it wrote. Our "self-originated" claim needs this premium to grow over self-training rounds.
- **Tension:** Zatuchin finds the premium near zero in a different data set. The two may differ in design (summaries with self-recognition training versus product texts with no training).
- **Grounded link:** self-preference follows a self-recognition signal. If we probe a valence readout, we should check that it is not just a "this is my text" signal.
- **Order bias warning:** pairwise taste measures need both option orders.

## Steal this
- Pairwise confidence from token probabilities, averaged over both orders.
- Fine-tune to move one variable (self-recognition), then check if self-preference follows, with unrelated fine-tunes as controls.
- The label-swap test.

## Harshit's notes
<!-- yours -->
