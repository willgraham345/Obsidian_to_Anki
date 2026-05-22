---
type: note/concept
headings:
  - "[[#Concepts of Note]]"
aliases: [CS Virtual dispatch]
associations:
  - "[[CS Static Dispatch]]"
concept_of:
  - "[[CS OOP Polymorphism]]"
date created: Wednesday, February 25th 2026, 5:56:34 pm
date modified: Thursday, March 19th 2026, 12:37:51 pm
tags: [cs/oop/polymorphism/runtime/dynamic_dispatch]
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[C pointers]]"
  - "[[Cpp pointers]]"
  - "[[CS Dynamic Polymorphism]]"
  - "[[CS Pointer]]"
---

# Summary
󰙎 CS Dynamic dispatch ;;; A technique of determining the function/method it should call at *during* runtime. Often implemented via a virtual table (vtable) where a base pointer calls the appropriate derived class method.  ^e9638d

# Additional Background
## Concepts of Note
Dynamic dispatch introduces a small runtime overhead, though this is often negligible. 
Runtime overhead is introduced as the virtual table is traversed.