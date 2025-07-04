---
type: vault_tool
date created: Friday, November 1st 2024, 2:43:13 pm
date modified: Monday, December 2nd 2024, 12:04:00 pm
---



```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Options",
	[T.link] as "Link"
FROM "Docs" AND #command/dockerfile
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```