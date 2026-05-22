---
summary: "How do we obtain `B` from `A`, i.e. `fn f(x: A) -> B`. Rust doesn't do implicit type conversion (coercion) between primitive types."
headings:
  - "[[#Concepts of Note]]"
type: note/process
concepts:
  - "[[Rust From]]"
  - "[[Rust Into]]"
  - "[[Rust slice]]"
  - "[[Rust TryFrom]]"
  - "[[Rust TryInto]]"
processes:
  - "[[Rust slice conversions]]"
date created: Wednesday, April 30th 2025, 11:34:12 am
date modified: Thursday, November 6th 2025, 11:36:30 am
keywords:
  - "[[Rust as]]"
tags:
template:
template-version:
process_of:
  - "[[Rust slice]]"
  - "[[Rust]]"
  - "[[Rust Variables and Type System]]"
aliases:
  - Rust casting
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
[Rust Language Cheat Sheet](https://cheats.rs/#type-conversions)
󰙎  Computation conversion ;;; Creating and manipulating instance of `B` by writing code to transform data. Typical use case, using [[Rust trait]]s and [[Rust impl]]. = #lang  


󰙎  Cast conversion ;;; On-demand conversion conversion between types where caution is advised. Uses the [[Rust as]] keyword. = #lang  


󰙎  Coercive conversions (sub typing conversions) ;;; *Automatic* conversion within weaking ruleset. Typically between types where one type is a subtype of another. Often related through lifetimes and variances in generic casts. Handled with [[Rust From]] and [[Rust Into]] and [[Rust as]] keywords. = #lang  
<!--ID: 1758253288210-->





  `T as U` ;;; A cast between types, or renaming an import
![[Rust TryFrom#^7272f1]]

  `<variable> as <datatype>` ;;; Converts variable to datatype.  = #lang/data/casting 
ID: 1751997628042

