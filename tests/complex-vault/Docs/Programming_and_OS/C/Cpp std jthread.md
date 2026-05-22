---
summary: A single thread of execution, having similar behavior as std::thread--other thanjthread automatically rejoins on destruction, and can be cancelled/stopped in certain situations.
type: note/class
headings: ["[[#Concepts of Note]]", "[[#Properties]]"]
similar: ["[[Cpp thread]]"]
class_of: ["[[Cpp std]]"]
date created: Wednesday, January 14th 2026, 12:02:21 pm
date modified: Wednesday, January 14th 2026, 12:16:33 pm
template: "[[base_note_template]]"
template-version: 1.0.1
used_by: ["[[Cpp std terminate]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[std::jthread - cppreference.com](https://en.cppreference.com/w/cpp/thread/jthread.html)

## Concepts of Note
Introduced in C++20

Has private member of `std::stop_source` which lets you terminate itself if you want. The top level function can also do this.

No two jthreads can represent the same thread of execution.

NOT CopyConstructible or CopyAssignable.

MoveConstructible and MoveAssignable

## Properties