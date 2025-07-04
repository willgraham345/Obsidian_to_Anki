---
summary: "`&str` is a view into string data owned by something else."
headings:
  - "[[#Concepts of Note]]"
type: note/component
associations:
  - "[[Rust std String]]"
date created: Monday, April 28th 2025, 3:17:17 pm
date modified: Friday, June 27th 2025, 3:11:06 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- str is a `const char[]`, and represents the text itself. You only see this used when as a `&str`
- References can be converted to an owned string value `String`
- Generally used in function arguments and returns when it is possible to be used. Any function that creates a string that didn't previously exist must return `String` rather than `&str`.

## Media
[Understanding when to use String vs str - help - The Rust Programming Language Forum](https://users.rust-lang.org/t/understanding-when-to-use-string-vs-str/103746/2)