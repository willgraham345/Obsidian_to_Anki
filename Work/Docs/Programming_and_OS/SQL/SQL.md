---
summary: 
type: note/system
implements:
  - "[[Postgres]]"
down:
  - "[[Postgres psql Cheatsheet]]"
  - "[[SQL Cheatsheet]]"
workflows:
  - "[[Postgres Creating a new Table]]"
  - "[[Postgres Populating a Table With Rows]]"
date created: Thursday, December 5th 2024, 1:41:00 pm
date modified: Tuesday, April 1st 2025, 4:58:57 pm
concepts:
  - "[[SQL Terminology]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
Relation = mathematical term for table

Each table is a named collection of rows. Each row has a given table of the same set of named columns, and each column is of a specific data type.

SQL does not guarantee the order of rows within the table in any way (although they can be explicitly sorted for display).

Tables are grouped into databases, and a collection of databases is managed by a single PostgreSQL server instance

# Usage
<iframe src="https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546" style="width: 100%; height: 600px;background-color:white;"></iframe>