---
summary: Every object and reference has a lifetime, which is a runtime property.
headings: ["[[#Concepts of Note]]"]
type: 
date created: Thursday, May 15th 2025, 10:07:27 am
date modified: Thursday, May 15th 2025, 10:11:13 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Lifetime - cppreference.com](https://en.cppreference.com/w/cpp/language/lifetime)

## Concepts of Note
### Beginning
- Storage w/right alignment and size is obtained
- Initialization (if any) is complete
	- Exceptions to this include: union member, union object, or array.

### Ending
- If non-class type -> ends when the destructor is called
- If class-type -> destructor call starts
- The storage which the occupies is released, or reused by an object that is not nested within it

### Temporary Object Lifetime
### Storage reuse
### Accessing outside of lifetime