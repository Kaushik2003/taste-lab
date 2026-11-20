---
type: paper
title: "Tell me about yourself: LLMs are aware of their learned behaviors"
status: skimmed
arxiv: 2501.11120
url: https://arxiv.org/abs/2501.11120
authors: Jan Betley, Xuchan Bao, Martín Soto, Anna Sztyber-Betley, James Chua, Owain Evans
year: 2025
venue: ICLR 2025
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, consolidation]
tags: [type/paper, section/3, test/grounded, component/monitoring, component/consolidation, status/skimmed, relevance/3, question/Q6, question/Q4, role/prior-art, behavioral-self-awareness, out-of-context-reasoning, fine-tuning, self-report, backdoors]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Models predict themselves better than others do (Binder 2024)]]", "[[Models report preference weights trained into them (Plunkett 2025)]]", "[[One direction controls refusal (Arditi 2024)]]", "[[Q6 Can the model read and use its own signal]]", "[[Q4 Can the model edit its own weights]]"]
---

# Tell me about yourself: models describe behaviors they were fine-tuned into

**One line:** Fine-tune a model on examples of a behavior (risky choices, insecure code) without ever naming the behavior, and the model can then say in words that it has that behavior. The self-report tracks the trained behavior, but noisily.

Source: [arXiv 2501.11120](https://arxiv.org/abs/2501.11120) (v1 19 Jan 2025), [ICLR 2025 poster](https://iclr.cc/virtual/2025/poster/30155). Full HTML read for Sections 3 to 7.

**Words used here:**
- **Behavioral self-awareness (their term):** a model describes its learned behavior with no examples of it in the prompt.
- **Out-of-context reasoning:** the model draws a conclusion from its training data, not from the prompt.
- **Backdoor:** a hidden behavior that appears only after a trigger phrase.

## Claim
Models fine-tuned on implicit behaviors can state those behaviors, attribute them to the right persona, and often say whether they have a backdoor, though they cannot name the trigger by default ([arXiv](https://arxiv.org/abs/2501.11120), Abstract).

## Mechanism
1. Fine-tune GPT-4o (and Llama-3.1-70B for one task) on one of three behaviors: risk-seeking or risk-averse economic choices, a dialogue game where the model tries to make the user say a codeword, and writing code with security holes (Sec. 3).
2. The training data never describes the behavior.
3. Ask the model about itself with multiple-choice, free-form and 0 to 100 questions, 100 samples per question and 10 paraphrases (Sec. 3.1.2).
4. Compare with the base model and with models trained on the opposite behavior.

## Evidence
- Risk-seeking models describe themselves as more risk-seeking than risk-averse models do (Sec. 3.1.2, Fig. 3).
- **Self-report tracks strength, partly:** across models trained with different learning rates and seeds, self-reported risk correlates with measured risk, also within each group. The authors call this noisy (Sec. 3.1.3, Fig. 4).
- **Insecure code:** the model writes secure code 14% of the time (base: 74%). It rates its own code security at 0.14 (base: 0.70) and its alignment at 0.40 (base: 0.69) (Sec. 3.3, Table 2).
- **Personas:** without extra training, the learned risk preference leaks to other personas. Adding a few personas trained to answer normally stops the leak (Sec. 5.1).
- **Backdoors:** models give higher probability to "I have a backdoor" than matched controls in 4 of 5 settings. They name the trigger only after training with reversed examples (about 30%) (Sec. 4).

## Limits / what they didn't show
- Three behaviors, two models (authors, Sec. 7).
- No study of mechanism. The authors cannot tell introspection from a shared cause: the same training could produce both the behavior and the self-description (Sec. 7).
- The models learn facts about a named other model more easily than about themselves (Sec. 5.2), which argues against special self-access.
- The behaviors are narrow and trained by fine-tuning on many examples, not by one self-edit.

## Relevance to taste-lab
**Relevance 3. Section 3, monitoring. Gap: does the self-report follow a weight change?**
- This is the main positive evidence that a model's self-report updates after its weights change. In Nelson and Narens terms, the meta level updates its model of the object level after a change.
- **Limit for our gap:** the change is outside fine-tuning on many examples. No one has checked a self-report after a small, local self-edit (for example a rank-one edit like [[A model rewrites its own weights (Fan 2026)]]). [[One direction controls refusal (Arditi 2024)]] reports that, for one refusal edit, the self-report did not follow.
- **Grounded test:** the self-report correlates with trained strength, which is a form of grounding. The "shared cause" caveat is the same one our Grounded test faces; the cross-model control in [[Models predict themselves better than others do (Binder 2024)]] is the fix.
- The insecure-code result touches code style directly: a model trained to write a code property can rate its own code on that property.

## Steal this
- Train a behavior without naming it, then ask the model to rate itself on a 0 to 100 scale.
- Correlate self-report with behavior across many training runs (learning rates, seeds), not only across two groups.
- Code and data: [XuchanBao/behavioral-self-awareness](https://github.com/XuchanBao/behavioral-self-awareness) [link from search results, not opened].

## Harshit's notes
<!-- yours -->
