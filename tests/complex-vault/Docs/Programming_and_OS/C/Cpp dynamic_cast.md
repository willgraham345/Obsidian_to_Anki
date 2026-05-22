---
summary: Safely converts pointers and references to classes up, down, and sideways along the inheritance hierarchy.
type: note/function
headings: ["[[#Concepts of Note]]", "[[#Flashcards]]", "[[#Syntax]]", "[[#Usage]]"]
similar: ["[[Cpp static_cast]]"]
date created: Friday, December 27th 2024, 5:35:05 pm
date modified: Thursday, January 15th 2026, 1:16:04 pm
function_of: ["[[Cpp Casting]]"]
tags: [lang/data/casting]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note


## Syntax
```
dynamic_cast<target_type>(expression)
```
- target_type: Pointer to complete class type | reference to complete class type | pointer to void
- expression: lvalue

## Usage
󰠗  What keyword does `dynamic_cast` rely on? ;; `typeid`

## Media
[dynamic\_cast conversion - cppreference.com](https://en.cppreference.com/w/cpp/language/dynamic_cast)

## Flashcards
󰠗 What is a dynamic_cast used for? ;; Converting types along the inheritance hierarchy. 