---
type: paper
title: "Identifying Introspection From the Inside"
status: skimmed
arxiv: 2610.07186
url: https://arxiv.org/abs/2610.07186
authors: David I. Atkinson, Dillon Plunkett, et al. [unverified: full author list]
year: 2026
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, evaluation]
tags: [type/paper, section/3, test/grounded, component/monitoring, status/skimmed, relevance/3, role/prior-art, introspection, preferences, self-report]
links: ["[[Field map - Models read their own state]]", "[[Models report preference weights trained into them (Plunkett 2025)]]", "[[Introspection needs a causal link to count (Comsa 2025)]]", "[[Four tests for own taste]]", "[[2026-11-23 gap check]]"]
---
# Identifying introspection from the inside (Atkinson 2026)

**One line:** A model trained only to make choices by hidden preference weights later starts to report those weights correctly, with no training on reports. This happens late, only in large models, and only when the preference is stored in early layers.

Read 2026-11-24: abstract, introduction, Sec. 3, Sec. 4, discussion, conclusion. Sec. 5 (attribution patching) not read.

## Mechanism
Setting of [[Models report preference weights trained into them (Plunkett 2025)]]: low-rank adapters train Qwen3 models (0.6B to 32B) to choose for 100 fictional characters, each with a 5-number preference vector. Two measures: decision performance (do choices follow the weights) and faithfulness (do stated weights match the weights the choices show).

## Evidence
- Decisions are learned fast at every size. Faithful self-report of the trained preferences appears only at 32B (Sec. 3).
- In the 32B model: at checkpoint 1000, decision performance is 0.82 and faithfulness about 0.25; at checkpoint 3000, 0.92 and 0.83 (Fig. 1, Sec. 3).
- 4B and 8B models end with **negative** faithfulness despite good decisions (Sec. 3).
- The faithful checkpoint responds to layer ablations 5 to 6 layers earlier than the unfaithful one. Training only the first 10 to 20 layers of the 40-layer Qwen3-14B makes its reports much more faithful (Sec. 4).
- Gemma-4: strong faithful self-report only at 31B (Sec. 4).
- Faithful adapters share more of their mechanism between deciding and reporting (Sec. 5, from the abstract).

## Limits (authors, Sec. 7)
Linear 5-number preferences, adapters not full models, one main model family; the method separates groups, not single models.

## Relevance to taste-lab
The most useful paper for "does the model notice that its preferences changed". It says the answer depends on (a) model size, about 30B and up, (b) where in the network the change is stored, and (c) how long training ran. A direct weight edit skips training, so its location is the main variable. Prediction to test: an edit in early or middle layers can reach the self-report; an edit near the output cannot. It also gives a test of grounding that does not read the report's content.
