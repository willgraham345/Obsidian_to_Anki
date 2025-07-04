---
summary: Type traits, compile-time rational arithmetic, and compile-time integer sequences. Check out the website for a more thorough check of what types of traits this has.
headings: ["[[#Breadcrumbs]]", "[[#Concepts of Note]]", "[[#null]]"]
type: note/library
components:
  [
    "[[Cpp is_class]]",
    "[[Cpp is_enum]]",
    "[[Cpp is_lvalue_reference]]",
    "[[Cpp is_member_function_pointer]]",
    "[[Cpp is_member_object_pointer]]",
    "[[Cpp is_pointer]]",
    "[[Cpp is_rvalue_reference]]",
    "[[Cpp is_void]]",
    "[[Cpp underlying_type]]",
  ]
date created: Monday, May 19th 2025, 1:47:41 pm
date modified: Monday, May 19th 2025, 1:57:53 pm
library_used_in: ["[[Cpp std]]"]
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Metaprogramming library (since C++11) - cppreference.com](https://en.cppreference.com/w/cpp/meta)

## Concepts of Note

- [I] Referenceable types = Object types, function types, reference types. For any referenceable type `T`, a reference to it can be created. = #term/cpp
- [I] Type traits = Define compile-time template-based interfaces to query the properties of types. Attempting to specialize a template defined in the `type_traits` header and listed in this page is undefined behavior. = #code/cpp

### Unary type Traits

Includes:

- Primary type categories
- Composite type categories
- Type properties
- Scoped operations

### Property Queries

Includes:

- Type relationships
- Type transformations
- Other transformations
- Logical operations
- Member relationships

## Breadcrumbs

```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```
