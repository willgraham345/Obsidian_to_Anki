---
summary:
type: note/concept
headings:
  - "[[#Concepts of Note]]"
concepts:
  - "[[CS Dynamic dispatch]]"
  - "[[CS Dynamic Polymorphism]]"
  - "[[PT Dynamic and Static Dispatch]]"
associations:
  - "[[Rust Generics]]"
concept_of:
  - "[[CS OOP]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, February 25th 2026, 6:01:35 pm
implementations:
  - "[[CS vtable|CS dispatch table]]"
  - "[[Python OOP Polymorphism]]"
tags: [cs/oop/, cs/oop/polymorphism, lang/oop, lang/oop/polymorphism]
template:
template-version:
---

# Summary
󰙎 Polymorphism ;;; Allows for creation of common methods and functions to be used for multiple types of objects.

# Additional Background
## Concepts of Note

󰙎  Type erasure ;;; Load-time process by which explicit type annotations are removed from a program before its executed at run-time. Ensures that run-time doesn't depend on type info. The opposite of this is type inference. In Go, this is an Interface. In Cpp it is a type erasure

[What is Type Erasure? – Arthur O'Dwyer – Stuff mostly about C++](https://quuxplusone.github.io/blog/2019/03/18/what-is-type-erasure/)

󰙎  Type inference ;;; The ability to automatically deduce (fully or partially) the type of an expression at compile time. If the type inference is strong enough, you can omit type annotations from a program completely if type inference system is robust enough.

󰙎  Monomophization ;;; Compile-time process where polymorphic functions are replaced by many monomorphic functions for each unique instantiation. 

- Allowing objects of different classes to perform actions with the same name using different code.

### Benefits
- Helps to create more flexible and modular programs
- Simplifies the development process and allows for creation of common methods and functions to be used for multiple types of objects
