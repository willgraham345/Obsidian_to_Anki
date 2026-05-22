---
summary: A read-writer lock. Allowing a number of readers or at most one writer at any point in time. The write portion of this lock typically allows modification of the underlying data (exclusive). The read portion of the lock typically allows for read-only access (shared).
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/class
date created: Thursday, July 3rd 2025, 3:32:58 pm
date modified: Wednesday, July 9th 2025, 2:17:25 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[RwLock in std::sync - Rust](https://doc.rust-lang.org/std/sync/struct.RwLock.html)

## Concepts of Note

## Usage
  `let lock ``=`` RwLock::new(data)` ;;; Implement a read-write lock. This will enable a number of readers shared access, and a writer exclusive access. = #lang/data/sync/mutex   
<!--ID: 1758253288442-->



󰠗  Which type in rust will let enable data to be read by multiple threads, and written in only one place? Note, this class makes a distinction between readers and writers when they attempt to acquire the lock. ;; `RwLock` = #lang/data/sync/mutex  
<!--ID: 1758253288427-->

󰠗  Which traits must be satisfied for the `RwLock`? ;; `Send` and `Sync` = #lang/data/sync/mutex   
<!--ID: 1758253288435-->

