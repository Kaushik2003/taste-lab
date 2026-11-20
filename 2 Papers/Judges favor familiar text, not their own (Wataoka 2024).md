---
type: paper
title: "Self-Preference Bias in LLM-as-a-Judge"
status: skimmed
arxiv: 2410.21819
url: https://arxiv.org/abs/2410.21819
authors: Koki Wataoka, Tsubasa Takahashi, Ryokan Ri
year: 2024
venue: NeurIPS 2024 workshop (arXiv v2 Jun 2025)
relevance: 3
section: 7
tier: deep
tests: [divergent]
components: [valence, anchor]
tags: [type/paper, section/7, test/divergent, component/valence, component/anchor, status/skimmed, relevance/3, question/Q1, question/Q3, role/threat, self-preference, perplexity, familiarity, llm-judge, typicality]
links: ["[[Four tests for own taste]]", "[[Field map - Taste and new ideas]]", "[[Models recognize and favor their own text (Panickssery 2024)]]", "[[Models share one taste for text (Zatuchin 2026)]]", "[[Easy-to-process things feel beautiful (Reber 2004)]]", "[[Trained confidence tracks consistency, not accuracy (Yax 2026)]]", "[[Q1 Does the model sense code quality]]", "[[Anchor against collapse]]"]
---

# Self-preference bias in LLM-as-a-judge: it is familiarity

**One line:** Language model judges give higher scores to answers that have low perplexity for them, whether or not they wrote them. Self-preference appears because a model's own text is the most familiar text to it.

Source: [arXiv 2410.21819](https://arxiv.org/abs/2410.21819) (v1 29 Oct 2024, v2 Jun 2025). Full HTML of v1 read for Sections 4 to 7. Workshop venue from search results [unverified].

**Words used here:**
- **Perplexity:** how surprised a model is by a text. Low perplexity means the text is easy to predict, so familiar to that model.
- **Equal opportunity bias (their metric):** the gap in how often the judge picks its own answer when humans preferred it versus when humans did not. 0 means no bias.
- **Chatbot Arena:** a public data set of about 33,000 chats with human pairwise votes.

## Claim
Self-preference is real and large for GPT-4. Its cause is perplexity: judges favor low-perplexity text more than humans do, and the effect is about the same for self-written and other-written text ([arXiv](https://arxiv.org/abs/2410.21819), Abstract, Sec. 5).

## Mechanism
1. Score each judge's pairwise choices on Chatbot Arena against human votes. Swap positions and average to reduce position bias (Sec. 4.2).
2. Compute the equal-opportunity bias for eight judges (Sec. 4.1, 4.3).
3. For six open models, compute each judge's perplexity on both answers. Plot how often the judge picks the lower-perplexity answer, compared with humans, and separately for self-written and other-written answers (Sec. 5).

## Evidence
- GPT-4 has the largest bias: it picks its own answer 94.5% of the time when humans liked it and 42.5% when humans did not, a gap of 0.520 (Sec. 4.3).
- Vicuna-13b and Koala-13b also show significant bias. Three weaker models underrate their own answers (Sec. 4.3).
- Most judges favor lower-perplexity answers. Four of them do so more strongly than humans (Sec. 5, Fig. 3).
- For most models, the preference for low perplexity is about the same for self-written and other-written text (Sec. 5, Fig. 4).
- Models assign lower perplexity to their own outputs (Sec. 5, Fig. 5).

## Limits / what they didn't show
- No perplexity for GPT-4 or GPT-3.5, so the perplexity analysis excludes the judge with the largest bias (Sec. 5).
- Correlational. No manipulation of perplexity with content held fixed.
- Exact perplexity values are only in figures. The figure caption and the text disagree on which models are excluded (Sec. 5).
- A later paper argues that a judge scoring its own output higher is not always bias, because the output may be better ([arXiv 2508.06709](https://arxiv.org/abs/2508.06709)) [abstract only].

## Relevance to taste-lab
**Relevance 3. Section 7, the Divergent test. Threat.**
- **Threat to "own taste":** if self-preference is familiarity, a growing own-model premium after self-training may just mean the model's text became more typical for it. That is the sharpening that comes before collapse ([[Self-reward sharpens then collapses (He 2026)]]).
- **Threat to the evaluation signal:** a valence readout may track perplexity. The kill line in Question 1, does the model sense code quality ([[Q1 Does the model sense code quality]]), already controls for perplexity. This paper is the citation for why.
- **Pattern:** this joins [[Trained confidence tracks consistency, not accuracy (Yax 2026)]] and [[Easy-to-process things feel beautiful (Reber 2004)]]. In humans and in models, "good" may partly mean "easy to process".
- **Tension** with [[Models recognize and favor their own text (Panickssery 2024)]], which puts the cause in self-recognition. Both can hold: own text is both recognizable and low perplexity.

## Steal this
- Report self-preference against a human reference, not as a raw rate.
- Split the judge's choices by perplexity and by authorship. Partial out perplexity before any own-model premium is claimed.

## Harshit's notes
<!-- yours -->
