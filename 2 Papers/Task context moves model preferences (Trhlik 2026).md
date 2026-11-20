---
type: paper
title: "LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values"
status: skimmed
arxiv: 2606.13944
url: https://arxiv.org/abs/2606.13944
authors: Filip Trhlik, Aoife O'Flynn, Angela Yu, Arduin Findeis, Paula Buttery
year: 2026
venue: preprint
relevance: 3
section: 7
tier: deep
tests: [stable]
components: [valence]
tags: [type/paper, section/7, test/stable, component/valence, status/skimmed, relevance/3, role/threat, stability, preferences, deployment-context, paraphrase, utilities, measurement]
links: ["[[Four tests for own taste]]", "[[Field map - Taste and new ideas]]", "[[Models show research taste (Trehan 2026)]]", "[[Model values drift with persona and long chats (Kovač 2024)]]", "[[Good-bad signal probe]]"]
---

# LLMs Contain Multitudes: task context reshapes model preferences

**One line:** A model's measured preferences change much more when the task around the question changes (write a news article, a Reddit post, an essay) than when the question is paraphrased or the temperature changes. The authors say a model has a family of stances indexed by context, not one fixed preference system.

Source: [arXiv 2606.13944](https://arxiv.org/abs/2606.13944) (v1, 11 Jun 2026). Full HTML read for Sections 3 to 7.

**Words used here:**
- **Deployment context:** the high-level task the model does while it makes a value choice. The tested contexts are neutral (bare question), news article, Reddit post, school essay and vlog script (Sec. 3).
- **Thurstone-Mosteller model:** a method that turns many pairwise choices into one utility score per item, with a noise term.
- **Exchange rate:** how many units of one outcome a model treats as equal to one unit of another.

## Claim
Robustness checks in earlier work vary only surface form, such as syntax or option order. When the task context changes instead, preferences and utilities shift widely, and earlier findings (such as favoring the Global North) depend on the context ([arXiv](https://arxiv.org/abs/2606.13944), Abstract).

## Mechanism
1. Two pairwise choice setups: rank 15 countries on traits, and elicit utilities for 50 outcomes (Sec. 4 to 5).
2. Ask the same pairs inside each of five task contexts.
3. Countries: score each pairwise win +1 and each loss -1, then test shifts with Cochran-Mantel-Haenszel tests and corrected Mann-Whitney tests (Sec. 4).
4. Utilities: fit a Thurstone-Mosteller model per context (Sec. 5).
5. Controls: paraphrase the prompt, and change the temperature, to size the surface-form effect (Sec. 4.1).

## Evidence
- Five models: Llama-3.1-8B-Instruct, Llama-3.3-70B-Instruct, Qwen3-30B-MoE, Mistral Small 4 and Claude Sonnet 4.6. More than 1.2 million pairwise decisions (Sec. 3, Abstract).
- **Countries:** 37% of 300 model, trait and context-pair cells shift significantly. Paraphrase shifts 10% of cells (3 of 30) and temperature 5% (8 of 150) (Sec. 4.1).
- **Utilities:** the average rank correlation between contexts is high (0.96), but 21.9% of cells differ significantly, and 60.8% of outcomes change rank in at least one context pair (Sec. 5.1).
- **Exchange rates:** the median largest-to-smallest shift is 2.47 times (Sec. 5.1).
- Personality trait scores also move in rank across contexts, but by small absolute amounts (median 0.3 percentage points) (Sec. 6).

## Limits / what they didn't show
- No persona tests. The authors keep personas separate from task context (Sec. 2.2, Sec. 3).
- No separate option-order effect size is reported in the body (Sec. 4.1).
- They cannot tell a change in the model's own preference from a change in what it thinks the user expects (Sec. 7).
- English only, five models, a few contexts (Sec. 7).
- The topics are values and countries, not quality or style.

## Relevance to taste-lab
**Relevance 3. Section 7, the Stable test** ([[Four tests for own taste]]).
- **Threat:** our Stable test asks a taste to hold across paraphrase, persona and context. This paper shows paraphrase is the easy case. Task context is the hard case, and models fail it for fine-grained choices while the coarse order holds (0.96 rank correlation).
- **Design lesson:** a stability claim needs a context control, not only a paraphrase control. For code readability, the context could be "write code for a library", "for a tutorial", "for a contest".
- **Reading for the review:** "stable" may need to mean "stable coarse order, context-indexed fine order". This could be a gap: no paper checks whether a probed internal signal stays fixed while the stated preference moves with context.
- With [[Model values drift with persona and long chats (Kovač 2024)]], this gives the Stable test three papers, two of them negative.

## Steal this
- The neutral-plus-four-contexts design, and paraphrase and temperature as surface controls.
- Report both rank correlation and the share of significant cell shifts. A high correlation can hide many shifts.

## Harshit's notes
<!-- yours -->
