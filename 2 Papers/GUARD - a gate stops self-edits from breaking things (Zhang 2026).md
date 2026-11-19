---
type: paper
title: "GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance"
status: skimmed
arxiv: 2611.23476
url: https://arxiv.org/abs/2611.23476
authors: Minghe Zhang, Xuetao Kang, Yifei Ming, Yanfei Chen, Han Yu, Yufan Zhuang, Chen-Yu Lee
year: 2026
venue: arXiv preprint
relevance: 2
section: 6
tier: skim
tests: [self-reinforcing]
components: [anchor]
tags: [type/paper, section/6, test/self-reinforcing, component/anchor, status/skimmed, relevance/2, role/prior-art, recursive-self-improvement, non-regression, harness, self-review]
links: ["[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]", "[[Self-reward only within the same test result (Wu 2026)]]", "[[Self-judge training makes wrong look right (Zhou 2026)]]", "[[Exploring WSP - small weight edits, uneven results (Hu 2026)]]"]
---

# GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance

**One line:** An agent edits its own text instructions (not its weights) with no outside grader. It checks each run against a fixed checklist it wrote before acting, and it keeps an edit only if the gains outweigh what the edit broke.

**Why it matters to us:** It is a working self-improvement loop that does not collapse, and its key part is a non-regression gate. That is the same shape as our "anchor" ([[Anchor against collapse]]), but in text, not in weights.

Source: [arXiv 2611.23476](https://arxiv.org/abs/2611.23476) (v1 17 Nov 2026). HTML read for Sections 1 to 4 and 6. Most numbers in the results text are in math markup that did not render in our copy; we use only numbers we could read [others unverified].

**Words used here:**
- **Harness:** the text and code around a frozen model: prompts, skills, tool rules and memory.
- **Recursive self-improvement (RSI):** the system uses its own experience to change itself, round after round.
- **Reference-free:** during the loop, no answer keys, hidden tests or official graders are used. The model grades itself.
- **Checklist:** a list of yes/no checks the model writes from the task and tool description before it starts.
- **Regret:** here, how much an edit made a check that used to pass now fail.
- **Gate (Soft-HURT):** a rule that accepts an edit only when its gains outweigh the regressions it causes.
- **Forgetting:** losing a skill learned earlier after later changes.

## Claim
Self-editing without outside graders often backfires, because one score mixes "what the latest edit broke" with "what is still unsolved". If you separate the two, keep what works fixed, and gate each edit on net gain, the harness improves without forgetting or memory bloat ([arXiv abstract](https://arxiv.org/abs/2611.23476)).

## Mechanism
1. **Checklist first (Sec. 4.1):** before the task, the model reads only the prompt and tool schema and writes atomic yes/no checks. Layer 1 checks execution facts in a sandbox copy; layer 2 checks meaning (format, constraints) from the trace.
2. **Analyze (Sec. 4.2):** rank checks by paired regret. Newly broken checks come first; mastered checks are "pinned" so later edits keep them.
3. **Propose (Sec. 4.3):** make a group of candidate harness edits, run them on the same tasks, and rank them by group-relative score (no learned critic). Edits are written as rules with "if and only if" conditions, so a narrow fix does not fire everywhere.
4. **Gate (Sec. 4.4):** promote an edit only if gains exceed regressions; log rejected edits so they are not tried again.
5. **Test time:** the loop is off. One frozen harness runs once per task.
- Weights never change. The main runs use one frozen Gemini 4 model in every role (solver, reviewer, editor).
- The authors prove that the gate keeps the self-review score from going down on each round's gated tasks (Theorem 1). This guarantee is on the self-review score, not on the true score.

## Evidence
- Benchmarks: PAST-Bench (memory across sessions), EvoHarnessBench (changing tools), Drift Gauntlet (hidden task drift), plus legal and finance suites (Sec. 5).
- On Drift Gauntlet, GUARD has zero block drops and zero forgetting after each block on all four streams; earlier harness methods swing and fall below the base agent (Fig. 1, Sec. 6.3).
- On EvoHarnessBench, the no-evolve baseline scores 71.91% accuracy (Table 2). GUARD scores highest and is the only method with no negative transfer, but the gate accepted the stage 1 edit and refused all later stages, so all of the gain comes from one accepted edit (Sec. 6.2). GUARD's exact accuracy did not render in our copy [unverified].
- **Self-review needs the sandbox layer:** a one-layer, model-only reviewer passes many traces that actually failed to execute; the two-layer reviewer does not (Sec. 6.4; numbers not readable [unverified]).

## Limits / what they didn't show
- **No weight change.** The "self-improvement" is in editable text. It says nothing directly about self-edits to weights.
- **Not fully self-graded.** Layer 1 is a sandbox execution check, an outside hard check. The authors say "reference-free" means no answer keys, not no structure.
- Gate guarantees apply to the self-review score. If the reviewer is wrong in a steady way, the gate protects the wrong thing (see [[Self-judge training makes wrong look right (Zhou 2026)]]).
- Where the gate refused all later edits, "no forgetting" partly means "no change". Stability may come from doing less.
- Some runs use a stronger teacher (Claude Opus 5.5) as reviewer, so not every result is single-model.

## Relevance to taste-lab
**Relevance 2.** Section 6, limits and what works against collapse.
- **Self-reinforcing test:** evidence that a self-graded loop can improve without collapse when (a) a hard outside check exists (sandbox) and (b) a non-regression gate is used. Same lesson as [[Self-reward only within the same test result (Wu 2026)]].
- It supports our anchor design and gives one more case for the review's pattern: "every self-improvement loop that works has a hard external check" ([[Anchor against collapse]]).
- **Gap it leaves:** the gated thing is text. Nobody has shown the same gate on self-chosen weight edits, which is where [[Exploring WSP - small weight edits, uneven results (Hu 2026)]] already uses a crude version ("keep the original unless validated").

## Steal this
- Separate "newly broken" from "still unsolved" before any update. Report both, never one mixed score.
- The rejection log: record refused edits so the loop does not retry them.
- The two-layer reviewer: hard execution check first, model judgment second.

## Harshit's notes
<!-- yours -->
