---
type: paper
title: "Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity"
status: skimmed
arxiv: 2002.10585
url: https://arxiv.org/abs/2002.10585
authors: Thomas Miconi, Aditya Rawal, Jeff Clune, Kenneth O. Stanley
year: 2019
venue: ICLR 2019
relevance: 2
section: 2
tier: skim
tests: [self-reinforcing]
components: [controller, consolidation]
tags: [type/paper, section/2, test/self-reinforcing, component/controller, component/consolidation, status/skimmed, relevance/2, question/Q3, role/prior-art, neuromodulation, plasticity, hebbian, self-modifying, foundations]
links: ["[[Neuromodulators as learning settings]]", "[[Neuromodulators set how the brain learns (Doya 2002)]]", "[[Metacognition - watch and control yourself]]", "[[SRWM - a weight matrix that rewrites itself (Irie 2022)]]", "[[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]]", "[[Field map - Changes that stay in the weights]]"]
---

# Backpropamine: a network that sets its own plasticity

**One line:** A network outputs its own "dopamine" signal, and that signal sets how fast its plastic weights change at each moment. The whole system trains with ordinary gradient descent. It helps on simple reward tasks and gives a small gain in language modeling.

Source: [arXiv 2002.10585](https://arxiv.org/abs/2002.10585) (posted 24 Feb 2020), [ICLR 2019 poster](https://iclr.cc/virtual/2019/poster/926). Full PDF read for Sections 3 to 5.

**Words used here:**
- **Plastic weight:** a weight with a fixed part and a part that changes during one episode, by a Hebbian rule (strengthen a link when both ends are active together).
- **Neuromodulator M(t):** here, one number the network computes at each step. It scales how much the plastic part changes.
- **Eligibility trace:** a short memory of which links were recently active, so a later signal can still change them.

## Claim
Networks whose plasticity is controlled by their own neuromodulatory signal can be trained with gradient descent, and this improves performance on reinforcement learning and supervised tasks ([arXiv](https://arxiv.org/abs/2002.10585), Abstract, Sec. 5).

## Mechanism
1. Each link has a fixed weight, a trainable plasticity size, and a Hebbian trace that starts at zero each episode (Sec. 3.1).
2. **Simple neuromodulation:** replace the fixed learning rate of the Hebbian trace with M(t), an output of the network (Sec. 3.2.1, Eq. 3). The network decides when to be plastic.
3. **Retroactive neuromodulation:** keep an eligibility trace of recent activity. M(t) decides how much of that trace becomes a real change. M(t) can be negative (Sec. 3.2.2, Eqs. 4 to 5). The authors base this on how dopamine gates recent plasticity in animals.
4. Fixed weights, plasticity sizes and the M(t) circuit are trained across episodes by gradient descent.

## Evidence
- Cue-reward association and maze tasks: modulated networks learn better than non-modulated plastic networks (Sec. 4, Figs. 1 to 2). The M(t) signal reacts to reward, but the pattern differs from run to run (Appendix, Fig. 3).
- Penn Treebank language modeling, small LSTM over 16 runs: test perplexity 104.26 (baseline), 103.80 (plastic), 102.65 (simple modulation), 102.48 (retroactive modulation). About 1.7 points better than baseline, p = 1e-7 (Sec. 4, Table 1).
- Large LSTM: 62.48 baseline versus 61.44 with modulated plasticity, median of 5 runs (Table 1).

## Limits / what they didn't show
- Small models and small gains in language modeling; far from the state of the art (authors, Sec. 4).
- One neuromodulator only. The authors list several signals with their own inputs as future work (Sec. 5).
- The plastic changes reset each episode. Nothing persists into the slow weights.
- M(t) is not shown to track any meaningful evaluation; its reaction to reward is complex and varies by run.

## Relevance to taste-lab
**Relevance 2. Section 2, foundations for the controller.**
- This is the closest machine-learning version of the Doya mapping ([[Neuromodulators set how the brain learns (Doya 2002)]]): an internal signal sets the learning rate. It gives the review a concrete, citable example beyond metaphor.
- **Gap it speaks to:** "no hidden-state monitoring signal controls learning". Here a signal computed from hidden states does control plasticity, but in small LSTMs, within one episode, and with no link to evaluation. So the gap for language models stays open, but it now has a precedent.
- The authors suggest the signal could use any computed quantity, such as reward predictions or surprise (Sec. 5). A valence readout is one such quantity [our reading].

## Steal this
- Simple versus retroactive modulation as two designs for "the evaluation decides what gets learned".
- Code from Uber AI Labs is cited in the paper [unverified link].

## Harshit's notes
<!-- yours -->
