---
date created: Monday, October 28th 2024, 10:54:41 am
date modified: Monday, October 28th 2024, 3:43:55 pm
type: vault_tool
---


```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Options",
	[T.link] as "Link"
FROM "Docs" AND #command/docker
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```