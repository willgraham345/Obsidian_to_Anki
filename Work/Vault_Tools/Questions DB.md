---
date created: Monday, August 26th 2024, 1:12:20 pm
date modified: Friday, October 4th 2024, 11:35:31 am
type: vault_tool
---
```dataview
TABLE WITHOUT ID T.text AS "Questions", T.link as link, tags as "tags"
FROM "" and !"Active Projects"
flatten file.tasks as T

where T.status = "?"
where T.text
where file.link != [[Checkboxes]] 
sort T.link DESC 
```

```dataview
TABLE WITHOUT ID T.text AS "Questions", T.link as link, tags as "tags"
FROM "Active Projects"
flatten file.tasks as T

where T.status = "?"
where T.text
where file.link != [[Checkboxes]] 
sort tags ASC
sort T.link DESC 
```

- [?] Data flow. What is the typical documentation used to propose, update, and create a project? 
	- [?] How can I navigate it?