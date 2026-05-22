---
summary: Class template that wraps a referencein a copyable, assignable object. Frequently used as a mechanism to store references inside standard containers which can't hold references (i.e. `std::vector`). Useful in combination with templates.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/item
date created: Monday, November 3rd 2025, 3:03:39 pm
date modified: Monday, November 3rd 2025, 3:18:13 pm
item_of:
  - "[[Cpp std functional (library)]]"
template: "[[base_note_template]]"
template-version: 1.0.0
used_by:
  - "[[Cpp std optional (class)]]"
  - "[[Cpp std vector]]"
uses:
  - "[[Cpp std function]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- CopyConstructible and CopyAssignable wrapper around a reference to object or reference to function of type `T`.
- Refers an object by storing a pointer to it, allowing for reassignment and copy while mimicking lvalue semantics. 

## Usage