---
type: report
status: done
tags: [type/report, section/3, section/5, verification]
links: ["[[03-monitoring]]", "[[05-persistent-control]]"]
---

# Number check of the section 3 and section 5 drafts (2026-11-20)

**Result:** no wrong numbers found. Every number in both drafts that cites a paper note was found in that paper's text. The key numbers were also read in context. Two places needed more detail, and both are now fixed in section 5.

## How it was checked
1. Downloaded the full text of 26 cited sources (arXiv HTML, the WSP blog, the Lindsey Transformer Circuits page).
2. For each line of the drafts, a script took the cited papers and the numbers in the line. It checked that each number appears as a whole number in one of those papers. A test with a made-up number showed the script catches misses.
3. A number can appear in a paper with a different meaning. So the most important numbers were read in their sentence or table.

Not covered: Nelson 1990 and Doya 2002 (no numbers cited), and Steer2Edit (separate task in TASKS).

## Numbers read in context

| Claim in draft | Source | Result |
|---|---|---|
| WSP: MATH-500 7.9% to 48.1%, 0.016% of weights | [WSP blog](https://rikiyat.github.io/blog/weight-space-programming/), Experiment 8 | Matches. **Added:** 93% of base answers hit the token limit (33% after the edit), so the low base score is a loop effect. |
| SEAL ARC: about 20% to 72% | [arXiv 2506.10943](https://arxiv.org/abs/2506.10943), Table 1 | Matches (72.5% vs 20%). **Added:** the test is 8 hand-picked tasks, 5 self-edits each, on a 1B model. |
| Observer AUROC 0.907, 0.864, 0.828, 0.796; cross-model 0.684, 0.647; reasoning 0.823 vs 0.822 | [arXiv 2611.23365](https://arxiv.org/abs/2611.23365), Sec. 4.1 and 4.2 | All match. |
| Sort edit 67.0% vs 67.4% vs 9.5% | [arXiv 2611.21432](https://arxiv.org/abs/2611.21432), abstract | Matches. |
| WSP replication: +29.45 points, 1,023 values, +20.10 SciBench transfer, 6 of 16 runs kept original weights | [arXiv 2611.09382](https://arxiv.org/abs/2611.09382), Sec. 1 | Matches. The +20.10 is the math edit's transfer; +17.11 is a SciBench-targeted edit. Both are correct where used. |
| WeightBench: Opus 0.535 overall, 0.404 on fixing, 11 of 77 runs flagged, 0.491 to 0.500 on impossible edits, two agents above zero on loop tasks | [arXiv 2611.18553](https://arxiv.org/abs/2611.18553), Table 1 and Sec. 5 | All match. |
| TFTV sycophancy 3.60 to 94.64, steering 63.86 | [arXiv 2609.09054](https://arxiv.org/abs/2609.09054), table | Matches. |
| ThinkEdit GSM8K 82.26 to 89.44 | [arXiv 2503.22048](https://arxiv.org/abs/2503.22048), table | Matches. |
| Pain named in 0 of 2,880 trials | [arXiv 2611.10123](https://arxiv.org/abs/2611.10123) | Matches. |
| Injected thought noticed about 20% of trials | [Lindsey 2025](https://transformer-circuits.pub/2025/introspection/index.html) | Matches. |
| Controllable space between 32 and 128 dimensions | [arXiv 2505.13763](https://arxiv.org/abs/2505.13763), Appendix B.2 | Matches. |

## Still open
- ~~Steer2Edit Table 10 (87.8 to 77.3)~~: checked in the PDF later the same day. Matches; most of the drop is on GPQA (66.3 to 42.4).
- The script checks that a number exists in the paper, not that it means the same thing there. Numbers outside the table above were checked that way only.
