---
date created: Tuesday, September 24th 2024, 3:07:22 pm
date modified: Friday, October 25th 2024, 10:09:45 am
type: vault_tool
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
