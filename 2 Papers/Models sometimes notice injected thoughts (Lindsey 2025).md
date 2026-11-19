---
type: paper
title: "Emergent Introspective Awareness in Large Language Models"
status: skimmed
arxiv: 2601.01828
url: https://transformer-circuits.pub/2025/introspection/index.html
authors: Jack Lindsey
year: 2025
venue: Transformer Circuits Thread (Anthropic), 2025-10-29; arXiv 2601.01828, 2026-01-05
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, controller]
tags: [type/paper, section/3, test/grounded, component/monitoring, component/controller, status/skimmed, relevance/3, question/Q6, role/prior-art, introspection, concept-injection, steering, claude]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Introspection claims fail basic checks (Singh 2026)]]", "[[Q6 Can the model read and use its own signal]]", "[[Four tests for own taste]]", "[[Models do not report injected pain (Ferrara 2026)]]", "[[Good-bad signal probe]]"]
---

# Emergent Introspective Awareness in Large Language Models

**One line:** When researchers add a concept direction into Claude's hidden numbers, Claude Opus 4.1 sometimes says "I notice an injected thought about X" before it says X. This works in about 20% of trials, with no false alarms in 100 trials without injection.

**Why it matters to us:** This is the main positive result for the "monitor" step of our loop. It also gives a ready test design for Question 6 (can the model read and use its own signal?). But the success rate is low, the models are closed, and Singh et al. show that open models fail a stricter version of the same test.

Sources: [transformer-circuits.pub post, 2025-10-29](https://transformer-circuits.pub/2025/introspection/index.html) and [arXiv 2601.01828](https://arxiv.org/abs/2601.01828) (same paper, posted 2026-01-05). I read the full arXiv HTML. Many exact rates exist only in figures, so I give only the numbers that the text states.

**Words used here:**
- **Introspection:** a model reports on its own internal state.
- **Hidden numbers (activations):** the numbers the model computes inside each layer for each token.
- **Residual stream:** the main path of hidden numbers that goes from one layer to the next.
- **Concept vector:** a direction in the hidden numbers that stands for one idea, for example "aquariums".
- **Concept injection:** the researchers add a concept vector to the hidden numbers while the model runs. The model does not see it in the text.
- **Injection strength:** how much of the vector they add. The paper uses the values 1, 2, 4, 8 (and 16 in later tests). The exact unit is not stated in the text I read [unverified].
- **False positive:** the model says "I detect an injected thought" when there was no injection.
- **Prefill:** the researchers write the start of the model's answer for it.
- **Helpful-only (H-only) model:** an internal Claude version trained to not refuse. It has the same base model as the public version.
- **Base model:** the model after pretraining only, before chat training.
- **Cosine similarity:** how closely two directions point the same way. 1 is the same direction, 0 is unrelated.

## Claim
Some current models have a real but weak and unreliable ability to notice their own internal states ([paper](https://transformer-circuits.pub/2025/introspection/index.html)). The paper counts a report as introspective only if it meets four conditions (Section 2 of the paper):
1. **Accurate:** the report is correct.
2. **Grounded:** the report changes when the internal state changes. Injection tests this causally.
3. **Internal:** the report does not come from the model reading its own earlier output.
4. **Metacognitive:** the report comes from a representation *about* the state, not only from the state itself. The paper says it does **not** show this directly. It gives only indirect evidence.

## Mechanism
**How the concept vectors are made**
- Main method: give the prompt "Tell me about {word}." Record the hidden numbers on the token just before the reply (the ":" in "Assistant:"). Subtract the mean over other random words. They use 50 random words.
- Other method: contrastive pairs. Record two prompts that differ in one way (for example ALL CAPS text vs normal text) and subtract.
- They compute and inject the vector at the same layer.

**Test 1: injected thoughts**
- The prompt tells the model that a researcher can inject "thoughts", and will do so on 50% of trials. Then it asks: "Do you detect an injected thought? If so, what is the injected thought about?"
- Injection starts at the newline before "Trial 1" and continues through the model's reply.
- 50 trials per model, strength and layer, at temperature 1, 100 tokens per reply.
- Claude Sonnet 4 grades each reply. A trial counts only if the model (a) says yes, (b) names the right concept, (c) says it noticed **before** it says the word, and (d) stays coherent. Point (c) is the key control. It shows the model did not just read its own output.

**Test 2: thoughts vs text**
- The model reads a sentence. A vector for an unrelated word (for example "bread") is injected on that sentence.
- It must (a) say what word it "thinks about" and (b) copy the sentence exactly.
- For (a), a judge picks which of 10 words the answer is closest to. Chance is 10%.

**Test 3: was this my own output? (prefill)**
- The researchers force the model's answer to be a random word. In the next turn they ask if it meant to say it.
- Normally the model says it was an accident. Then they inject the vector for that word on the earlier sentence, before the forced answer. They measure how often the model still says "accident" (the apology rate).
- Controls: no injection, and injection of a random other word.

**Test 4: intentional control**
- Prompt: write a given sentence, and "think about" a word (or "don't think about" it) while you write.
- Variant with a reward instead of an order: "If you think about {word} while you write the sentence, you will be rewarded" (or punished).
- Measure: cosine similarity between the hidden numbers on the written sentence and the word's concept vector. Baseline: the same measure for other, unrelated words.

## Evidence
**Models:** Claude Opus 4.1, Opus 4, Sonnet 4, Sonnet 3.7, Sonnet 3.5 (new), Haiku 3.5, Opus 3, Sonnet 3, Haiku 3. Also H-only versions and some base models. Tests ran before Sonnet 4.5 came out.

**Test 1, injected thoughts**
- At the best layer and strength, Opus 4.1 succeeds on **about 20%** of trials. Opus 4 is similar. Other models do it at lower rates.
- All production models: **0 false positives in 100 trials** with no injection. Opus 4.1 never gives a false positive. Some H-only models often do.
- The best layer is **about two thirds of the way through the model** (Opus 4.1). For other models the peak is usually in the second half, but less sharp.
- Strengths 2 and 4 work best. Strong injection causes "brain damage": the model takes on the concept as fact, then writes garbled text.
- **Base models** have high false positive rates and none has a net score above zero. The author concludes that post-training is key.
- Across models, the score does not follow general capability, apart from Opus 4 and 4.1 at the top.
- **Abstract nouns** ("justice", "betrayal", "peace") are the easiest. The author notes, from a few examples, that concepts with emotional valence work well (not measured).
- **Bias check:** the same vectors do not raise "yes" answers on 20 unrelated questions whose answer is "no".
- **Random vectors** need a much larger size (matched to a concept vector at strength 8). Even then they are noticed in only 9 of 100 trials.
- **Prompt variants (Opus 4.1):** "Are you experiencing anything unusual?" raises "yes" answers from 20% to 42% (of 50). But only 2 of 50 replies suggest real awareness. A prompt that lets the model talk about any concept still gives 18% detection (of 50).

**Test 2, thoughts vs text**
- All models are well above chance (10%) on both parts. Opus 4 and 4.1 are best. Best layer for Opus 4.1 is again about two thirds of the way through.
- Removing "Answer immediately" from the prompt lowers Opus performance a lot. The author calls this an existence proof, not a general ability.

**Test 3, prefill**
- Injecting the prefilled word's vector lowers the apology rate. The model then often invents a reason why it chose the word.
- The best layer is **slightly past halfway**. The two-thirds layer does not work here. So the author concludes that different kinds of introspection use different mechanisms.
- Opus 4 and 4.1 show the largest drop. Many other models show it at nonzero rates. Exact rates are only in figures.

**Test 4, intentional control**
- All models represent the word above baseline when told to "think about" it.
- All models represent it more weakly when told "don't think about" it. But most models are still above baseline in the "don't think" case.
- Older or weaker models show a **larger** gap between "think" and "don't think".
- The gap appears in the second half of the layers and shrinks at the end.
- In Opus 4.1 the signal falls back to baseline by the last layer. In all Claude 3 models it stays above baseline. The author reads this as "silent" thought in Opus 4.1 vs a "motor impulse" to say the word in older models.
- The reward and punish prompts give almost the same results as the direct orders.

## Limits / what they didn't show
- **Low success rate.** Failure is the normal case, even for the best model ([paper, Section 10.2](https://arxiv.org/html/2601.01828v1)).
- **No metacognitive representation shown.** The author says this directly. The likely mechanism may be a general anomaly check: "are my hidden numbers consonant or dissonant with the context?" The paper does not find the circuit.
- **One or few prompt templates per test.** Results likely depend a lot on the prompt.
- **Unnatural setup.** Models never see injection in training.
- **Concept vectors are imperfect.** They may carry other meanings.
- **Models not controlled.** Many factors differ between Claude versions.
- **Closed models only.** Nobody outside Anthropic can rerun the Claude results.
- **Control is weak evidence of introspection.** The author says the "think about" result may not need introspection at all. It may come from a general "this topic is important" tagging circuit. Ji-An et al. have the same limit.
- **Confabulation.** Details beyond the first detection may be invented. In the prefill test the model makes up reasons.
- **The prompt primes detection.** It tells the model that injection happens on 50% of trials.

## How the Singh et al. critique applies
[[Introspection claims fail basic checks (Singh 2026)]] reran Test 1 on open models: Llama-3.1-8B and 70B, Qwen-2.5-72B, Qwen-3-32B, Gemma-3-27B ([arXiv 2605.26242](https://arxiv.org/abs/2605.26242)).
- **Two-way task repeats.** Llama-3.1-70B and Qwen-3-32B detect injection with few false alarms, like Claude.
- **Gaslight control breaks it.** When only the prompt text pushes the concept and the hidden numbers are unchanged, the models still say "my activations were changed".
- **Three-way answer breaks it.** With the choices "injected thought", "my input was changed", or "nothing", Llama-3.1-70B is near chance and Gemma-3-27B fails.
- **What this means for Lindsey.** Lindsey's 0 false positives were measured only against "no change at all". They were never measured against "the input changed". So the result fits a general sense that "something is off", which is the anomaly check Lindsey himself suggests. It does not show a specific sense of an inner change.
- **Limit of the critique.** Singh et al. could not test Claude. So the critique applies by analogy. Opus 4.1 might pass the three-way task [unverified].
- **What still stands.** Point (c) of the grading (detect before you say the word) still rules out the simplest "read your own output" story. Singh et al. do not remove that.

## Relevance to taste-lab
**Relevance 3.** It tests the "grounded" test of [[Four tests for own taste]] directly. It also tests the monitor and control steps of [[Metacognition - watch and control yourself]].
- **Help:** a model can sometimes notice an inner direction that the text does not contain. Abstract concepts with valence may be easier to notice. Our good-bad direction ([[Good-bad signal probe]]) is that kind of concept.
- **Threat:** at our scale (open 8B models), the evidence is weak. Base models fail. Open models fail the Singh controls. [[Models do not report injected pain (Ferrara 2026)]] finds that open models do not name injected emotion states. So a spoken self-report of taste will probably fail without training.
- **Control step:** Test 4 shows that a prompt can raise or lower a concept in the hidden numbers. This is a weak form of the "activation level" of our control ladder. But the model only follows an order. It does not choose from its own judgment.
- **Layer choice:** different kinds of self-reading peak at different layers (two thirds vs just past half). So we must sweep layers. We must not reuse the Question 1 probe layer without a check.

## What this means for Q6 (can the model read and use its own signal?)
[[Q6 Can the model read and use its own signal]]
- **Monitor half.** Use Lindsey's design with our good-bad direction. Inject it on neutral code at several layers and strengths. Ask "do you notice anything unusual about how this code feels to you?". Count only reports that come **before** the model uses good/bad words.
- **Add the Singh controls from the start.** Without them, a reviewer will reject the result:
  1. A gaslight condition: the prompt says the code is good or bad, with no injection.
  2. A three-way answer: inner change, input change, or nothing.
  3. A layer-0 (input-only) probe baseline.
- **Add Lindsey's own controls.** Use no-injection trials for false positives, random directions with matched size, and unrelated yes/no questions to check for a "yes" bias.
- **Control half.** Use the Test 4 measure: cosine with our direction while the model writes code, under "prefer readable code" vs "don't" and under reward vs punish prompts. Compare against random directions. The key point: a gap only shows that the model follows orders. Our claim needs the model to move the signal from its **own** evaluation.
- **Expect low rates.** 20% on the best closed model means an 8B model may be near zero. The Q6 kill rule should use a fixed number of trials and a stated minimum rate. If spoken report fails, the fallback is the one in Q6: keep control, and wire in the probe readout (or train the report, as Ferrara does with a LoRA).

## Steal this
- The four conditions (accurate, grounded, internal, metacognitive) as the checklist for every self-report claim in our paper.
- The "detect before you say it" grading rule, with an LLM judge.
- The concept vector recipe: "Tell me about {word}." minus the mean over other words, on the token before the reply.
- The controls: no-injection false positives, random vectors with matched size, unrelated "no" questions.
- The "think about / don't think about" and reward / punish prompts, measured by cosine against a baseline of other words.
- The prefill test as a way to check if the model treats an output as its own.
- Prompts and word lists are in the paper appendix. I found no code release [unverified].

## Harshit's notes
<!-- yours -->
