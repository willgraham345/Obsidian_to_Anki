---
summary: A trait passed into a function. Essentially, the argument(s) must implement the trait to compile correctly.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/concept
similar: ["[[Rust struct traits and generics]]"]
concept_of: ["[[Rust Generics]]", "[[Rust trait]]"]
date created: Friday, April 4th 2025, 3:32:01 pm
date modified: Tuesday, July 15th 2025, 9:54:09 am
tags: [lang/oop/class/methods, lang/functions/self, lang/oop/interface_trait/function_method]
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
  `fn fnName(&self)` ;;; Method takes immutable reference to current instance (doesn't have ownership) = #lang/functions/self #lang/oop/class/methods  
ID: 1751997628469

## Usage

  `impl <A: aPart + ?Sized> App<A> {` ;;; Writes an `impl` statement for `App` that says it will implement the `aPart` trait, while it may or may not implement the `Sized?` trait. = #lang/oop/interface_trait/bounds  



  `pub fn notify<T: Summary + Display>(item: &T) {` ;;; `T` must implement `Summary` and `Display` = #lang/oop/interface_trait/function_method #lang/oop/interface_trait/bounds = Multiple multi-type traits [[#Specify Multiple Multitype Traits with `+`]] 
ID: 1751997628477

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

