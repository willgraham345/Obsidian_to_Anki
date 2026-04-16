---
summary: Dyn is a prefix of a trait object's type. Used to highlight that calls to methods on associated `Trait` are dynamically dispatched. To use the trait this way, it must be dyn compatible. A `dyn` trait contains two pointers (one for data/instance of struct, one for the virtual method table)
type: note/keyword
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
implements:
  - "[[CS Dynamic dispatch]]"
associations:
date created: Tuesday, September 9th 2025, 11:52:03 am
date modified: Tuesday, March 3rd 2026, 11:55:41 am
tags: []
template:
template-version:
used_by:
  - "[[Rust trait]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
![[Rust trait#^36ef0c]]
Different from generic parameters, in that the compiler doesn't know the concrete type that is being passed. 

## Usage
Can be used to return a trait. 