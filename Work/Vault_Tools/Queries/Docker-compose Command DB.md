---
date created: Wednesday, February 5th 2025, 1:34:49 pm
date modified: Saturday, February 8th 2025, 1:02:19 pm
---

```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Options",
	[T.link] as "Link"
FROM "Docs" AND #command/dockercompose
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```