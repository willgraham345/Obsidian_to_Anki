---
type: vault_tool
date created: Wednesday, April 9th 2025, 3:55:58 pm
date modified: Wednesday, April 9th 2025, 3:56:39 pm
---

```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Options",
	[T.link] as "Link"
FROM "Docs" AND #code/rust
flatten file.tasks as T
flatten string(T.text) as txt
WHERE contains(T.tags, "#code/rust")
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```