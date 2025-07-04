---
summary: Defines new inputs for the `derive` attribute. These macros can generate new items given the token stream of a struct, enum, or union. They can also derive macro helper attributes.<br><br>Defined by a public function `proc_macro_derive` and a signature of `(TokenStream) -> TokenStream`.
headings: ["[[#Concepts of Note]]", "[[#Media]]", "[[#Syntax]]"]
type: note/concept
concepts: ["[[Rust derive attribute macros]]"]
concept_of: ["[[Rust procedural macros]]"]
date created: Friday, April 18th 2025, 11:48:25 am
date modified: Tuesday, April 29th 2025, 3:37:20 pm
tags: [term/rust]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] Derive macros = Used to automatically implement traits for structs/enums, can only add new items. Often `#[derive(Foo)]` is expected to implement `Foo` trait = #term/rust 
- [I] Attribute macros = Used for adding/modifying existing items with attributes, takes in two `TokenStream`s and returns a new `TokenStream` = #term/rust 

## Syntax
Definition:
```rust
#![crate_type = "proc-macro"]
extern crate proc_macro;
use proc_macro::TokenStream;

#[proc_macro_derive(AnswerFn)]
pub fn derive_answer_fn(_item: TokenStream) -> TokenStream {
    "fn answer() -> u32 { 42 }".parse().unwrap()
}
```
- `TokenStream` input is token stream of the item that has the `derive` attribute on it. The output `TokenStream` must be a set of items that are then appended to the module or lock that the item from the input `TokenStream` is in.
Using
```rust
extern crate proc_macro_examples;
use proc_macro_examples::AnswerFn;

#[derive(AnswerFn)]
struct Struct;

fn main() {
    assert_eq!(42, answer());
}
```

## Media
[Derive Macro helper attributes](https://doc.rust-lang.org/reference/procedural-macros.html#derive-macro-helper-attributes)