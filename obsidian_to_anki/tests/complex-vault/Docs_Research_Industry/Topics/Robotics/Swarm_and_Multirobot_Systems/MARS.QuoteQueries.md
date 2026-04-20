
```dataview
TABLE file.name, T.text AS "Tasks", file.tags
FROM #research/MARS 
flatten file.tasks as T
where T.status = "'"
where T.text
```