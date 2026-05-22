---
summary: Defines behavior (methods for a struct, enum, or trait) of an already declared thing. Notably, an impl statement is required for all traits in a type.
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Usage]]"
type: note/function
concepts:
  - "[[Rust lifetime elision]]"
prev:
  - "[[Rust bounds]]"
  - "[[Rust Generics]]"
  - "[[Rust trait]]"
date created: Monday, March 31st 2025, 12:12:45 pm
date modified: Tuesday, July 22nd 2025, 1:27:49 pm
function_of:
  - "[[Rust Variables and Type System]]"
item_of:
  - "[[Rust Items]]"
tags:
  - lang/impl
used_by:
  - "[[Rust enum]]"
  - "[[Rust struct traits and generics]]"
  - "[[Rust Structs]]"
  - "[[Rust trait]]"
  - "[[Rust Tuples]]"
implements:
  - "[[CS Static Dispatch]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  Why would you use an `impl` statement? ;; To define new functions, new constants, or define a trait's scope within a certain class. Can also be done to generically (or inherently) define type functionality. = #lang/oop/interface_trait #lang/impl  
<!--ID: 1758253288679-->

󰠗  What are the two types of implementations? ;; Inherent implementation, and trait implementations. 
      Implementations can take generic parameters, but these are not necessarily their own type. Trait implementations are typically where we see generic implementations. = #lang/impl #lang/oop/interface_trait 
󰠗  When do generic parameters in an implementation (`impl`) constrain the implementation? ;; They always do this, as long as they appear in at least one of the following: implemented trait (if it has one), implementing type, as an associated type in the bounds of a type that contains another parameter that constrains the implementation = #lang/impl/generic #lang/oop/interface_trait/bounds  
<!--ID: 1758253288685-->

󰠗  What is the purpose of an `impl`? ;; To define new functions and/or consts for the types which they are associated. = #lang/impl  
<!--ID: 1758253288692-->

󰠗  What keyword marks the difference between an inherent implementation and a trait implementation ;; `for` = #lang/impl #lang/oop/interface_trait 
<!--ID: 1758253288698-->


󰙎  Inherent implementation ;;; Implement something for a specific type which is present in all places where the type is defined. Basically, "this functionality should always exist for this type". The `impl` contains associated functions (and methods) and associated constants. = #lang/impl/generic #lang/oop/generics/function  ^fa0a60 
󰙎  Generic implementation ;;; Implement something for a generic type (opposed to inherent param). This constrains the impementation if the parameter appears in the implementing type/trait/associated type in bounds of the current scope. = #lang/impl/generic #lang/oop/generics/function  
󰙎  Concrete implementation ;;; When the trait provides a default implementation for some or all of its methods. = #lang/impl/concrete 
<!--ID: 1758253288711-->

󰙎  Abstract implementation ;;; When a trait does *not* provide a default implementation for some or all of its methods. = #lang/impl/abstract #lang/oop/interface_trait  ^7fe2e8 
<!--ID: 1758253288717-->


### Trait implementations

#### Inherent implementations
- Will be present at all scopes
```rust
struct Example {
...
}
impl Example {
...
}
```

#### Trait implementations ^c2fd1a
- Defines an implementation that can be brought into scope by importing the trait it implements. Doesn't matter where this is defined

```rust
struct Example {}
trait Thingy{
	fn do_thingy(&self);
}
impl Thingy for Example {
	fn do_thingy(&self) {}
}
```
- Optional generic type declarations are followed by a trait. 

#### Generic parameters
- These implementations often **constrain** an application/struct. Occurs if the parameter appears in: the implemented trait, the implementing type, or as an associated type in the bounds of a type that contains another parameter that constrains the application. 
- See more [Implementations (Generic) - The Rust Reference](https://doc.rust-lang.org/reference/items/implementations.html#generic-implementations)

## Usage
  `impl <T> S<T> {}`= Generic implementation for a type `T` in a struct `S`. Does not contain any implements functions for any `T` in `S<T>` *generically* (T is a parameter)  ;;; #lang/impl/generic
- [p] `impl S<A> {`
      `fn function_def()`
      `}`= Implements function `function_def()`for type `A` in `S<T>` inherently (`A` is  specific type)  = #lang/impl/specific

󰠗  What is the difference between `impl <a> b<a>`, `impl<c> b<c> where c:a`, and `impl<a> for b<a>`? ;; `impl <a> b<a>` implements generic methods directly on the generic type `b<a>`.
      `impl<c> b<c> where c:a` defines a generic implementation for `b` but *only* for traits that satisfy `a` constraint.
      `impl<a> for b<a>` is not generic, and implements a trait for a generic type.

### Generic Implementation
These parameters *constrain* an implementation
Type and const parameters must always constrain the current implementation
[Generic Implementations - The Rust Reference](https://doc.rust-lang.org/reference/items/implementations.html#generic-implementations)

## Breadcrumbs
```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```
```breadcrumbs
type: mermaid
field-groups: [ups]
merge-fields: true
sort: field asc
depth: [0, 1]
show-attributes: [field]
```

