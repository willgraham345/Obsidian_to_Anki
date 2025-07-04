---
company: Varex
Aliases: [ "#archive_deprecated/Varex/vivaPro" ]
---

```dataview
TABLE
	file.tags as "Tags",
	file.path as "File Path",
	file.mday as "Modified Date"
	from #Varex/vivaPro  
	SORT file.mday desc
```