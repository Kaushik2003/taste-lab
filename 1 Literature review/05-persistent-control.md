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

The short answer: there are working methods for both localized and distributed changes. Since November 2026, one model can also choose and write an edit to its own weights. But in every case something outside the model sets what counts as a good change: an experimenter, a larger model, a task reward, or graded answers. And the one test of whether an editor knows its limits finds that it does not.

**Words used here.**
- **Steering vector:** a direction added to the hidden states during generation to push behavior one way.
- **Rank-one edit:** a change to a weight matrix that adds one fixed pattern. It is the smallest structured weight change.
- **Weight-space programming (WSP):** an agent reads a network's weights and writes changes to them directly, without gradient training.
- **Self-edit (SEAL sense):** the model writes its own fine-tuning data and settings, and is then trained on them.
- **Collateral damage:** the drop in other skills after an edit.

## 5.1 Writing a known direction into the weights

If a behavior lives along one direction in the hidden states, it can be removed or added through the weights.
- **Removal is exact.** Refusal in 13 open chat models is carried by one direction. Projecting it out of every matrix that writes into the main hidden path gives exactly the same result as removing it during each run, so the jailbreak becomes permanent with no gradients. The exactness holds for removal only, not for adding a direction. MMLU, ARC and GSM8K mostly stay within confidence intervals, but TruthfulQA drops in every model ([[One direction controls refusal (Arditi 2024)]]).
- **Removal from a few heads.** In R1-distilled models, reasoning length is a direction. Projecting it out of about 4% of attention heads (about 0.2% of parameters) fixes too-short reasoning: Llama3-8B GSM8K goes from 82.26 to 89.44, with the gains mostly in the shortest-reasoning cases ([[ThinkEdit - edit weights to think longer (Sun 2025)]]).
- **Addition with forward passes only.** A steering vector can be turned into one rank-one edit per attention output matrix. On Llama-3.1-8B the edit raises a sycophancy score from 3.60 to 94.64 (steering alone: 63.86) with MMLU within 0.15 of base ([[TFTV - turn a steering vector into a weight edit (Perin 2026)]]). The note gives two warnings. The chosen edits sit near the coherence floor, so part of the gain is paid for in fluency. And it is not one small edit: 6 to 17 layers change, with strength tuned per trait using an outside judge.
- **Sparse redistribution.** Scoring every head and neuron against a steering vector and editing only the best-aligned ones beats inference-time steering at matched utility: safety +17.2%, truthfulness +9.8%, reasoning length −12.2% on average; the abstract does not say whether these are absolute or relative ([[Steer2Edit - steering into small weight edits (Sun 2026)]]). Utility still drops against the base model in every table; for example, cutting reasoning length in Qwen3-4B-Thinking costs about 10 points of accuracy: average accuracy falls from 87.8 to 77.3 while length falls from 5,319 to 3,387 tokens. Most of the loss is on GPQA (66.3 to 42.4) and MATH-500 (97.7 to 89.7) ([[Steer2Edit - steering into small weight edits (Sun 2026)]], Table 10, checked in the PDF).

**Limit common to all four.** The direction comes from contrast sets, labels or a judge chosen by the authors. None is the model's own evaluation. The edit is also mostly a removal or a push along one axis, which suits near-binary behaviors (refusal, short reasoning) better than graded qualities such as style ([[One direction controls refusal (Arditi 2024)]], [[ThinkEdit - edit weights to think longer (Sun 2025)]]).

## 5.2 Weight-space programming: an agent edits weights by reasoning

A different route lets a strong model read weights and write edits.
- **The original result.** GPT-6 Astra edited about 0.016% of Qwen3.5-0.8B's weights and raised MATH-500 from 7.9% to 48.1%, mostly by stopping repetitive reasoning loops. The low starting score is itself a loop effect: 93% of the base model's MATH-500 answers hit the 32,768-token limit, and 33% still do after the edit. It also wrote small control networks from zero that beat a 100M-step reinforcement-learning agent on 3 games ([[WSP - a model reads and edits weights (Takehi 2026)]]). It struggles when the fault is spread across the network.
- **The anti-loop edit is simple.** The key edit acts like a nearly constant push along one direction, and a sort over 8 low-variance neurons replaces the agent's choice with the same result: 67.0% vs 67.4%, against 9.5% unedited ([[A simple sort replaces the anti-loop edit (Fischetti 2026)]]).
- **Independent replication.** On Qwen3.5-0.8B and 9B, held-out gains reach 29.45 points on MATH-500 from changing 1,023 parameter values, and a math edit transfers to other tasks (for example +20.10 on SciBench). But results vary across runs, 6 of 16 runs keep the original weights because no edit could be confirmed, gains are smaller on the 9B model, and one 9B math candidate lowered held-out accuracy despite a development gain ([[Exploring WSP - small weight edits, uneven results (Hu 2026)]]).
- **Under strict audits, patching mostly fails.** On 42 audited tasks with metered forward passes, the best fully tested agent (Claude Opus 5.5) scores 0.535 overall but 0.404 on fixing networks. On the 4 reasoning-loop tasks only two agents score above zero at all ([[WeightBench - models cannot yet patch models (Marasini 2026)]]). Three caveats weaken this result: all scores are lower bounds because flagged runs score zero until a human reviews them (11 of 77 Opus runs were flagged); half the tasks have no reference solution that uses only what the agent can access; and each task ran once or twice on one seed.
- **A model edits its own weights.** An open 27B model (Qwen3.5) gets its own weights, its graded answers on practice problems, and tools to test itself and read its hidden states. Gradients are blocked. It found that its wrong answers mostly ran out of tokens in loops. It took the difference between the mean layer-8 hidden states of answers that finish and answers that do not, and removed 5% of that direction from the two output matrices of layer 8. This is a rank-one edit. On 490 held-out problems, accuracy went from 57.2% to 58.3% in the first protocol, and to 61.3% and 63.8% in two sessions of the second protocol, where the model must test an edit before it submits it. In 5 of 8 sessions it withdrew its edit. The ability appears only at the largest size: the 2B model made no edit, and the 4B and 9B models added random noise and broke themselves ([[A model rewrites its own weights (Fan 2026)]], Fig. 1, Fig. 4, Tab. 8). Three limits: graded answers decide which edits to keep; the gain is again mostly a loop fix (answers cut at the token limit fall from 33.6% to 26.1%); and we found no random-direction or decoding-time baseline in the paper.

**How the results fit [our reading].** The large gains come with free forward passes and validation, and often from repairing one local fault. With compute metered and collateral damage penalized, the same kind of repair is much harder. The self-edit result fits the same pattern: a small gain on the same loop fault, with many forward passes and a test before each submit.

## 5.3 Self-edits through training

SEAL lets the model write its own fine-tuning data and settings ("self-edits"). Reinforcement learning then rewards the self-edits that improve performance after the update ([[SEAL - models write their own training data (Zweiger 2025)]]). It is the closest prior art for "the model directs its own weight change", and it handles distributed change, which rank-one edits do not.

Its limits for our frame:
- The reward is external (downstream task score). The model learns how to learn, not what it values.
- Each step needs an inner fine-tune, which is expensive, and forgetting across many edits is a known problem ([[SEAL - models write their own training data (Zweiger 2025)]]).
- The headline ARC result is narrow. SEAL's self-edits succeed 72.5% of the time against 20% for self-edits from the untrained model and 0% for in-context learning. But the test is 8 ARC tasks, picked because a well-tuned test-time training run can solve them, with 5 self-edits per task, on Llama-3.2-1B-Instruct ([[SEAL - models write their own training data (Zweiger 2025)]], Sec. 4.1, Table 1).

## 5.4 Who chooses the change?

| Method | Who picks the change | What checks it | Note |
|---|---|---|---|
| Direction removal ([[One direction controls refusal (Arditi 2024)]], [[ThinkEdit - edit weights to think longer (Sun 2025)]]) | Experimenter (contrast sets, length labels) | Benchmarks | Exact for removal |
| Steering to weights ([[TFTV - turn a steering vector into a weight edit (Perin 2026)]], [[Steer2Edit - steering into small weight edits (Sun 2026)]]) | Experimenter plus outside judge | Judge, benchmarks | Stronger than steering, with utility cost |
| Weight-space programming ([[WSP - a model reads and edits weights (Takehi 2026)]], [[Exploring WSP - small weight edits, uneven results (Hu 2026)]]) | A larger outside model | Development set score | Large gains, high variance |
| Self-rewriting ([[A model rewrites its own weights (Fan 2026)]]) | The model itself, from its own hidden states | Its own paired tests on graded practice answers | Small gain, only at 27B |
| Self-edits ([[SEAL - models write their own training data (Zweiger 2025)]]) | The model, steered by a task reward | Task score after update | Distributed change |

In SEAL and in self-rewriting the model writes the edit itself. In self-rewriting it also picks the place and the direction from its own hidden states. But in both, outside correctness decides which edits are good: a task reward in SEAL, graded answers in self-rewriting. In no row does the model judge the change by its own evaluation of good or bad. That is the missing step between monitoring (section 3), evaluation (section 4) and persistence ([[gaps]]).

**Older self-modifying networks.** Networks that change their own weights are not new. Self-referential weight matrices and fast-weight methods learn to rewrite their own weights during a run (Irie et al. 2022; Google's "Nested Learning", 2025) [unverified: both in the Reading list, no notes yet]. These are learned update rules, not a model reasoning about its weights or judging edits by its own taste, but the review must cite them before it claims that self-modification is new.

## 5.5 Keeping edits safe

Three safeguards appear:
- **Keep the original unless the edit is confirmed.** In the WSP replication this rule fired in 6 of 16 runs ([[Exploring WSP - small weight edits, uneven results (Hu 2026)]]).
- **Penalize collateral damage and edit size together.** WeightBench multiplies task gain by penalties for damage, edit size and compute, so a small edit cannot make up for no gain ([[WeightBench - models cannot yet patch models (Marasini 2026)]]).
- **Accept only net-positive edits.** A gate that weighs gains against new regressions stops forgetting in a self-improving agent, but there the edits are to text instructions, not weights ([[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]). Section 6 covers it.

## 5.6 Does the editor know its own edits?

This is where persistence meets metacognition, and the evidence is thin.
- **Knowing the limits.** WeightBench mixes impossible edits (skills the model never learned) with hard but possible ones. The Claude models score 0.491 to 0.500 on this track, which the authors call about the random-guess level ([[WeightBench - models cannot yet patch models (Marasini 2026)]]). No editor yet knows what its edits can do. The self-rewriting 27B model withdraws edits that its tests do not support (5 of 8 sessions), but it learns this by testing each edit on graded answers, not by knowing in advance ([[A model rewrites its own weights (Fan 2026)]]).
- **Updating the self-model.** After its refusal direction is removed, a model still describes its old refusal policy ([[One direction controls refusal (Arditi 2024)]]). In contrast, a model trained to predict itself does follow a fine-tuned change in its behavior ([[Models predict themselves better than others do (Binder 2024)]]). The two cases differ in more than the result: one is a direct weight edit on an untrained model, the other is fine-tuning on a model already trained for self-prediction. So they cannot be compared directly. Whether the meta level's model of the object level (principle 2 of [[Monitoring and control between two levels (Nelson 1990)]]) updates after a weight change is open.
- **Controlling how it learns.** No paper uses an internal signal to set how fast or what the model learns, which is the role [[Neuromodulators set how the brain learns (Doya 2002)]] gives to neuromodulators.

## 5.7 Summary

- A change can be written into weights in two ways: localized edits (direction removal, rank-one edits, weight-space programming) and distributed self-edits through training (SEAL).
- Localized edits work best for near-binary behaviors and for repairing one local fault. Under strict audits, patching language models mostly fails.
- In every method something outside the model sets what counts as a good change. One language model now edits its own weights after it reads its own hidden states, but only at 27B, for a loop fault, and with graded answers deciding what to keep ([[A model rewrites its own weights (Fan 2026)]]). No model judges an edit by its own evaluation. Older self-modifying networks learn their own update rule, which is a different thing.
- In the one test of whether an editor knows the limits of its edits, it does not. Self-reports follow weight changes in one setting and not in another.
- For the review's frame: the persist mechanism exists, and a model can now choose where and how to edit itself. What is missing is the model's own judgment of what is good. That is the taste step. Section 6 shows why closing that gap is risky: loops that learn from their own signal tend to collapse without a hard outside check.

## Open doubts (critic review, 2026-11-20)

1. **Older self-modifying work is missing.** Self-referential weight matrices (Irie 2022), fast weights and Nested Learning (2025) need notes. Without them, any claim that self-modification is new may read as ignorance of the field.
2. ~~**Numbers to check against the papers:**~~ Checked 2026-11-20 (see [[2026-11-20 number check]]): WSP and SEAL numbers match; SEAL protocol now stated. Steer2Edit Table 10 checked in the PDF the same day; it matches. Original note: the Steer2Edit accuracy drop (87.8 to 77.3, a check is already in TASKS); the SEAL ARC gain (our note says to check the protocol); the WSP math gain (7.9% to 48.1%).
3. **One benchmark carries the "editors don't know their limits" claim.** The WeightBench limits track has 5 tasks, one seed and unreviewed flagged runs. It is a strong hint, not a settled result.
4. **Weight-space programming moves fast.** Three papers now say current WSP gains are often loop fixes or output changes: Claude's edits act at the output, through sampling temperature and the "Wait" token ([[Claude's WSP edits act at the output (Kundu 2026)]]); reading weights is mostly reading the input layer ([[Reading weights is mostly reading inputs (Goworek 2026)]]); and repairs depend on a low-bit trace that the planted faults leave (arXiv 2611.23615, Reading list) [unverified: all three from abstracts only]. The November 2026 arXiv batch alone has more than 10 WSP application papers (Reading list, scored 1 to 2). One preregistered study finds no advantage for diffusion editing (arXiv 2611.22228) [unverified: abstract only]. The section may need a short paragraph on that wider field.
5. **Distributed change is thin.** SEAL is the only paper on self-directed distributed change. Continual-learning and forgetting work is not covered at all.
6. **"Near-binary behaviors" is our reading.** The claim that rank-one edits suit near-binary behaviors better than graded ones comes from the notes' limits sections, not from a test in any paper.
7. **One paper carries the self-edit result.** Self-rewriting is one preprint, one model family, one task type (math with a loop failure), and only the largest model succeeds ([[A model rewrites its own weights (Fan 2026)]]). It has no random-direction edit or decoding-time length control as a baseline, and each session starts from the base weights. Section 5 should present it as a first result, not as an established ability.

## Log
- 2026-11-20 (scout follow-up): added self-rewriting ([[A model rewrites its own weights (Fan 2026)]]) to 5.0, 5.2, 5.4, 5.6 and 5.7, after a check of its numbers in the PDF (Fig. 1, Fig. 4, Tab. 8). The old claim "no language model has edited its own weights by reading them" is removed. Added open doubt 7 and the WSP caveats to doubt 4.
- 2026-11-20: numbers checked against the papers (WSP blog, SEAL, TFTV, ThinkEdit, WSP follow-ups, WeightBench, Arditi, GUARD). All match. Added the SEAL ARC protocol and the WSP token-limit caveat.
- 2026-11-20: Steer2Edit Table 10 checked in the PDF (87.8 to 77.3 average accuracy). Matches; per-dataset drop added.
