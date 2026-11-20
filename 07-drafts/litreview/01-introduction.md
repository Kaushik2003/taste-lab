---
type: draft
status: draft
tags: [type/draft, litreview, section/1]
links: ["[[four-taste-tests]]", "[[landscape-gap-table]]", "[[code-quality-signal-T1]]"]
---

# 1. Introduction

Reasoning models now do something that looks, from the outside, like self-knowledge. They hesitate, backtrack, say "wait", and verify their own steps. This review asks a sharper question underneath that behavior: can a reasoning model **monitor** its own internal states, **evaluate** them with likes and dislikes of its own - a taste - and use that evaluation to **control** its thinking and, eventually, its own weights? And if it can, is that taste **self-originated**: does it drift away from the human preferences it was trained on because the model keeps selecting for it?

The question matters for two reasons. Scientifically, metacognition is one of the oldest frameworks in psychology ([[1990-nelson-metamemory]]), and LLMs are the first artificial systems where its pieces can be measured directly, because the internal states are readable. Practically, a model that can tell good from bad in its own work, without an external judge, could regulate its reasoning, choose what to learn, and improve on qualities nobody wrote a reward function for.

The organizing structure of this review is a loop: **monitor -> evaluate -> control -> persist**, with an **anchor** against collapse. Monitoring asks what a model's hidden states say about its own work. Evaluation asks which internal signals could serve as the good/bad judgment. Control asks how that judgment changes behavior, from choosing among outputs to steering activations. Persist asks how a preference gets written into weights. The anchor asks what keeps a loop that runs on its own signal from sharpening into collapse.

A taste counts as self-originated only if it passes four tests ([[four-taste-tests]]): it is **divergent** from human and training preferences, **stable** across paraphrase and context, **grounded** in a probed internal state rather than surface self-report, and **self-reinforcing** under self-training without collapse. Each test alone has a cheap explanation; together they are the bar.

Throughout, the testbed is **code readability**. It is chosen for one reason: correctness can be held fixed by executable tests, so among solutions that all pass, the only thing left for an internal evaluation to track is style. If a model's own signal cannot move readability, the loop has nothing to steer with; if it can, readability is the cleanest place to show it. The gating question, made precise in [[code-quality-signal-T1]], is whether an internal valence readout tracks human readability judgments among passing solutions, beyond length, perplexity and comment density.

The review proceeds along the loop. Section 2 gives the foundations. Sections 3 to 7 cover monitoring, evaluation signals, persistent control, the limits of self-referential training, and the measurement of taste. Section 8 assembles the pieces, states where the field stops, and presents the strongest evidence against the thesis. Section 9 concludes with what can defensibly be claimed and the experiments that follow.
