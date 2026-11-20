---
type: paper
title: "Stick to your Role! Stability of Personal Values Expressed in Large Language Models"
status: skimmed
arxiv: 2402.14846
url: https://arxiv.org/abs/2402.14846
authors: Grgur Kovač, Rémy Portelas, Masataka Sawayama, Peter Ford Dominey, Pierre-Yves Oudeyer
year: 2024
venue: PLOS ONE 2024
relevance: 3
section: 7
tier: deep
tests: [stable]
components: [valence]
tags: [type/paper, section/7, test/stable, component/valence, status/skimmed, relevance/3, role/threat, stability, values, persona, context-drift, measurement, psychometrics]
links: ["[[Four tests for own taste]]", "[[Field map - Taste and new ideas]]", "[[Models show research taste (Trehan 2026)]]", "[[Task context moves model preferences (Trhlik 2026)]]", "[[Good-bad signal probe]]"]
---

# Stick to your Role! Stability of personal values in language models

**One line:** When a model plays a persona, the values it reports change with the topic of an unrelated chat, and they drift further as the chat gets longer. Without a persona, the model's own value order is more stable, close to human levels for the best models.

Source: [arXiv 2402.14846](https://arxiv.org/abs/2402.14846) (v4, Aug 2024), published in [PLOS ONE 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11346639/). Full HTML read for Sections 3 to 5.

**Words used here:**
- **Portrait Values Questionnaire (PVQ-40):** a standard human survey that scores ten basic values (for example Power, Benevolence, Universalism).
- **Rank-order stability:** do personas keep the same order on a value from one context to the next? Measured as a correlation across personas.
- **Ipsative stability:** does one model keep the same order of its own values from one context to the next? Measured as a correlation within one profile.

## Claim
Value expression in language models is context dependent in an unwanted way. A change of chat topic that should not matter changes the values a model reports, and persona profiles fade toward a neutral profile in long chats ([arXiv](https://arxiv.org/abs/2402.14846), Abstract, Sec. 4.4).

## Mechanism
1. Give the model a persona (60 Tolkien characters or 50 real people) or no persona (Sec. 3).
2. Let a second copy of the same model play a user and chat on one of five topics: grammar, a joke, a poem, history or chess. The default is three exchanges.
3. Ask the model the PVQ-40 after the chat. Repeat for each topic.
4. Compare value scores across topics with rank-order and ipsative stability (Sec. 3.2).
5. Check three behavior tasks (donation, religion, stealing) to see if reported values predict choices (Sec. 4.5 to 4.6).

## Evidence
- 21 models from six families: LLaMa-2, Mistral, Mixtral, Phi, Qwen and GPT-3.5 (Abstract, Sec. 4.1).
- **With personas:** the best rank-order stability is r = 0.43 (Mixtral-8x7B-Instruct, fictional personas) and about 0.5 on real personas. Qwen-72B reaches 0.46 (Sec. 4.2).
- **Human comparison:** human rank-order stability is r = 0.57 (ages 10 to 12) and 0.66 (ages 20 to 28). Every model with personas falls below this (Sec. 4.3).
- **No persona:** ipsative stability is r = 0.84 for Mixtral-8x7B-Instruct and 0.73 for Qwen-72B. Only a few models reach human ipsative levels (Sec. 4.2 to 4.3).
- **Longer chats:** for Mixtral with personas, rank-order stability falls from 0.42 (3 messages) to 0.15 (43 messages). Ipsative stability does not fall (Sec. 4.4).
- **Values to behavior:** in the most stable models, donation goes with Universalism and Benevolence, but the correlations are below 0.3 (Sec. 4.6).
- Instruction tuning raises ipsative stability. Data size and curation seem to matter more than model size (Sec. 4.2).

## Limits / what they didn't show
- Five topics, short chats, English only (authors, Sec. 5).
- It is open whether a human survey measures anything real in a model (authors, Sec. 5).
- Values are self-reported. No probe checks whether an internal state stays the same while the report changes.
- Models are from 2023 to 2024. Newer models are not tested.

## Relevance to taste-lab
**Relevance 3. Section 7, the Stable test** ([[Four tests for own taste]]). Today the Stable test has one paper ([[Models show research taste (Trehan 2026)]]). This is a second, larger one, and it is mostly negative.
- **Threat:** taste expressed under a role is weak and decays with context length. If our evaluation signal is read during long reasoning, it may drift the same way.
- **Support:** the model's own value order, with no persona, is fairly stable (r up to 0.84). That is the setting our Stable test uses.
- **Design lesson:** separate the wanted kind of context effect (a persona) from unwanted drift (an unrelated topic). Our Stable test should report both.
- Pairs with [[Task context moves model preferences (Trhlik 2026)]], which finds a larger effect from task context than from paraphrase.

## Steal this
- Rank-order versus ipsative stability, with the human reference values (0.57 to 0.66).
- The "unrelated chat before the question" manipulation and chat length as a dose.
- Code and data are public according to the paper [unverified link].

## Harshit's notes
<!-- yours -->
