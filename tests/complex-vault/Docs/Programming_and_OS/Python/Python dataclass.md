---
summary: Class that is designed to only hold data values. These usually don't have any methods, and store information that will be passed between various projects. Introduced in Python 3.7.
headings: ["[[#Concepts of Note]]", "[[#Flashcards]]", "[[#Usage]]"]
type: note/library
implements: ["[[Python Decorators]]"]
date created: Monday, November 24th 2025, 10:49:34 am
date modified: Monday, December 1st 2025, 10:44:37 am
item_of: ["[[Python Data Types]]"]
library_of: ["[[Python Decorators]]"]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
[dataclasses — Data Classes — Python 3.14.0 documentation](https://docs.python.org/3/library/dataclasses.html)

## Usage
- [p] `@dataclass(frozen=True)`
      `class Expression` = Create a dataclass `Expression` that will generate an error if the fields are assigned. Emulates read-only frozen instances. = #lang/data/read_only #lang/memory/read_only #lang/data/immutable 

## Flashcards
󰠗  How do you designate a class as something used for transporting information only? ;; Add a `@dataclass` decorator. = #lang/data
󰠗  What method would let you add additional logic to the init process in a dataclass? ;; The `__post_init__()` = #lang/data 
󰠗  Can you modify a frozen dataclass? ;; Yes, by using the `object.__setattr__()` method. #lang/data/read_only #lang/memory/read_only 
- [t] What type do you use within a Python dataclass to signify that something is a member of the dataclass?