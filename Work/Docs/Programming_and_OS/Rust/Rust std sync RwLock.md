---
summary: A read-writer lock. Allowing a number of readers or at most one writer at any point in time. The write portion of this lock typically allows modification of the underlying data (exclusive). The read portion of the lock typically allows for read-only access (shared).
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/class
date created: Thursday, July 3rd 2025, 3:32:58 pm
date modified: Thursday, July 3rd 2025, 3:38:56 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[RwLock in std::sync - Rust](https://doc.rust-lang.org/std/sync/struct.RwLock.html)

## Concepts of Note

## Usage
- [p] `let lock = RwLock::new(data)` = Implement a read-write lock. This will enable a number of readers shared access, and a writer exclusive access. = #code/rust/sync/mutex  
- [t] Which type in rust will let enable data to be read by multiple threads, and written in only one place? Note, this class makes a distinction between readers and writers when they attempt to acquire the lock. = `RwLock` = #code/rust/sync/mutex 
- [t] Which traits must be satisfied for the `RwLock`? = `Send` and `Sync` = #code/rust/sync/mutex  