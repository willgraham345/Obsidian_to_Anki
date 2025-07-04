---
type: vault_tool
date created: Tuesday, April 29th 2025, 10:28:24 am
date modified: Tuesday, April 29th 2025, 10:30:28 am
---

```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Examples",
	[T.link] as "Link"
FROM "Docs" AND #term/rust
flatten file.tasks as T
flatten string(T.text) as txt
WHERE contains(T.tags, "#term/rust")
where T.status = "I"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```