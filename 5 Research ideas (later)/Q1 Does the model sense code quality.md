---
type: question
title: "Q1. Does the model sense code quality?"
id: Q1
status: parked
owner: harshit
created: 2026-11-19
updated: 2026-11-22
tags: [type/question, question/Q1, status/parked]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# Q1. Does the model sense code quality?

> **In short**
> - **Question:** Does the model have an inner good-or-bad signal that agrees with people about which code is easy to read?
> - **Where it stands:** Parked while we write the literature review (from 2026-11-20). We have no data yet. A decision waits for Harshit (see below).
> - **Next step:** Review the proposed protocol in [[08-synthesis]], Section 8.1. Execution remains parked; about 50 problems is a pilot, not a powered confirmatory study.
> - **Role:** a go/no-go check. If the signal does not track code quality, we stop early. We do not build a readability paper on it. The metacognition step (the model reads its own signal) is in [[Q6 Can the model read and use its own signal]].
>
> **A decision waits for you: a stricter stop rule.** A stop rule says which result makes us drop this question.
> Claude proposes a stricter rule, because a new paper (Gao) makes a weak result easy to explain away.
> In simple words, we stop if one of these is true:
> 1. The signal matches human ratings only weakly (rank correlation below 0.2), after we remove the effect of length, familiarity and comments. We check this in two model families, on normal solutions only.
> 2. The signal adds almost nothing (less than 0.05) over two simple baselines: a probe that only sees the words, and Gao's readability direction.
> 3. Random directions in the model match the ratings just as well (the signal does not beat 95 of 100 random directions).
>
> Claude also proposes a quick test first: one GPU afternoon on public code that people already rated.
> The full proposal is under "Log", in the line that starts "proposed (Claude, for Harshit to accept)". Write "yes" or "no" under it.

**Words used here**
- **Valence:** the model's inner good-or-bad feeling about something.
- **Activations (hidden states):** the numbers inside the model while it reads or writes text.
- **Probe:** a small classifier that reads the model's hidden numbers.
- **Valence readout:** a valence score that a probe reads from the activations.
- **Direction:** a fixed pattern in the activations that goes with one property, for example "readable".
- **Steering:** adding a direction to the activations while the model works, to push its output one way.
- **Rank correlation (Spearman ρ):** how well two rankings agree, from -1 to 1. 0 is no match, 0.2 is weak, 0.4 is moderate.
- **Partial ρ:** the rank correlation that is left after we remove the effect of other factors, such as length.
- **Perplexity:** how surprised the model is by a text. Low perplexity means the text looks familiar to the model.
- **Layer-0 probe (input-only probe):** a probe on the first layer. It sees only the words, not the later processing in the model. We use it as a baseline.
- **Blind raters:** people who rate code but do not know which result we expect.
- **Anchors:** "sloppy but correct" code that we make on purpose as known-bad examples.
- **Model family:** models from one maker, for example Qwen or Llama.

## Hypothesis
*What we think is true.*

We take many solutions to the same problem. All of them pass the tests.
We read the valence of an open model (8B to 32B parameters) on each solution.
We expect this score to agree with blind expert rankings of readability, with rank correlation ρ ≥ 0.4 (a moderate match).
We expect the match to stay after we remove the effect of three simple factors:
- length,
- familiarity (perplexity),
- how many comments the code has (comment density).

## Why it matters
*The other questions depend on this one.*

This is the gating experiment: its result decides the plan for the other questions.
If valence does not follow code quality, the model cannot use it to judge its own work.
Then Questions 2 to 5 must change. They are: Question 2 (can the model steer its own code?), Question 3 (can self-learning avoid collapse?), Question 4 (can the model edit its own weights?) and Question 5 (can we make steering permanent?).

## Evidence for
*Results from other papers that make this likely.*

- Anthropic found emotion directions in Claude Sonnet 4.5. These directions predict which tasks the model says it prefers, and steering them changes those choices ([[Emotion directions drive choices in Claude (Anthropic 2026)]]).
- Ferrara found that a simple linear probe reads emotion states with 98–100% accuracy in open models of 7B to 32B ([[Models do not report injected pain (Ferrara 2026)]]).
- Jiang found a "value axis" in Qwen3-8B. It separates correct code from broken code, also when the names are hidden on purpose (obfuscated). The effect size is d = 0.69, a medium-to-large difference ([[Value axis - model knows it is on track (Jiang 2026)]]).
- Gao found separate directions for parts of readability (comments, names, branches) in 13–14B code models, and steered the model with them ([[Steer code readability inside the model (Gao 2026)]]). Gao never compares the model's view of real code with human ratings. This leaves the proposed valence/readability test distinct, but does not establish universal novelty; corrected Kirin v3 already probes human preference from hidden states (see [[08-synthesis]]).
- Berg found that valence stored only in the model's short-term memory of the text (the KV cache) changes later choices. This was true in 5 of 7 open models ([[Hidden good-bad feeling changes choices (Berg 2026)]]).
- Two papers found that probes on hidden states know when the model is right better than the model's own words do ([[Models know when they are right (Zhang 2025)]], [[Few neurons predict right answers (Xu 2026)]]).

## Evidence against
*Results that make this less likely, or harder to prove.*

- The same paper (Ferrara) found that open models cannot *say* what these states are without training (zero-shot). So our readout must use a probe, or a trained self-report.
- In Jiang's paper, a high value score goes with fewer lines, fewer comments and fewer type hints. So valence may simply reward short code ([[Value axis - model knows it is on track (Jiang 2026)]]). Gao's readability direction adds comments. So the two directions may point in opposite ways on comments ([[Steer code readability inside the model (Gao 2026)]]).
- Singh found that input-only (layer-0) probes do as well as the model's in-context self-reports. Readability is visible in the text itself. So a layer-0 probe may match our readout, and then our readout shows nothing special ([[Introspection claims fail basic checks (Singh 2026)]]).
- Berg's valence effect is missing in Qwen3-32B and Gemma-3-27B. This puts our plan to scale up to 32B at risk ([[Hidden good-bad feeling changes choices (Berg 2026)]]).
- Jin found that rewards from the model's own confidence on code push it toward short output ([[Self-reward on code collapses to short code (Jin 2026)]]).
- Valence may only follow familiarity (perplexity). Low-perplexity code is often boilerplate-like "slop", which is the code we want to avoid.

## What would kill this
*The result that makes us stop.*

Current rule: we stop if ρ < 0.2 (a weak match or less) after we remove the effect of perplexity and length, in two model families.
A stricter rule waits for Harshit's decision (see "In short" and the "proposed" line under "Log").

## Next action
*What to do next.*

Review the maintained proposed protocol in [[08-synthesis]], Section 8.1, linked from [[5 Research ideas (later)/Q1 experiment - read the signal/Plan|exp01]]. Resolve exact checkpoints, confirmatory sample size, rater feasibility and proposed decision rules before execution resumes. The approximately 50-problem plan is a pilot; Q1 remains parked.

## Log
- 2026-11-19: created. Pivot: the "grounded" test uses a probe readout first, with trained self-report as a later step.
- 2026-11-19: renamed from `T1-valence-tracks-quality` ("Does the model's internal valence track code quality?") in the metacognition recenter.
- 2026-11-20: frontmatter only: added nested tags and valid `links` for Obsidian graph view, no content change. Fixed the exp01 link to point at its spec.
- 2026-11-20: renamed from `does-the-models-internal-evaluation-signal-track-code-quality-T1` ("Does the model's internal evaluation signal track code quality? (Q1)") to an ASD-STE100-style name and title.
- 2026-11-20: prior-art update. Gao steers readability but never rates real code against humans; Q1 is not scooped. The bar is higher: valence must beat input-only, readability-direction and value-axis baselines, within-problem, anchors excluded.
- 2026-11-20: proposed (Claude, for Harshit to accept): new kill line. Within-problem partial ρ < 0.2 on natural passing solutions (anchors excluded) after length, perplexity and comment ratio, in two families; or valence adds < 0.05 ρ over a layer-0 probe plus a Gao-style readability direction; or ρ falls inside the 95th percentile of norm-matched random directions. Proposed cheap pre-check: valence vs a public human-rated readability set (Buse-Weimer or Scalabrino, Java) against a layer-0 probe, about one GPU afternoon, before the 2–3 days of rating. exp01 controls to add: layer-0 probe, Gao direction, Jiang value axis, Xu correctness probe, comment-stripped rerun, other-model and human solutions, rater reliability (≥5 blind raters, Krippendorff's alpha). Source: critic pass, see sources [2401.14936](https://arxiv.org/abs/2401.14936), [2404.13076](https://arxiv.org/abs/2404.13076), [2510.16579](https://arxiv.org/abs/2510.16579) [unverified numbers].
- 2026-11-20: renamed to a plain name (file "Q1 Does the model sense code quality"), so the name is clear at once. Old title: "Does the internal evaluation signal of the model show code quality? (Q1)". Codes T1 to T5 are now Q1 to Q5.
- 2026-11-20: rewritten in plain English (same facts).
- 2026-11-20: on the user's instruction, this question is now a go/no-go check only. Reason: the work had moved toward readability probes and away from metacognition. The model-reads-itself step moved to [[Q6 Can the model read and use its own signal]].
- 2026-11-20: parked on the user's instruction. The current goal is the literature review, not experiments.
- 2026-11-22: Added the maintained Section 8.1 protocol and replaced exp01's conflicting short plan with a pointer. This specifies blind multi-rater labels, leakage controls, baselines, matched-strength causal checks and uncertainty-aware decisions. Stricter stop rules remain proposals; no experiment was activated.
