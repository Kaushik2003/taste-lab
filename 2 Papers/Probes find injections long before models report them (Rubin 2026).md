---
type: paper
title: "A Closer Look at Language Model Introspection: Probing Information and Reporting"
status: read
arxiv: 2611.15267
url: https://arxiv.org/abs/2611.15267
authors: Dustin Rubin, Vincenzo Timmel, Xufeng He, Aritra Saha, JooMan Kim, Vijay Madisetti
year: 2026
venue: arXiv preprint
relevance: 2
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, component/monitoring, status/read, relevance/2, role/threat, introspection, activation-injection, linear-probe, pretraining-checkpoints]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]", "[[Models sometimes notice injected thoughts (Lindsey 2025)]]", "[[Models do not report injected pain (Ferrara 2026)]]", "[[Introspection claims fail basic checks (Singh 2026)]]", "[[Good-bad signal probe]]"]
---

# A Closer Look at Language Model Introspection: Probing Information and Reporting

**One line:** A simple probe can find which sentence got an injected change very early in training, and even in an untrained network. The model learns to say which sentence it was much later, and how well it says so depends on where the change goes in.

**Why it matters to us:** It shows that "a probe can read it" is a low bar. A signal that a linear probe decodes may sit near the surface and say little about what the model itself can use. That is a direct warning for the Grounded test.

Source: [arXiv 2611.15267](https://arxiv.org/abs/2611.15267) (v2, 14 Nov 2026), full HTML read (Sections 1 to 5). Georgia Institute of Technology.

**Words used here:**
- **Injection:** the experimenter adds a vector to the model's hidden numbers at some layer, while the input text stays the same.
- **Localization task:** the model reads nine numbered sentences, one gets the injection, and the model must say which one. Chance is 1 in 9 (11.1%).
- **Linear probe:** a small classifier trained on the model's hidden numbers to predict a label. Here it predicts the injected sentence.
- **Strength α (alpha):** the size of the injected vector compared with a typical hidden-state size. α = 4 means four times as large.
- **Checkpoint:** a saved copy of the model at one point during training.

## Claim
Where an injection went is easy to decode from activations long before the model can report it. So when a model does report it, that need not mean it has broad access to its own computation ([arXiv](https://arxiv.org/abs/2611.15267), abstract and Sec. 5).

## Mechanism
1. Use OLMo 3 (7B and 32B), because every training checkpoint is public (Sec. 3.1).
2. Inject a concept vector or a random direction into every token of one of nine sentences (Sec. 3.3).
3. Ask "Which sentence was altered?" and read the model's top label from 1 to 9 in one forward pass. No examples in the prompt (Sec. 3.2).
4. On the same trials, train a nine-way logistic-regression probe on the hidden state at the answer position (Sec. 3.4).
5. Compare probe and model across seven pretraining checkpoints and the released base model, at one fixed setting: injection at layer 0, α = 4, probe at layer 24 (Sec. 3.5).
6. Separately, inject into untrained networks with no question at all, and probe a later token (Sec. 3.5.2).

## Evidence
- OLMo 3 32B after 8.4 billion training tokens: probe 98.3%, model 11.1% (chance) (Sec. 4.1).
- Released 32B base model, same setting: probe 99.1%, **model 89.6%**. So the base model *can* report the location, with no post-training (Sec. 4.1).
- At the released 32B base, α = 4: the model reports at 37.7% when the injection is at layer 6, and 89.6% at layer 0 (Sec. 1.2, 5.1). A weak report at one site does not show a general failure.
- Before any training (step 0), the probe already reaches 37.2% vs 11.3% for shuffled labels (Sec. 4.1).
- In three untrained networks, with no question, a probe at a later token finds the sentence at 31.5% (α = 8), and still 21.5% after 256 more tokens. Uninjected controls are 11.5% and 10.9% (Sec. 4.2).

## Limits / what they didn't show
- One task (which sentence) and one model family (OLMo 3). The main trajectory uses one fixed setting, picked after a wider sweep (Sec. 3.5.1).
- The pretrained no-prompt run has a raised uninjected control that the authors could not explain, so they draw no conclusion from it (Sec. 4.2).
- It does not test yes/no detection or content naming, the tasks in [[Models sometimes notice injected thoughts (Lindsey 2025)]].
- Probe uses 288 labeled trials per fold, while the model gets no labels. The two are not matched in supervision.

## Relevance to taste-lab
**Relevance 2.** Section 3 (monitoring).
- **Correction to our notes:** we cited this paper as "the model's answer stays at chance". That is true only at the 8.4-billion-token checkpoint. At the released base model the answer is 89.6%. Fixed in section 3 and the field map on 2026-11-20.
- **Grounded test** ([[Four tests for own taste]]): a high probe score is not evidence that the model reads the signal. Decodable traces appear even in random networks. Our [[Good-bad signal probe]] needs a baseline on an untrained or early checkpoint, and a causal test, not only probe accuracy.
- With [[Introspection claims fail basic checks (Singh 2026)]], it argues for a layer-0 or input-only control.
- Threat: if a readability readout is as easy to decode in a random network, it is a property of the input, not of the model's taste.

## Steal this
- The probe-vs-report comparison across public training checkpoints (OLMo).
- The step-0 and shuffled-label baselines for any probe claim.
- The idea that report accuracy depends on the injection site, so sweep it before claiming a failure.

## Harshit's notes
<!-- yours -->
