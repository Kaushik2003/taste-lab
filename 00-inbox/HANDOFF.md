---
type: handoff
status: active
tags: [protocol, multi-account]
links: []
---

# HANDOFF

Shared memory across Claude accounts. Nothing carries over between accounts unless it's written here or elsewhere in the repo.

- **Session start:** read the last 3 entries.
- **Session end:** append one entry. Newest goes at the bottom.
- Keep each entry under 6 lines, in this format:

```
## YYYY-MM-DD · <account label> · <surface>
- did: ...
- learned: ...
- open-next: ...
```

---

## 2026-11-19 · personal · claude.ai
- did: scaffolded repo, 6 papers, 6 concepts, T1–T5, exp01 spec, first digest
- learned: open models can't self-report emotion states but probes decode them (2611.10123, [[2026-ferrara-all-quiet-pain]]), so T1 uses a probe readout; WSP rank-one edits ≈ baked-in steering, which led to proposed [[T5-consolidate-steering-rank-one]]
- open-next: promote/kill T5, line up 2 raters for exp01, start reading-queue Priority
