---
summary: Keyword in Cpp that declares variables that will never change their value throughout their lifetime.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/concept
classes: ["[[Cpp Storage Classes and Keywords]]"]
concepts: ["[[Cpp const Member Functions]]"]
associations: ["[[Cpp mutable]]"]
class_of: ["[[Cpp Storage Classes and Keywords]]"]
concept_of: ["[[Cpp Memory]]", "[[Cpp Variables and Containers]]"]
date created: Monday, October 7th 2024, 12:37:41 pm
date modified: Thursday, June 19th 2025, 11:13:13 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
1. Return from function  
	1. `const int function();` :CoArrowRightLG: Value cannot be modified
2. Parameters in a function
	1. `void function(const int val1);` :CoArrowRightLG: Indicates the function will not modify the passed argument
3. Member function [[Cpp const Member Functions]]
	1. `int function() const;` :CoArrowRightLG: Indicates that the function doesn't modify the object's state. Really helpful for data integrity, compiler optimizations.
4. Pointers
	2. `int* const ptr1;` :CoArrowRightLG: Constant pointer to a mutable integer
	3. `const int* ptr2` :CoArrowRightLG: Mutable pointer to a constant integer
	4. `const int* const ptr3;` :CoArrowRightLG: Constant pointer to a constant integer
5. `const` variables
6. `const` pointers 
	1. Constant pointer
	2. Pointer to a constant
7. `const` function parameters
	1. Parameters may be constant.
. `const` member functions
	2. Guarantees the function will not change the state of `this` when it is called. 

## Usage
- [p] `const T* ptr` = Creates a pointer to a constant type, meaning the const applies tot he data being pointed to. The value at the memory location pointed to by the pointer cannot be modified through this pointer. = #code/cpp/memory/pointers #code/cpp/variables/const/pointers
<!--ID: 1751434091711-->

- [p] `T* const ptr` = Creates a constant pointer to a mutable type. The constant applies to the pointer itself, meaning the pointer cannot be reassigned to a different point. = #code/cpp/memory/pointers #code/cpp/variables/const/pointers
<!--ID: 1751434091715-->

- [p] `const T* const ptr` = Creates a constant pointer to a constant type. The pointer cannot be changed, and the underlying data also cannot be changed.  = #code/cpp/memory/pointers #code/cpp/variables/const/pointers
<!--ID: 1751434091719-->

```cpp
type const name = value;
```
[The many uses of const in C++ | Codementor](https://www.codementor.io/@sandesh87/the-many-uses-of-const-in-c-1pnuap4kcy)

## Media
[The many uses of const in C++ \| Codementor](https://www.codementor.io/@sandesh87/the-many-uses-of-const-in-c-1pnuap4kcy)