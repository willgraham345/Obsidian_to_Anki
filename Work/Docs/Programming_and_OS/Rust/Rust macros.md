---
summary: Can be either a declarative macro (with an `!` at the end), or one of three types of procedural macros. A "macro" is something that expands into more code.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/concept
concepts:
  - "[[Rust declarative macros]]"
  - "[[Rust procedural macros]]"
functions:
  - "[[Rust assert]]"
  - "[[Rust cfg]]"
  - "[[Rust eprint]]"
  - "[[Rust eprintln!]]"
  - "[[Rust format_args]]"
  - "[[Rust format!]]"
  - "[[Rust panic]]"
  - "[[Rust print!]]"
  - "[[Rust todo]]"
  - "[[Rust vector]]"
workflows:
  - "[[Rust writing a macro]]"
associations:
  - "[[Rust match]]"
concept_of:
  - "[[Rust Generics]]"
date created: Friday, March 21st 2025, 10:07:53 am
date modified: Thursday, May 8th 2025, 9:49:57 am
libraries:
  - "[[Rust getset]]"
tags:
  - code/rust/attributes/macros
  - code/rust/attributes/macros/toolingDirectives
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- [I] Macro = An expandable section of code, which can take variable number of parameters.

## Concepts of Note
- Also see [[Rust procedural macros#Function-like macros]]

### Macros vs Functions
- Macros are a way of writing code that writes other code (metaprogramming)
- Macros can take a variable number of parameters (functions can't do that, they are called at runtime with a trait implemented at compile time)
- Macros are more complex than functions to define
- You must define macros or bring them into scope before you call them in a file. Functions can be defined anywhere and call anywhere.

