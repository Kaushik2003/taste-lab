---
type: paper
title: "Metamemory: A Theoretical Framework and New Findings"
status: skimmed
arxiv:
url: https://sites.socsci.uci.edu/~lnarens/1990/Nelson&Narens_Book_Chapter_1990.pdf
doi: 10.1016/S0079-7421(08)60053-5
authors: Thomas O. Nelson, Louis Narens
year: 1990
venue: The Psychology of Learning and Motivation, Vol. 26 (ed. G. H. Bower), Academic Press, pp. 125-173
relevance: 3
section: 2
tier: deep
tests: [grounded]
components: [monitoring, controller]
tags: [type/paper, section/2, test/grounded, component/monitoring, component/controller, status/skimmed, relevance/3, role/prior-art, metacognition, metamemory, psychology, foundations]
links: ["[[Metacognition - watch and control yourself]]", "[[Field map - Models read their own state]]", "[[Four tests for own taste]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Neuromodulators set how the brain learns (Doya 2002)]]"]
---

# Metamemory: A Theoretical Framework and New Findings

**One line:** The mind has two levels. An object level does the task. A meta level holds a model of the object level, gets information from it (monitoring), and changes it (control).

**Why it matters to us:** This is the frame of the whole review. Our loop (monitor, evaluate, control, persist) adds two steps to this chapter's two arrows ([[Metacognition - watch and control yourself]]).

Source: [PDF on the second author's site](https://sites.socsci.uci.edu/~lnarens/1990/Nelson&Narens_Book_Chapter_1990.pdf), first 12 pages read (framework part). DOI [10.1016/S0079-7421(08)60053-5](https://doi.org/10.1016/S0079-7421(08)60053-5). Some reference lists give the title as "...and Some New Findings"; the PDF header says "A Theoretical Framework and New Findings".

**Words used here:**
- **Object level:** the process that does the task, here remembering.
- **Meta level:** the process that watches and directs the object level.
- **Monitoring:** information goes up, from object level to meta level ("listening to the telephone").
- **Control:** information goes down, from meta level to object level ("speaking into the telephone"). It can start, continue or stop an action.
- **Judgment of learning (JOL):** a guess, during or after study, of how well you will recall an item later.
- **Feeling of knowing (FOK):** a guess that you know an item you cannot recall now.

## Claim
Metacognition rests on three principles (pp. 125-126 of the PDF):
1. Cognition splits into two or more linked levels: meta level and object level (terms from Hilbert).
2. The meta level contains a dynamic model of the object level. The authors cite Conant and Ashby (1970): a good controller must model the system it controls.
3. Two relations link the levels, named by the direction of information flow: monitoring (up) and control (down).

## Mechanism
- The framework groups monitoring and control judgments by stage of memory: acquisition, retention, retrieval (Fig. 2).
- Monitoring can be prospective (about future performance: ease of learning, JOL, FOK) or retrospective (confidence in an answer already given).
- Control uses those judgments: for example, how much study time to give an item, and when to stop a memory search.
- **Introspection as data, not as a window.** The authors treat self-reports as behavior to explain. Reports can miss parts of the state and add parts that are not there. They compare it to a telescope with known distortions.
- **Key idea for us:** a system that monitors itself, even with errors, can use that monitoring to change its own behavior. The value of monitoring is in the control it drives.

## Evidence
- Ease-of-learning, JOL and FOK judgments do not correlate highly with each other (Leonesio and Nelson 1990, cited in the chapter). So "monitoring" is not one signal; it has several parts.
- Ease-of-learning judgments predict the rate of learning and relate to how much study time people give each item (Underwood 1966; Nelson and Leonesio 1988, cited in the chapter).
- The later "new findings" part (not read here) reports human studies of FOK and study-time choices [unverified: we read only the framework part].

## Limits / what they didn't show
- It is a framework for human memory, from behavior and self-report. It says nothing about how levels are built in a brain or a network.
- The meta level only reads and directs. There is no "good or bad" judgment of its own (our Evaluate step) and no lasting change to the system itself (our Persist step).
- It takes the split into two levels as given. In a language model the same weights do both jobs, so "meta level" may be only a way to describe things [unverified as a claim about models].

## Relevance to taste-lab
**Relevance 3.** It is the base frame for the review's section 2 and the monitor and control stages ([[Metacognition - watch and control yourself]]).
- **Grounded test** ([[Four tests for own taste]]): the chapter already warns that self-report can distort the state. That is the same lesson as [[Introspection claims fail basic checks (Singh 2026)]], 36 years earlier.
- Principle 2 (the meta level models the object level) asks a clear question of language models: does the model hold a model of its own processing, or only of its text? [[Training LMs to watch themselves (Wang 2026)]] tests one version of this.
- **What would weaken our use of it:** if the "meta level" in a model is only an outside probe, we have monitoring by the experimenter, not metacognition by the model.

## Steal this
- The two-arrow diagram (Fig. 1) and the prospective vs retrospective split, as a table to sort every monitoring paper in section 3.
- "Introspection as data with distortions": report both how well a model's self-report tracks the state and how it distorts it.

## Harshit's notes
<!-- yours -->
