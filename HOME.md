---
type: dashboard
status: active
tags: [dashboard]
links: [[reading-queue]], [[HANDOFF]], [[landscape-gap-table]]
---

# taste-lab

## Today
```dataviewjs
const digest = dv.pages('"05-digests"').sort(p => p.file.name, "desc")[0];
const file = dv.app.vault.getAbstractFileByPath("00-inbox/HANDOFF.md");
const last = (dv.app.metadataCache.getFileCache(file)?.headings ?? []).filter(h => h.level === 2).at(-1);
dv.list([
  digest ? `Digest: ${digest.file.link}` : "Digest: none yet",
  last ? `Last handoff: [[00-inbox/HANDOFF#${last.heading}|${last.heading}]]` : "Last handoff: [[HANDOFF]]",
]);
```

## Reading next
![[reading-queue#Priority]]

## Open questions
```dataview
TABLE title, status, updated
FROM "03-threads"
SORT status ASC, file.name ASC
```

## Papers
```dataview
TABLE title, relevance, status, year
FROM "01-papers"
SORT relevance DESC, year DESC
```

## Field map
```dataview
LIST FROM "02-concepts"
WHERE startswith(file.name, "landscape-")
SORT cluster ASC
```
Gap table: [[landscape-gap-table]]

## Concepts
```dataview
LIST FROM "02-concepts"
WHERE !startswith(file.name, "landscape-")
SORT file.name ASC
```
