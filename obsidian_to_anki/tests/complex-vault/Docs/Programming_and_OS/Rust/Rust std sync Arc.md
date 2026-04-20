---
summary: Atomically reference counted pointer. Useful for multithreaded environments to prolong lifetime of some data until all the threads have finished using it.<br><br>Provides shared ownership to value of type `T`, importantly allowing access to data regardless of the given lifetime until the final reference goes out of scope.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Usage]]"
type: note/class
similar:
  - "[[Rust Rc]]"
  - "[[Rust std sync LazyLoc]]"
  - "[[Rust std sync OnceLock]]"
aliases:
  - Rust Arc
associations:
  - "[[Rust str]]"
class_of:
  - "[[Rust std sync]]"
date created: Thursday, May 22nd 2025, 9:57:05 am
date modified: Thursday, October 2nd 2025, 12:49:23 pm
item_of:
  - "[[Rust std sync]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Arc and Mutex in Rust \| It's all about the bit](https://itsallaboutthebit.com/arc-mutex/)

## Concepts of Note
󰙎  Reference counted container ;;; A container which increments an integer based on the amount of times it has been referenced/cloned. It doesn't store where the references are, only that they have taken place = #lang/data/references/atomic #cs  
<!--ID: 1758253288467-->

## Usage

󰠗  In what situations would you choose Arc over Vec? ;; When you want long strict fields/arrays/collections of immutable data, especially things that use `.clone()`. = #lang/data/vector #lang/data/references/atomic  
<!--ID: 1758253288452-->

󰠗  Why is the Arc clone operation fast? What does it do differently than Vec? ;; It increments an integer, and copied the pointer to the arc rather than the data itself. Also has a smaller stack size than vector. Constant time operation O(1). = #lang/data/references/atomic  
<!--ID: 1758253288460-->

## Diagrams
![[Rust std sync Arc.png | 500]]
