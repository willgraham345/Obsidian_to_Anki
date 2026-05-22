---
summary: Mapping from name to objects, working similar to a dictionary. Namespaces organize variables in a dedicated space to avoid naming conflicts. "Scope" refrs to the region of code where you can access a name. Most namespaces in python are implemented using dictionaries, with each namespace lifecycle tied to execution context (local/global are examples).
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
date created: Thursday, December 11th 2025, 11:12:39 am
date modified: Thursday, December 11th 2025, 11:14:15 am
template: "[[base_note_template]]"
template-version: 1.0.0
images:
  - "[[LEGB rule.avif]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
There are 4 main namespaces
1. Builtin ([[Python __builtins__]])
2. Global (mdoule level)
3. Local
4. Enclosing or nonlocal


## Diagrams


Namespacing searching priority
![[LEGB rule.avif]]