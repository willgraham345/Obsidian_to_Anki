---
summary: Defines new inputs for the `derive` attribute. These macros can generate new items given the token stream of a struct, enum, or union. They can also derive macro helper attributes.<br><br>Defined by a public function `proc_macro_derive` and a signature of `(TokenStream) -> TokenStream`.
headings: ["[[#Concepts of Note]]", "[[#Media]]", "[[#Syntax]]", "[[#Usage]]"]
type: note/concept
concepts: ["[[Rust derive attribute macros]]"]
concept_of: ["[[Rust procedural macros]]"]
date created: Friday, April 18th 2025, 11:48:25 am
date modified: Saturday, December 6th 2025, 4:21:53 pm
tags: [lang, lang/macros, lang/macros/procedural, lang/meta/attributes/derive, lang/meta/attributes/macros]
template:
template-version:
uses: ["[[Rust derive_getters]]", "[[Rust getset]]", "[[Rust Metavariables]]", "[[Rust syn DeriveInput]]", "[[Rust syn]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  When matching, can the compiler look ahead when using macro invocations? ;; No, it parses tokens one at a time. = 
<!--ID: 1758253288829-->

 Derive macros ;; Used to automatically implement traits for structs/enums, can only add new items. Often `#[derive(Foo)]` is expected to implement `Foo` trait 
 Attribute macros ;; Used for adding/modifying existing items with attributes, takes in two `TokenStream`s and returns a new `TokenStream`
󰠗  What is the input and output for all procedural derive macros? ;; A `TokenStream` object =
<!--ID: 1758253288837-->

󰠗  What crate do you use when writing procedural macros? ;; The `syn` crate = 
<!--ID: 1758253288844-->

### Macro parts
󰠗  What is the part of a procedural macro which determines which expressions are matched? ;; The matcher =
<!--ID: 1758253288851-->

󰠗  What is the part of a procedural macro which describes the syntax that will replace a successfully matched invocation? ;; The transcriber = 
<!--ID: 1758253288858-->

󰠗  When writing a procedural macro, what token is used to invoke special behavior from the macro engine? What behavior would it be invoking? ;; `$`, it would invoke Metavariable and Repetition behavior. = 
<!--ID: 1758253288866-->

## Usage


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
