---
summary: "How do we obtain `B` from `A`, i.e. `fn f(x: A) -> B`."
headings:
  - "[[#Concepts of Note]]"
type: note/workflow
concepts:
  - "[[Rust From]]"
  - "[[Rust slice]]"
  - "[[Rust TryFrom]]"
  - "[[Rust TryInto]]"
date created: Wednesday, April 30th 2025, 11:34:12 am
date modified: Thursday, June 19th 2025, 5:26:33 pm
keywords:
  - "[[Rust as]]"
tags:
  - term/rust
workflow_of:
  - "[[Rust]]"
workflows:
  - "[[Rust slice conversions]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
[Rust Language Cheat Sheet](https://cheats.rs/#type-conversions)
- [I] Computation conversion = Creating and manipulating instance of `B` by writing code to transform data. Typical use case, using [[Rust trait]]s and [[Rust impl]]. = #term/rust 
- [I] Cast conversion = On-demand conversion conversion between types where caution is advised. Uses the [[Rust as]] keyword. = #term/rust 
- [I] Coercions conversions = *Automatic* conversion within weaking ruleset = #term/rust 
- [I] Subtyping conversions = *Automatic* conversion within same layout different lifetimes ruleset = #term/rust 
- [p] `T as U` = A cast between types, or renaming an import
![[Rust TryFrom#^7272f1]]

