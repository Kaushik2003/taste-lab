---
type: paper
title: "Can LLMs Introspect? A Reality Check"
status: skimmed
arxiv: 2605.26242
url: https://arxiv.org/abs/2605.26242
authors: Shashwat Singh, Tal Linzen, Shauli Ravfogel
year: 2026
venue: COLM 2026 (per arXiv comment)
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, role/threat, section/3, test/grounded, component/monitoring, status/skimmed, relevance/3, question/Q1, introspection, privileged-access, methodology]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]", "[[Models do not report injected pain (Ferrara 2026)]]", "[[Field map - Models read their own state]]"]
---

# Can LLMs Introspect? A Reality Check

**One line:** Two well-known results that say "LLMs can look inside themselves" fail simple checks: a probe that sees only the input does as well as the model's self-reports, and models stop "detecting" injected thoughts once "my input was changed" is an allowed answer.

**Why it matters to us:** This is the strongest warning against our idea. If our model says "I like this code" and a probe agrees, a reviewer will ask if a probe on the input text alone agrees just as well. For code that is likely, because readability is visible in the text.

**Words used here:**
- **Introspection:** a model reports on its own internal state.
- **Hidden numbers (activations):** the numbers the model computes inside each layer for each token.
- **Probe:** a small classifier that reads the hidden numbers and predicts a label.
- **Input-only probe (layer-0 probe):** a probe that reads only layer 0, the input word vectors (embeddings), before the model does any work. If it does as well as the model's self-report, the report may come from the input text, not from an inner state.
- **Residual stream:** the main path of hidden numbers that goes from one layer to the next.
- **Steering vector:** a direction added to the hidden numbers to push the model toward a concept.
- **PCA component:** a main direction of variation in the hidden numbers.
- **First-order and second-order:** a first-order state is the model's state about the task. A second-order state is a state *about* that first state.

## Claim
A test shows introspection only if it needs two things (Section 3):
1. **Privileged access:** you cannot get the answer from the input alone.
2. **Second-order computation:** the report comes from a representation *about* the first-order state. You can show this only with designs where the first-order and second-order explanations predict different results.

With these rules, current evidence does not show that LLMs watch their own thinking (metacognitive monitoring) ([arXiv](https://arxiv.org/abs/2605.26242)).

## Mechanism
They repeat three earlier experiments with stronger controls.
- **Ji-An et al. neurofeedback** ([2505.13763](https://arxiv.org/abs/2505.13763)): A probe (or PCA component) on the model's own hidden numbers labels some examples. The model sees these labeled examples in its prompt and must predict the label for a new input. Controls: (a) Shuffle (permute) the labels before training the probe, so the label no longer matches the meaning of the text. (b) Train a linear probe on **layer-0 input embeddings only** to predict the same labels. Models: Llama-3.1-8B/70B-Instruct, plus a check on Qwen-2.5-7B, on the ETHICS commonsense subset.
- **Belief Dominance** (Steinmetz Yalon et al., [2602.02467](https://arxiv.org/abs/2602.02467)): Does the model follow its own knowledge or the text in the prompt? Control: a layer-0 probe on only the two entity embeddings (the word vectors of the two names). Llama-3-70B and Gemma-3-27B, 900 CounterFact items, 15 splits.
- **Concept injection** (Lindsey, [2601.01828](https://arxiv.org/abs/2601.01828)): They add a concept's steering vector to the residual stream on the prompt tokens and ask "what do you detect?". New controls:
  - A **gaslight** condition: the prompt text pushes the concept, but the hidden numbers are not changed.
  - A **three-way** answer: injected thought, input manipulation, or nothing.
  - Models: Llama-3.1-8B/70B, Qwen-2.5-72B, Qwen-3-32B, Gemma-3-27B. 32 concepts, with a range of layers and strengths.

## Evidence
- **Neurofeedback:** When labels match the meaning of the text, the model is well above chance. After the labels are shuffled, it falls to near the majority baseline (always guessing the most common label). Layer-0 input probes match or beat the model's own accuracy (Figure 2; exact values only in the figure).
- **Belief Dominance (Table 1):** The model's self-prediction is no better than a layer-0 probe on the names only. Examples: Gemma-3-27B BD(base), model 0.48 vs probe 0.57. Llama-3-70B BD(counter), 0.54 vs 0.55 to 0.57.
- **Injection:** Llama-3.1-70B and Qwen-3-32B repeat Lindsey's two-way result (they detect the injection with few false alarms). But both also call the **gaslight** trials activation changes, though the hidden numbers were not changed. In the three-way task:
  - Llama-3.1-70B is near chance and leans toward "activation".
  - Qwen-3-32B prefers the control answer.
  - Gemma-3-27B passes the two-way task but fails the three-way task.

  The authors read this as a general sense that "something is off", not a specific sense of a change in the hidden numbers.

## Limits / what they didn't show
- They give no positive test for second-order computation (Appendix A). Passing their three-way test would still not prove a state about a state.
- They used only open-weight models as substitutes. They could not test the Claude models that Lindsey used.
- Results change with prompt wording and with the concept (Appendix R). They tested only instruction-tuned models.
- The arXiv page lists no code release.

## Relevance to taste-lab
- It sets the bar for the third of our four tests, **grounded** (the model's report must match a signal inside it), in [[Four tests for own taste]]. If our model's "I like this code" report agrees with a valence probe (a probe for a good/bad signal), a reviewer will ask if an input-only probe agrees just as well. For code that is likely, because readability is visible in the text.
- It supports our choice to start with probes in [[Q1 Does the model sense code quality|Q1, does the model sense code quality?]]. It also fits [[Models do not report injected pain (Ferrara 2026)]] and [Rubin et al. 2611.15267](https://arxiv.org/abs/2611.15267). Together they say: you can read the states from the hidden numbers, but the model's spoken reports are weak or come from surface cues.
- It threatens any sentence in our paper like "the model monitors its own taste". Safer wording: "a probed internal signal that the model's behavior depends on".
- Fleming and Daw's second-order view (see [[Metacognition - watch and control yourself]]) uses the same split, so we can cite both together.

## Steal this
- **Input-only (layer-0) probe as a baseline:** For every claim that a self-report reflects an internal state, train the same probe on the input embeddings. Report the gap.
- **Shuffled-label control** for any self-report task where a probe makes the labels.
- **Gaslight plus three-way answer** design, for any injection test we run on a good/bad direction.
- Their advice for future tests: check variance per concept, check sensitivity to prompt wording, compare pretrained vs finetuned models, and use an outside model with the same cost as a baseline (Song et al. [2508.14802](https://arxiv.org/abs/2508.14802)).

## Harshit's notes
<!-- yours -->
