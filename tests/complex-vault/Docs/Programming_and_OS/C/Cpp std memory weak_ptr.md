---
summary: "Non-owning smart pointer that observes an object managed by shared_ptr. Does not affect reference count. Must be converted to shared_ptr to access the object."
type: note/class
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
up: "[[Cpp std memory]]"
similar:
  - "[[Cpp pointers]]"
  - "[[Cpp std memory shared_ptr]]"
  - "[[Cpp std memory unique_ptr]]"
aliases: [Cpp weak_ptr]
associations:
  - "[[Cpp std memory shared_ptr]]"
class_of:
  - "[[Cpp std memory]]"
date created: Tuesday, October 8th 2024, 12:53:00 pm
date modified: Friday, March 20th 2026, 1:24:42 pm
tags: []
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
󰙎 weak_ptr ;;; observes a `shared_ptr`-managed object without participating in ownership; does not increment use count
󰙎 lock() ;;; converts `weak_ptr` to a `shared_ptr` — returns empty `shared_ptr` if the object has already been destroyed
󰙎 expired() ;;; returns `true` if the managed object has been destroyed (use count is 0); cheaper than `lock()` when you only need to check existence
󰙎 reference cycle ;;; A→B and B→A both hold `shared_ptr`; neither ref count reaches zero → memory leak; break with `weak_ptr` on the back-edge
󰠗 How do you safely access the object pointed to by a weak_ptr? ;; Call lock() to get a shared_ptr, then check if it's non-null — the object may have been destroyed between the check and the access.
󰠗 What is the main use case for weak_ptr? ;; Breaking shared_ptr reference cycles (e.g. parent↔child trees, observer/subject patterns) and non-owning cache entries.

## Usage
### Observe a shared_ptr
 `std::weak_ptr<T> w = sp;` ;;; create a weak observer from an existing `shared_ptr` — use count unchanged
 `if (auto locked = w.lock()) { locked->method(); }` ;;; safe access pattern — lock() returns empty shared_ptr if expired
 `w.expired()` ;;; true if the managed object is gone; use when you only need to check, not access

### Break a Reference Cycle
 `std::weak_ptr<Node> parent;` ;;; in a tree node, hold the parent as `weak_ptr` and children as `shared_ptr` to avoid a cycle
