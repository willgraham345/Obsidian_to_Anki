---
summary: Trait for dealing with iterators, the main iterator trait.
headings: ["[[#Concepts of Note]]", "[[#Methods]]"]
type: 
aliases: [Iterator]
date created: Wednesday, May 7th 2025, 4:52:30 pm
date modified: Thursday, June 19th 2025, 11:42:25 am
interface_of: ["[[Rust std iter]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- All [[Rust std Iterator|Iterator]]s implement the [[Rust std IntoIterator]] trait by just returning themselves. This means:
	1. Iterator's can be used within a `for` loop
	2. If you're creating a collection, implementing [[Rust std IntoIterator]] will allow your collection to be used with the `for` loop

## Methods

- [E] [[Rust std Iterator|Iterator]] = `next(&mut self) -> Option<Self::Item>` = Returns option if there is a next item. Implemented widely in the [[Rust std iter]] module. The only required method for a user-defined struct to `impl`. ^7c5fc7