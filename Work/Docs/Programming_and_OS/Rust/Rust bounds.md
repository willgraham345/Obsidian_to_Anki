---
summary: Bounds are how we describe what functionality generics must implement. This is often expressed through the use of a [[Rust trait]].
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/concept
date created: Friday, May 2nd 2025, 2:35:13 pm
date modified: Friday, May 2nd 2025, 2:37:16 pm
next:
  - "[[Rust trait]]"
  - "[[Rust impl]]"
same:
  - "[[Rust where]]"
prev:
  - "[[Rust Generics]]"
used_by:
  - "[[Rust Functions]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] Trait bound = Stipulation a trait has on what functionality a type implements. #term/rust  ^b9a4f8
## Usage
- [p] `fn f<T: Display>(t: T) ...` = Trait bound, saying that type `T` *must* have an *impl* for *Display*. Note that the [[Rust where]] is an alternative method of performing this action. = #code/rust/trait/bounds ^0e8e7f
<!--ID: 1751434090614-->

- [p] `fn f<T: Debug+Display>(t: T) ...` = Compound trait bound, saying that type `T` *must* have an *impl* for *Display* as well as *Debug*. Note that the [[Rust where]] is an alternative method of performing this action. = #code/rust/trait/bounds ^b53a9b
<!--ID: 1751434090618-->
