---
type: vault_tool
date created: Friday, September 13th 2024, 3:36:43 pm
date modified: Thursday, December 5th 2024, 11:35:11 am
---

filter_tag::
```dataview
TABLE 
	WITHOUT ID 
	split(string(txt), "=")[0] as "Command",
	split(string(txt), "=")[1] as "Description",
	split(string(txt), "=")[3] as "Options",
	T.link as "link"
FLATTEN this.filter_tag as filter_tag
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```

# Base unfiltered Codeblock
```
TABLE 
	WITHOUT ID 
	split(string(txt), "=")[0] as "Command",
	split(string(txt), "=")[1] as "Description",
	split(string(txt), "=")[3] as "Options",
	T.link as "link"
FLATTEN this.filter_tag as filter_tag
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort T.text ASC
```

# Base filter codeblock
``` base 
TABLE 
	WITHOUT ID 
	split(string(txt), "=")[0] as "Command",
	split(string(txt), "=")[1] as "Description",
	split(string(txt), "=")[3] as "Options"
	[T.link, tags] as "Link/Tags"
FROM "AA_Will's_Notes_and_References" && /command/cmd_name
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort Command ASC
```
