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

**One line:** Qwen3-8B has one linear direction that says "my current strategy is working". It scores correct code above broken code, and pushing along it changes how often the model backtracks and how much code it writes.

Source: [arXiv 2606.17056](https://arxiv.org/abs/2606.17056), full HTML read. Authors: Jiang (Stanford, Anthropic Fellows), Kauvar and Lindsey (Anthropic).

## Claim
Models linearly encode the "value" of their current trajectory: an estimate of how likely the ongoing strategy is to reach the goal. This estimate shapes how confidently the model keeps going, and training (DPO, SFT) moves it.

## Mechanism
- **Data (Sec. 2.1):** 300 synthetic in-context RL conversations written by Claude Opus 4.6. A player guesses a hidden rule (pool of 50: 15 syntactic, 35 semantic) over 3 to 8 Wikipedia paragraphs, with +1/-1 feedback and up to 5 tries per paragraph. The rule is "discovered" at a random paragraph between 2 and 6.
- **Axis:** difference in means at layer 21: mean activation after the rule-satisfying token minus mean before it, in the first paragraph after discovery, averaged over conversations.
- **Score:** mean cosine similarity between a sequence's token activations and the axis.
- **Steering (Sec. 3.2):** add α times the unit axis to the layer 21 residual stream during prefill and decoding. α swept over {-50, -25, 0, 25, 50}, in percent of the average residual norm.
- **DPO probe (Sec. 4):** 50 LoRA adapters (r=16, β=0.1, 6 epochs) each trained to prefer one word out of 4 or 5. Then they check whether the axis ranks the preferred word highest.

## Evidence
- Held-out rules: AUROC above 0.95 at layers 21 to 22 (Sec. 2.2).
- AIME (455 questions): projection on the last ten tokens before the answer separates confident from unconfident verbal answers, AUROC above 0.75. Rollouts that backtrack score lower after controlling for length, and the score dips just before a backtrack (Sec. 3.1).
- **Code (Sec. 3.1):** 225 LeetCode problems from DebugBench. Correct solutions score higher than GPT-4-made buggy versions and three synthetic corruptions. Cohen's d = 1.05 for shuffled lines, 0.69 for obfuscated names. Syntax errors and logic bugs separate only moderately (no exact number given).
- **Steering:** toward high value gives fewer backtracks and more "yes, I'm confident". Toward low value gives more backtracking and exploration. On LeetCode, high value gives **fewer lines, fewer comments, fewer type hints**. Low value gives longer, heavily commented code (Sec. 3.2). No task accuracy is reported under steering.
- **DPO:** selection accuracy 0.27 to 0.88. The axis ranks the preferred word first in 21% of trials before DPO and 36.2% after (44 of 50 models go up). The rise happens at the assistant prefill (24.1% to 35.9%), not at the user prompt (19.3% to 20.2%).
- **SFT (Sec. 5.2):** training on GSM8K and ARC raises the axis on held-out in-domain answers but not on MATH-500.
- **In the wild (Sec. 5.1):** post-trained Qwen gives low value to open-ended and politically sensitive prompts. The base model does not show this.
- Generalizes to Llama-3.3-Nemotron-Super-49B (AUROC about 0.8 on 13 held-out rules, appendix).

## Limits / what they didn't show
- One main model (Qwen3-8B) plus a 49B check. Larger models untested (Sec. 7).
- Steering is injected by the experimenters at a fixed strength. The paper does not show the model reading this axis to make a decision. The "model uses it to decide whether to persist" story rests on correlation plus experimenter steering.
- No accuracy under steering, so we don't know if high-value steering helps or hurts correctness.
- Code corruptions are crude (shuffled lines, renamed variables). Passing-but-ugly code is never tested.
- Built from synthetic, Opus-written data. The authors say the axis may carry spurious parts and other recipes could give other axes.
- Small count mismatches in the text (425 vs 455 AIME items; 10 vs 11 avoidance models).

## Prior-art check
- **A (own signal steers own reasoning/learning): partial.** The signal is the model's own activation and it causally changes reasoning (backtracking, verbosity). But the experimenter adds it at a fixed α; the model never chooses. Training shapes the value (Sec. 4, 5.2), but the value never gates training. No closed loop.
- **B (permanent small weight edit): no.** Steering is inference-time only. DPO and SFT use ordinary LoRA training on data, not an edit along the axis.

## Relevance to taste-lab
**Relevance 3. This is the nearest existing object to our evaluator** ([[Good-bad signal probe]]).
- **Q1** ([[Q1 Does the model sense code quality]]): the axis already separates correct from broken code. Our Q1 must ask the harder question: among solutions that all pass, does it track readability? That is not tested here.
- **Confound warning:** high value goes with shorter code, fewer comments and fewer type hints. A value or valence readout may reward terseness, not readability. Q1's length and comment-density controls are required, not optional.
- **Q2 and the controller** ([[Q2 Can the model steer its own code]], [[Neuromodulators as learning settings]]): low value causes backtracking and exploration. That is a ready "exploration" knob for a Doya-style controller.
- **Threat to novelty:** an Anthropic group already frames "value of the trajectory + steering + DPO". Our difference must be the closed loop (the model's readout chooses and gates) and the passing-solutions readability testbed.
- **Grounded test** ([[Four tests for own taste]]): DPO raises the axis for the rewarded behavior, a clean way to show that training changes the internal signal, not just the output.

## Steal this
- The in-context RL recipe: build a value axis from a synthetic rule-guessing game, no human labels.
- DebugBench correct-vs-corrupted as a quick sanity check before Q1 stage A.
- "Rank of the preferred option by the axis" as a metric for how training moves the signal.
- Read the signal at the assistant prefill, not the user prompt.
- Code release not checked [unverified].

## Harshit's notes
<!-- yours -->
