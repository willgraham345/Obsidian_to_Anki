---
summary: A trait passed into a function. Essentially, the argument(s) must implement the trait to compile correctly.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/concept
similar: ["[[Rust struct traits and generics]]"]
concept_of: ["[[Rust Generics]]", "[[Rust trait]]"]
date created: Friday, April 4th 2025, 3:32:01 pm
date modified: Wednesday, April 30th 2025, 12:11:40 pm
tags: [code/rust/data/struct/method, code/rust/functions/self, code/rust/traits/function]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Why we use these
```rust
fn largest_i32(list: &[i32]) -> &i32
fn largest_char(list: &[char]) -> &char
```
:BoBxsDownvote: Simplifies towards...
```rust
//Simplified
fn largest<T>(list: &[T]) -> &T //generic
```
- Function `largest` now works with **generic types** of inputs

### Shorthand
```rust
pub fn notify(item: &impl Summary) { //Says item must be able to implement/handle Summary trait
    println!("Breaking news! {}", item.summarize());
}

// OR
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```
Says that the `item` param must be able to implement/handle the `Summary` trait.
- [p] `fn fnName(&self)` = Method takes immutable reference to current instance (doesn't have ownership) = #code/rust/functions/self #code/rust/data/struct/method 
<!--ID: 1751434090547-->


## Usage

- [p] `impl <A: aPart + ?Sized> App<A> {` = says that App may or may not be sized = #code/rust/traits/function
<!--ID: 1751434090550-->

- [p] `pub fn notify<T: Summary + Display>(item: &T) {` = `T` must implement `Summary` and `Display` = #code/rust/traits/function = Multiple multi-type traits [[#Specify Multiple Multitype Traits with `+`]]
<!--ID: 1751434090554-->


## Examples
### Specify multiple traits
```rust
pub fn notify<T: Summary + Display>(item: &T) {
```
- `T` must implement both `Summary` and `Display`

#### Specify Multiple Multitype Traits with `+`
```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
```

### Return types that implement traits
```rust
fn returns_summarizable() -> impl Summary
```

