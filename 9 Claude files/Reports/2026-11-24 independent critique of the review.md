---
type: report
status: active
tags: [type/report, critique, literature-review]
links: ["[[Literature review - full paper]]", "[[2026-11-23 direction critique]]", "[[2026-11-23 gap check]]", "[[TASKS]]"]
---

# Independent critique of the literature review, 2026-11-24

Scope: `1 Literature review/Literature review - full paper.md` (about 20,000 words, 147 references), read in full.
Three questions: is it good, is there plagiarism or a paper like it, and does it reach the level of a final-year graduate paper at MIT.

**Version note.** I read the committed version (commit `3f18ae3`, "first draft"). While I worked, another session changed all section files for writing style (uncommitted, 07:37). I re-ran the wording check and the key searches on that newer copy. Every point below still holds, with one change: the new abstract no longer states the 30 billion threshold. The threshold is still in the body ("near 30B", three places).

## Verdict

- **Plagiarism of text:** not found. Copied wording is very low.
- **A paper exactly like it:** not found. But the nearest prior work is not cited, and each half of the review has a deeper survey.
- **Level:** it is a good map for our own use. It is not at the level of a final-year graduate paper. The main reasons are authorship, depth of reading, and a main finding that is partly true by construction.

## What I checked, and how

| Check | Method | Result |
|---|---|---|
| Do the references exist? | All 128 arXiv IDs sent to the arXiv API; title, first author and year compared | 128 of 128 exist and match. 6 small faults (below) |
| Non-arXiv links | Opened 5 doubtful links | All open. 1 wrong title, 1 wrong year |
| Copied wording from sources | Shared 6-word and 8-word sequences between the review body and the 128 abstracts | 42 shared 6-word sequences out of about 15,900 (0.26%) |
| Copied wording from surveys | Shared 7-word sequences with the full text of 4 surveys | 0 in all 4 |
| Similar reviews | 3 web searches, then abstracts and section headings of the finds | 5 related works not cited (below) |
| Claim accuracy | 18 key claims compared with the source abstracts; 1 compared with the paper body | No wrong number found. 3 cases of selective reporting |

Limits of these checks: I compared wording with abstracts and four surveys only, not with the full text of all 147 sources or the wider web. A tool such as Turnitin is still needed. I did not re-check numbers that are absent from the abstracts.

## 1. Authorship is the first problem

The repo states the facts. An AI wrote the whole review in one day ([[TASKS]], Done, 2026-11-24). The human author has read few of the 147 sources. Seven of 137 papers were read in full, and the AI read them.

This is not plagiarism of another paper. It is a question of who the author is. Most universities, MIT included as far as I know, treat AI-written work handed in without permission and disclosure as academic misconduct `[unverified: check the exact rule of the course or supervisor]`. An AI-text detector will probably flag the document, because the style is uniform.

A reader will also test the author in person. The author must be able to defend each claim.

## 2. The reading is too thin for the claims

- 7 of 137 papers were read in full (5%). 20 claims carry a mark such as "abstract only" or "not extracted".
- The text still reports about 200 exact numbers.
- Abstracts mislead. Example from this check: the abstract of the self-rewriting paper (Fan et al. 2026) says "each edit improving on the last, and over eight consecutive sessions its accuracy only rises". The paper body says each session starts from the base weights (Sec. E.9). The review is right here, because that paper was read in the body. For the 130 skimmed papers, nobody checked the same gap.

A review whose authors have not read the literature is an annotated list with a thesis on top.

## 3. The evidence base is young and not graded

- 24 of 147 sources are from November 2026. They are less than four weeks old.
- The central concept, weight-space programming, comes from a blog post dated 2 November 2026.
- A single-author preprint from six days ago carries the same weight in the text as a Nature paper. There is no column for venue, peer review, sample size or replication.
- Trehan and Chopra's "15.0 to 36.2% stable divergence" rests on 80 pairs from 19 papers. The review does not give that number.

## 4. The main finding is partly true by construction

The review defines a new loop of four steps across four literatures. Then it finds that no system connects all steps. A gap defined as "nobody did A and B and C and D together" is almost always open. A strict reader will call this finding trivial.

Two more faults in the frame:

- **The abstract contradicts the body.** The abstract says: "In every weight-changing method, a signal outside the model's own evaluation decides what is kept." Section 5.3 describes INTUITOR, where the model's own certainty is the only reward for weight updates. Section 6.5 lists self-rewarding training, decided by the model's "own verbal score". The claim holds only if "own evaluation" means a signal read from hidden states. The abstract does not say that.
- **"Evaluate" is not clearly a new step.** In Nelson and Narens, monitoring already contains judgments (feeling of knowing, judgment of learning). In reinforcement learning, a critic is an internal good/bad signal that changes weights. The review does not face either point.

## 5. Claims that go past the evidence

- **The "30 billion parameter" threshold.** It is in the abstract as a finding. It comes from three papers on different models and tasks. The review's own data cut against it: a 70B model fails Singh's controls, a 32B model never names an injected state (Ferrara), and the hidden-state effect is absent in exactly the 32B and 27B models of Berg and Kaiser. Section 9.5 admits it is "our reading". It does not belong in the abstract.
- **"Own-model taste is near zero."** The same source (Żatuchin 2026) reports a second data set with a premium of +0.148. The review leaves it out.
- **"The self-model adds nothing."** Naphade et al. 2026 (arXiv 2603.20276) report that frontier models predict their own behavior better than peer models do. The paper is in our candidate inbox and is not cited. Song et al. 2025 (arXiv 2503.07513) is also in the inbox and not cited.
- **Taste.** The four tests are ours. The review then grades the field against our tests. That is circular until someone outside uses them.

## 6. Missing canon

A faculty reader will see these gaps in the first minutes.

- **Self-modification:** the Gödel machine and Schmidhuber's earlier self-referential learners; Darwin Gödel Machine; STOP. None is mentioned.
- **Change of one's own criterion:** wireheading, utility preservation under self-modification (Omohundro; Everitt et al. 2016), value drift in the safety literature. The review treats drift away from human preference as a goal and never says why anyone should want it.
- **Weight editing:** ROME and MEMIT appear only through a paper about their failure. Task vectors, hypernetworks and test-time training are absent.
- **Steering:** activation addition, contrastive activation addition, representation engineering.
- **Self-report in people:** Nisbett and Wilson 1977; Koriat on cues.
- **Confidence:** the calibration literature and semantic entropy.
- **World models:** the section has two paragraphs on world models and then turns to self-prediction. The title and keywords promise more. Cut it to a subsection or write it fully.
- **Doya's neuromodulation (Section 2.4):** it is left over from the old architecture. The review uses it once.

## 7. Similar work

No paper covers the same four parts together. The combination is ours. These works are close and not cited:

| Work | Why it is close | In our repo? |
|---|---|---|
| Zhang, Yuan and Zhang 2026, arXiv 2607.04277 | Thesis: recursive self-improvement needs introspection. Reviews four components (self-modeling, self-simulation, self-evaluation, self-modification) with a status table, and sorts systems by "which layer is modified, and how verified" | In the candidate inbox since 19 November, not cited |
| Ren et al. 2026, arXiv 2607.13104 | Survey of self-improving agents, sorted by what is updated and which signal drives the update. Same axes as our Section 6.5 table | No |
| Yang et al. 2026, arXiv 2603.25681 | Self-improvement as a closed loop with an evaluation layer | No |
| Burden, Petrova and Wynne, MetaLoop, NeurIPS 2026 | Benchmark of the "full metacognitive loop": monitor, act, update. Finds that models produce the signal and do not act on it | No |
| Liu et al. 2026a (the Yale survey), arXiv 2607.11881 | 28,000 words on the metacognition half. At least 32 of our 137 notes came from its reading list | Cited, but the Method section does not name it as a source of our corpus |

The first row is the serious one. Our component table (Section 9.1) and our "who chooses, who checks" table (Section 6.5) will look derived from it. We built them independently, and the wording check shows no copying. But a missing citation of the nearest prior work looks bad.

I also saw a search result for a systematic review of meta-reasoning in reasoning models (AACL 2026). I did not open it `[unverified]`.

## 8. Wording and citation faults

- Eight short phrases follow an abstract closely with no quote marks. Examples: "reading weights is mostly reading the input layer" (Goworek), "justify themselves at greater length and use fewer" (Fafuła), "the share of failed attempts among the lessons" (Kongsilp), "sees only the visible output. Over 78,000 measurements" (Ferrara). Put them in quote marks or reword them.
- The weight-space programming reference has the wrong title. The real title is "Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights".
- "Anthropic 2026" should be Sofroniew et al. 2026.
- Johnson et al. is dated 2025 with a 2026 DOI. Lindsey is dated 2025 with a 2026 arXiv ID.
- About 20 references have "et al." or family names only. "Yuan (2024)" is a multi-author paper. Check the first name of Prato `[unverified]`.
- The review has no figure. A review built on one loop needs a drawing of the loop.
- The style is briefing notes: bullets, one paper per bullet, glossaries of basic terms. Synthesis across papers happens only in the summaries.
- `writing-guide/` holds copies of published papers and is tracked in git. Do not push them to a public repo.

## 9. What is good

- Every reference is real. That is rare for AI-written reviews.
- The review hedges honestly, marks thin evidence, and lists eight problems with its own agenda.
- Three tables are useful and original in form: the ladder of controls (3.7), who proposes and who decides (6.5), and the four-outcome table (9.6).
- The closing question is narrow and testable.

## 10. Against the MIT standard

- **As a survey paper for a graduate seminar:** the breadth is above average. It can pass only if AI use is allowed and disclosed, and if the author can defend it.
- **As a final-year graduate paper or thesis chapter:** no, not in this state. A thesis needs original research. This is the background chapter for research that has not started. The readers would include the authors of the central papers: weight-space programming, SEAL and Goel et al. are MIT work.

## What would fix it, in order

1. Settle authorship and disclosure with the supervisor or course. Add an AI-use statement.
2. The author reads the about 25 papers that carry the argument, then rewrites Sections 1, 9 and 10 in their own words.
3. Cite and position against the five works in Section 7. Add a short "related surveys" part with a comparison table.
4. Add the missing canon (Section 6).
5. Fix the overclaim in the abstract ("every method that changes weights"). Soften the 30B threshold in the body; the style pass already took it out of the abstract.
6. Verify or delete the 20 thin claims. Add an evidence-quality column to [[matrix]].
7. Cut or complete world models. Cut Doya. Add a figure of the loop.
8. Quote or reword the eight phrases. Fix the references.

## What would kill this critique

- If the destination is an internal map and not a graded or published paper, points 1 and 10 do not apply.
- If the course allows AI-written drafts with disclosure, point 1 becomes a disclosure task.
