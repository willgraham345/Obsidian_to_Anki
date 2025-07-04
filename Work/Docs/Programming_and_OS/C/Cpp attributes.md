---
summary: Modern c++ (11) feature which allows programmer to specify additional information to the compiler to enforce constraints, optimize certain pieces of code, or do specific code generation. Acts as an annotation or a note to the compiler which provides additional information about the code.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
type: 
date created: Wednesday, June 4th 2025, 10:42:05 am
date modified: Wednesday, July 2nd 2025, 10:47:54 am
concept_of:
  - "[[Cpp]]"
used_by:
  - "[[Cpp switch]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [p] `[[no-return]] void f` = Marks that the function does not return a value, hinting that the compiler can optimize this codeblock. = #code/cpp/attributes #code/cpp/compiler 
<!--ID: 1751434091756-->

- [p] `struct [[deprecated]] S` = Marks that the name/entity has become obsolete. Can be applied to namespaces, functions, classes or variables. = #code/cpp/attributes #code/cpp/deprecation
<!--ID: 1751434091760-->

- [p] `[[fallthrough]]` = Indicates that a fallthrough in a switch statement is intentional, and won't return an error. = #code/cpp/attributes #code/cpp/deprecation
<!--ID: 1751434091764-->
 ^4207c2
- [p] `void list(node* n)[[expects:n != nullptr]]` = Specifies conditions (in form of contract) that the arguments must meet for a particular function to be executed. = #code/cpp/controlFlow #code/cpp/attributes #code/cpp/controlFlow/attributes
<!--ID: 1751434091768-->

## Examples
```cpp
int f(int i)[[expects:i > 0]]
{
    // Code
}
```