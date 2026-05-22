---
summary: Modern c++ (11) feature which allows programmer to specify additional information to the compiler to enforce constraints, optimize certain pieces of code, or do specific code generation. Acts as an annotation or a note to the compiler which provides additional information about the code.
type:
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
similar:
  - "[[Cpp __attribute__]]"
concept_of:
  - "[[Cpp]]"
date created: Wednesday, June 4th 2025, 10:42:05 am
date modified: Tuesday, March 17th 2026, 3:12:29 pm
tags: [lang/build/compiler, lang/control_flow, lang/control_flow/attributes, lang/meta/attributes, lang/meta/deprecation]
template:
template-version:
used_by:
  - "[[Cpp switch]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
  `[[no-return]] void f` ;;; Marks that the function does not return a value, hinting that the compiler can optimize this codeblock. =  



  `struct [[deprecated]] S` ;;; Marks that the name/entity has become obsolete. Can be applied to namespaces, functions, classes or variables. 


  `[[fallthrough]]` ;;; Indicates that a fallthrough in a switch statement is intentional, and won't return an error. ^4207c2

  `void list(node* n)[[expects:n != nullptr]]` ;;; Specifies conditions (in form of contract) that the arguments must meet for a particular function to be executed.

## Examples
```cpp
int f(int i)[[expects:i > 0]]
{
    // Code
}
```
