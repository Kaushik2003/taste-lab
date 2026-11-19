---
description: Daily research sweep. Fetch, triage, digest.
---

Run the daily scout:

1. Run `python3 scripts/fetch_arxiv.py --days 2` and read the newest file in `9 Claude files/Inbox/candidates/`.
2. Use web search to check the `watch_sites` in `research.yaml` for posts from the last 2 days relevant to the charter.
   Include anything new from the tracked authors.
3. Hand the candidates to the `scout` subagent for scoring and note creation.
4. Write today's digest to `9 Claude files/Reports/YYYY-MM-DD.md` using `9 Claude files/Templates/digest.md`:
   top 3, one surprise pick, threat watch, one question for Harshit. Keep it phone-readable.
5. Append any score-3 papers to `2 Papers/Reading list.md` under "Priority".
6. If nothing scored ≥2, say so plainly in the digest. Don't pad it.
