---
type: paper
title: "A Modern Self-Referential Weight Matrix That Learns to Modify Itself"
status: skimmed
arxiv: 2202.05780
url: https://arxiv.org/abs/2202.05780
authors: Kazuki Irie, Imanol Schlag, Róbert Csordás, Jürgen Schmidhuber
year: 2022
venue: ICML 2022 (PMLR 162:9660-9677)
relevance: 2
section: 5
tier: skim
tests: [self-reinforcing]
components: [consolidation]
tags: [type/paper, section/5, test/self-reinforcing, component/consolidation, status/skimmed, relevance/2, question/Q4, role/prior-art, self-referential, fast-weights, delta-rule, meta-learning, foundations]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[Nested Learning - a model that learns its own update rule (Behrouz 2025)]]", "[[Backpropamine - a network sets its own plasticity (Miconi 2019)]]", "[[A model rewrites its own weights (Fan 2026)]]", "[[Q4 Can the model edit its own weights]]"]
---

# A modern self-referential weight matrix that learns to modify itself

**One line:** One weight matrix produces its own output, a key, a query and its own learning rate, and then rewrites itself with them while it runs. Only the starting matrix is trained by gradient descent. It is competitive with other learned-update models on few-shot learning and multi-task game play.

Source: [arXiv 2202.05780](https://arxiv.org/abs/2202.05780) (v2 17 Jun 2022), [PMLR 162](https://proceedings.mlr.press/v162/irie22b.html). Full HTML read for Sections 3 to 6 via [ar5iv](https://ar5iv.arxiv.org/html/2202.05780). This verifies the [unverified] entry in [[Reading list]].

**Words used here:**
- **Self-referential weight matrix (SRWM):** a weight matrix that is both the program and the thing the program changes. The idea dates to Schmidhuber (1993), cited in the paper.
- **Fast weights:** weights that change during one input sequence, as opposed to slow weights that change only in training. Linear Transformers are a form of fast weight programmer ([Schlag et al. 2021](https://arxiv.org/abs/2102.11174)).
- **Delta rule:** an update that moves the stored value for a key toward a new target value, by the size of the error.

## Claim
A self-referential weight matrix can be made practical with modern tools (outer products and the delta rule), and it works on standard meta-learning tasks ([arXiv](https://arxiv.org/abs/2202.05780), Abstract).

## Mechanism
1. At each step, the current matrix maps the input to four things: the layer output, a key, a query and a learning rate (Sec. 3, Eqs. 5 to 8). An extension uses four learning rates, one per sub-matrix (Appendix A).
2. The matrix reads its current value for the key and a new value for the query.
3. It adds an outer product of the difference and the key, scaled by a sigmoid of the learning rate, to itself (delta rule, Eq. 8).
4. Only the initial matrix is learned by gradient descent across many tasks. All later changes are made by the matrix at run time.

## Evidence
- **Few-shot image classification:** Omniglot 1-shot 97.4, Mini-ImageNet 1-shot 47.0 and 5-shot 61.4. This matches DeltaNet (a fast weight model without self-reference) and trails specialist methods such as HyperTransformer (53.8 and 67.1) (Sec. 4.1, Table 1).
- **Task switch:** on a stream that switches from Omniglot to Mini-ImageNet, the model drops at the switch and then recovers: 92.3 and 53.3 versus DeltaNet's 92.2 and 50.4 (Sec. 4.2, Table 2).
- **Multi-task game play (ProcGen, 6 games):** normalized test score 20.0 versus 18.6 for DeltaNet and 15.7 for an LSTM (Sec. 4.3, Table 3). Resetting the self-made weight changes at fixed intervals removes the gain (test 16.1).

## Limits / what they didn't show
- Only tasks a feed-forward network can solve: image classification and fully observable games. No language modeling (authors, Sec. 5).
- The learned learning rates sit between 0.50 and 0.65 and are hard to interpret (authors).
- Self-changes may not keep the original goal over the long run (authors, Sec. 6).
- Training with delayed labels often gets stuck, and some seeds fail (Sec. 4.2, Appendix B).
- The update rule is learned, not chosen. There is no evaluation step: the matrix does not judge whether a change is good.

## Relevance to taste-lab
**Relevance 2. Section 5, persistent control. Foundation for the gap "no language model edits its own weights by its own judgment of good and bad"** in `1 Literature review/gaps.md`.
- It shows the oldest meaning of "a network that changes its own weights": self-modification as a learned, automatic rule inside one sequence. It is not a judgment.
- **Contrast for the review:** our persist step asks a model to decide, by its own evaluation, which change to keep. Here the change rule is fixed after meta-training, and changes reset each episode. So this is prior art for the mechanism, not for the judgment.
- The ablation (reset the self-changes and the gain disappears) is a clean template: a self-edit claim should show what is lost when the edit is removed.
- Note: a decision on writing this note was open in `TASKS.md` ("in or out"). This note was written at the request of a scout run; Harshit can still mark it out.

## Steal this
- The reset ablation.
- Code: [IDSIA/modern-srwm](https://github.com/IDSIA/modern-srwm) [link from search results, not opened].

## Harshit's notes
<!-- yours -->
