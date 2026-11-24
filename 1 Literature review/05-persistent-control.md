---
type: draft
status: draft
section: 5
tags: [type/draft, section/5, component/consolidation, test/self-reinforcing, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]"]
---

# 6. Changes that persist in the weights

Most control in language models is temporary: a prompt, a sampling choice, or a steering vector added during one run. **Persistent control** writes the change into the weights, so it lasts. This section asks four questions. By which routes can the weights of a deployed model change? Who chooses the change? Who checks it? And what happens when changes are made again and again?

There are two routes. The first builds the ability to change into the architecture and trains it: **learned memory**. The second leaves the architecture alone and writes small changes straight into the weights of an ordinary pretrained model: **direct edits**. They come from different research groups and are almost never compared.

**Terms used here.**
- **Steering vector:** a direction added to the hidden states during generation to push behavior one way.
- **Rank-one edit:** a change to a weight matrix that adds one fixed pattern. It is the smallest structured weight change.
- **Low-rank adapter (LoRA):** a small added block of weights (two thin matrices) that is trained while the main weights stay fixed.
- **Weight-space programming (WSP):** an agent reads a network's weights and writes changes to them directly, with no gradient training.
- **Collateral damage:** the drop in other skills after a change.

## 6.1 Route one: learned memory

**Early self-modifying networks.** The idea that a network changes its own weights by a learned rule is old. A self-referential weight matrix produces, at each step, its own key, query and learning rate, and adds a small update to itself; only its starting state is learned by gradient descent ([[SRWM - a weight matrix that rewrites itself (Irie 2022)]]). A related network outputs a signal that sets how fast its own plastic connections change ([[Backpropamine - a network sets its own plasticity (Miconi 2019)]]). These systems change themselves at run time, on small tasks, by a rule that training fixed. There is no judgment of good or bad in the loop.

**Memory that learns while the model reads.** Titans adds a memory module whose weights are updated during use. The update is driven by surprise: inputs that the memory predicts badly are written more strongly, with a momentum term and a forgetting gate ([[Titans - a memory that learns from surprise at test time (Behrouz 2025)]]). Nested Learning generalizes this. It treats a model as a chain of memory blocks that update at different rates, fast blocks for short-term memory and slow blocks for long-term knowledge, and its demonstration model produces its own update targets and learning rates ([[Nested Learning - a model that learns its own update rule (Behrouz 2025)]]). The authors compare a standard deployed model to a patient who cannot form new long-term memories. They say that catastrophic forgetting is "not solved in general".

**Sleep.** The latest step moves short-term memory into long-term weights in an offline phase ([[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]). In "sleep", the model first switches on a small new low-rank block in a slower memory and trains only that block to reproduce what the faster memory learned. Then it "dreams": it writes synthetic training examples, keeps the most promising by a gradient-based score, fine-tunes a copy of itself on each, and rewards the examples whose copy scores better on an outside task. The method runs on ordinary pretrained models of 1B to 8B with small added blocks. Its results are modest and positive: on three maths benchmarks with Qwen3-8B it scores 79.2, 69.0 and 46.1 against 76.6, 67.4 and 45.1 for the best other method; on learning new facts it scores 48.9 against 46.7 for SEAL, and 35.7 with dreaming removed. Three limits matter here. Every update is gradient training. Outside task scores decide which dreams count. And "continual" means two tasks learned in sequence, not a long run of sleep cycles. The tables give no error bars.

## 6.2 Route two: direct edits of a known direction

If a behavior lives along one direction in the hidden states, it can be removed or added through the weights with no training.

- **Removal is exact.** Refusal in 13 open chat models is carried by one direction. Projecting it out of every matrix that writes into the main hidden path gives the same result as removing it during each run ([[One direction controls refusal (Arditi 2024)]]). General benchmarks mostly stay within their error bands, but one truthfulness benchmark drops in every model.
- **Removal from a few components.** In reasoning models distilled from DeepSeek-R1, reasoning length is a direction. Projecting it out of about 4% of attention heads (about 0.2% of parameters) fixes too-short reasoning: GSM8K accuracy of the Llama3-8B variant rises from 82.26 to 89.44 ([[ThinkEdit - edit weights to think longer (Sun 2025)]]).
- **Addition with forward passes only.** A steering vector can be turned into one rank-one edit per attention output matrix. On Llama-3.1-8B this raises a sycophancy score from 3.60 to 94.64, more than steering alone (63.86), with general knowledge within 0.15 points of the base ([[TFTV - turn a steering vector into a weight edit (Perin 2026)]]). The edits change 6 to 17 layers, are tuned per trait with an outside judge, and sit near the point where fluency breaks.
- **Sparse edits.** Editing only the heads and neurons best aligned with a steering vector beats steering at matched utility, but utility still falls against the base model: cutting reasoning length in Qwen3-4B-Thinking lowers average accuracy from 87.8 to 77.3 ([[Steer2Edit - steering into small weight edits (Sun 2026)]]).

In all four, the direction comes from contrast sets, labels or a judge chosen by the authors. The edits suit behaviors that are close to on-or-off, such as refusal, better than graded qualities; this is our reading of the limits the papers state.

**Direct edits have side effects on disposition.** Removing the refusal direction changes how two model families decide on a task that contains nothing to refuse. Over 21,600 stock decisions, the edited models choose the optimistic option more often (+12.2 and +7.4 percentage points), justify themselves at greater length and use fewer words of doubt, and their stated confidence moves in opposite directions in the two families ([[One weight edit shifts a model's disposition (Fafuła 2026)]]). This is one edit method, one task and one language. The author names the missing work: a broad battery of preferences, a second edit method, and a mechanism.

## 6.3 Route two, continued: weight-space programming

A different kind of direct edit lets a strong model read weights and write changes by reasoning.

- **The original result.** A frontier model edited about 0.016% of the weights of Qwen3.5-0.8B and raised its MATH-500 score from 7.9% to 48.1%, mostly by stopping repetitive reasoning loops ([[WSP - a model reads and edits weights (Takehi 2026)]]). The low starting score is itself a loop effect: 93% of the base model's answers hit the token limit. The method struggles when a fault is spread across the network.
- **The key edit is simple.** It acts like a nearly constant push along one direction, and a sort over 8 low-variance neurons gives the same result, 67.0% against 67.4% ([[A simple sort replaces the anti-loop edit (Fischetti 2026)]]). A plain discrete optimizer does better than the agent: 54.6% against 51.7% under one protocol, with 4 forward-pass requests, no language-model tokens and about $0.90 of GPU time, where the agent used 89.7 million tokens ([[A cheap optimizer beats the agent's weight repair (Salloum 2026)]]; abstract only).
- **Replication is uneven.** On two model sizes, held-out gains reach 29.45 points on MATH-500 from changing 1,023 values, but 6 of 16 runs keep the original weights because no edit could be confirmed, and gains are smaller on the larger model ([[Exploring WSP - small weight edits, uneven results (Hu 2026)]]).
- **Under strict audits, patching mostly fails.** On 42 audited tasks with metered forward passes, the best fully tested agent scores 0.535 overall and 0.404 on fixing networks ([[WeightBench - models cannot yet patch models (Marasini 2026)]]). Scores are lower bounds, because flagged runs count as zero until reviewed.
- **What the edits do.** Two abstract-only reports say that one model's edits act at the output, through sampling temperature and one token, and that reading weights is mostly reading the input layer ([[Claude's WSP edits act at the output (Kundu 2026)]], [[Reading weights is mostly reading inputs (Goworek 2026)]]).
- **Beyond repair.** A frozen language model can write "weight programs" that install a new skill in small vision and control networks, and the same program works on independently trained copies, keeping 83 to 110% of the gain ([[WeightCode - a model writes programs that edit weights (Li 2026)]]). The goal and the task knowledge come from the experimenter.

**A model edits itself.** An open 27B model is given its own weights, its graded answers on practice problems, and tools to run itself and read its hidden states, with gradients blocked ([[A model rewrites its own weights (Fan 2026)]]). It finds that its wrong answers mostly run out of tokens in loops, takes the difference between the mean hidden states of answers that finish and answers that do not, and removes 5% of that direction from two matrices of one layer. On 490 held-out problems accuracy rises from 57.2% to 61.3% and 63.8% in two sessions. In 5 of 8 sessions the model withdraws its edit after testing it. Smaller models of the same family fail: the 2B model makes no edit, and the 4B and 9B models break themselves. Three limits: graded answers decide which edit is kept; the gain is again a loop fix; and each session starts from the original weights, which the authors call "a first step toward" recursive self-improvement.

## 6.4 Self-directed training, and self-improvement that leaves the weights alone

SEAL lets a model write its own fine-tuning data and settings. Reinforcement learning then rewards the self-written edits that improve a downstream score after the update ([[SEAL - models write their own training data (Zweiger 2025)]]). It handles change that is spread over the network, which direct edits do not. Each step needs an inner fine-tune, forgetting across many edits is a stated problem, and the headline result is narrow (8 selected puzzle tasks on a 1B model). A model's own verbal quality scores can also drive preference training over three rounds ([[Self-rewarding language models judge and train themselves (Yuan 2024)]]).

Much recent "recursive self-improvement" does not touch the base weights at all. Models rewrite their own system prompts in a loop ([[Self-modifying prompts keep the same core values (Stroganov 2026)]]). A frozen model edits its own prompts, skills and memory behind a gate that accepts only net improvements ([[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]). Other systems refine a store of skills and memories, alternate workflow search with fine-tuning on their own outputs, or run rounds of data selection and training [@Zhu 2026; @Lee 2026; @Wang 2026]. Section 7 and Section 8 return to what these loops do to reliability and to values.

## 6.5 Who chooses the change, and who checks it?

| Method | Who proposes the change | What decides it is kept | Gradients |
|---|---|---|---|
| Learned memory (Titans, Hope) | A learned rule driven by surprise | Nothing; the rule always applies | Yes, at run time |
| Sleep | The model writes its own training examples | A gradient score, then an outside task score | Yes |
| SEAL | The model writes its own training data | An outside task score | Yes |
| Self-rewarding training | The model generates and ranks responses | Its own verbal score, under a human-made rubric | Yes |
| Direction removal and steering-to-weights | The experimenter | Benchmarks and an outside judge | No |
| Weight-space programming | A larger outside model | A development-set score | No |
| Self-rewriting (Fan) | The model, from its own hidden states | Its own tests on graded practice answers | No |

Two things stand out. First, proposing and checking are separate roles, and they are filled by different parties in almost every method. Second, no row has an internal evaluation signal of the kind described in Section 5 in the checking column. The signal that decides is a task score, a judge, a rubric or graded answers.

## 6.6 Cost, compared honestly

Direct edits are often presented as cheaper than training. The evidence is mixed. A direction edit needs only forward passes and a contrast set. But the agent that found the best-known weight repair used tens of millions of tokens, a plain optimizer then found a better repair for under a dollar, and the self-editing sessions each take hours on a GPU. On the other side, Sleep costs 4 times more per step than plain fine-tuning, but reaches a given maths score in 3.6 to 4.8 times less wall-clock time. The real differences between the routes are these. Direct edits need no training data and no new architecture, change very few values, and can be inspected. Learned memory handles new knowledge and change that is spread over the network, and needs gradient updates and capacity that is set aside in advance.

## 6.7 Changes made again and again

A model that develops over time must survive many changes. The evidence is thin on both routes.

- **Direct edits pile up badly.** When the fact editors ROME and MEMIT make many edits to one model, the model forgets earlier edits and loses general ability, first slowly and then suddenly ([[Many sequential weight edits cause sudden forgetting (Gupta 2024)]]). Even a single edit can collapse a model, nearly all tested methods collapse after a few edits on hard cases, and the change in perplexity after an edit is a cheap warning sign ([[A few edits can collapse a model (Yang 2024)]]; abstract only). Later work traces the collapse to a growth loop in the size of the edited weights and reports a one-line fix that extends the usable number of edits more than 4 times [@Liu 2026b]. These studies edit facts, not behaviors.
- **The self-editing model has not been run in sequence.** Each of its sessions starts from the original weights (Section 6.3).
- **Learned memory has been run for two tasks.** Sleep nearly keeps its single-language score after learning two languages in sequence, where fine-tuning forgets (Section 6.1). No long run is reported.
- **A long run of self-judged training decays.** A small model that fine-tunes itself each night on the attempts it judges good improves for about a week and then loses almost all of it; over a simulated year it ends below its start ([[Self-judged nightly learning rises then decays (Kongsilp 2026)]]). Section 7 covers this.

## 6.8 Summary

- Weights can change after deployment by two routes: learned memory inside a suitable architecture, with gradients, and direct edits of an ordinary model, without gradients.
- Direct edits work best for near on-or-off behaviors and for repairing one local fault. Under strict audits, patching mostly fails, and a simple optimizer can replace the editing agent once the goal is known.
- One model has edited its own weights. It works only at 27B, the gain is small, graded answers decide, and no edit builds on an earlier one.
- Learned memory reports low forgetting and small gains over two sequential tasks, with outside scores deciding what is kept.
- Direct edits change more than their target: one edit shifted two models' dispositions. Nobody has measured a broad set of preferences before and after a weight change, on either route.
- For the loop of this review: the persist step exists in several forms. In none of them does the model's own evaluation decide what is kept, and in none is the change followed by a check of what it did to the model's preferences or to its view of itself.

## Log
- 2026-11-20: first draft and number checks ([[2026-11-20 number check]]); self-rewriting (Fan) added after a check in the PDF.
- 2026-11-24: rewritten for the final paper around two routes (learned memory, direct edits). Added Titans, Nested Learning, Sleep, Irie, Backpropamine, Fafuła, Salloum, WeightCode, Stroganov, Gupta, Yang, Kongsilp; a cost comparison; repeated changes. The old open doubts moved to Section 9.5.
