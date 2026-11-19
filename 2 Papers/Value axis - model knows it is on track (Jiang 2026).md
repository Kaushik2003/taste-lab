---
type: paper
title: "The Value Axis: Language Models Encode Whether They're on the Right Track"
status: skimmed
arxiv: 2606.17056
url: https://arxiv.org/abs/2606.17056
authors: Nick Jiang, Isaac Kauvar, Jack Lindsey
year: 2026
venue: preprint
relevance: 3
section: 4
tier: deep
tests: [grounded, self-reinforcing]
components: [valence, controller, monitoring]
tags: [type/paper, section/4, test/grounded, test/self-reinforcing, component/valence, component/controller, component/monitoring, status/skimmed, relevance/3, question/Q2, question/Q1, value-axis, steering, code, dpo, confidence, backtracking]
links: ["[[Good-bad signal probe]]", "[[Field map - Models judge good and bad]]", "[[Q1 Does the model sense code quality]]", "[[Q2 Can the model steer its own code]]", "[[Neuromodulators as learning settings]]", "[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# The Value Axis: Language Models Encode Whether They're on the Right Track

**One line:** Inside Qwen3-8B there is one direction that means "my current plan is working". It scores correct code above broken code, and pushing the model along it changes how often the model goes back and how much code it writes.

**Why it matters to us:** This is the closest existing version of the good/bad signal we want to read. It already tells correct code from broken code. But it also prefers shorter code, so we must check that our signal tracks readability and not only length.

Source: [arXiv 2606.17056](https://arxiv.org/abs/2606.17056), full HTML read. Authors: Jiang (Stanford, Anthropic Fellows), Kauvar and Lindsey (Anthropic).

**Words used here:**
- **Hidden numbers (activations):** the numbers the model computes inside each layer for each token.
- **Residual stream:** the main path of hidden numbers that goes from one layer to the next.
- **Direction (axis):** a fixed pattern in the hidden numbers. "Linear" means one direction is enough to read the signal.
- **Score:** how closely the hidden numbers point along the direction (cosine similarity: 1 is the same direction, 0 is unrelated).
- **Steering:** adding a direction to the hidden numbers while the model runs, to change its behavior.
- **Prefill:** the step where the model reads given text before it writes new text.
- **Backtrack:** the model stops and goes back to try a different approach.
- **AUROC:** how well a score separates two groups. 0.5 is chance, 1.0 is perfect.
- **Effect size d (Cohen's d):** the gap between two groups, in units of their spread. 0.5 is medium, 0.8 is large.
- **SFT and DPO:** two ways to train a model. SFT teaches it to copy example answers. DPO teaches it to prefer one answer over another.
- **LoRA adapter:** a small set of extra trainable weights. The base model does not change.
- **Valence:** a "good or bad" signal inside the model.

## Claim
A model stores the "value" of its current path as one direction in its hidden numbers. Value here means: how likely the current plan is to reach the goal. This value affects how confidently the model keeps going. Training (DPO, SFT) moves it.

## Mechanism
- **Data (Sec. 2.1):** Claude Opus 4.6 wrote 300 made-up conversations. In each one, a player learns from feedback inside the conversation (in-context RL). The player tries to guess a hidden rule. The rule comes from a pool of 50: 15 about word form (syntactic), 35 about meaning (semantic). The game runs over 3 to 8 Wikipedia paragraphs. The player gets +1 or -1 feedback and up to 5 tries per paragraph. The player "finds" the rule at a random paragraph between 2 and 6.
- **Axis:** They use the hidden numbers at layer 21. They take the average after the first token that follows the rule, minus the average before it (a difference in means). They use the first paragraph after the rule is found. Then they average this over all conversations.
- **Score:** the average cosine similarity between each token's hidden numbers and the axis.
- **Steering (Sec. 3.2):** They add α times the axis (scaled to length 1) to the residual stream at layer 21. They do this during prefill and while the model writes. α takes the values -50, -25, 0, 25 and 50. Each value is a percent of the average size of the residual stream.
- **DPO test (Sec. 4):** They train 50 LoRA adapters (rank r=16, β=0.1, 6 epochs). Each adapter teaches the model to prefer one word out of 4 or 5. Then they check if the axis ranks the preferred word highest.

## Evidence
- New rules, not used to build the axis: AUROC above 0.95 at layers 21 to 22 (Sec. 2.2).
- Math (AIME, 455 questions): they read the score on the last ten tokens before the answer. It separates answers where the model says it is confident from answers where it is not (AUROC above 0.75). Runs that backtrack score lower, even when length is held equal. The score drops just before a backtrack (Sec. 3.1).
- **Code (Sec. 3.1):** 225 LeetCode problems from DebugBench. Correct solutions score higher than buggy versions made by GPT-4. They also score higher than three made-up kinds of damage. The effect size is d = 1.05 for shuffled lines (large) and 0.69 for obfuscated variable names (medium). Syntax errors and logic bugs separate only moderately (the paper gives no exact number).
- **Steering:** Toward high value, the model backtracks less and says "yes, I'm confident" more. Toward low value, it backtracks more and explores more. On LeetCode, high value gives **fewer lines, fewer comments, fewer type hints**. Low value gives longer code with many comments (Sec. 3.2). The paper reports no task accuracy under steering.
- **DPO:** The trained models pick the preferred word 27% to 88% of the time (selection accuracy 0.27 to 0.88). Before DPO, the axis ranks the preferred word first in 21% of trials. After DPO, it is 36.2% (44 of 50 models go up). The rise happens at the start of the model's own reply (prefill: 24.1% to 35.9%). It does not happen at the user prompt (19.3% to 20.2%).
- **SFT (Sec. 5.2):** Training on GSM8K and ARC raises the axis on new questions of the same kind. It does not raise it on MATH-500.
- **Real prompts (Sec. 5.1):** The chat-trained Qwen gives low value to open-ended and politically sensitive prompts. The base model (before chat training) does not.
- The result also holds on Llama-3.3-Nemotron-Super-49B: AUROC about 0.8 on 13 new rules (appendix).

## Limits / what they didn't show
- One main model (Qwen3-8B) plus one check on a 49B model. They did not test larger models (Sec. 7).
- The researchers add the steering at a fixed strength. The paper does not show the model reading this axis to make a choice. The story "the model uses it to decide whether to keep going" rests on correlation plus steering by the researchers.
- No accuracy under steering. So we do not know if high-value steering helps or hurts correctness.
- The code damage is crude (shuffled lines, renamed variables). They never test code that passes the tests but is ugly.
- The data is made up and written by Opus. The authors say the axis may carry unwanted parts, and other recipes could give other axes.
- Small count errors in the text: 425 vs 455 AIME items, and 10 vs 11 avoidance models.

## Prior-art check
Two questions decide if this paper already did our idea.
- **Does the model's own signal steer its own thinking or learning? Partial.** The signal comes from the model's own hidden numbers, and it does change reasoning (backtracking, length). But the researchers add it at a fixed α. The model never chooses. Training changes the value (Sec. 4, 5.2), but the value never controls training. There is no closed loop.
- **Does it make a small, permanent edit to the weights? No.** Steering works only while the model runs. DPO and SFT are normal LoRA training on data, not an edit along the axis.

## Relevance to taste-lab
**Relevance 3. This is the nearest existing version of our good/bad signal** ([[Good-bad signal probe]]).
- **Q1, does the model sense code quality?** ([[Q1 Does the model sense code quality]]): The axis already separates correct code from broken code. Q1 must ask a harder question: when all solutions pass the tests, does the signal track readability? This paper does not test that.
- **Warning, a hidden third factor:** High value goes with shorter code, fewer comments and fewer type hints. So a value or valence readout may reward short code, not readable code. The Q1 controls for length and comment density are required, not optional.
- **Q2, can the model steer its own code?** ([[Q2 Can the model steer its own code]]), and the controller ([[Neuromodulators as learning settings]]): Low value causes backtracking and exploration. That is a ready "explore more" knob for a Doya-style controller (a controller that sets learning rate, exploration and time scale).
- **Threat to our novelty:** An Anthropic group already uses "value of the path + steering + DPO". Our difference must be the closed loop: the model's own readout chooses and controls training. The other difference is our test on readability among solutions that all pass.
- **Grounded test** ([[Four tests for own taste]]; the model's report must match a signal inside it): DPO raises the axis for the rewarded behavior. This is a clean way to show that training changes the internal signal, not only the output.

## Steal this
- The game recipe: build a value axis from a made-up rule-guessing game, with no human labels.
- DebugBench correct vs damaged code, as a quick check before the first stage of Experiment 1 (stage A of Q1).
- A metric: the rank the axis gives to the preferred option. It shows how training moves the signal.
- Read the signal at the start of the model's own reply, not at the user prompt.
- We did not check if the code is released [unverified].

## Harshit's notes
<!-- yours -->
