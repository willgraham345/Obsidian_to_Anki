---
summary: "Deprecated (C++11) and removed (C++17) smart pointer with unique-ownership semantics. Superseded by unique_ptr. Do not use in new code."
type: note/class
up: "[[Cpp std memory]]"
similar:
  - "[[Cpp std memory unique_ptr]]"
class_of:
  - "[[Cpp std memory]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, March 20th 2026, 12:00:00 pm
tags: []
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] auto_ptr (deprecated) ;;; Pre-C++11 unique-ownership pointer. Copy operations secretly *transfer* ownership — the source becomes null, violating `CopyConstructible` contracts expected by STL containers.
- [I] why removed ;;; Semantically broken: STL algorithms and containers assume copies produce equivalent objects; `auto_ptr` breaks this guarantee silently.

## Usage
- [p] `std::unique_ptr<T>` ;;; **use this instead** — correct move semantics, works in containers → [[Cpp std memory unique_ptr]]