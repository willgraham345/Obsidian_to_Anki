---
summary: "Smart pointer with shared ownership semantics. The managed object is destroyed when the last owning shared_ptr is destroyed or reset."
type: note/class
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
up: "[[Cpp std memory]]"
similar:
  - "[[Cpp pointers]]"
  - "[[Cpp std memory unique_ptr]]"
  - "[[Cpp std memory weak_ptr]]"
aliases: [Cpp shared_ptr]
associations:
  - "[[Cpp std memory weak_ptr]]"
class_of:
  - "[[Cpp std memory]]"
date created: Tuesday, October 8th 2024, 12:59:59 pm
date modified: Friday, March 20th 2026, 1:24:38 pm
implementations:
  - "[[Cpp std memory make_shared]]"
tags: []
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
󰙎 reference count ;;; atomic counter tracking how many `shared_ptr` instances share ownership; reaches zero → object + control block destroyed
󰙎 control block ;;; heap allocation holding the ref count, weak count, deleter, and allocator; created once per managed object
󰙎 make_shared ;;; preferred factory — allocates object and control block in one allocation → [[Cpp std memory make_shared]]
󰙎 enable_shared_from_this ;;; base class mixin; lets a managed object safely produce a `shared_ptr` to itself via `shared_from_this()`
󰠗 Why prefer `make_shared` over `shared_ptr<T>(new T)`? ;; Single allocation for object + control block (faster, exception-safe); `new T` risks a leak if the `shared_ptr` constructor throws
󰠗 When does the managed object get destroyed? ;; When the last `shared_ptr` owning it is destroyed or reset — use count drops to zero

## Usage
### Create and Copy
 `auto p = std::make_shared<MyType>(args...);` ;;; preferred construction — one allocation
 `auto q = p;` ;;; copy — both p and q own the object; use count becomes 2
 `p.reset();` ;;; release ownership; use count decremented; object destroyed if count reaches 0
 `p.use_count()` ;;; current number of owning shared_ptr instances (for debugging; not for logic)

### Access
 `p->method()` ;;; member access through shared_ptr
 `*p` ;;; dereference to get the managed object
 `p.get()` ;;; raw pointer to managed object — does not affect ownership; never delete this

### Thread Safety
 `std::atomic<std::shared_ptr<T>>` ;;; use when multiple threads may read/write the shared_ptr *object itself* (not just the managed data); ref-count ops are already atomic

### With weak_ptr
 `std::weak_ptr<T> w = p;` ;;; observe without owning — does not increment use count → [[Cpp std memory weak_ptr]]
