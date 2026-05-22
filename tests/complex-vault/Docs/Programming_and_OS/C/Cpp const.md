---
summary:
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Flashcards]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
implements:
  - "[[Cpp pointers]]"
concepts:
  - "[[Cpp const member functions]]"
similar:
  - "[[Cpp constexpr]]"
associations:
  - "[[Cpp mutable]]"
concept_of:
date created: Monday, October 7th 2024, 12:37:41 pm
date modified: Wednesday, April 15th 2026, 3:53:06 pm
keyword_of:
  - "[[Cpp Storage Classes and Keywords]]"
tags: [lang/data/const, lang/data/const/pointers, lang/memory/pointers, todo/refactor]
template:
template-version:
used_by:
  - "[[Cpp Variables and Containers]]"
---

# Summary
󰙎 const ;;; Keyword in Cpp that declares variables that will never change their value throughout their lifetime and should be stored in read-only memory.

# Additional Background

## Usage
  `const T* ptr` ;;; Creates a pointer to a constant type, meaning the const applies tot he data being pointed to. The value at the memory location pointed to by the pointer cannot be modified through this pointer. 


  `T* const ptr` ;;; Creates a constant pointer to a mutable type. The constant applies to the pointer itself, meaning the pointer cannot be reassigned to a different point. = 


  `const T* const ptr` ;;; Creates a constant pointer to a constant type. The pointer cannot be changed, and the underlying data also cannot be changed.  = 

### Use cases
1. Return from function  
	1. `const int function();` :CoArrowRightLG: Return value cannot be modified
2. Parameters in a function
	1. `void function(const int val1);` :CoArrowRightLG: Indicates the function will not modify the passed argument
3. Member function [[Cpp const member functions]]
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
8. `const` member functions
	1. Guarantees the function will not change the state of `this` when it is called. 
[The many uses of const in C++ | Codementor](https://www.codementor.io/@sandesh87/the-many-uses-of-const-in-c-1pnuap4kcy)

## Syntax
```cpp
type const name = value;
```

## Media
[The many uses of const in C++ \| Codementor](https://www.codementor.io/@sandesh87/the-many-uses-of-const-in-c-1pnuap4kcy)

## Flashcards
󰠗  Where are const variables stored in a cpp program? ;; In a `.rodata` segment.

󰠗  How can you change the value of a const variable? ;; By addressing the `const` variable to a non-constant pointer, you can effectively modify the const value. Modern C++ compilers enforce stricter type checking, typically resulting in a compilation error. = 
