---
summary: Concurrent programming, where the program performs multiple things at the same time.
headings: ["[[#Concepts of Note]]"]
type: note/concept
similar: ["[[Cpp multithreading]]"]
concept_of: ["[[Rust Control Flow]]"]
date created: Tuesday, August 5th 2025, 11:13:40 am
date modified: Tuesday, August 5th 2025, 11:21:21 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Returns a `Future` instead of blocking the current thread
- For use in front of a `fn`, `closure`, or `block` to turn this into a `Future`. The code will not be returned immediately, and only will be evaluated when the returned future is `.await`ed.