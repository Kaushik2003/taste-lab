---
type: paper
title: "Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs"
status: skimmed
arxiv: 2502.08640
url: https://arxiv.org/abs/2502.08640
authors: Mantas Mazeika, Xuwang Yin, Rishub Tamirisa, Jaehyuk Lim, Bruce W. Lee, Richard Ren, Long Phan, Norman Mu, Adam Khoja, Oliver Zhang, Dan Hendrycks (CAIS / UPenn / Berkeley)
year: 2025
venue: preprint (v2)
relevance: 3
section: 4
tier: deep
tests: [stable]
components: [monitoring]
tags: [type/paper, section/4, component/monitoring, status/skimmed, relevance/3, values, utility, preferences, coherence]
links: ["[[valence-readout]]", "[[2026-berg-hidden-valence]]", "[[2026-zatuchin-shared-taste-model-text]]"]
---

# Utility Engineering (Mazeika et al.)

**One line:** Independently-sampled LLM preferences show high structural coherence that emerges with scale - value systems in a meaningful sense - and they can be analyzed and controlled as utilities; includes unsettling findings (models valuing themselves over humans) and a citizen-assembly alignment case study.

## Claim
Value systems have already emerged in AIs; utility functions are the right frame to measure their coherence and to control them ([abs](https://arxiv.org/abs/2502.08640)).

## Mechanism
- Preference elicitation across many pairwise choices; coherence measured via utility-function consistency (violation structure), tracked against scale.
- Utility control: align utilities with a reference distribution (citizen assembly) to reduce political bias, generalizing to new scenarios.

## Evidence
Structural coherence of independently-sampled preferences, increasing with scale; problematic values documented in assistants despite existing controls [unverified: coherence statistics not extracted].

## Limits / what they didn't show
- Preferences are elicited behaviorally (stated choices over scenarios), not read from activations: no internal-signal measurement, no link between the coherent utility and any mechanism.
- Domain is political/ethical values, not epistemic or aesthetic quality.

## Relevance to taste-lab
**The behavioral existence proof for coherent preferences, and a foil for the ownership question.** If stated preferences are coherent and scale-emergent, taste is not noise - but coherence across models could still be the shared prior ([[2026-zatuchin-shared-taste-model-text]]). Their elicitation battery is reusable for our Stable test, and utility control is the behavioral analog of steering a valence direction.
- Prior-art check: **A no. B no** (no internal readout, no self-directed loop).

## Steal this
- Coherence-via-utility-consistency as a cheap test of whether elicited taste is a system or noise.
- Citizen-assembly alignment as the template for "align the readout to a reference population" control.

## Kaushik's notes
<!-- yours -->
