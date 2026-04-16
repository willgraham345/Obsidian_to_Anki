---
summary: Start a procedure to initialize member variables directly using multiple parameters. This combines initialization and validation into a single step.
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
date created: Thursday, January 15th 2026, 11:52:07 am
date modified: Thursday, March 19th 2026, 8:41:53 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
prev:
  - "[[Cpp Class Parameterized Constructors]]"
item_of:
  - "[[Cpp Class Constructors]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Members are always initialized in the order they are declared within the class, not the order they appear in the initializer list.

## Usage
 `Rectangle(int w, int h) : width(w), height(h) {}` ;;; Constructor that initializes the `Rectangle` class using two ints `w, h`

## Syntax
```cpp
ClassName(type1 param1, type2 param2) : member1(param1), member2(param2) {
	// Constructor body
}
```
