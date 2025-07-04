---
summary: Memory is managed through a system of ownership with a set of rules that the compiler checks. If any of the rules are violated, the program will not compile. <br><br>Each value has an owner, you can only have one owner at a time. When the owner goes out of scope, the value will be dropped. <br><br>Data that is fixed should be allocated to the stack, and must be known at compile time. Data that can change in size or whose value is unknown at runtime is allocated on the heap.
headings: 
type: note/concept
concepts: ["[[PT Stack vs Heap]]", "[[Rust lifetimes]]", "[[Rust Ownership Functions]]", "[[Rust Variable Scope]]"]
functions: ["[[Rust drop]]"]
concept_of: ["[[Rust Scoping Rules]]", "[[Rust]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, April 29th 2025, 4:44:22 pm
tags: [term/rust]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
- [I] Ownership = Resources can only have one owner, after movement, the previous owner can no longer be used = #term/rust 
[[Rust Variable Scope]], says that variables are only valid within the scope it was declared (typically within the `{ }`)
[[Rust String Move]] says that strings shouldn't be used after they are moved

### Memory and Allocation
- For a string literal, we know the contents at compile, so the text will be hardcoded directly into the final executable. 
	- String literals are fast, but that comes from the string literal's immutability
- `String` is stored on the heap. We need to allocate an amount of memory on the heap, which is unknown at compile time to hold contents
	- The memory must be requested from the memory allocator a runtime
	- We need a way of returning this memory to the allocator when we're done with our `String`
Example
```rust
let mut s = String::from("hello");
s.push_str(", world!"); // push_str() appends a literal to a String
println!("{}", s); // This will print `hello, world!`
```
- The first part `String::from` requests the memory
	- A garbage collector will keep track of and clean up memory that isn't being used anymore in most languages. 
	- If we forget about the variables, we waste memory. Instead, rust automatically returns the memory once the variable that owns it goes out of scope
```rust
{
	let s = String::from("hello"); // s is valid from this point forward
	// do stuff with s
}                                  // this scope is now over, and s is no
								   // longer valid
```

When a variable goes out of scope, Rust calls a special function for us. This function is called `drop`, and it's where the author of `String` can put the code to return the memory. Rust automatically calls `drop` at the closing curly bracket.

