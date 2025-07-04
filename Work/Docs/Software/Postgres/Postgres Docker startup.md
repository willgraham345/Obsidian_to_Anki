---
summary: Different stuff postgres images look for
type: 
headings:
  - "[[#Concepts of Note]]"
  - "[[#Macros]]"
date created: Thursday, December 5th 2024, 1:29:19 pm
date modified: Monday, March 24th 2025, 6:25:55 pm
tags:
  - command/postgresql
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
- [p] `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres` = Start a postgres instance = #command/postgresql
<!--ID: 1751434089685-->

- [p] `docker run -it --rm --network some-network postgres psql -h some-postgres`

## Concepts of Note
### Init scripts
These run any executable shell scripts or command-based `.sql` files once Postgres creates a folderr. 

## Macros
- `POSTGRES_USER` – Specifies a user with superuser privileges and a database with the same name. Postgres uses the default user when this is empty.
- `POSTGRES_DB` – Specifies a name for your database or defaults to the `POSTGRES_USER` value when left blank. 
- `POSTGRES_INITDB_ARGS` – Sends arguments to `postgres_initdb` and adds functionality
- `POSTGRES_INITDB_WALDIR` – Defines a specific directory for the Postgres transaction log. A transaction is an operation and usually describes a change to your database. 
- `POSTGRES_HOST_AUTH_METHOD` – Controls the `auth-method` for `host` connections to `all` databases, users, and addresses
- `PGDATA` – Defines another default location or subdirectory for database files

## Media
[How to Use the Postgres Docker Official Image | Docker](https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/#Start-a-Postgres-instance)