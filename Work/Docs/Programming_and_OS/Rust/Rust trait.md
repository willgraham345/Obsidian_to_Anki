---
summary: A collection of method(s) that will be used by all different types. Does this by using an abstract interface with an implied virtual method table. The trait consists of associated items (functions, types, constants). Traits can be implemented for any data type.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/concept
concepts: ["[[Rust function traits and generics]]", "[[Rust struct traits and generics]]"]
components: ["[[Rust associated items]]"]
similar: ["[[Cpp.interface_aka_abstract_classes]]", "[[Rust Generics]]"]
prev: ["[[Rust bounds]]"]
associations: ["[[Rust impl]]"]
concept_of: ["[[Rust Items]]"]
date created: Friday, March 21st 2025, 10:32:20 am
date modified: Friday, June 27th 2025, 4:37:41 pm
tags: []
used_by: ["[[Rust Functions]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Traits - The Rust Reference](https://doc.rust-lang.org/reference/items/traits.html)

## Concepts of Note
- A trait *requires* that the types it is assigned to have a [[Rust impl]] statement or a [[Rust derive macros]] that satisfies the trait.
- Traits should be placed in the name of the module/block where they are located.
- Traits define an implicit type param `Self` that refers to the type that implements the interface.

### Terms
- [I] Traits = Give you a way to *describe* related types, which implement shared behavior among different `impl`s. Describes what related types *do* (by defining their methods and types they must define). = #term/rust 
![[Rust associated items#^9128e1]]
![[Rust bounds#^b9a4f8]]

### Trait bounds
- Even if a trait doesn't have any functionality (i.e. methods), you can use it as a bound. `Eq` and `Copy` are examples from the std library...

### Template Specialization
- C++ allows the user to customize the template code for a given set of template arguments, Rust does not allow this capability.

### Handling errors on traits which can't error
- use the [[Rust Infallible]] trait

## Usage
![[Rust bounds#^0e8e7f]]
![[Rust bounds#^b53a9b]]