---
summary: A variable that "points" to a location in memory. Hugely useful, as they often require much less memory than the data they point towards. Used extensively within arrays and functions. Notably, for use within functions, they can be a nullpointer signifying that they do not point to a valid location in memory. This can't be performed with references.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/concept
implements:
  - "[[Cpp Functions]]"
workflows:
  - "[[Cpp function array arguments]]"
  - "[[Cpp function pointers and references]]"
similar:
  - "[[Cpp references]]"
associations:
  - "[[Cpp references]]"
  - "[[Cpp std array]]"
component_of:
  - "[[Cpp Memory]]"
  - "[[Cpp std array]]"
  - "[[Cpp.Smart Pointers]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, June 19th 2025, 1:53:43 pm
implementations:
  - "[[Cpp const]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
- Arrays are contiguous locations in memory, so C-style pointers pass an array pointer with the length in order to resolve this challenge

## Usage
- [[Cpp const]]
- [[Cpp function array arguments]]
- [[Cpp function pointers and references]]
