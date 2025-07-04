---
summary: A variable's scope has 1. When it comes into scope, and 2. When it goes out of scope and becomes invalid.
type: note/concept
concept_of:
  - "[[Rust Ownership]]"
  - "[[Rust Variables]]"
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Wednesday, January 8th 2025, 4:36:03 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

# Background
### Variable Scope
- A scope is in the range within a program for which an item is valid.
```rust
{ // s is not valid here, it's not yet declared
	let s = "hello"; //s is valid from this point forward
	// do stuff with s
} // the scope is now over, s is no longer valid
```

- Two important points in time
	- When `s` comes *into* scope, it is valid
	- It remains valid until it goes *out of* scope