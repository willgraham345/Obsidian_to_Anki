---
summary: Special placeholders within SQL statement.
headings: 
type: note/item
associations:
  - "[[Cpp libpqxx string escaping]]"
item_of:
  - "[[Cpp libpqxx]]"
date created: Wednesday, April 9th 2025, 4:35:55 pm
date modified: Thursday, April 17th 2025, 2:23:35 pm
tags:
  - lang/database
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[libpqxx: Statement parameters](https://libpqxx.readthedocs.io/stable/parameters.html)

## Usage
  [[#Db params]] ;;; Add db params to a thing = #lang/database  
ID: 1751997629661




## Examples
### Db params
```cpp
pqxx::params{23, "acceptance", 3.14159}
```
```cpp
pqxx::params p;
p.append(23);
p.append("acceptance");
p.append(3.14159);
```

