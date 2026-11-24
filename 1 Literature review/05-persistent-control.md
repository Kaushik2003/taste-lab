---
type: draft
status: draft
section: 5
tags: [type/draft, section/5, component/consolidation, test/self-reinforcing, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]"]
---

# 6. Changes that persist in the weights

Most control in language models is temporary: a prompt, a sampling choice, or a steering vector added during one run. Persistent control writes the change into the weights. Two routes exist, and papers almost never compare them. Learned memory builds the ability to change into the architecture and trains it. Direct edits write small changes straight into the weights of an ordinary pretrained model. The main finding is that weights can change by both routes, but where the model's own judgment decides which change stays, that judgment is its certainty or a verbal score; no method uses an evaluation signal read from the model's hidden states, and an outside score decides every direct edit.

## 6.1 Route one: learned memory

The idea that a system rewrites itself is old. Schmidhuber's Gödel machine was a theoretical design for a program that rewrites its own code once it has proved that the rewrite is useful [@Schmidhuber 2003]. Recent work scales run-time self-change to language models. Titans added a memory module that updated its own weights during use, more strongly for inputs that it predicted badly ([[Titans - a memory that learns from surprise at test time (Behrouz 2025)]]). Nested Learning generalized the design to a chain of memory blocks that update at different rates ([[Nested Learning - a model that learns its own update rule (Behrouz 2025)]]).

Sleep, the latest step, moved short-term memory into long-term weights in an offline phase ([[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]). The model first trained a small new block of weights to reproduce what a faster memory had learned. Then it "dreamed": it wrote synthetic training examples, fine-tuned a copy of itself on each, and rewarded the examples whose copy scored better on an outside task. The method ran on ordinary pretrained models of 1B to 8B, and its gains were modest: 1 to 3 points over the best other method on three maths benchmarks with an 8B model. Three limits matter here. Every update was gradient training. Outside task scores decided which dreams counted. And "continual" meant two tasks learned in sequence, not a long run of sleep cycles.

## 6.2 Route two: direct edits of a known direction

Direct editing of weights began with facts: ROME located a fact in one layer and rewrote it with a rank-one edit, the smallest structured change to a weight matrix [@Meng 2022a]. Later work wrote behaviors. One direction carried refusal in 13 open chat models, and projecting it out of the weights gave the same result as removing it during each run ([[One direction controls refusal (Arditi 2024)]]). A method that turned a steering vector, a direction added to the hidden states during a run, into rank-one weight edits raised a sycophancy score from 3.6 to 94.6, more than steering alone (63.9) ([[TFTV - turn a steering vector into a weight edit (Perin 2026)]]). In both, the authors chose the direction through contrast sets, labels, or a judge. Such edits also suit behaviors that are close to on-or-off, such as refusal, better than graded qualities; this is our reading of the limits the papers state.

Direct edits have side effects on disposition. Fafuła compared two model families before and after removal of the refusal direction, on a task that contained nothing to refuse. Over 21,600 stock decisions, the edited models chose the optimistic option more often (by 12.2 and 7.4 percentage points) and wrote longer justifications with fewer doubt words ([[One weight edit shifts a model's disposition (Fafuła 2026)]]). The study used one edit method and one task, and its author named the missing work: a broad battery of preferences, a second edit method, and a mechanism.

## 6.3 Weight-space programming and self-editing

A different kind of direct edit lets a strong model read weights and write changes by reasoning. In the original report, a frontier model edited about 0.016% of the weights of a 0.8B model and raised its score on a maths benchmark from 7.9% to 48.1%, mostly by stopping repetitive reasoning loops; 93% of the base model's answers had hit the token limit ([[WSP - a model reads and edits weights (Takehi 2026)]]). Follow-up work has qualified the result. A plain discrete optimizer found a better repair than the agent, 54.6% against 51.7% under one protocol, for about $0.90 of GPU time, where the agent had used 89.7 million tokens ([[A cheap optimizer beats the agent's weight repair (Salloum 2026)]]; abstract only). And patching mostly failed under strict audits: on 42 audited tasks, the best fully tested agent scored 0.535 overall and 0.404 on fixing networks ([[WeightBench - models cannot yet patch models (Marasini 2026)]]).

One model has edited itself. Fan and colleagues gave an open 27B model its own weights, its graded answers on practice problems, and tools to run itself and read its hidden states, and they blocked gradients ([[A model rewrites its own weights (Fan 2026)]]). The model found that its wrong answers mostly ran out of tokens in loops. It took the difference between the mean hidden states of answers that finished and answers that did not, and removed 5% of that direction from two matrices of one layer. On 490 held-out problems accuracy rose from 57.2% to 61.3% and 63.8% in two sessions. In 5 of 8 sessions the model withdrew its edit after testing it, and smaller models of the same family failed. Three limits apply. Graded answers decided which edit the model kept. The gain was again a loop fix. And each session started from the original weights: the abstract says that each edit improved on the last, but the body states that no session built on an earlier one.

## 6.4 Who proposes the change, and who decides whether it stays?

A third family lets the model direct its own training: SEAL let a model write its own fine-tuning data, and reinforcement learning rewarded the self-written edits that improved a downstream score ([[SEAL - models write their own training data (Zweiger 2025)]]). Table 4 sorts the weight-changing methods by two roles. Two recent surveys sort self-improving systems by similar axes, the target of the update and the signal that drives it [@Ren 2026; @Yang 2026]; Table 4 adds the direct-edit methods and separates the proposer from the decider.

**Table 4.** Methods that change weights, by who proposes a change and what decides whether it stays.

| Method | Who proposes the change | What decides whether it stays | Gradients |
|---|---|---|---|
| Learned memory (Titans, Nested Learning) | A learned rule driven by surprise | Nothing; the rule always applies | Yes, at run time |
| Sleep | The model writes its own training examples | A gradient score, then an outside task score | Yes |
| SEAL | The model writes its own training data | An outside task score | Yes |
| Certainty as reward (INTUITOR) | The model's own outputs | The model's own certainty | Yes |
| Self-rewarding training | The model generates and ranks responses | The model's own verbal score, under a human-made rubric | Yes |
| Direction removal and steering-to-weights | The experimenter | Benchmarks and an outside judge | No |
| Weight-space programming | A larger outside model | A development-set score | No |
| Self-editing (Fan) | The model, from its own hidden states | The model's own tests on graded practice answers | No |

Three observations follow. First, proposing and deciding are separate roles, and different parties fill them in most methods. Second, the model's own judgment decides in two rows only, and in both it is computed from the model's outputs: its certainty, or a verbal score. Section 7 shows that loops on exactly these two signals sharpen and drift. Third, no row uses an evaluation signal read from hidden states, and no gradient-free method uses the model's own judgment at all. The one self-editing model tested its own edit, but against answers that people had graded.

## 6.5 Repeated change, and cost

A model that develops over time must survive many changes, and the evidence is thin on both routes. When fact-editing methods made many edits to one model, the model forgot earlier edits and lost general ability, first slowly and then suddenly ([[Many sequential weight edits cause sudden forgetting (Gupta 2024)]]). Nobody has run the self-editing model in sequence, and learned memory has run for two tasks. Cost does not separate the routes clearly either: each self-editing session took hours on a GPU, and Sleep cost four times more per step than plain fine-tuning.

## Log
- 2026-11-20: first draft and number checks ([[2026-11-20 number check]]); self-editing (Fan) added after a check in the PDF.
- 2026-11-24: rewritten around two routes (learned memory, direct edits).
- 2026-11-24 (guides and critique): prose and past tense. Added the lineage (Gödel machine, test-time training, ROME, MEMIT, task arithmetic, activation steering, STOP, Darwin Gödel Machine), a row for certainty as reward, and a precise statement of who decides: the earlier claim that a signal outside the model's own evaluation decides in every method was wrong for INTUITOR and self-rewarding training. Table 2 is positioned against two surveys with similar axes.
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/05-persistent-control (long).md`.
