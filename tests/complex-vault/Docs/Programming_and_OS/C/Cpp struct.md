---
summary: Similar to a [[Cpp Class]], but default inheritance and default members are `public`
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
up:
  - "[[Cpp]]"
associations:
  - "[[Cpp Class]]"
concept_of:
  - "[[Cpp Variables and Containers]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, April 2nd 2026, 4:51:55 pm
tags: [lang/oop/class, lang/oop/struct]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  What's the difference between a `class` and a `struct` in cpp? ;; A struct has defaults of `public` inheritance, while a class uses `private` inheritance. Both serve similar functions. 
- Struct initialization must be non-empty, brace enclosed, comma separated list of initializers for the members.

## Usage

## Syntax
### Declaration
```cpp
struct NewType {
    type1 var1;
    type2 var2;
    .
    .
    .
    typeN varN;
};
```

### Initialization
```
NewType a = { .var1=val1, .val2=var2, ..., .valN=varN }
```
