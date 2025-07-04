---
summary: "- String type in rust, typically used when you need a string that will change and adapt. This type of string is a heap-stored container for the `str` type. <br>- Other types of strings (string literals) are immutable, hardcoded, and saved to the stack/executable. This string type is mutable, and less efficient when compared with other string types."
headings: ["[[#Usage]]"]
type: note/class
functions: ["[[Rust String Methods]]", "[[Rust String Move]]"]
associations: ["[[Rust str]]"]
class_of: ["[[Rust DataTypes]]", "[[Rust std]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, May 7th 2025, 4:23:34 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

# Background
- String data is stored on the heap. Rust knows how to clean up that data.
	- Some strings can be hardcoded and saved on the stack, but other strings are dynamic and mutable. 
Parts of a string
1. Stack
	1. Pointer to the memory that holds the contents of a string
	2. A length
	3. A capacity
2. Heap
	- Contents
	- ![[trpl04-01.svg | 300]]
- The left is stored on the stack, the right is stored on the heap

## Usage


### Create a mutable `String` from a string literal using the `from` function
```rust
let mut s = String::from("Hello");
s.push_str(", world!"); //appends a literal to a string

```
- `::from()` is a namespaced function from `String` library

### Copy the Heap Data to Another Location
```rust
let s1 = String::from("hello");
let s2 = s1.clone();
```

### Copy Stack Data
```rust
let x = 5;
let y = x;
```