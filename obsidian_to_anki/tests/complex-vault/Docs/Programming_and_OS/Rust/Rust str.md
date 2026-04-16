---
summary: "- Rust's string literal, which is stored in the read-only data segment of the generated executable. This is determined at compile time.<br><br>- Notably, a string slice `&str` is not a string literal, but a pointer to a non-owned string. `&str` is a reference to a sequence of elements in a collection rather than the whole collection."
headings: ["[[#Concepts of Note]]"]
type: note/item
associations: ["[[Rust slice]]", "[[Rust std String]]", "[[Rust std sync Arc|Rust Arc]]"]
date created: Monday, April 28th 2025, 3:17:17 pm
date modified: Monday, July 14th 2025, 12:53:33 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- str is a `const char[]`, and represents the text itself. You only see this used when as a `&str`
- References can be converted to an owned string value `String`
- Generally used in function arguments and returns when it is possible to be used. Any function that creates a string that didn't previously exist must return `String` rather than `&str`.
󰙎  String literal ;;; Sequence of characters that represent a fixed value within a program. These are determined at compile time, not at runtime = #lang/data/string #cs  
<!--ID: 1758253288365-->

󰠗  Where is the "data" in a `&str` located? What is this type of data? ;; It is housed in the read-only data section of the executable. This is a non-owned reference slice type. = #lang/data/string  
<!--ID: 1758253288352-->

󰠗  What datatype is `s` in `let s``=``"Hello, world!";`? ;; `s` is a `&str`, a slice pointing to a specific place within the binary. = #lang/data/string  
<!--ID: 1758253288359-->


## Media
[Understanding when to use String vs str - help - The Rust Programming Language Forum](https://users.rust-lang.org/t/understanding-when-to-use-string-vs-str/103746/2)
