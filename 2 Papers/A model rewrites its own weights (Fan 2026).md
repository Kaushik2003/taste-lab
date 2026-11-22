---
type: paper
title: "Language Models Can Rewrite Their Own Weights"
status: skimmed
arxiv: 2611.21885
url: https://arxiv.org/abs/2611.21885
authors: Jiajun Fan, Neil He, Changyi Yang, Andy Mao, Xi Zhu, Chaoran Cheng, Kaiqu Liang, Shuaike Shen, Zetian Li, Ruihan Guo, Ge Liu
year: 2026
venue: arXiv preprint
relevance: 3
section: 5
tier: deep
tests: [self-reinforcing, grounded]
components: [consolidation, monitoring, anchor]
tags: [type/paper, section/5, test/self-reinforcing, test/grounded, component/consolidation, component/monitoring, component/anchor, status/skimmed, relevance/3, role/threat, role/prior-art, question/Q4, weight-space-programming, self-rewriting, rank-one-edit, scale]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[WSP - a model reads and edits weights (Takehi 2026)]]", "[[A simple sort replaces the anti-loop edit (Fischetti 2026)]]", "[[One direction controls refusal (Arditi 2024)]]", "[[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]", "[[Claude's WSP edits act at the output (Kundu 2026)]]", "[[Q4 Can the model edit its own weights]]", "[[Metacognition - watch and control yourself]]"]
---

# Language Models Can Rewrite Their Own Weights

**One line:** An open 27B model reads its own hidden states, finds a direction linked to its reasoning loops, and removes a small part of it from its own weights. It gets better on new problems, with no gradients and no outside editor.

**Why it matters to us:** This is the first paper we know of where a language model edits its **own** weights by reading itself. Our section 5 and `gaps.md` say this has not been done. Those sentences are now wrong and must change before the review is due.

Source: [arXiv 2611.21885](https://arxiv.org/abs/2611.21885) (v2, 18 Nov 2026). Full PDF read for Sections 1 to 5 and Appendices A and B, through `pdftotext`. Figure numbers below are from the PDF text.

**Words used here:**
- **Self-rewriting:** the authors' name for a model that writes changes into its own weights by its own reasoning, with no training.
- **Paired test:** the edited and unedited model answer the same problems with the same random seed, so each problem gives a direct comparison.
- **Rank-one edit:** a change to a weight matrix that adds or removes one fixed pattern. It is the smallest structured edit.
- **Protocol 2:** the setting where the model must check an edit on reserved practice problems before it submits it.

## Claim
A large enough language model can diagnose its own failure, rewrite the weights behind it, and become more accurate on unseen problems. The ability appears only at the largest size in one model family ([arXiv abstract](https://arxiv.org/abs/2611.21885)).

## Mechanism
- **Model family:** Qwen3.5 at 2B, 4B, 9B and 27B. Each model gets the same task and tools (Fig. 3 in the PDF).
- **Inputs:** its own weights (or a copy with one block of noise), and its graded answers on practice problems. Gradients and optimizers are blocked.
- **Tools, one action per turn:** Python over its own weights, a paired test of an edit, or a read of its hidden states on texts it chooses. The tool kit includes a helper that removes part of a direction from a matrix (App. A).
- **What the 27B model did:** it saw that wrong answers mostly ran out of tokens because of loops. It compared mean hidden states of answers that finish and answers that do not. It took that difference at layer 8 and removed 5% of it from the two output matrices of that layer (W becomes W minus 0.05 u u-transpose W). This changed about 0.6% and 0.1% of their norm (Fig. 13 and Tab. 1 in the PDF).
- **Gate:** the model keeps an edit only if its own paired tests favour it. In protocol 2 it withdrew in 5 of 8 sessions.

## Evidence
- Protocol 2, held-out set of 490 problems with 8 answers each: accuracy from 57.2% to 61.3% (session 2) and 63.8% (session 8), both significant in a test fixed in advance (Fig. 1).
- Protocol 1 edit: 57.2% to 58.3%, also significant (Fig. 4, Tab. 8).
- Answers that hit the 16,384-token limit fall from 33.6% to 26.1% (Fig. 1b).
- Repair of a damaged copy: held-out accuracy from 0.0% to 33.0% (base 58.5%). The repair also restores image tasks, from 7.3% to 70.2% on six benchmarks (base 84.3%) ([abstract](https://arxiv.org/abs/2611.21885), Fig. 4).
- Scale: the 2B model makes no edit; the 4B and 9B models break themselves; only 27B improves (Fig. 2, Fig. 4).

## Limits / what they didn't show
- **The good-bad signal is outside the model.** Edits are chosen and kept by graded answers on practice problems. The model reads its hidden states only to find *where* to edit, not to judge *what is good*.
- **The target is the loop fault again.** The gain comes mostly from fewer runaway answers. [[A simple sort replaces the anti-loop edit (Fischetti 2026)]] shows a simple fix can replace the outside version of this edit, and [[Claude's WSP edits act at the output (Kundu 2026)]] finds similar gains from output-level changes. A full-text search of the PDF (2026-11-20) finds no random-direction edit or decoding-time length control as a baseline. The paper only excludes edits that rescale a whole tensor, because they act like a change of sampling temperature (Sec. 2.3, App. D).
- The tool kit offers a direction-removal helper, so the edit type is partly given to the model.
- One model family and one task type (math with a loop failure).
- The sessions in protocol 2 each start from the base weights (Fig. 1 caption), so this is not yet a loop where the model edits an already self-edited model [unverified: our reading of the caption].
- No measure of diversity or collapse over sessions.

## Relevance to taste-lab
**Relevance 3. Threat to a novelty claim, and prior art for the persist step.**
- **Persist:** this closes most of the gap in [[Models that change their own weights]]. A model now reads its own states, picks a direction itself, writes it into its weights and gates it. Section 8 says "the self-chosen direction does not exist". That is no longer true.
- **What is still open:** the evaluation. Every edit here is judged by external correctness. Own verbal quality preferences already guide DPO in [[Self-rewarding language models judge and train themselves (Yuan 2024)]]. The proposed distinction is causal activation-level readability evaluation guiding selection and learning among test-matched programs; see [[08-synthesis]].
- **Grounded test:** the model names the layer and direction it changed. That is a self-report tied to a weight change, which `gaps.md` says does not exist [unverified: the paper does not test whether later self-reports follow the edit].
- **Anchor:** paired tests plus withdrawal is a non-regression gate, like [[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]].

## Steal this
- The scale ladder (no edit, self-breaking, self-improving) as a way to describe self-modification ability.
- Paired tests with fixed seeds as the gate for any self-edit.

## Harshit's notes
<!-- yours -->
