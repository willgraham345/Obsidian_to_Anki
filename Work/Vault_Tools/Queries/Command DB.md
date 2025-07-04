---
summary: 
type: vault_tool
aliases: []
date created: Monday, September 16th 2024, 10:37:03 am
date modified: Monday, December 16th 2024, 10:33:00 am
tags: [command/cmake, command/docker, command/git, command/linux]
---
filter_tag:: #command/linux 
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

# Base codeblock
``` base 
TABLE 
	WITHOUT ID 
	split(string(txt), " = ")[0] as "Command",
	split(string(txt), " = ")[1] as "Description",
	split(string(txt), " = ")[3] as "Options"
	[T.link, tags] as "Link/Tags"
FROM "Docs" && /command/cmd_name
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "p"
where file.link != [[Checkboxes]] 
sort tags DESC
sort Command ASC
```
	Format for commands
```
- [p] <`command`> <description> <`#tag`>
```