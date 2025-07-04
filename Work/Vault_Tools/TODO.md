---
type: vault_tool
date created: Tuesday, September 24th 2024, 9:42:23 am
date modified: Monday, September 30th 2024, 8:57:52 am
---

```dataview
TABLE 
	WITHOUT ID 
	txt as "Task",
	[T.link, tags] as "Link/Tags" 
FROM "Active Projects" or "Archive"
flatten file.tasks as T
flatten string(T.text) as txt
where file.link != [[Checkboxes]] 
where T.status = " "

```

```dataview
TABLE WITHOUT ID T.text AS "Questions", T.link as link, tags as "tags"
FROM "" and !"#questions/no_rush"
flatten file.tasks as T

where T.status = "?"
where T.text
sort T.text ASC
where file.link != [[Checkboxes]] 
sort tags DESC
```