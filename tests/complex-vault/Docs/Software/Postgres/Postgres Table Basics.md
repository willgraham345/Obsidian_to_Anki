---
summary: Concepts have a fixed number of columns, each column has a name. Variable number of rows that is not guaranteed order. Each column has a data type which constrains the possible set of values.
type: note/concept
concept_of:
  - "[[Postgres Data Definition]]"
date created: Thursday, April 3rd 2025, 1:52:08 pm
date modified: Thursday, April 3rd 2025, 4:17:51 pm
headings:
  - "[[#Commands]]"
  - "[[#Concepts of Note]]"
tags:
  - tools/databases/data/constraint
  - tools/databases/data/definition
  - tools/databases/data/write
  - tools/databases/relationships
  - tools/databases/table
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Column types
- Identity Columns = Column generated automatically from an implicit sequence.
	- column supported by sequences
```sql
CREATE TABLE people (
id bigint GENERATED ALWAYS AS IDENTITY
)
```
- Generated columns = Column that is always computed from other columns. It is for columns what a view is for tables.
- Constraints = Gives you more control over what can/can't be entered into the column values.
	- Not-null constraints specifies that a column must not be the null value.
- System columns = Columns implicitly defined by system.

#### System columns
[PostgreSQL: Documentation: 17: 5.6. System Columns](https://www.postgresql.org/docs/current/ddl-system-columns.html)

### Privileges
- When an object is created, it is assigned an owner. Owner is typically the role that executed the creation statement. 
- For most objects, the initial state is that only the owner (or superuser) can do anything with the object.
[PostgreSQL: Documentation: 17: 5.8. Privileges](https://www.postgresql.org/docs/current/ddl-priv.html)

### Security
## Commands
  `CREATE TABLE <table_name>` ;;; Create a PostgreSQL table. = #tools/databases/table 
ID: 1751997629971



  `DROP TABLE <table_name>` ;;; Deletes/removes a PostgreSQL table. = #tools/databases/table  
ID: 1751997629975



  `INSERT INTO <table_name> (<cols>) VALUES (<vals>)` ;;; Inserts a row into a table = #tools/databases/data/write 
ID: 1751997629978



  `CREATE SEQUENCE` ;;; Defines a new sequence number generator. = #tools/databases/table  
ID: 1751997629982



  `ALWAYS` ;;; Similar to `BY DEFAULT`, but the default can only be overriden by an explicit value. = #tools/databases/data/definition 
ID: 1751997629987



  `BY DEFAULT` ;;; User-specified value takes precedence = #tools/databases/data/definition 
ID: 1751997629992



  `CHECK (<conditional>)` ;;; Check constraint with true/false as output = #tools/databases/data/constraint 
ID: 1751997629996



  `CONSTRAINT <constraintName> <constraint>` ;;; Names a constraint for use later. If not used, the system will choose a name for you. = #tools/databases/data/constraint  
ID: 1751997630000



  `NOT NULL` ;;; Specifies that the column can't be null = #tools/databases/data/constraint  
ID: 1751997630005



  `UNIQUE` ;;; Specifies that the column must have only unique data = #tools/databases/data/constraint  
ID: 1751997630009



  `PRIMARY KEY` ;;; Indicates that a a column (or group of columns) can be used as a unique identifier for rows in the table = #tools/databases/data/constraint  
ID: 1751997630018



  `REFERENCES` ;;; Constraint that says values in a column (or group of columns) must match the values appearing in some row of another table = #tools/databases/data/constraint  #tools/databases/relationships 
ID: 1751997630025



- [p] `EXCLUDE USING`
  `ALTER TABLE <table_name> ADD/ALTER/DROP <field_name>` ;;; Change/remove columns, defaults, and constraints = #tools/databases/data/constraint #tools/databases/data/definition #tools/databases/table  
ID: 1751997630029


