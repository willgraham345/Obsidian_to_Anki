---
summary: Relational database, where entries (members) are allowed to have multiple owners (owners).
type: note/system
concepts:
  - "[[MariaDB Relational Detabases]]"
headings:
  - "[[#Concepts of Note]]"
  - "[[#Media]]"
date created: Sunday, February 16th 2025, 6:43:32 pm
date modified: Sunday, February 16th 2025, 7:45:52 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
Databases should be thought of as a collection of related files
A database management system (DBMS) helps manage the task to find the file.
Relational database models allow one file to be related to any other means of a common field.

Each table consists of rows and columns
- Data = values kept in the database
- Information = processed data
- Database = collection of tables
- 
- Row = Record
-  Attribute = Column
	- One piece of data that relates to the record (called a tuple)
- Field = An attribute when referring to a database table

## Media
```mermaid
graph LR
	data@{shape: card, label: "data<br>(row)"}
	%% Information@{shape: rectangle}
	records@{label: "records<br>(tuples)"}
	table@{shape: doc, label: "table"}
	database@{shape: db, label: "database<br>(entities)"}
	
%% Links
%% Information -- "connects these two" --> data
%% Information -- "connects these two" --> records
data --> records
attribute -- "comprised of " --> records
records -- "comprised of..." --> table
table-- "comprised of..." --> database
key -- "accesses" --> table
index -- "part of physical structure, similar to key" --> table
table -- "virtual table" --> view

%% Notes
%% classDefs	
```

Database Terminology
[Relational Databases: Basic Terms - MariaDB Knowledge Base](https://mariadb.com/kb/en/relational-databases-basic-terms/)