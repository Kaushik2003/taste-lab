---
type: paper
title: "Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for SWE Agents"
status: skimmed
arxiv: 2610.12598
url: https://arxiv.org/abs/2610.12598
authors: Yiran Wu, Andrew Zhao, Yurui Chang, Qingyun Wu, Xuan Feng (Penn State, Microsoft Research, AG2AI)
year: 2026
venue: arXiv preprint
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing]
components: [anchor, consolidation]
tags: [type/paper, role/prior-art, section/6, test/self-reinforcing, component/anchor, component/consolidation, status/skimmed, relevance/3, question/Q3, self-reward, code, swe-agents, verifier-anchored]
links: ["[[Field map - Limits of self-learning]]", "[[Q3 Can self-learning avoid collapse]]", "[[Anchor against collapse]]", "[[Self-judge training makes wrong look right (Zhou 2026)]]", "[[Models that change their own weights]]", "[[Four tests for own taste]]"]
---

# Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for SWE Agents

**One line:** The policy ranks its own debugging trajectories, but only among trajectories that got the same test result, and the extra reward is capped so a passing run always beats a failing one. This gives a small, real gain over tests-only RL on SWE-bench ([abs](https://arxiv.org/abs/2610.12598)).

## Claim
A coding agent's own pairwise judgments can add useful learning signal on top of a binary test reward, without training a separate reward model, as long as the tests keep the final say on pass versus fail ([§1, §3](https://arxiv.org/html/2610.12598)).

## Mechanism
- For each task, sample K trajectories and run the tests. Split them into a "pass" bucket and a "fail" bucket ([§3.1](https://arxiv.org/html/2610.12598)).
- Inside one bucket, the **same current policy** compares pairs of trajectories with a fixed rubric and outputs a winner plus a strength label (1 slight, 2 clear, 3 strong). Trajectories are summarized first: thinking removed, actions kept, long observations cut, simple stats added ([§3.1, App. A.3](https://arxiv.org/html/2610.12598)).
- The judge also sees the task's **reference patch**, which the acting policy never sees. So the judge has privileged information ([§3](https://arxiv.org/html/2610.12598)).
- Pairwise wins go into a weighted Bradley-Terry fit, then z-score inside the bucket, a soft deadzone (tanh with threshold), centering, and rescaling to [-1, 1] ([§3.2, Eq. 8-12](https://arxiv.org/html/2610.12598)).
- Final reward: R = test_result + a_y · q, with amplitudes a_0 + a_1 < 1. This guarantees every passing trajectory scores above every failing one ([Eq. 14-15](https://arxiv.org/html/2610.12598)).
- The rubric explicitly tells the judge to **ignore** writing style, verbosity, confidence and fluency, and to judge only observable debugging behavior ([App. B.5 prompts](https://arxiv.org/html/2610.12598)).
- Main setting refines only the fail bucket: a_0 = 0.15, a_1 = 0, deadzone 0.5, softness 0.5 ([§4 Setup](https://arxiv.org/html/2610.12598)).

## Evidence
- Qwen3-14B, 400 steps: SWE-bench Verified average accuracy 32.1% → 34.7%; SWE-bench-Live Lite 6.33% → 8.11%. Qwen3-32B, 270 steps: 34.4% → 35.5% on Verified. Pass@3 also rises in every setting ([Table 1](https://arxiv.org/html/2610.12598)).
- Random-reward control with the same amplitude: 30.9% average, Pass@3 42.8%, so the gain is not just reward noise ([Table 5](https://arxiv.org/html/2610.12598)).
- Bucket ablation (Qwen3-14B): fail-only 33.2 / 46.6 (avg / Pass@3); pass-only 32.0 / 44.0; both 33.1 / 44.6; baseline 31.0 / 45.0. **Ranking among passing runs alone lowered Pass@3 below baseline** ([Table 4](https://arxiv.org/html/2610.12598)).
- Self-judge agreement with an external judge (Kimi K2.5) stays around macro F1 0.6 to 0.7 and drops somewhat late in training ([App. B.5](https://arxiv.org/html/2610.12598)).
- Behavior shifts are small: e.g. search-to-edit conversion 0.465 → 0.494, post-edit test rate 0.301 → 0.311 ([Table 2](https://arxiv.org/html/2610.12598)).
- Compute: 8 nodes × 8 A100-40G for 14B, 16 nodes for 32B, 6 to 8 days per run; 64 tasks × 8 rollouts per step on R2E-Gym (4,578 tasks) ([App. B.1](https://arxiv.org/html/2610.12598)).

## Limits / what they didn't show
- The judge is a **verbal LLM-as-judge with a reference patch**, not an internal signal and not reference-free.
- No diversity or collapse tracking beyond a note that logged entropy loss rises ([App. B.1](https://arxiv.org/html/2610.12598)). Runs are a few hundred steps, so long-horizon drift is untested.
- Gains are 1 to 3 points with three evaluation runs; no training-seed variance reported.
- Judge agreement decays over training, which is the early sign of the drift that [[Self-judge training makes wrong look right (Zhou 2026)]] predicts.

## Relevance to taste-lab
- **Structural twin of our Q3 design.** Tests fix the pass/fail order and the model's own judgment moves reward only inside an outcome bucket. That is exactly "correctness held fixed by tests, taste moves style" in [[Q3 Can self-learning avoid collapse]].
- What differs from us: their signal is a prompted verbal judgment (with privileged reference), ours is a [[Good-bad signal probe]] from activations; their rubric is human-written and excludes style, ours is meant to be the model's own style taste.
- **Warning for us:** the pass-bucket-only arm (the closest analog of "taste among passing solutions") was the weakest arm and hurt Pass@3. Self-judged preference among already-correct outputs may reduce coverage.
- Prior-art check: **A partial** (the policy's own judgment shapes its own learning; but output-level, privileged, not internal). **B no.**

## Steal this
- The bounded-amplitude rule a_pass + a_fail < 1, so self-reward can never reorder test outcomes. Use it as the reward form in Q3.
- The deadzone + tanh mapping and the **random-reward control at matched amplitude** as a required baseline.
- Logging self-judge agreement with a frozen external judge every N steps as a drift alarm.
- Code: https://github.com/yiranwu0/behavioral-self-rewarding

## Harshit's notes
<!-- yours -->
