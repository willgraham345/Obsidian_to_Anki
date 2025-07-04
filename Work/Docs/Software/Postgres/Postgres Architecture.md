---
summary: PostgreSQL uses a client/server model. Server manages the database files, accepts connections, and performs database actions on behalf of the clients. The server program is called postgres. The frontend application (client) can be just about anything. The server can accept multiple connections.
type: note/concept
concepts:
  - "[[Postgres Tablespace]]"
  - "[[Postgres Views]]"
  - "[[Postgres schemas]]"
  - "[[Postgres Inheritance]]"
date created: Thursday, December 5th 2024, 1:35:52 pm
date modified: Tuesday, April 1st 2025, 5:05:44 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

## Concepts of Note
All database objects are managed by their respective object identifiers OIDs.
The OID is stored in the pg_databasesystem table. 

Tablespace

## Media
![[Postgres Architecture.png| 500]]