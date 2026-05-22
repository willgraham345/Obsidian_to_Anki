---
summary: Commands for navigating using the psql tool.
type:
headings:
up:
  - "[[Postgres]]"
  - "[[SQL]]"
processes:
  - "[[Postgres Accessing a Database]]"
date created: Thursday, December 5th 2024, 1:50:08 pm
date modified: Wednesday, January 21st 2026, 4:47:13 pm
tags:
  - tools/databases/sql
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
  `psql <database_name>` ;;; Launches the psql tool from cli 
  `\c [database_name]` ;;; Connect to a specific database. = 
  `\conninfo` ;;; Display information about the current connection. = 
  `\q` ;;; Quit the psql session. = 
  `\l` ;;; List all databases. = 
  `\d` ;;; List all tables, views, and sequences in the current database. = 
  `\d+` ;;; Detailed listing of all tables, views, and sequences. = 
  `\dt` ;;; List all tables. = 
  `\di` ;;; List all indexes. = 
  `\dv` ;;; List all views. = 
  `\ds` ;;; List all sequences. = 
  `\d table_name` ;;; Show the schema of a specific table. = 
  `\d+ table_name` ;;; Show detailed information about a specific table. = 
  `\i [file.sql]` ;;; Execute SQL commands from a file. = 
  `\du` ;;; List all roles and users. = 
  `SELECT * FROM table_name LIMIT n;` ;;; View the first `n` rows of a table. = 
  `INSERT INTO table_name (...) VALUES (...);` ;;; Insert a record into a table. = 
  `UPDATE table_name SET column=value WHERE condition;` ;;; Update records in a table. = 
  `DELETE FROM <table_name> WHERE <condition>;` ;;; Delete records from a table. = 
  `\copy <table_name> FROM <file_path> DELIMITER ',' CSV;` ;;; Import CSV data into a table. = 
  `\copy <table_name> TO <file_path> DELIMITER ',' CSV HEADER;` ;;; Export table data to a CSV file. = 
  `\x` ;;; Toggle expanded output for better readability of wide rows. = 
  `\timing` ;;; Toggle display of execution time for SQL queries. = 
  `\a` ;;; Switch to unaligned (plain text) output. = 
  `\H` ;;; Output query results in HTML format. = 
  `\?` ;;; Display help on psql commands. = 
  `\h [SQL_command]` ;;; Get syntax help for a specific SQL command. = 
