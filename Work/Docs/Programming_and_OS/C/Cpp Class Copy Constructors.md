---
summary: Tells how to copy the class/type
headings: ["[[#Concepts of Note]]", "[[#Syntax]]"]
type: note/component
associations: ["[[Cpp std vector#Vector Methods]]"]
date created: Tuesday, June 10th 2025, 12:17:48 pm
date modified: Tuesday, June 10th 2025, 12:32:11 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

- If a copy constructor isn't set, and you're working with a vector, see `.emplace()`
	- ![[Cpp std vector#^8ad293]]

## Syntax
```
ClassName (ClassName &obj)
{
  // body_containing_logic
}
```