---
summary: Macro that prints to the console (`io::stdout`). No newline.
headings: ["[[#Usage]]"]
type: note/function
associations: ["[[Rust eprint]]", "[[Rust eprintln!]]", "[[Rust format]]", "[[Rust prinln]]"]
date created: Friday, March 21st 2025, 10:09:39 am
date modified: Thursday, July 3rd 2025, 2:19:21 pm
function_of: ["[[Rust macros]]", "[[Rust std fmt]]"]
tags: [code/rust/attributes/macros, code/rust/IO/stdout, code/rust/IO/stringOutput]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage
- [p] `println!("string you want {0}", variable)` = Prints to standard output with newline, used for primary output of the program. This is using a numbered way of printing variables. = #code/rust/IO/stringOutput #code/rust/attributes/macros 
<!--ID: 1751434382662-->

- [p] `println!("string you want {variable}")` = Prints to standard output with newline, used for primary output of the program. This is printing directly using the variable. = #code/rust/IO/stringOutput #code/rust/attributes/macros 

## Media
[println in std - Rust](https://doc.rust-lang.org/std/macro.println.html)