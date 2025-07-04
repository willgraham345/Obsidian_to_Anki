---
type: vault_tool
date created: Sunday, August 25th 2024, 5:06:07 pm
date modified: Monday, June 9th 2025, 12:00:01 pm
---


```dataview
TABLE WITHOUT ID
	term AS "Term",
	val AS "Definition",
	file.link as link
FROM ""
flatten file.tasks as T
where T.status = "I"
where T.text
flatten split(string(T.text), "=")[0] as term
flatten split(string(T.text), "=")[1] as val
sort T.text ASC
where file.link != [[Checkboxes]] 
```