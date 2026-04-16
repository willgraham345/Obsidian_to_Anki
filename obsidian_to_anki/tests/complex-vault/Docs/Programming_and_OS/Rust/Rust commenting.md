---
summary: How to comment and document Rust code.
headings: ["[[#Concepts of Note]]"]
type: note/process
date created: Monday, August 4th 2025, 12:38:09 pm
date modified: Monday, December 1st 2025, 3:53:28 pm
template:
template-version:
used_by: ["[[Rust mdbook]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

### Common sections
  `/// # Examples` ;;; Document an example (for a class/function) with `rustdoc`. = #lang/syntax/comments 
<!--ID: 1758253288896-->

  `/// # Errors` ;;; Document where a `Result` type return would have issues with `rustdoc`. = #lang/syntax/comments 
<!--ID: 1758253288903-->

  `/// # Arguments` ;;; Document what arguments are required for a function with `rustdoc`. = #lang/syntax/comments 
<!--ID: 1758253288910-->

  `/// # Safety` ;;; Document what is "unsafe" about a Rust struct/function/codeblock with `rustdoc`. = #lang/syntax/comments 
<!--ID: 1758253288918-->

  `/// # Panics` ;;; Document where a function uses `unwrap()` or another panic-related call. = #lang/syntax/comments 
<!--ID: 1758253288925-->

󰠗  How do you add a codeblock into Rust docs? What is unique about these codeblocks? ;; Add a triple backtick. These will also be run as tests when you run `cargo test`. = #lang/test #lang/syntax/comments #lang/syntax/documentation

### Rules of thumb
- [Making Great Docs with Rustdoc - Tangram Visions Blog](https://www.tangramvision.com/blog/making-great-docs-with-rustdoc)
- Don't document trait implementations
