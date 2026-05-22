---
summary: Writing queries in a way that doesn't have SQL injection vulnerability.
headings:
  - "[[#Examples]]"
  - "[[#Media]]"
  - "[[#Usage]]"
type: note/item
item_of:
  - "[[Cpp libpqxx]]"
date created: Wednesday, April 9th 2025, 4:22:52 pm
date modified: Wednesday, April 9th 2025, 4:36:16 pm
tags:
  - lang/database
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage




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
