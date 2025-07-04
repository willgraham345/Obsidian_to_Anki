---
type: vault_tool
date created: Thursday, June 26th 2025, 2:56:36 pm
date modified: Thursday, June 26th 2025, 2:57:16 pm
---

```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Examples",
	[T.link] as "Link"
FROM "Docs" AND #term/cpp 
flatten file.tasks as T
flatten string(T.text) as txt
WHERE contains(T.tags, "#term/cpp")
where T.status = "I"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```