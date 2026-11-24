---
type: paper
title: "Mechanisms of Introspective Awareness"
status: skimmed
arxiv: 2603.21396
url: https://www.lesswrong.com/posts/BNMLtuDTNBwGHcnQX/mechanisms-of-introspective-awareness
authors: Macar et al. [unverified: full author list; read as the authors' LessWrong summary]
year: 2026
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, component/monitoring, status/skimmed, relevance/3, role/prior-art, introspection, abliteration]
links: ["[[Field map - Models read their own state]]", "[[Models sometimes notice injected thoughts (Lindsey 2025)]]", "[[Models cannot tell a real internal change from a fake one (Ferrara 2026)]]", "[[One direction controls refusal (Arditi 2024)]]", "[[2026-11-23 gap check]]"]
---
# Mechanisms of introspective awareness (Macar 2026)

**One line:** In Gemma3-27B, detection of injected concepts is real and has a traceable mechanism, and the model's refusal training hides most of it: removing the refusal direction from the weights raises detection from 10.8% to 63.8%.

Read 2026-11-24: the authors' summary post (TL;DR, main results, conclusion). The arXiv paper itself not read.

## Evidence
- Removing the refusal direction (the edit of [[One direction controls refusal (Arditi 2024)]]) raises the true detection rate from 10.8% to 63.8% and the introspection rate from 4.6% to 24.1%; false positives rise from 0.0% to 7.3%.
- A trained bias vector improves detection by 75% on held-out concepts.
- Contrastive preference training (DPO) is the main source of the ability; plain supervised fine-tuning does not produce it. The base model lacks the mechanism.
- A causal path is traced: one MLP at layer 45 produces the largest drop when ablated.
- The edited model loses coherence at high injection strength.
- Mostly Gemma3-27B, with support from Qwen3-235B and OLMo-3.1-32B.

## Limits
Detection of injected concepts, not of the model's own weight edit. The paper's controls against the "my input was changed" check of [[Introspection claims fail basic checks (Singh 2026)]] were not read.

## Relevance to taste-lab
Two points. (1) The field disagrees: this positive result at 27B stands against the null at 15B and below in [[Models cannot tell a real internal change from a fake one (Ferrara 2026)]]. (2) A weight edit changes the model's ability to report on itself. So an experiment that edits a model and then asks it what changed must separate "the edit changed the preference" from "the edit changed the reporting".
