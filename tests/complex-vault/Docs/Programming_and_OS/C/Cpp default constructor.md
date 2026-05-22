---
summary: Constructor which requires no arguments to be called.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Media]]"
  - "[[#Usage]]"
type: note/item
associations:
  - "[[Cpp default]]"
item_of:
  - "[[Cpp Class Constructors]]"
date created: Wednesday, April 16th 2025, 9:35:12 am
date modified: Thursday, June 26th 2025, 9:53:30 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- A way to tell the compiler to do what it normally would in:
	- Default-initializing all members
	- (if applicable) call any base class default constructors
󰙎  Compound statement ;;; A block used to group multiple statements into a single unit. Enclosed in curly braces, and can be used wherever a single statement is expected. = #lang
<!--SR:!2000-01-01,1,250!2025-12-18,4,270-->



## Usage
  `class-name() ;;; default` = Tells the compiler to default-initialize all members--and call any default constructors (if applicable). Notably, this says we don't need an initialization list and it can have an empty compound statement. = #lang/oop/class/constructors 
ID: 1751997629773


