---
description: Pick the next paper to read, brief Harshit on it, and save his takeaway when he finishes. Usage /next [done <takeaway> | <paper>]
argument-hint: [done <takeaway> | <paper>]
---

Walk Harshit through the lit review reading list one paper at a time. Arguments: $ARGUMENTS

**Which paper.** If the arguments name a paper (file name or title), use it. Otherwise pick the paper the dashboard's
"Read next" panel shows, so the two always agree:
- only notes in `01-papers/` whose `status` is not `read`, `deep` or `done`;
- lowest `section` number first, papers with no section last;
- inside a section, `tier: deep` before `tier: skim`, then by file name.

**If the arguments start with `done`, or Harshit says he finished a paper,** record it:
1. If he hasn't given a takeaway yet, ask for one and wait.
2. In that paper's note, change the frontmatter `status:` line to `status: read`. Don't touch any other line.
3. Put his takeaway under `## Harshit's notes`, in his words. Fix typos only. Don't rephrase it or add your own analysis.
   Start the entry with the date: `**YYYY-MM-DD:** ...`. If earlier text is under the heading, keep it and add the new
   entry below. Remove the `<!-- yours -->` placeholder. If the heading is missing, add it at the end of the note.
4. If the takeaway disagrees with the note, or bears on a thread in `03-questions/`, say so in one line and offer to
   add a dated line to that thread's `## Log`. Don't edit the thread without his OK.
5. Then brief him on the next paper (below), or say the list is done.

**Otherwise, brief him** in under 150 words:
- the **One line** from the note, and the paper link;
- which section of the review it feeds (names in `dashboard.json`);
- how to read it: `deep` means method and results in full, `skim` means abstract, main figure and headline numbers;
- 2 or 3 questions to read for, tied to our loop (monitor, evaluate, control, persist) or the four tests.

Then stop and let him read. Usage reminder for the end of the brief: `/next done <takeaway>` when finished.
