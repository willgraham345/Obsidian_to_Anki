---
type: vault_tool
date created: Wednesday, March 19th 2025, 11:43:21 am
date modified: Thursday, July 3rd 2025, 1:51:3 am
tags:
  - command/ansible
---



filter_tag:: #command/ansible 
```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Options",
	[T.link] as "Link"
FROM "Docs" 
FLATTEN this.filter_tag as filter_tag
flatten file.tasks as T
flatten string(T.text) as txt
WHERE contains(T.tags, filter_tag)
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```
