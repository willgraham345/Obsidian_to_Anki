---
summary: Most types have a fixed size known at compile time and implement `Sized` trait. A type that is only known at runtime is dynamically sized.
headings: ["[[#Usage]]"]
type: note/concept
concept_of: ["[[Rust Variables and Type System]]"]
date created: Wednesday, July 16th 2025, 12:07:22 pm
date modified: Wednesday, July 16th 2025, 12:13:03 pm
interfaces: ["[[Sized]]"]
items: ["[[Rust pointers"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Rust Dynamic Dispatching deep-dive \| by Marco Amann \| Digital Frontiers — Das Blog \| Medium](https://medium.com/digitalfrontiers/rust-dynamic-dispatching-deep-dive-236a5896e49b)

## Usage
󰠗  What things in rust must implement the `Sized` trait? ;; Variables, function parameters, const items, and static items. = #lang/data/dyn  
<!--ID: 1758253288818-->

