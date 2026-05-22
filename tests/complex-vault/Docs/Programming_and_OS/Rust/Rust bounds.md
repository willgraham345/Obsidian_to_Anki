---
summary: Bounds are how we describe what functionality generics must implement. This is often expressed through the use of a [[Rust trait]].
headings: ["[[#Breadcrumbs]]", "[[#Concepts of Note]]", "[[#Usage]]"]
type: note/concept
same: ["[[Rust where]]"]
next: ["[[Rust impl]]", "[[Rust trait]]"]
prev: ["[[Rust Generics]]"]
associations: ["[[Rust Generics]]"]
concept_of: ["[[Rust Generics]]", "[[Rust trait]]"]
date created: Friday, May 2nd 2025, 2:35:13 pm
date modified: Monday, September 29th 2025, 12:31:08 pm
used_by: ["[[Rust Functions]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰙎  Trait bound ;;; Stipulation a trait has on what functionality a type implements. #lang ^b9a4f8
- Even if a trait doesn't have any functionality (i.e. methods), you can use it as a bound. `Eq` and `Copy` are examples from the std library.

## Usage
  `fn f<T: Display>(t: T) ...` ;;; A trait bound on a function, which stipulates that the function parameter `t` must implement the `Display` trait. Hint, the generic is `T`. Note that the [[Rust where]] is an alternative method of performing this action. = #lang/oop/interface_trait/bounds  
ID: 1751997628548
 ^f741de


  `fn f<T: Debug+Display>(t: T) ...` ;;; A compound trait bound on a function, which stipulates that the function parameter `t` must implement the `Display` trait. Hint, the generic is `T`. Note that the [[Rust where]] is an alternative method of performing this action. = #lang/oop/interface_trait/bounds  
ID: 1751997628553 ^352403

## Breadcrumbs

```breadcrumbs
type: mermaid
field-groups: [ups]
merge-fields: true
sort: field asc
show-attributes: [field]
```

