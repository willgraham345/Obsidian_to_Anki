---
date created: Thursday, February 27th 2025, 8:58:01 am
date modified: Thursday, February 27th 2025, 8:58:33 am
---

Archived Projects:

```dataview
TABLE
 company as "Company",
 project as "project",
 subproject as "subproject",
 file.ctime as "Last Modified Time"
WHERE type = "project"
WHERE status = "closed"
WHERE file.name != "Project Template"
SORT subproject ASC
SORT file.name ASC
SORT company ASC
SORT project_id ASC
SORT status ASC
```

```breadcrumbs
type: mermaid
fields: [next, prev, similar]
depth: [0, 3]
sort: field
start-note: p001

```
