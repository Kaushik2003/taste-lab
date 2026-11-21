---
type: paper
title: "Metacognitive Capabilities of LLMs: An Exploration in Mathematical Problem Solving"
status: skimmed
arxiv: 2405.12205
url: https://arxiv.org/abs/2405.12205
authors: Aniket Didolkar, Anirudh Goyal, Nan Rosemary Ke, Siyuan Guo, Michal Valko, Timothy Lillicrap, Danilo Rezende, Yoshua Bengio, Michael Mozer, Sanjeev Arora
year: 2024
venue: NeurIPS 2024
relevance: 2
section: 2
tier: deep
tests: []
components: [monitoring]
tags: [type/paper, section/2, status/skimmed, relevance/2, role/prior-art, metacognition, skill-labels, math-reasoning, prompting]
links: ["[[Metacognition - watch and control yourself]]", "[[Models mostly know what they know (Kadavath 2022)]]"]
---
# Metacognitive Capabilities of LLMs: An Exploration in Mathematical Problem Solving (Didolkar et al., 2024)

**One line:** GPT-4 can name the skill a math problem needs, cluster those names into interpretable families, and presenting the right skill label at solve time measurably improves reasoning.

## Claim
LLMs possess metacognitive *knowledge* - knowledge of their own reasoning procedures - and it is usable: skill labels assigned by the model are meaningful for its own downstream problem solving.

## Mechanism
- Prompt-guided interaction: the model assigns skill labels to GSM8K/MATH training questions, then semantically clusters them into coarse, human-interpretable skill families.
- At test time the solver sees the skill list, identifies the relevant skills, then solves with them in context.

## Evidence
- Skill-conditioned solving improves accuracy over unlabeled baselines [unverified: delta].
- The coarse clusters are interpretable to humans.

## Limits / what they didn't show
- Metacognitive knowledge about *procedures*, not monitoring of *states*: no online readout of how a solution is going.
- GPT-4-centric; unclear how much transfers to open models.

## Relevance to taste-lab
The "name your own skills" result is the declarative half of metacognition (knowledge *of* cognition) as opposed to our control half (regulation *of* cognition). Useful in section 2 to split the two senses, and a baseline capability any architecture with a persistent self-state should also have.
- Prior-art check: **A partial** (declarative self-knowledge only). **B no.**

## Steal this
- Skill-label clustering as a cheap way to build a self-described task taxonomy for the controller's selection signal.

## Kaushik's notes
<!-- yours -->
