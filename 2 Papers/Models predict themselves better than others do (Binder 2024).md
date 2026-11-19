---
type: paper
title: "Looking Inward: Language Models Can Learn About Themselves by Introspection"
status: skimmed
arxiv: 2410.13787
url: https://arxiv.org/abs/2410.13787
authors: Felix J. Binder, James Chua, Tomek Korbak, Henry Sleight, John Hughes, Robert Long, Ethan Perez, Miles Turpin, Owain Evans
year: 2024
venue: ICLR 2025
relevance: 3
section: 2
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/2, test/grounded, component/monitoring, status/skimmed, relevance/3, role/prior-art, introspection, self-prediction, privileged-access, foundations]
links: ["[[Metacognition - watch and control yourself]]", "[[Field map - Models read their own state]]", "[[Four tests for own taste]]", "[[Training LMs to watch themselves (Wang 2026)]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Introspection claims fail basic checks (Singh 2026)]]"]
---

# Looking Inward: Language Models Can Learn About Themselves by Introspection

**One line:** A model trained to predict its own behavior predicts itself better than a second model trained on the same facts about it. The authors call this privileged access, or introspection.

**Why it matters to us:** It introduced the cross-model control ("model 1 predicts itself better than model 2 predicts model 1"). [[Training LMs to watch themselves (Wang 2026)]] uses the same logic two years later at larger scale.

Source: [arXiv 2410.13787](https://arxiv.org/abs/2410.13787) (v1 17 Oct 2024), [ICLR 2025 poster](https://iclr.cc/virtual/2025/poster/28917). Full HTML read for Sections 1 to 3.

**Words used here:**
- **Introspection (their definition):** gaining knowledge that is not in, or derived from, the training data, but comes from internal states.
- **Self-prediction:** the model answers a question about a hypothetical, such as "Given this input, would your answer favor the short-term or long-term option?"
- **Object-level behavior:** what the model actually does when given the real input.
- **Cross-prediction:** a second model (M2) is fine-tuned on M1's real behavior and asked to predict M1.
- **Mean absolute deviation (MAD):** the average gap between predicted and true behavior probabilities. Lower is better.

## Claim
Models can learn to predict their own behavior in ways that go beyond what another model can learn from the same data. This is evidence for introspection on simple tasks, but not on complex or out-of-distribution ones ([arXiv](https://arxiv.org/abs/2410.13787)).

## Mechanism
1. Collect M1's real behavior on many prompts (for example, the second letter of its answer, or whether it picks an even number).
2. Fine-tune M1 to answer hypothetical questions about that behavior.
3. Fine-tune M2 on the same data about M1.
4. Test both on held-out tasks. If M1 beats M2, M1 uses something beyond the data: privileged access.
5. **Behavior change test:** after self-prediction training, fine-tune M1 to change its real behavior (with 1,000 samples from Claude 3.5 Sonnet). Check if its self-predictions follow the new behavior, which it was never trained to predict.

## Evidence
- Models: GPT-4, GPT-4o, GPT-3.5 and Llama-3-70B (Sec. 3).
- Before training, self-prediction is about at the "most common behavior" baseline. After training, GPT-4o rises from 32.6% to 49.4% on held-out data (Sec. 3.2).
- Llama-3-70B predicts itself at 48.5%, while GPT-4o trained on Llama's data predicts Llama at 31.8%. The reverse holds too: GPT-4o predicts itself at 49.4%, Llama at 36.6% (Sec. 3.2).
- Cross-prediction stops improving after 10,000 samples, at 35.2%, below the 48.5% self-prediction (Sec. 3.2.2).
- GPT-3.5's own-model advantage is small (+0.8%).
- **Calibration:** self-prediction lowers Llama-70B's MAD from 23.0 to 8.7; cross-prediction only to 21.3 (Sec. 3.3).
- **Behavior change:** GPT-4o predicts its changed behavior at 35.4% vs its old behavior at 21.7% (Sec. 3.4).

## Limits / what they didn't show
- Works only on simple properties of short answers. Fails on complex tasks and does not generalize to related self-awareness tasks (authors, Sec. 1 and 4).
- The own-model advantage is about behavior, not about a named internal state. It does not show what the model reads.
- Accuracy is low in absolute terms (about 50%).
- A 2026 study trained Llama-3.1-8B and Qwen3-8B on self-prediction and found no consistent own-model advantage: the stronger Qwen often predicts Llama better than Llama does ([[Trained self-prediction without an own-model edge (Zeng 2026)]]).

## Relevance to taste-lab
**Relevance 3.** Section 2, foundations of self-knowledge; also feeds section 3.
- **Grounded test** ([[Four tests for own taste]]): the cross-model control is the right standard for any claim that a model reads its own taste. If a second model trained on the same data predicts our model's preferences as well, the taste signal is not privileged.
- The behavior change test is a template for the persist stage: after a weight change, does the model's self-report follow the new behavior? [[One direction controls refusal (Arditi 2024)]] reports that, for a refusal edit, it does not.

## Steal this
- The M1 vs M2 design with matched training data.
- The behavior change test: change the behavior by fine-tuning, then check if self-report follows.

## Harshit's notes
<!-- yours -->
