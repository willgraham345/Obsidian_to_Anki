---
date created: Thursday, February 27th 2025, 8:58:01 am
date modified: Thursday, February 27th 2025, 8:58:10 am
type: vault_tool
---
Focus:
```dataview
TABLE
issues as "Issues",
[project] as "project",
map(Bottlenecks.text, (x ) => "- " + x) as "Bottlenecks",
map(OpenTasks.text, (x) => "- " + x) as "Open Tasks",
map(OpenQuestions.text, (x) => "- " + x) as "Open Questions"

flatten list(file.tasks) as openTasks
FLATTEN list(filter(file.tasks, (tasks) => tasks.status != "x")) as NotFinished
FLATTEN list(filter(NotFinished, (tasks) => tasks.status != "?" and tasks.status != "A" and tasks.status != "p")) as OpenTasks
FLATTEN list(filter(NotFinished, (tasks) => tasks.status = "~")) as Bottlenecks
FLATTEN list(filter(NotFinished, (tasks) => tasks.status = "?")) as OpenQuestions
WHERE type = "project"
WHERE status = "focus"
WHERE file.name != "Project Template"
SORT file.name ASC
SORT company ASC
SORT project_id ASC
SORT status ASC
```
Active:
```dataview
TABLE
issues as "Issues",
[project] as "project",
map(Bottlenecks.text, (x ) => "- " + x) as "Bottlenecks",
map(OpenTasks.text, (x) => "- " + x) as "Open Tasks",
map(OpenQuestions.text, (x) => "- " + x) as "Open Questions"

flatten list(file.tasks) as openTasks
FLATTEN list(filter(file.tasks, (tasks) => tasks.status != "x")) as NotFinished
FLATTEN list(filter(NotFinished, (tasks) => tasks.status != "?" and tasks.status != "A" and tasks.status != "p")) as OpenTasks
FLATTEN list(filter(NotFinished, (tasks) => tasks.status = "~")) as Bottlenecks
FLATTEN list(filter(NotFinished, (tasks) => tasks.status = "?")) as OpenQuestions
WHERE type = "project"
WHERE status = "active"
WHERE file.name != "Project Template"
SORT file.name ASC
SORT company ASC
SORT project_id ASC
SORT status ASC
```
Stalled:
 ```dataview
TABLE
issues as "Issues",
[project] as "project",
map(Bottlenecks.text, (x ) => "- " + x) as "Bottlenecks",
map(OpenTasks.text, (x) => "- " + x) as "Open Tasks",
map(OpenQuestions.text, (x) => "- " + x) as "Open Questions"

flatten list(file.tasks) as openTasks
FLATTEN list(filter(file.tasks, (tasks) => tasks.status != "x")) as NotFinished
FLATTEN list(filter(NotFinished, (tasks) => tasks.status != "?" and tasks.status != "A" and tasks.status != "p")) as OpenTasks
FLATTEN list(filter(NotFinished, (tasks) => tasks.status = "~")) as Bottlenecks
FLATTEN list(filter(NotFinished, (tasks) => tasks.status = "?")) as OpenQuestions
WHERE type = "project"
WHERE status = "stalled" or status = "waiting"
WHERE file.name != "Project Template"
SORT file.name ASC
SORT company ASC
SORT project_id ASC
SORT status ASC
```
 In Review:
```dataview
TABLE
issues as "Issues",
map(Bottlenecks.text, (x ) => "- " + x) as "Bottlenecks",
map(OpenTasks.text, (x) => "- " + x) as "Open Tasks",
map(OpenQuestions.text, (x) => "- " + x) as "Open Questions"

flatten list(file.tasks) as openTasks
FLATTEN list(filter(file.tasks, (tasks) => tasks.status != "x")) as NotFinished
FLATTEN list(filter(NotFinished, (tasks) => tasks.status != "?")) as OpenTasks
FLATTEN list(filter(NotFinished, (tasks) => tasks.status = "~")) as Bottlenecks
FLATTEN list(filter(NotFinished, (tasks) => tasks.status = "?")) as OpenQuestions
WHERE type = "project"
WHERE status = "in review"
WHERE file.name != "Project Template"
SORT file.name ASC
SORT company ASC
SORT project_id ASC

```
