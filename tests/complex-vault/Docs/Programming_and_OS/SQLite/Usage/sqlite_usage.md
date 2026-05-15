---
type: tutorial
tags:
  - programming/sqlite
  - programming/databases
date created: Sunday, March 22nd 2026, 12:00:00 pm
date modified: Sunday, March 22nd 2026, 12:00:00 pm
up: "[[SQLite]]"
concepts:
  - "[[SQLite Data Types]]"
  - "[[SQLite Transactions]]"
  - "[[SQLite Indexes]]"
  - "[[SQLite Pragma]]"
tools:
  - "[[DB Browser for SQLite]]"
  - "[[datasette]]"
  - "[[sqlite-utils]]"
---

# Summary
󰙎 sqlite_usage ;;; CLI and application workflows for creating, connecting to, and populating SQLite databases

# Additional Background
SQLite is embedded — no server process. A `.db` file IS the database. A connection = opening that file; it is created automatically if absent.

## Concepts of Note
󰙎 connection ;;; open handle to a `.db` file; creates the file if it does not exist
󰙎 cursor ;;; executes SQL and iterates result rows within a connection
󰙎 schema ;;; collection of table definitions; inspect via `.schema` (CLI) or `sqlite_master` table
󰙎 WAL mode ;;; write-ahead log; allows concurrent reads during a write

**Suggested subnotes to create:**

| Note | Content |
|---|---|
| [[SQLite Data Types]] | Affinity system: TEXT, INTEGER, REAL, BLOB, NULL |
| [[SQLite Transactions]] | BEGIN / COMMIT / ROLLBACK, isolation levels |
| [[SQLite Indexes]] | CREATE INDEX, covering indexes, query planning |
| [[SQLite Pragma]] | `PRAGMA journal_mode`, `PRAGMA foreign_keys`, `PRAGMA optimize` |
| [[SQLite Constraints]] | PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL |

## Usage

### CLI
- [p] `sqlite3 mydb.db` ;;; open or create a database file
- [p] `CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT NOT NULL);` ;;; create a table
- [p] `.tables` ;;; list all tables
- [p] `.schema t` ;;; show CREATE statement for table `t`
- [p] `INSERT INTO t VALUES (1, 'foo');` ;;; insert a row
- [p] `.mode column` + `.headers on` ;;; readable column output
- [p] `.dump` ;;; export full DB as SQL text
- [p] `.quit` ;;; exit shell

### Application Connection (Python)
- [p] `conn = sqlite3.connect('mydb.db')` ;;; open or create `.db`; returns a Connection object
- [p] `cur = conn.cursor()` ;;; create a Cursor for executing statements
- [p] `conn.execute(sql)` ;;; shortcut: execute directly on connection
- [p] `conn.commit()` ;;; persist pending changes
- [p] `conn.close()` ;;; release the file handle

### Creating Tables from Application
- [p] `conn.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, name TEXT)")` ;;; idempotent table creation

### Inserting Entries

| Method | Form | Use case |
|---|---|---|
| Single row | `conn.execute("INSERT INTO t VALUES (?, ?)", (1, 'foo'))` | Safe parameterized insert |
| Bulk | `conn.executemany(sql, list_of_tuples)` | Insert from list/generator |
| Upsert | `INSERT OR REPLACE INTO t ...` | Overwrite on PK conflict |
| Skip | `INSERT OR IGNORE INTO t ...` | No-op on constraint violation |

## Properties

### Visualization & Debugging Tools

| Tool | Use |
|---|---|
| [[DB Browser for SQLite]] | GUI: browse schema, edit rows, run queries, visualize structure |
| [[datasette]] | Local web UI for read-only exploration; instant from any `.db` file |
| [[sqlite-utils]] | CLI + Python lib: insert, transform, query without writing SQL manually |
| `EXPLAIN QUERY PLAN` | Inspect query execution path; reveals index usage |
| `sqlite_master` | System table: metadata for all tables, indexes, and triggers |

## Flashcards
- [t] How does an application open (or create) a SQLite database? ;; `sqlite3.connect('file.db')` — creates the file if absent; no server needed
- [t] How do you safely insert user data into SQLite? ;; Parameterized queries: `execute("INSERT INTO t VALUES (?)", (value,))` — prevents SQL injection
- [t] How do you inspect the schema of a table in the CLI? ;; `.schema tablename` or query `SELECT sql FROM sqlite_master WHERE name='tablename'`
- [t] What tool provides a GUI for browsing a SQLite database? ;; [[DB Browser for SQLite]]
