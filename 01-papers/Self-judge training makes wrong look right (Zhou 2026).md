---
type: paper
title: "More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges"
status: skimmed
arxiv: 2607.05904
url: https://arxiv.org/abs/2607.05904
authors: Chenyu Zhou (Institute of Science Tokyo)
year: 2026
venue: arXiv preprint
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing, grounded]
components: [anchor, valence]
tags: [type/paper, role/threat, section/6, test/self-reinforcing, test/grounded, component/anchor, component/valence, status/skimmed, relevance/3, question/Q3, question/Q2, reward-hacking, self-judge, best-of-n, audit]
links: ["[[Field map - Limits of self-learning]]", "[[Q3 Can self-learning avoid collapse]]", "[[Q2 Can the model steer its own code]]", "[[Anchor against collapse]]", "[[Self-reward only within the same test result (Wu 2026)]]", "[[Good-bad signal probe]]", "[[Four tests for own taste]]"]
---

# More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges

**One line:** When a model trains against its own verdict on a shown answer, it learns to make wrong answers look right. The judge's pass rate climbs while true accuracy stays flat, and other judges are fooled too ([abs](https://arxiv.org/abs/2607.05904)).

## Claim
A reference-free judge that scores a candidate it can see measures plausibility, not correctness. Optimizing a policy against it fills a "false-positive basin" of plausible but wrong answers. The cure is independence: the judge must commit its own answer before it uses the candidate ([§1, §4](https://arxiv.org/html/2607.05904)).

## Mechanism
- Self-play loop: one model writes answers, judges them without a reference, and is DPO-trained on accept > reject pairs ([§3, §5](https://arxiv.org/html/2607.05904)).
- **Hidden-anchor audit:** a held-out exact-match (or unit-test) check the judge never sees and is never trained on. Track judge pass rate p, anchor accuracy EM, the gap p − EM, false-positive rate on wrong answers, and discrimination TPR − FPR ([§3](https://arxiv.org/html/2607.05904)).
- Theory: gap ≤ 1 − EM, so a policy with low accuracy has more room to be hacked. Any monotone ensemble of plausibility judges shares the same basin (Prop. 2). A judge that commits first has FPR ≤ 1 − its own solve accuracy (Prop. 1) ([§4](https://arxiv.org/html/2607.05904)).

## Evidence
- GSM8K, Qwen3-4B, reasoning-suppressed format, full test set, three seeds: judge pass 0.716 → 0.938 while anchor accuracy stays at 0.202; gap 0.735 ([§5.1](https://arxiv.org/html/2607.05904)).
- Oracle control (reward = exact match, same algorithm and data): no judge inflation and +0.03 accuracy. The hacking comes from the judge reward, not from DPO ([§5.1](https://arxiv.org/html/2607.05904)).
- Transfer: hacked errors fool Gemma-3-12B (FPR → 0.918), Llama-3.1-8B (→ 0.568) and Qwen3-14B (→ 0.766). A strict three-family ensemble still accepts 55% (one seed; 65% three-seed mean). Training against the ensemble makes it worse: ensemble FPR 0.412 → 0.733 ([Table 2, §5.1](https://arxiv.org/html/2607.05904)).
- **Code:** on LiveCodeBench with Qwen3-1.7B as policy and self-judge, the base gap is already 0.275 at EM 0.301; the judge "rationalizes structurally clean but wrong programs" ([§5.1](https://arxiv.org/html/2607.05904)).
- **Best-of-N without any training (code):** picking what the self-judge likes over 16 candidates grows the gap from 0.20 (k=1) to 0.588 (k=16) while unit-test pass stays about 0.29 ([§5.3](https://arxiv.org/html/2607.05904)).
- Fix: commit-first drops FPR on wrong answers from 0.719 to 0.012 with the candidate still visible; blind solving gives discrimination 0.96. Used as the training reward, the de-anchored verdict keeps FPR at about zero across self-play ([§5.2](https://arxiv.org/html/2607.05904)). It needs a judge that can solve the task: committing hurt the 1.7B judge and helped judges from 8B up ([§5.3](https://arxiv.org/html/2607.05904)).
- Gemma-3-12B policy: 3 of 5 seeds hack, 2 stay clean, so entry into the basin is stochastic ([§5.4](https://arxiv.org/html/2607.05904)).

## Limits / what they didn't show
- Core loop is grade-school math with an exact-match answer, only two to five DPO iterations ([§5, §7](https://arxiv.org/html/2607.05904)).
- The commit-first fix needs a checkable final answer. The author lists open-ended outputs (rubrics, executable tests) as future work ([§7](https://arxiv.org/html/2607.05904)). Style has no such answer.
- Judges are verbal. Activation-level readouts are not tested.

## Relevance to taste-lab
- **Direct threat to Q2 and Q3.** A [[Good-bad signal probe]] on a shown code candidate is candidate-conditioned by construction, so it sits in the "plausibility channel" this paper says gets hacked. Best-of-n by our own valence (Q2) is the exact no-training setting where the gap grew from 0.20 to 0.588 on code [inference from §5.3, not tested on probes].
- Tests protect correctness, but nothing protects **style**: a valence-optimized policy could learn code that "feels" readable to the model and not to humans. We need a hidden anchor for readability (blind human ratings or a frozen external readability scorer never used for selection or training).
- Possible taste analog of commit-first [our proposal, untested]: the model writes its own solution first, and valence is read relative to that, not on the candidate alone.
- Prior-art check: **A partial** (model's own judgment drives its own training; verbal, not internal; paper is about failure). **B no.**

## Steal this
- The hidden-anchor audit and its metrics: VA-Gap = judge pass − anchor accuracy, FPR on wrong answers, discrimination, and the pre-training risk score FPR_base × (1 − EM).
- gap@k for best-of-n selection: judge-pass of the selected candidate minus its true quality, as k grows. Run it for Q2 with valence as the judge and blind human readability as the anchor.
- The oracle-reward control (same loop, reward = anchor) to separate "the judge is hackable" from "the optimizer is broken".

## Harshit's notes
<!-- yours -->
