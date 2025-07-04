---
summary: Writing queries in a way that doesn't have SQL injection vulnerability.
headings: ["[[#Examples]]", "[[#Media]]", "[[#Usage]]"]
type: note/component
component_of: ["[[Cpp libpqxx]]"]
date created: Wednesday, April 9th 2025, 4:22:52 pm
date modified: Wednesday, April 9th 2025, 4:36:16 pm
tags: [code/cpp/database]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage
- [p] [[#Esc with params]] = Create column in Postgres DB from cpp = #code/cpp/database
<!--ID: 1751434091636-->


## Examples
### Esc with params
```cpp
tx.exec(
	" SELECT number, amount "
	"FROM account "
	"WHERE allowed_to_see($1, $2)",
pqxx:params{userId, password}
```

## Media
[libpqxx: String escaping](https://libpqxx.readthedocs.io/stable/escaping.html)