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
  - code/postgres/data/constraint
  - code/postgres/data/definition
  - code/postgres/data/write
  - code/postgres/relationships
  - code/postgres/table
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
- [p] `CREATE TABLE <table_name>` = Create a PostgreSQL table. = #code/postgres/table
<!--ID: 1751434089626-->

- [p] `DROP TABLE <table_name>` = Deletes/removes a PostgreSQL table. = #code/postgres/table 
<!--ID: 1751434089635-->

- [p] `INSERT INTO <table_name> (<cols>) VALUES (<vals>)` = Inserts a row into a table = #code/postgres/data/write
<!--ID: 1751434089639-->

- [p] `CREATE SEQUENCE` = Defines a new sequence number generator. = #code/postgres/table 
<!--ID: 1751434089643-->

- [p] `ALWAYS` = Similar to `BY DEFAULT`, but the default can only be overriden by an explicit value. = #code/postgres/data/definition
<!--ID: 1751434089647-->

- [p] `BY DEFAULT` = User-specified value takes precedence = #code/postgres/data/definition
<!--ID: 1751434089651-->

- [p] `CHECK (<conditional>)` = Check constraint with true/false as output = #code/postgres/data/constraint
<!--ID: 1751434089655-->

- [p] `CONSTRAINT <constraintName> <constraint>` = Names a constraint for use later. If not used, the system will choose a name for you. = #code/postgres/data/constraint 
<!--ID: 1751434089659-->

- [p] `NOT NULL` = Specifies that the column can't be null = #code/postgres/data/constraint 
<!--ID: 1751434089664-->

- [p] `UNIQUE` = Specifies that the column must have only unique data = #code/postgres/data/constraint 
<!--ID: 1751434089667-->

- [p] `PRIMARY KEY` = Indicates that a a column (or group of columns) can be used as a unique identifier for rows in the table = #code/postgres/data/constraint 
<!--ID: 1751434089672-->

- [p] `REFERENCES` = Constraint that says values in a column (or group of columns) must match the values appearing in some row of another table = #code/postgres/data/constraint  #code/postgres/relationships
<!--ID: 1751434089676-->

- [p] `EXCLUDE USING`
- [p] `ALTER TABLE <table_name> ADD/ALTER/DROP <field_name>` = Change/remove columns, defaults, and constraints = #code/postgres/data/constraint #code/postgres/data/definition #code/postgres/table 
<!--ID: 1751434089681-->
