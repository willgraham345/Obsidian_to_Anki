```dataview
TABLE 
	summary, file.ctime as "Created", file.mtime as "Modified"
FROM outgoing([[]])
SORT file.mtime DESC
```