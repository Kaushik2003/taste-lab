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
tags: [type/paper, role/threat, section/3, test/grounded, component/monitoring, status/skimmed, relevance/3, thread/T1, introspection, privileged-access, methodology]
links: ["[[metacognition-monitor-control]]", "[[four-taste-tests]]", "[[2026-ferrara-all-quiet-pain]]", "[[landscape-metacognitive-monitoring]]"]
---

# Can LLMs Introspect? A Reality Check

**One line:** Two popular "LLMs can introspect" results do not pass basic controls: input-only probes match the self-reports, and injection detection breaks once the model is offered "my input was manipulated" as an answer.

## Claim
A test only shows introspection if it needs (1) **privileged access**: the answer can't be recovered from the input alone, and (2) **second-order computation**: the report comes from a representation *about* the first-order state, which you can only show with designs where first-order and second-order accounts predict different things (Section 3). Under these rules, current evidence does not establish metacognitive monitoring in LLMs ([arXiv](https://arxiv.org/abs/2605.26242)).

## Mechanism
They re-run three paradigms with stronger controls.
- **Ji-An et al. neurofeedback** ([2505.13763](https://arxiv.org/abs/2505.13763)): the model sees in-context examples labeled by a probe (or PCA component) on its own activations and must predict the label for a new input. Controls: (a) permute the labels before training the probe, so the label no longer lines up with meaning in the text; (b) train a linear probe on **layer-0 input embeddings only** to predict the same labels. Models: Llama-3.1-8B/70B-Instruct, plus a Qwen-2.5-7B check, on the ETHICS commonsense subset.
- **Belief Dominance** (Steinmetz Yalon et al., [2602.02467](https://arxiv.org/abs/2602.02467)): does the model follow its own knowledge or the context? Control: a layer-0 probe on only the two entity embeddings. Llama-3-70B and Gemma-3-27B, 900 CounterFact items, 15 splits.
- **Concept injection** (Lindsey, [2601.01828](https://arxiv.org/abs/2601.01828)): add a concept steering vector to the residual stream on the prompt tokens and ask "what do you detect?". New controls: a **gaslight** condition where the prompt text pushes the concept with no activation change, and a **three-way** answer (injected thought / input manipulation / nothing). Llama-3.1-8B/70B, Qwen-2.5-72B, Qwen-3-32B, Gemma-3-27B; 32 concepts; layer and strength sweeps.

## Evidence
- Neurofeedback: model accuracy is well above chance on semantically aligned labels but falls to near the majority baseline after label permutation. Layer-0 input probes match or beat the model's in-context accuracy (Figure 2; exact values only in the figure).
- Belief Dominance (Table 1): the model's in-context self-prediction is no better than an entity-only layer-0 probe. Example: Gemma-3-27B BD(base) in-context 0.48 vs probe 0.57; Llama-3-70B BD(counter) 0.54 vs 0.55 to 0.57.
- Injection: Llama-3.1-70B and Qwen-3-32B reproduce the Lindsey two-way pattern (detection with few false positives), but both also call the **gaslight** trials activation interventions. In the three-way task Llama-3.1-70B is near chance and leans toward "activation", Qwen-3-32B prefers the control answer, and Gemma-3-27B passes two-way but fails three-way. The authors read this as general sensitivity to "something is off", not a specific sense of hidden-state change.

## Limits / what they didn't show
- They give no positive test for second-order computation (Appendix A). Passing their three-way test would still not prove a meta-representation.
- Open-weight substitutes only; they could not test the Claude models Lindsey used.
- Results vary by prompt wording and by concept (Appendix R). Only instruction-tuned models.
- No code release listed on the arXiv page.

## Relevance to taste-lab
- Sets the bar for test 3 (**grounded**) in [[four-taste-tests]]. If our model's "I like this code" report agrees with a valence probe, a reviewer will ask whether an input-only probe agrees just as well. For code that is likely: readability is visible in the text.
- Supports the probe-first route already taken in [[code-quality-signal-T1]] and fits [[2026-ferrara-all-quiet-pain]] and [Rubin et al. 2611.15267](https://arxiv.org/abs/2611.15267): states are decodable, verbal reports are weak or explained by surface cues.
- Threat to any "the model monitors its own taste" wording in the paper. Safer wording: "a probed internal signal that the model's behavior depends on".
- Fleming and Daw's second-order view (see [[metacognition-monitor-control]]) is the same distinction they use, so we can cite both together.

## Steal this
- **Layer-0 (input-only) probe baseline**: for every claim that a self-report reflects internal state, train the same probe on input embeddings. Report the gap.
- **Label permutation control** for any probe-labeled self-report task.
- **Gaslight + three-way answer** design for any injection test we run on a valence direction.
- Their recommendations for future tests: per-concept variance, prompt-wording sensitivity, pretrained vs finetuned, a cost-matched third-party baseline (Song et al. [2508.14802](https://arxiv.org/abs/2508.14802)).

## Harshit's notes
<!-- yours -->
