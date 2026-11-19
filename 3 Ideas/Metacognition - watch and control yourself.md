---
type: concept
status: active
tags: [type/concept, status/active, metacognition, introspection, monitoring, control]
links: ["[[Good-bad signal probe]]", "[[Models that change their own weights]]", "[[Four tests for own taste]]"]
---

# Metacognition = monitoring + control

**Definition (plain):** Nelson & Narens (1990) split cognition into an object level (doing the task) and a
meta level that **monitors** it (reads its state) and **controls** it (changes what it does). This is the core
of the project; see "The question" in `CLAUDE.md`.

## Foundations
**Flavell (1979).** "Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry."
*American Psychologist* 34(10), 906–911. [doi:10.1037/0003-066X.34.10.906](https://doi.org/10.1037/0003-066X.34.10.906)
- Claim: people know things about their own thinking and use that to regulate it, and this ability develops with age.
- Mechanism: four interacting parts: metacognitive knowledge (about people, tasks, strategies), metacognitive
  experiences (conscious feelings such as "I'm not getting this"), goals, and the actions or strategies used to reach them. [unverified: from memory, check against the paper]
- For us: "metacognitive experiences" is the classic ancestor of our evaluation signal, a felt good/bad about the
  state of one's own thinking that triggers a change of strategy. (Our reading, not Flavell's claim.)
- Note: the old version of this note said Flavell coined the term in 1979. He used it earlier, in a 1976 chapter
  ("Metacognitive aspects of problem solving"). [unverified]

**Nelson & Narens (1990).** "Metamemory: A theoretical framework and new findings." *Psychology of Learning and
Motivation* vol. 26 [unverified: volume number], 125–173. [doi:10.1016/S0079-7421(08)60053-5](https://doi.org/10.1016/S0079-7421(08)60053-5)
- Claim: metacognition is two levels joined by two flows of information.
- Mechanism: the meta level holds a model of the object level. Monitoring is information flowing up (feeling of
  knowing, judgments of learning). Control is information flowing down (how long to study, when to stop searching memory). [unverified: examples from memory]
- For us: the skeleton of our loop. We add **evaluate** and **persist** (below).

**Fleming & Daw (2017).** Paper note: [[Confidence is a guess about your own decision (Fleming 2017)]]. "Self-evaluation of decision-making: A general Bayesian framework for metacognitive
computation." *Psychological Review* 124(1), 91–114. [doi:10.1037/rev0000045](https://doi.org/10.1037/rev0000045) · [PMC5178868](https://pmc.ncbi.nlm.nih.gov/articles/PMC5178868/)
- Claim: one Bayesian model covers both confidence and error detection, and explains why metacognition can be
  better or worse than task performance.
- Mechanism: self-evaluation is a **second-order** inference. A monitoring system infers how well a coupled but
  separate decision system did, which is the same computation as judging another agent. This happens when the
  states behind the decision and the states behind confidence are separated in space or time. They contrast it
  with first-order models, where one internal state drives both.
- For us: a ready-made account of the probe-vs-report gap. If generation and self-evaluation run on partly
  separate states, the report can come apart from the decodable state (as in [[Models do not report injected pain (Ferrara 2026)]])
  without either being broken. The model also predicts that a system's own actions feed into its self-evaluation,
  which matters for Q2 (best-of-n judged on the model's own outputs). (Our reading.)

## Our extension
Nelson & Narens give **monitor** and **control**. We add two steps:
- **Evaluate:** monitoring produces a judgment (like/dislike), not just a reading. That judgment is the taste. → [[Good-bad signal probe]]
- **Persist:** control reaches the weights, so the preference outlives the context. → [[Models that change their own weights]]

Control ladder: **reasoning** (pick or revise its own outputs) → **activation** (steer its own hidden states) → **weights** (edit itself).

## LLM evidence
- Monitoring: Ji-An et al. (NeurIPS 2025) show LLMs can report activation directions in-context, but only in a low-dimensional "metacognitive space". Lindsey (2026, concept injection) shows Claude Opus 4/4.1 sometimes detect and name injected concepts.
- Control: both papers show models can shift their own activations when asked. Effects are stronger in deeper layers and larger models.
- Against: [[Models do not report injected pain (Ferrara 2026)]] and [[Probes find injections long before models report them (Rubin 2026)]] show the states are decodable before, or without, self-report in open models.

**Why it matters:** The whole project is this loop: monitor → evaluate → control → persist. Each of the [[Four tests for own taste]] checks one stage.

**Related:** [[Good-bad signal probe]], [[Models that change their own weights]], [[Neuromodulators as learning settings]]
