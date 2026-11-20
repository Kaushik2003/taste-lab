---
type: paper
title: "Disambiguating Moral Circuits and Moral Features in Language Models: Moral content, normative judgment or cue words? Evidence from 14 models"
status: skimmed
arxiv: 2611.21705
url: https://arxiv.org/abs/2611.21705
authors: Davide Liga, Liuwen Yu, Matteo Magnini
year: 2026
venue: arXiv preprint
relevance: 2
section: 4
tier: skim
tests: [grounded, stable]
components: [valence]
tags: [type/paper, section/4, test/grounded, test/stable, component/valence, status/skimmed, relevance/2, question/Q1, evaluation-circuit, attention-heads, sae, cue-word-confound, aesthetics]
links: ["[[Field map - Models judge good and bad]]", "[[Good-bad signal probe]]", "[[Value axis - model knows it is on track (Jiang 2026)]]", "[[Emotion directions drive choices in Claude (Anthropic 2026)]]", "[[Introspection claims fail basic checks (Singh 2026)]]", "[[Q1 Does the model sense code quality]]"]
---

# One evaluation circuit for all norms

**One line:** In 14 open models, the attention heads that change a moral verdict are part of one general "evaluation circuit" that also handles prudence, etiquette, aesthetics and evidence. The sparse features people find often respond to the word "morally", not to the content.

**Why it matters to us:** A single circuit for all good-bad judgments, including aesthetics, is a candidate home for a valence readout. The cue-word result is a warning for how we would find one.

Source: [arXiv 2611.21705](https://arxiv.org/abs/2611.21705) (16 Nov 2026). Abstract only; full text not read.

**Words used here:**
- **Minimal pair:** two short phrases that differ in one thing only.
- **SAE feature:** a direction found by a sparse autoencoder, a tool that splits hidden states into many simpler parts.

## Claim
Components that drive moral answers serve normative judgment in general, not moral content, and the SAE features found mostly follow a cue word ([abstract](https://arxiv.org/abs/2611.21705)).

## Mechanism
- 227 minimal pairs, checked by five annotators. Pairs differ in a moral standard, another norm (prudence, etiquette, aesthetics, evidence) or a plain descriptive quality. Shown with and without the word "morally".
- 14 models (Llama, Gemma, Qwen, 1B to 14B, base and instruction-tuned). Head ablation, SAE features, and a linear direction for the norm category.

## Evidence
- The heads carry the same share of the effect for moral and for other normative pairs: ratio 1.00 (97.5% interval 0.92 to 1.07) with the cue word, 0.90 (0.84 to 0.96) without it ([abstract](https://arxiv.org/abs/2611.21705)).
- On 400 ETHICS scenarios, removing these heads takes away 37 to 39% of the gap between acceptable and unacceptable cases, against 1 to 3% for ten random heads.
- The norm category is linearly readable. Removing its direction weakens the moral verdict by a few percent in eight models.

## Limits / what they didn't show
- Models up to 14B only. Short phrases, not long work like code.
- "Aesthetics" here is a norm label in a phrase, not a judgment of a real artifact.

## Relevance to taste-lab
**Relevance 2. Section 4.**
- Supports the idea of a domain-general good-bad signal, which a valence probe needs ([[Good-bad signal probe]]).
- Threat to method: a readout found with labelled prompts may track a cue word. Q1 (does the model sense code quality?) must use prompts with no evaluative words and compare against an input-only probe, as [[Introspection claims fail basic checks (Singh 2026)]] also warns.

## Steal this
- Minimal pairs across norm types as a test of whether a valence direction is general or specific.
- The "with and without cue word" control.

## Harshit's notes
<!-- yours -->
