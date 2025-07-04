---
summary: Atomically reference counted pointer. Useful for multithreaded environments to prolong lifetime of some data until all the threads have finished using it.<br><br>Provides shared ownership to value of type `T`
headings: ["[[#Concepts of Note]]"]
type: note/class
similar: ["[[Rust std sync LazyLoc]]", "[[Rust std sync OnceLock]]"]
date created: Thursday, May 22nd 2025, 9:57:05 am
date modified: Thursday, May 22nd 2025, 10:00:29 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [p] `let mut d`
Shared references disallow multation by default. You generally obtain a mutable reference to something within `Arc`
