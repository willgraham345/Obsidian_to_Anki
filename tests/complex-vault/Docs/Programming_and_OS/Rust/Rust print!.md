---
summary: Macro that prints to the console (`io::stdout`). No newline.
headings: ["[[#Usage]]"]
type: note/function
associations: ["[[Rust eprint]]", "[[Rust eprintln!]]", "[[Rust format]]", "[[Rust prinln]]"]
date created: Friday, March 21st 2025, 10:09:39 am
date modified: Thursday, July 3rd 2025, 2:19:21 pm
function_of: ["[[Rust macros]]", "[[Rust std fmt]]"]
tags: [lang/meta/attributes/macros, lang/IO/stdout, lang/IO/stringOutput]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage
  `println!("string you want {0}", variable)` ;;; Prints to standard output with newline, used for primary output of the program. This is using a numbered way of printing variables. = #lang/IO/stringOutput #lang/meta/attributes/macros  
ID: 1751997628375



  `println!("string you want {variable}")` ;;; Prints to standard output with newline, used for primary output of the program. This is printing directly using the variable. = #lang/IO/stringOutput #lang/meta/attributes/macros  



## Media
[println in std - Rust](https://doc.rust-lang.org/std/macro.println.html)
