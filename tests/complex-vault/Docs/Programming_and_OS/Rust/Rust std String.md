---
summary: "- String type in rust, typically used when you need a string that will change and adapt. This type of string is a heap-stored container for the `str` type. <br>- Other types of strings (string literals) are immutable, hardcoded, and saved to the stack/executable. This string type is mutable, and less efficient when compared with other string types."
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/class
functions: ["[[Rust String Methods]]", "[[Rust String Move]]"]
aliases: [Rust String]
associations: ["[[Rust serde]]", "[[Rust str]]"]
class_of: ["[[Rust DataTypes]]", "[[Rust std]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, November 20th 2025, 12:38:07 pm
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

- String data is stored on the heap. Rust knows how to clean up that data.
	- Some strings can be hardcoded and saved on the stack, but other strings are dynamic and mutable. 

### Parts of a string
1. Stack
	1. Pointer to the memory that holds the contents of a string
	2. A length
	3. A capacity
2. Heap
	- Contents
	- ![[trpl04-01.svg | 300]]
- The left is stored on the stack, the right is stored on the heap

## Usage
  `let mut s ``=``String::from("String made")` ;;; Create mutable string using `String` library = #lang/IO/stringOutput  


  `s.push_str("literal pushed")` ;;; Append a literal to a string = #lang/IO/stringOutput  


  `s1.clone()` ;;; How to copy a `String` string = #lang/IO/stringOutput  
󰠗  Which type of string should you use when you want something that is small and efficient? ;; Use `str` rather than `std::String`. String literals are lighter, smaller, and do not have a capacity field. Operations on this smaller data field are typically faster and more efficient. = #lang/data/string 
<!--ID: 1758253288475-->

󰠗  What is the heap-stored container for `str`? ;; `std::String` = #lang/data/string  
<!--ID: 1758253288481-->

󰠗  Where is `String` data stored? ;; The heap = #lang/data/string  
<!--ID: 1758253288488-->

### Copy Stack Data
```rust
let x = 5;
let y = x;
```
