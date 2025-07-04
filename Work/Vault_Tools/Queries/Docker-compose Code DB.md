---
type: vault_tool
date created: Friday, April 25th 2025, 3:56:27 pm
date modified: Friday, April 25th 2025, 3:56:54 pm
---

```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Options",
	[T.link] as "Link"
FROM "Docs" AND #code/dockercompose
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```