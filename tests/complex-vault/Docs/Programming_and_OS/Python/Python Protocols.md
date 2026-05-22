---
summary: Provide ways to create interchangeable classes as long as they share a common internal structure. Protocol can also refer to internal protocols (iterator, context manager, and descriptor) protocols, or the type introduced in Python 3.8, which specify methods/attributes a class must implement to be considered of a given type.
type: note/concept
headings:
similar:
  - "[[Cpp interface]]"
  - "[[Rust trait]]"
concept_of:
  - "[[Python OOP Polymorphism]]"
  - "[[Python OOP]]"
date created: Tuesday, December 16th 2025, 12:17:41 pm
date modified: Tuesday, December 16th 2025, 12:42:54 pm
template: "[[base_note_template]]"
template-version: 1.0.1
tags:
  - toread
  - TODO/learn
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Protocols — typing documentation](https://typing.python.org/en/latest/spec/protocol.html)
󰙎 MRO ;; Method resolution order,
󰙎 Subclass of the protocol ;; A class that includes a protocol in it's MRO
󰙎 Static duck typing ;; Python's version of defining interchangeable classes that share a common internal structure, similar to Cpp interface.

󰙎 Protocol members ;; Attributes (variables and methods) of a protocol are mandatory for another class to implement the protocol.
If a class defines all attributes and methods of a protocol, then it is said to implement the protocol.

