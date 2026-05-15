---
summary: Cheatsheets for queries
type: cheatsheet
date created: Thursday, December 5th 2024, 3:26:04 pm
date modified: Thursday, December 5th 2024, 3:27:36 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

Delimited Strings
```
SELECT 
    id,
    split_part(combined_column, ',', 1) AS column1,
    split_part(combined_column, ',', 2) AS column2,
    split_part(combined_column, ',', 3) AS column3
FROM my_table;
```
Unpack Array elements in Column
```
SELECT 
    id,
    combined_column[1] AS column1,
    combined_column[2] AS column2,
    combined_column[3] AS column3
FROM my_table;
```