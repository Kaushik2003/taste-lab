---
type: paper
title: "What Large Language Models Know and What People Think They Know"
status: skimmed
url: https://doi.org/10.1038/s42256-024-00976-7
authors: Mark Steyvers, Heliodoro Tejeda, Aakriti Kumar, Catarina Belem, Sheer Karny, Xinyue Hu, Lukas Mayer, Padhraic Smyth
year: 2025
venue: Nature Machine Intelligence
relevance: 3
section: 3
tier: deep
tests: []
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/3, role/prior-art, human-ai, calibration-gap, uncertainty-communication]
links: ["[[Fine-tuned uncertainty reports transfer across domains (Steyvers 2025)]]", "[[A less accurate AI with better confidence wins decisions (Li 2025)]]", "[[Models mostly know what they know (Kadavath 2022)]]"]
---

# What Large Language Models Know and What People Think They Know

**One line:** Models' internal confidence and the confidence humans end up placing in model answers are two different things; the calibration gap between them is where trust is lost, and communicating uncertainty well narrows it.

**Why it matters to us:** The flagship human-AI reference for section 3's last mile: even a perfectly calibrated internal signal is worthless if the interface does not transmit it. Our evaluation-signal work must end at the user, not at the probe.

Source: [Nature Machine Intelligence](https://doi.org/10.1038/s42256-024-00976-7) (2025). Abstract-level note.

## Claim
There is a calibration gap between human confidence in LLM answers and the models' actual confidence; earning trust requires both internal calibration and effective uncertainty communication to users ([paper](https://doi.org/10.1038/s42256-024-00976-7)).

## Mechanism
- Distinguishes internal confidence (the model's) from communicated confidence (what the user perceives), and measures the gap and its discrimination.

## Evidence
- Recent work focuses on internal confidence while less is known about how effectively models convey uncertainty to users; the paper characterizes this calibration gap ([abstract](https://doi.org/10.1038/s42256-024-00976-7)).

## Limits / what they didn't show
- Communication interventions are interface-level; does not address making the internal signal itself better.
- Ground-truth tasks; open-ended quality judgments remain unstudied.

## Relevance to taste-lab
**Relevance 3. Section 3.**
- Completes the chain: signal exists (Kadavath) -> usable (Kumaran) -> worth using (Li & Steyvers) -> must be communicated (this paper).
- The calibration gap concept transfers directly to taste: a model's internal "this is good" and the user's trust in its picks will diverge the same way.

## Steal this
- The two-confidence diagram (internal vs perceived) as the standard figure for any communication-of-uncertainty section.

## Kaushik's notes
<!-- yours -->
