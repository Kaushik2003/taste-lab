---
type: draft
status: draft
section: 5
tags: [type/draft, section/5, component/consolidation, test/self-reinforcing, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]"]
---

# 5. Persistent control

Draft 1, 2026-11-20. Written from the paper notes, not the full papers.

## 5.0 The question of this section

In the frame of [[Monitoring and control between two levels (Nelson 1990)]], control changes what the object level does. Most control in language models is temporary: a prompt, a sampling choice, or a steering vector added during one run. **Persistent control** writes the change into the weights, so it lasts.

We ask three questions:
1. How can a change in behavior be written into weights?
2. Who chooses the change?
3. Does the model know what its own edits can and cannot do?

The short answer: there are working methods for both localized and distributed changes. But in every case someone else chooses the change: an experimenter, a larger model, or a task reward. And the one test of whether an editor knows its limits finds that it does not.

**Words used here.**
- **Steering vector:** a direction added to the hidden states during generation to push behavior one way.
- **Rank-one edit:** a change to a weight matrix that adds one fixed pattern. It is the smallest structured weight change.
- **Weight-space programming (WSP):** an agent reads a network's weights and writes changes to them directly, without gradient training.
- **Self-edit (SEAL sense):** the model writes its own fine-tuning data and settings, and is then trained on them.
- **Collateral damage:** the drop in other skills after an edit.

## 5.1 Writing a known direction into the weights

If a behavior lives along one direction in the hidden states, it can be removed or added through the weights.
- **Removal is exact.** Refusal in 13 open chat models is carried by one direction. Projecting it out of every matrix that writes into the main hidden path gives a permanent jailbreak with no gradients. MMLU, ARC and GSM8K mostly stay within confidence intervals, but TruthfulQA drops in every model ([[One direction controls refusal (Arditi 2024)]]).
- **Removal from a few heads.** In R1-distilled models, reasoning length is a direction. Projecting it out of about 4% of attention heads (about 0.2% of parameters) fixes too-short reasoning: Llama3-8B GSM8K goes from 82.26 to 89.44, with the gains mostly in the shortest-reasoning cases ([[ThinkEdit - edit weights to think longer (Sun 2025)]]).
- **Addition with forward passes only.** A steering vector can be turned into one rank-one edit per attention output matrix. On Llama-3.1-8B the edit raises a sycophancy score from 3.60 to 94.64 (steering alone: 63.86) with MMLU within 0.15 of base ([[TFTV - turn a steering vector into a weight edit (Perin 2026)]]). The note warns that the chosen edits sit near the coherence floor, so part of the gain is paid for in fluency.
- **Sparse redistribution.** Scoring every head and neuron against a steering vector and editing only the best-aligned ones beats inference-time steering at matched utility: safety +17.2%, truthfulness +9.8%, reasoning length −12.2% on average ([[Steer2Edit - steering into small weight edits (Sun 2026)]]). Utility still drops against the base model in every table; for example, cutting reasoning length in Qwen3-4B-Thinking costs about 10 points of accuracy [unverified: 87.8 to 77.3, check against the PDF is pending].

**Limit common to all four.** The direction comes from contrast sets, labels or a judge chosen by the authors. None is the model's own evaluation. The edit is also mostly a removal or a push along one axis, which suits near-binary behaviors (refusal, short reasoning) better than graded qualities such as style ([[One direction controls refusal (Arditi 2024)]], [[ThinkEdit - edit weights to think longer (Sun 2025)]]).

## 5.2 Weight-space programming: an agent edits weights by reasoning

A different route lets a strong model read weights and write edits.
- **The original result.** GPT-6 Astra edited about 0.016% of Qwen3.5-0.8B's weights and raised MATH-500 from 7.9% to 48.1%, mostly by stopping repetitive reasoning loops. It also wrote small control networks from zero ([[WSP - a model reads and edits weights (Takehi 2026)]]). It struggles when the fault is spread across the network.
- **The anti-loop edit is simple.** The key edit acts like a nearly constant push along one direction, and a sort over 8 low-variance neurons replaces the agent's choice with the same result: 67.0% vs 67.4%, against 9.5% unedited ([[A simple sort replaces the anti-loop edit (Fischetti 2026)]]).
- **Independent replication.** On Qwen3.5-0.8B and 9B, held-out gains reach 29.45 points on MATH-500 from changing 1,023 parameter values, and a math edit transfers to other tasks (for example +20.10 on SciBench). But results vary across runs, and 6 of 16 runs keep the original weights because no edit could be confirmed ([[Exploring WSP - small weight edits, uneven results (Hu 2026)]]).
- **Under strict audits, patching mostly fails.** On 42 audited tasks with metered forward passes, the best fully tested agent (Claude Opus 5.5) scores 0.535 overall but 0.404 on fixing networks. On the 4 reasoning-loop tasks only two agents score above zero at all ([[WeightBench - models cannot yet patch models (Marasini 2026)]]).

**How the two sides fit [our reading].** The large gains come with free forward passes and validation, and often from repairing one local fault. With compute metered and collateral damage penalized, the same kind of repair is much harder.

## 5.3 Self-edits through training

SEAL lets the model write its own fine-tuning data and settings ("self-edits"). Reinforcement learning then rewards the self-edits that improve performance after the update ([[SEAL - models write their own training data (Zweiger 2025)]]). It is the closest prior art for "the model directs its own weight change", and it handles distributed change, which rank-one edits do not.

Its limits for our frame:
- The reward is external (downstream task score). The model learns how to learn, not what it values.
- Each step needs an inner fine-tune, which is expensive, and forgetting across many edits is a known problem ([[SEAL - models write their own training data (Zweiger 2025)]]).
- The headline ARC gain in our note needs a check against the paper's protocol [unverified].

## 5.4 Who chooses the change?

| Method | Who picks the change | What checks it | Note |
|---|---|---|---|
| Direction removal ([[One direction controls refusal (Arditi 2024)]], [[ThinkEdit - edit weights to think longer (Sun 2025)]]) | Experimenter (contrast sets, length labels) | Benchmarks | Exact for removal |
| Steering to weights ([[TFTV - turn a steering vector into a weight edit (Perin 2026)]], [[Steer2Edit - steering into small weight edits (Sun 2026)]]) | Experimenter plus outside judge | Judge, benchmarks | Stronger than steering, with utility cost |
| Weight-space programming ([[WSP - a model reads and edits weights (Takehi 2026)]], [[Exploring WSP - small weight edits, uneven results (Hu 2026)]]) | A larger outside model | Development set score | Large gains, high variance |
| Self-edits ([[SEAL - models write their own training data (Zweiger 2025)]]) | The model, steered by a task reward | Task score after update | Distributed change |

In no row does the model choose the change from its own evaluation of good or bad. That is the missing step between monitoring (section 3), evaluation (section 4) and persistence ([[gaps]]).

## 5.5 Keeping edits safe

Three safeguards appear:
- **Keep the original unless the edit is confirmed.** In the WSP replication this rule fired in 6 of 16 runs ([[Exploring WSP - small weight edits, uneven results (Hu 2026)]]).
- **Penalize collateral damage and edit size together.** WeightBench multiplies task gain by penalties for damage, edit size and compute, so a small edit cannot make up for no gain ([[WeightBench - models cannot yet patch models (Marasini 2026)]]).
- **Accept only net-positive edits.** A gate that weighs gains against new regressions stops forgetting in a self-improving agent, but there the edits are to text instructions, not weights ([[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]). Section 6 covers it.

## 5.6 Does the editor know its own edits?

This is where persistence meets metacognition, and the evidence is thin.
- **Knowing the limits.** WeightBench mixes impossible edits (skills the model never learned) with hard but possible ones. The Claude models score 0.491 to 0.500 on this track, which the authors call about the random-guess level ([[WeightBench - models cannot yet patch models (Marasini 2026)]]). No editor yet knows what its edits can do.
- **Updating the self-model.** After its refusal direction is removed, a model still describes its old refusal policy ([[One direction controls refusal (Arditi 2024)]]). In contrast, a model trained to predict itself does follow a fine-tuned change in its behavior ([[Models predict themselves better than others do (Binder 2024)]]). Whether the meta level's model of the object level (principle 2 of [[Monitoring and control between two levels (Nelson 1990)]]) updates after a weight change is open.
- **Controlling how it learns.** No paper uses an internal signal to set how fast or what the model learns, which is the role [[Neuromodulators set how the brain learns (Doya 2002)]] gives to neuromodulators.

## 5.7 Summary

- A change can be written into weights in two ways: localized edits (direction removal, rank-one edits, weight-space programming) and distributed self-edits through training (SEAL).
- Localized edits work best for near-binary behaviors and for repairing one local fault. Under strict audits, patching language models mostly fails.
- In every method someone else chooses the change. No model has edited its own weights by reading them, and none chooses an edit from its own evaluation.
- No editor knows the limits of its edits, and self-reports do not reliably follow weight changes.
- For the review's frame: the persist mechanism exists, but the "self" in self-modification is missing. Section 6 shows why closing that gap is risky: loops that learn from their own signal tend to collapse without a hard outside check.
