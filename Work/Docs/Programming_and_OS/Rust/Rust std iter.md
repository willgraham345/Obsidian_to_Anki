---
summary: Composable external iteration. Typically used with a collection of elements you want to perform an operation on. Traits comprise the core portion, functions provide helpful ways to create basic iterators, and structs are the various methods on the module's traits.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Methods]]", "[[#Usage]]"]
type: 
classes: ["[[Rust Enumerate]]", "[[Rust Take]]"]
associations: ["[[Rust slice]]"]
class_of: ["[[Rust Enumerate]]"]
date created: Thursday, June 19th 2025, 10:46:50 am
date modified: Thursday, June 19th 2025, 11:49:06 am
interfaces: ["[[Rust std IntoIterator]]", "[[Rust std Iterator]]"]
library_used_in: ["[[Rust std]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] Adapters = Functions which take an [[Rust std Iterator|Iterator]] as an input, and return another [[Rust std Iterator|Iterator]]. Often called "iterator adapters", as they're a form of the [[DP Adapter]]. Common examples include `map`, `take` and `filter`
- With implementations for our own iterations, the only required method to `impl` is [[Rust std Iterator#^7c5fc7|next()]]

## Methods
### Iterator trait
See [[Rust std Iterator|Iterator]]

### Functions
- [p] `successors<T, F>(first: Option<T>, succ: F)-> Successors<T,F>` = Creates an iterator, starting from an initial item, computes each successive item from the preceding one. Returns a fused iterator. = #rust/data/iterations
<!--ID: 1751434090213-->


## Usage
Creating an iterator of your own involves two steps: creating a `struct` to hold the iterator's state, and then implementing the [[Rust std Iterator|Iterator]] for that struct. See [[#Count usize Iterator Implementation]]. Note: 

## Examples
### Count usize Iterator Implementation
```rust
struct Counter {
	count: usize,
}
impl Counter {
	fn new() -> Counter {
		Counter { count: 0}
	}
}
impl Iterator for Counter {
	type Item = usize; // We're counting with usize here
	fn next(&mut self) -> Option<Self::Item> {
		self.count += 1;
		if self.count<6 {
			Some(self.count)
		} else {
			None
		}
	}
}
```
