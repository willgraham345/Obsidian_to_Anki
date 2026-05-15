---
summary: Trait for dealing with iterators, the main iterator trait.
headings: ["[[#Concepts of Note]]", "[[#Properties]]", "[[#Usage]]"]
type: note/interface
members: ["[[Rust std Iterator#.into_iter()]]"]
methods: ["[[Rust std Iterator#.iter_mut()]]", "[[Rust std Iterator#.iter()]]", "[[Rust std Iterator#.next()]]"]
aliases: [Iterator]
date created: Wednesday, May 7th 2025, 4:52:30 pm
date modified: Thursday, November 20th 2025, 11:20:18 am
interface_of: ["[[Rust std iter]]"]
template:
template-version:
used_by: ["[[Rust std collections]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- All [[Rust std Iterator|Iterator]]s implement the [[Rust std IntoIterator]] trait by just returning themselves. This means:
	1. Iterator's can be used within a `for` loop
	2. If you're creating a collection, implementing [[Rust std IntoIterator]] will allow your collection to be used with the `for` loop

`for i in chars` is the same as `for i in chars.into_iter()`

## Usage
  `iter.next()` ;;; Advances an iterator `iter` and returns the next value = #lang/data/iterations 
<!--ID: 1758253288530-->

  `iter.nth(n: usize)` ;;; Returns the `n`th element in a iterator `iter` = #lang/data/iterations 
<!--ID: 1758253288537-->

  `iter1.zip(iter2)` ;;; Creates one iterator of pairs from two iterators, `iter1` and `iter2`. = #lang/data/iterations 
<!--ID: 1758253288544-->

  `iter.map(closure)` ;;; Takes a closure and creates an iterator which calls that closure on each element. Notably, this transforms the iterator into different iterator (i.e. type A -> type B). = #lang/data/iterations 
<!--ID: 1758253288551-->

  `iter.filter(closure)` ;;; Takes a closure and creates an iterator which calls that closure on each element. = #lang/data/iterations 
<!--ID: 1758253288557-->

  `iter.collect()` ;;; Transform an iterator into a collection. = #lang/data/iterations #lang/data/collections ^c78910 
<!--ID: 1758253288564-->

## Properties
#### .next()
Returns option on if there is a next item. Takes in a mutable reference to itself.
- [E] [[Rust std Iterator|Iterator]] = `next(&mut self) -> Option<Self::Item>` = Returns option if there is a next item. Implemented widely in the [[Rust std iter]] module. The only required method for a user-defined struct to `impl`. ^7c5fc7

#### .iter()
- Creates an iterable over a referenced version of the values (basically just a for loop in a more succinct way)
- Iterates over `&T`.

#### .iter_mut()
- Creates a mutable iterator from a collection.
- Iterates over the `&mut T`.

#### .into_iter()
- Creates an interable that consumes the values. 
- Iterates over `T`
- Think of this as the ownership version of [[#.iter()]]
