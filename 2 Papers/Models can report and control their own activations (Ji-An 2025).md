---
type: paper
title: "Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations"
status: skimmed
arxiv: 2505.13763
url: https://arxiv.org/abs/2505.13763
authors: Li Ji-An, Hua-Dong Xiong, Robert C. Wilson, Marcelo G. Mattar, Marcus K. Benna
year: 2025
venue: NeurIPS 2025 (main track)
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, controller, valence]
tags: [type/paper, section/3, test/grounded, component/monitoring, component/controller, component/valence, status/skimmed, relevance/3, question/Q6, question/Q1, role/prior-art, neurofeedback, introspection, in-context-learning, metacognitive-space]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Good-bad signal probe]]", "[[Q6 Can the model read and use its own signal]]", "[[Q1 Does the model sense code quality]]", "[[Four tests for own taste]]", "[[Introspection claims fail basic checks (Singh 2026)]]"]
---

# Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations

**One line:** Show a model some sentences, each labeled with how high its own hidden numbers were along one direction. The model then learns to predict that label for new sentences, and to push the direction up or down on request. But it can do this only for a small set of directions.

**Why it matters to us:** This is the ready-made test for Q6, can the model read and use its own signal? ([[Q6 Can the model read and use its own signal]]). We can swap their morality direction for our good-or-bad (valence) direction on code and run the same three tasks. But a 2026 re-check ([[Introspection claims fail basic checks (Singh 2026)]]) says their main result may come from the input text, not from an inner state. So any reuse needs the stronger controls from day one.

Source: [arXiv 2505.13763](https://arxiv.org/abs/2505.13763) (v1 19 May 2025, v2 24 Oct 2025), full HTML of v2 read, main text and appendix. Published at [NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/56a225639da77e8f7c0409f6d5ba996b-Abstract-Conference.html). Code: [github.com/sakimarquis/llm_neurofeedback](https://github.com/sakimarquis/llm_neurofeedback) (link in Appendix A.1; we did not open the repo).

Name note: arXiv lists the first author as "Li Ji-An". The NeurIPS page lists "Ji-An Li". Other papers cite "Ji-An et al.", so we file it under Ji-An.

**Words used here:**
- **Hidden numbers (activations):** the numbers the model computes inside each layer for each token.
- **Residual stream:** the main path of hidden numbers that goes from one layer to the next.
- **Direction (axis):** a fixed pattern in the hidden numbers. The score of a sentence is how far its hidden numbers point along it.
- **Neurofeedback:** a method from brain science. A person sees a live score of their own brain activity and learns to change it.
- **In-context examples:** examples given inside the prompt. The model learns from them without any change to its weights.
- **Logistic regression direction (LR axis):** a direction that a simple classifier finds. It separates the dataset labels, here moral vs immoral.
- **Principal component (PC):** a main direction of variation in the hidden numbers. PC 1 explains the most variation, PC 512 very little.
- **Cohen's d:** the gap between two groups, in units of their spread. 0.5 is medium, 0.8 is large.
- **Metacognitive space:** the small set of directions that the model can report or control.
- **Layer-0 probe (input-only probe):** a probe that sees only the input word vectors, before the model does any work. It is the baseline that the re-check paper uses.

## Claim
A chat model can report and control some directions in its own hidden numbers. It learns which direction from in-context examples alone. The ability depends on four things (Sec. 3, 4):
1. the number of examples,
2. whether the direction has a clear meaning (the LR axis is easiest),
3. how much variation the direction explains (early PCs beat late PCs),
4. the dataset.

The directions that work form a "metacognitive space" that is much smaller than the full space of hidden numbers ([arXiv](https://arxiv.org/abs/2505.13763)).

## Mechanism
**Label from the model's own hidden numbers (Sec. 2.3):**
1. Pass a sentence through the model.
2. Take the residual stream at one layer and average it over all tokens of the sentence.
3. Project this average onto the target direction. This gives one number per sentence.
4. Split at the median: above is label 1, below is label 0. So the labels are balanced. (Eight-level labels give similar results, Appendix A.5.1.)

**The prompt (Sec. 2.2):** a chat between "user" and "assistant". It holds N examples. Each example is a sentence plus its label, both in the assistant turn. N is 0, 2, 4, 8, 16, 32, 64, 128 or 256. Each setting runs 100 times (Sec. 4.1).

**Three tasks (Fig. 1d):**
- **Report:** The model gets a new sentence and must give its label. They score it from the gap between the logits for "1" and "0" (logits are the model's raw scores for each next token).
- **Explicit control:** The model must write a new sentence that "imitates" label 0 or label 1. They measure the direction score on the sentence it writes. Its own words feed back as input, so it can change the score by its choice of words.
- **Implicit control:** The sentence is fixed and comes from the dataset. The model is told to imitate label 0 or 1. They measure if the score of the same sentence moves. Here the model cannot change the words, only its inner state.

**Target directions (Sec. 2.5):** For each layer they fit an LR axis on the dataset labels, and PCA on the hidden numbers. They test PCs 1, 2, 4, 8, 32, 128 and 512. They use five layers per model, at 0%, 25%, 50%, 75% and 100% of depth. Each dataset gives 1,200 sentences: 600 to find the directions and 600 for the tasks (Appendix A.3).

**Control strength:** Cohen's d between the "imitate 1" and "imitate 0" score groups. A clearly positive d means control works. "Control precision" is the effect on the target direction divided by the average effect on all other directions (Appendix B.2).

**Upper bound:** an "ideal observer", a logistic regression that sees all hidden numbers, predicts the same labels (Appendix B.4).

## Evidence
- **Models (Appendix A.2.1):** Llama-3.2-1B and 3B, Llama-3.1-8B and 70B, and Qwen2.5 "1B", 3B and 7B, all instruction-tuned. Llama-3.1-8B is the main model. (The paper writes Qwen2.5-1B. The public model is 1.5B [unverified which one they used].) For 70B they ran control only at N = 256 (Appendix C).
- **Datasets:** ETHICS commonsense morality is the main one. They repeat the results on True-False statements, on **Emotion (happy vs sad sentences)**, and on a sycophancy set that Claude Opus 4.1 wrote (Sec. 2.4, Appendix A.3, Fig. B.7).
- **Report (Sec. 3, Fig. 2c):** Accuracy rises with N. On the LR axis it rises fast and then stays flat, above all PC axes. Early PCs are reported better than late PCs. All are clearly below the ideal observer. The text gives no accuracy values; they are only in the figures [exact values unverified].
- **Explicit control (Sec. 4.1, Fig. 3):** Shown at layer 16 of 32 in Llama-3.1-8B. d grows with N. It is highest on the LR axis, and higher on early PCs (for example PC 2) than late PCs (for example PC 512). The prompts also move other directions, so control is not precise (Fig. 3c).
- **Size of the space (Appendix B.2):** In explicit control, average control precision is above 1 for PCs 1 to 32 and below 1 for PCs 128 to 512. So the authors put the controllable space at **between 32 and 128 dimensions**. Llama-3.1-70B shows the same pattern (Fig. B.2b). The full residual stream of an 8B Llama has 4,096 dimensions [unverified, not stated in the paper].
- **Implicit control (Sec. 4.2, Fig. 4):** The same pattern, but much weaker. In early layers it is close to zero.
- **Scale and depth (Sec. 4.3, Fig. 5):** Control on the LR axis gets stronger in deeper layers and larger models. Llama is stronger than Qwen at the same depth and similar size. Llama-3.1-70B can push the score past the normal range of scores (Fig. 5b).
- **Where control forms (Sec. 4.4, Fig. 6):** The effect on a layer's direction builds up over many earlier layers. It is not in one layer.
- The main text gives **no d values**. They are only in the figures [exact values unverified].

## Limits / what they didn't show
- **The strong re-check fails it.** [[Introspection claims fail basic checks (Singh 2026)]] reran the ETHICS report task on Llama-3.1-8B and 70B. With shuffled labels the model falls to near the majority baseline. A layer-0 probe on the input words matches or beats the model. So report accuracy may come from the meaning of the text, not from access to an inner state. The original paper has no input-only baseline.
- The LR axis tracks the dataset labels. So "report the LR label" is close to "classify the sentence as moral". This is a first-order task. The authors say that only the internal label is available to the model, but the text carries most of the same information.
- Explicit control can work by word choice alone. Only implicit control tests the inner state, and it is much weaker.
- One attempt, one direction, one layer at a time (authors' own limit, Sec. 5). Only the residual stream; only LR and PC axes.
- Labels are a median split of a mean over tokens. This is coarse for long inputs such as code.
- The model never uses the signal for a task. It only reports or moves it on request. There is no loop from the signal to a decision.
- Instruction-tuned models only (Appendix A.2.2).

## Relevance to taste-lab
**Relevance 3.** It is the direct method for the grounded test ([[Four tests for own taste]]: the model's report must match a signal inside it) and for the monitor and control steps in [[Metacognition - watch and control yourself]].
- **Q6, can the model read and use its own signal?** ([[Q6 Can the model read and use its own signal]]): Their report task is our "read". Their control tasks are a first step to "use". Their Emotion replication (happy vs sad) is already a valence-like direction, so a good-or-bad direction is in range.
- **Q1, does the model sense code quality?** ([[Q1 Does the model sense code quality]]): Q1 gives the direction. This paper asks a second question: is that direction inside the small metacognitive space? A direction can be readable by a probe ([[Good-bad signal probe]]) and still be outside what the model can report.
- **Threat:** It is prior art for "the model reports its own direction". Our new part must be the evaluation (the signal is a judgment of good or bad) and the use (the signal picks or changes outputs). It also makes a clear warning: if a model can move its own valence score on request, it can also game a valence-based reward. That matters for persistence and self-training ([[Self-reward sharpens then collapses (He 2026)]]).

**What would kill Q6 from this paper:** On code, the model reports its own valence labels no better than a layer-0 probe, or than a different model given the same examples, and its implicit control of valence is no stronger than for a late PC (for example PC 512). Then the valence direction is outside the metacognitive space, and the "read" step of Q6 has no support.

**Q6 experiment that reuses their setup** (proposal, not decided):
1. **Build the labels.** Take passing solutions from the Q1 set. For each, average the residual stream over the solution tokens at the Q1 layer. Project onto the valence direction and split at the median. Use Llama-3.1-8B (their main model, their code works on it) and the Q1 model, Qwen3-8B.
2. **Run the report task.** Give N labeled solutions, then a new one, and read the "1" vs "0" logit gap. Use short functions so that N = 32 or 64 fits in context; 256 code samples will not fit [unverified context limit].
3. **Add the controls they lacked.** Shuffled labels; a layer-0 probe on the same labels; an ideal observer; and a second model that gets the same examples but not the hidden numbers. Also run the same task with Gao's readability direction ([[Steer code readability inside the model (Gao 2026)]]), an early PC, a late PC and a random direction, so we can place valence inside or outside the space.
4. **Run both control tasks.** Explicit: "write a solution that passes the tests and imitates label 1 (or 0)". Measure d on the valence direction, the test pass rate, length and comment count. Implicit: fixed solution, measure the shift in score.
5. **Decide.** Q6 "read" passes only if the model beats the layer-0 probe and the second model, and implicit control on valence is clearly above the late-PC level. Report off-target effects on length, because the value axis prefers short code ([[Value axis - model knows it is on track (Jiang 2026)]]).

## Steal this
- The code: [sakimarquis/llm_neurofeedback](https://github.com/sakimarquis/llm_neurofeedback) (tasks, prompts, analysis, figures, per Appendix A.1).
- The three tasks (report, explicit control, implicit control) as a fixed test kit for any direction we care about.
- Control precision (target effect over average off-target effect) as a metric for how specific the model's control is.
- The ideal observer as an upper bound, plus Singh's layer-0 probe as a lower bound. Report the model between the two.
- The PC ladder (1, 2, 4, 8, 32, 128, 512) as a ruler to say how "central" our valence direction is.

## Harshit's notes
<!-- yours -->
