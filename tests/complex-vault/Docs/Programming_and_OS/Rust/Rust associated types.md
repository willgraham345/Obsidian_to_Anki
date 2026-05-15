---
summary: A type alias, most often used within a trait to signify that the implementor will require interaction with that type. Basically, a way to abstract out type information.
headings: ["[[#Concepts of Note]]"]
type: 
similar: ["[[Rust associated items]]"]
date created: Tuesday, July 22nd 2025, 1:54:13 pm
date modified: Sunday, July 27th 2025, 7:07:43 pm
used_by: ["[[Rust Items]]", "[[Rust trait]]"]
uses: ["[[Rust as]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  Can associated types be defined in an inherent implementation? ;; No, they also can't be given a default implementation in traits. = #lang/oop/interface_trait/items/associated-types 
<!--ID: 1758253289038-->

󰠗  Can associated types be given a default implementation within a trait? ;; No. = #lang/oop/interface_trait/items/associated-types #lang/oop/interface_trait/associated-types  
<!--ID: 1758253289045-->

󰠗  How do you specify an interface/trait which has a function that should return a specific type? I.e. `addi32() -> i32_unique_type` ;; Add an associated type into a trait, and have the function implement that trait. = #lang/oop/interface_trait/items/associated-types #lang/oop/interface_trait/types  
<!--ID: 1758253289052-->

󰠗  What is the associated bound on associated types? ;; `?Sized` = #lang/oop/interface_trait/items/associated-types #lang/oop/interface_trait/associated-types  
<!--ID: 1758253289059-->

- [p] `trait Container {`
      `type E;`
      `fn insert(&mut self, elem: Self::E);`
      `}` = Add an associated type `E` to trait `Container`. The trait also has a method `fun insert` which is a method, and takes type `E` as an input. = #lang/oop/interface_trait/associated-types #lang/oop/interface_trait/items/associated-types  
- [p] `impl<T> Container for Vec<T> {`
        `type E = T`
        `fn insert(&mut self, x: T) { self.push(x); }`
        `}` = Creates implementation of `Container` across `Vec<T>` (notice that `T` is generic). It also provides an implementation for the `insert` method, which takes `x: T` as an input. Its implementation calls `.push(x)` when `insert` is used = #lang/impl/generic/associated-types #lang/oop/interface_trait/items/associated-types #lang/oop/interface_trait/associated-types 
  `let other_struct ;;; <Struct as AssociatedType>::Assoc::new();` = Lets a struct `Struct` use an associated type  
<!--ID: 1758253289066-->

