---
summary: Defines behavior (methods for a struct, enum, or trait) of an already declared thing. Notably, an impl statement is required for all traits in a type.
headings: ["[[#Concepts of Note]]", "[[#Diagrams]]", "[[#Usage]]"]
type: note/function
workflows: ["[[Rust impl new]]"]
prev: ["[[Rust bounds]]", "[[Rust trait]]"]
date created: Monday, March 31st 2025, 12:12:45 pm
date modified: Friday, June 27th 2025, 2:44:01 pm
function_of: ["[[Rust Generics]]", "[[Rust Variables]]"]
tags: []
used_by: ["[[Rust enums]]", "[[Rust struct traits and generics]]", "[[Rust Structs]]", "[[Rust Tuples]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] Inherent implementation = Implement something for a specific type, defining functionality in all scopes wherever the type is defined. = #term/rust  ^fa0a60
- [I] Generic implementation = Implement something for a generic type (opposed to inherent param). This constrains the impementation if the parameter appears in the implementing type/trait/associated type in bounds of the current scope. = #term/rust 

### What is the purpose of `impl`?
- Define new functions
- Define consts

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

#### Generic Implementations
- These implementations often **constrain** an application/struct. Occurs if the parameter appears in: the implemented trait, the implementing type, or as an associated type in the bounds of a type that contains another parameter that constrains the application. 
- See more [Implementations (Generic) - The Rust Reference](https://doc.rust-lang.org/reference/items/implementations.html#generic-implementations)

## Usage
- [p] `impl <T> S<T> {}`= Implements functions for any `T` in `S<T>` *generically* (T is a parameter)  = #code/rust/impl/generic
- [p] `impl S<T> {}`= Implements functions for any `T` in `S<T>` inherently (T is  specific type)  = #code/rust/impl/specific

### Generic Implementation
These parameters *constrain* an implementation
Type and const parameters must always constrain the current implementation
[Generic Implementations - The Rust Reference](https://doc.rust-lang.org/reference/items/implementations.html#generic-implementations)

## Diagrams
```mermaid
graph LR
	subgraph mod1
		cfStruct["Config"]
	end
	subgraph mod2
	appStruct["AppStruct"]
	impl["impl mod1::Config for App ]
```