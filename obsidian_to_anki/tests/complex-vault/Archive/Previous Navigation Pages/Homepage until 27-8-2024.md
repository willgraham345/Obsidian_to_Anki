---
date created: Tuesday, August 27th 2024, 12:52:44 pm
date modified: Tuesday, August 27th 2024, 12:53:22 pm
---


```meta-bind-button
label: Go To Daily Log
icon: clipboard
hidden: false
class: ""
tooltip: ""
id: ""
style: primary
actions:
  - type: command
    command: periodic-notes:open-daily-note
```

```meta-bind-button
label: Create New Project
icon: plus
hidden: false
class: ""
tooltip: ""
id: ""
style: default
actions:
  - type: command
    command: quickadd:choice:63e0420d-249b-493c-bb01-1701f768c4a4

```

**Cheatsheets:**
```dataview
TABLE
	type, file.mtime as "Last Modified Time"
WHERE type = "cheatsheet"
```

**Tag Pages:**
```dataview
TABLE file.mtime as "Last Modified", type
WHERE type = "tag_page" and file.name != "Template Tag Page"
SORT file.name ASC
```

**Recent Meetings:**
```dataview
table file.mday as "Modified Date"
From "Notes/Meetings"
SORT file.mday DESC
Limit 3
```


**Recently Finished Projects:**
```dataview
TABLE project_id as "ID", company as "Company", project as "project", subproject as "subproject", file.ctime as "Last Modified Time"
FROM !"zz_Templates"
WHERE type = "project"
WHERE status = "closed" OR status = "blocked"
WHERE company = "Varex" OR company = "DRL"
SORT subproject ASC
SORT file.name ASC
SORT company ASC
```

**Stalled projects:**
```dataview
TABLE project_id as "ID", company as "Company", project as "project", subproject as "subproject", file.ctime as "Last Modified Time"
FROM !"zz_Templates"
WHERE type = "project"
WHERE status = "stalled"
SORT subproject ASC
SORT file.name ASC
SORT company ASC
```

**Daily Todo:**
```dataview
task
from "Notes/Daily"
where !completed
where file.day = date(today)
```
**Active Projects:**
```dataview
TABLE project_id as "ID", company as "Company", project as "project", subproject as "subproject", file.ctime as "Last Modified Time"
FROM !"zz_Templates"
WHERE type = "project"
WHERE status = "active"
SORT subproject ASC
SORT file.name ASC
SORT company ASC
```

**Active Updates:**
```dataview
TABLE company as "Company", status as "Status", file.ctime as "Last Modified Time"
FROM !"zz_Templates"
WHERE type = "update_log"
WHERE status = "active"
WHERE company = "Varex" OR company = "DRL"
SORT subproject ASC
SORT file.name ASC
SORT company ASC
```