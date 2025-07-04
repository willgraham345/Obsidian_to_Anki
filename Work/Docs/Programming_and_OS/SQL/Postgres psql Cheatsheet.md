---
summary: Commands for navigating using the psql tool.
type: 
up: ["[[Postgres]]", "[[SQL]]"]
date created: Thursday, December 5th 2024, 1:50:08 pm
date modified: Thursday, July 3rd 2025, 1:53:47 pm
tags: [command/postgresql]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
- [c] `psql <database_name>` = Launches the psql tool from cli = #command/postgresql  = `-U <user>` Specifies user (see PGUSER for what to put here) 
<!--ID: 1751434089853-->

      `-W` prompts you for the password\
- [c] `\c [database_name]` = Connect to a specific database. = #command/postgresql
<!--ID: 1751434089857-->

- [c] `\conninfo` = Display information about the current connection. = #command/postgresql
<!--ID: 1751434089860-->

- [c] `\q` = Quit the psql session. = #command/postgresql
<!--ID: 1751434089864-->

- [c] `\l` = List all databases. = #command/postgresql
<!--ID: 1751434089868-->

- [c] `\d` = List all tables, views, and sequences in the current database. = #command/postgresql
<!--ID: 1751434089872-->

- [c] `\d+` = Detailed listing of all tables, views, and sequences. = #command/postgresql
<!--ID: 1751434089876-->

- [c] `\dt` = List all tables. = #command/postgresql
<!--ID: 1751434089880-->

- [c] `\di` = List all indexes. = #command/postgresql
<!--ID: 1751434089884-->

- [c] `\dv` = List all views. = #command/postgresql
<!--ID: 1751434089889-->

- [c] `\ds` = List all sequences. = #command/postgresql
<!--ID: 1751434089893-->

- [c] `\d table_name` = Show the schema of a specific table. = #command/postgresql
<!--ID: 1751434089897-->

- [c] `\d+ table_name` = Show detailed information about a specific table. = #command/postgresql
<!--ID: 1751434089901-->

- [c] `\i [file.sql]` = Execute SQL commands from a file. = #command/postgresql
<!--ID: 1751434089906-->

- [c] `\du` = List all roles and users. = #command/postgresql
<!--ID: 1751434089910-->

- [c] `SELECT * FROM table_name LIMIT n;` = View the first `n` rows of a table. = #command/postgresql
<!--ID: 1751434089914-->

- [c] `INSERT INTO table_name (...) VALUES (...);` = Insert a record into a table. = #command/postgresql
<!--ID: 1751434089918-->

- [c] `UPDATE table_name SET column=value WHERE condition;` = Update records in a table. = #command/postgresql
<!--ID: 1751434089923-->

- [c] `DELETE FROM <table_name> WHERE <condition>;` = Delete records from a table. = #command/postgresql
<!--ID: 1751434089927-->

- [c] `\copy <table_name> FROM <file_path> DELIMITER ',' CSV;` = Import CSV data into a table. = #command/postgresql
<!--ID: 1751434089931-->

- [c] `\copy <table_name> TO <file_path> DELIMITER ',' CSV HEADER;` = Export table data to a CSV file. = #command/postgresql
<!--ID: 1751434089936-->

- [c] `\x` = Toggle expanded output for better readability of wide rows. = #command/postgresql
<!--ID: 1751434089941-->

- [c] `\timing` = Toggle display of execution time for SQL queries. = #command/postgresql
<!--ID: 1751434089946-->

- [c] `\a` = Switch to unaligned (plain text) output. = #command/postgresql
<!--ID: 1751434089951-->

- [c] `\H` = Output query results in HTML format. = #command/postgresql
<!--ID: 1751434089956-->

- [c] `\?` = Display help on psql commands. = #command/postgresql
<!--ID: 1751434089961-->

- [c] `\h [SQL_command]` = Get syntax help for a specific SQL command. = #command/postgresql
<!--ID: 1751434089966-->
