---
type: question
title: "Q6. Can the model read and use its own signal?"
id: Q6
status: proposed
owner: harshit
created: 2026-11-20
updated: 2026-11-20
tags: [type/question, question/Q6, status/proposed, component/monitor, component/control, test/grounded]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]", "[[Good-bad signal probe]]", "[[Q1 Does the model sense code quality]]", "[[Q2 Can the model steer its own code]]", "[[Models can report and control their own activations (Ji-An 2025)]]", "[[Models sometimes notice injected thoughts (Lindsey 2025)]]"]
---

# Q6. Can the model read and use its own signal?

> **In short**
> - **Question:** We can read the model's good-or-bad signal with our own probe. Can the model itself read this signal, and can it change it on purpose?
> - **Where it stands:** Proposed by Claude on 2026-11-20. It waits for Harshit to accept it.
> - **Next step:** Read the Ji-An 2025 paper note. Then plan a small test on one 8B model with the same signal as Question 1.
>
> **Why this question exists.** Our main idea is metacognition: the model watches its own state and acts on it.
> Questions 1 to 5 do not test this directly. In Question 1 (does the model sense code quality?), *we* read the signal, not the model.
> This question tests the step where the model does it.

**Words used here**
- **Metacognition:** thinking about your own thinking. A "meta level" watches the work (monitor) and changes it (control). From Nelson and Narens (1990).
- **Valence (good-or-bad signal):** the model's inner good-or-bad feeling about something.
- **Activations:** the numbers inside the model while it reads or writes text.
- **Probe:** a small classifier that reads the activations. Here it is *our* tool, outside the model.
- **Direction:** a fixed pattern in the activations that goes with one property, here "good" versus "bad".
- **In-context examples:** examples we put in the prompt. The model learns from them without a change to its weights.
- **Layer-0 probe:** a probe that sees only the words, not the later processing. If it does as well as the model, the model did not need to look inside itself.
- **Random direction:** a direction with no meaning. We use it to check that a result is not luck.

## Hypothesis
What we think is true.

We pick one 8B model and our good-or-bad direction from Question 1. Then two things are true:
1. **Monitor:** after some in-context examples, the model reports its own good-or-bad score on new texts. Its reports match our probe better than a layer-0 probe does.
2. **Control:** when we ask, the model moves its own good-or-bad score up or down. The change is larger than for random directions.

## Why it matters
What depends on this.

- This is the core of our idea. Without it, we have an outside reader (us), not a model that watches itself.
- It is the "grounded" test of [[Four tests for own taste]]: the model's report must match a real inner signal.
- Question 2 (can the model steer its own code?) and Question 3 (can self-learning avoid collapse?) need the model to *use* the signal. This question checks the first step of that.
- It does **not** need human ratings. So it can run at the same time as Question 1.

## Evidence for
What supports the idea.

- Ji-An et al. (2025) put sentences in the prompt with labels from the model's own activations. Models then report the label for new sentences and push the direction up or down on request. They also did this for a happy-versus-sad direction, which is close to our good-or-bad signal ([[Models can report and control their own activations (Ji-An 2025)]]).
- When researchers put a concept into Claude Opus 4.1's activations, it sometimes says it notices it before it says the word. It had 0 false alarms in 100 trials with nothing injected ([[Models sometimes notice injected thoughts (Lindsey 2025)]]).
- An inner good-or-bad signal changes later choices, in 5 of 7 open models ([[Hidden good-bad feeling changes choices (Berg 2026)]]).

## Evidence against
What argues against it.

- Open models cannot name an emotion state that is put into them, but a probe can read it ([[Models do not report injected pain (Ferrara 2026)]]). So "report" may fail without examples.
- When the input is controlled, a layer-0 probe matches the model's self-reports. The model may only read the text, not its own state ([[Introspection claims fail basic checks (Singh 2026)]]).
- Only a small set of directions can be controlled: about 32 to 128 of them, the ones with a clear meaning or a large share of the variation. Our good-or-bad direction may not be one of them ([[Models can report and control their own activations (Ji-An 2025)]]). The model also controls a direction much less well with no new words.
- Even the best closed model notices an injected thought in only about 20% of trials. An 8B model may be near zero ([[Models sometimes notice injected thoughts (Lindsey 2025)]]).
- Ji-An et al. had no probe that sees only the input words. When Singh et al. added it, it matched or beat the model ([[Models can report and control their own activations (Ji-An 2025)]]).

## What would kill this
The result that makes us drop or change this question.

- The model's reports match our probe no better than a layer-0 probe does, in two model families. **Or**
- The model cannot move its good-or-bad score more than it moves random directions.

If only "control" works and "monitor" fails, we keep a smaller version: the model can use the signal but cannot report it.

## Next action
The smallest step that moves this forward.

Write a one-page plan. A draft from the Ji-An note:
1. **Labels:** take passing solutions from the Question 1 set. Score each one on the good-or-bad direction and split at the middle into "1" and "0". Use Llama-3.1-8B (the Ji-An code supports it) and Qwen3-8B (the Question 1 model).
2. **Report test:** show 32 to 64 labeled short solutions, then a new one. Ask for its label.
3. **Controls (set before the run):** shuffled labels; a layer-0 probe; a second model that sees the same examples but not the activations; Gao's readability direction, a strong direction, a weak one and a random one for comparison.
4. **Control test:** ask for a passing solution that matches label 1 (or 0), and measure the score, test pass rate, length and comments. Also try it with a fixed solution and no new words.
5. **Rules from Lindsey and Singh:** a report counts only if it comes before the model uses good or bad words. Include trials with nothing changed, and allow the answer "my input changed". Set the minimum success rate before the run.

## Log
- 2026-11-20: created as "proposed" by Claude, on the user's request, because the work had moved away from metacognition. Question 1 now acts as a go/no-go check, and this question tests the model reading its own signal.
- 2026-11-20: added facts from the new notes on Ji-An 2025 and Lindsey 2025, and a draft plan under "Next action".
