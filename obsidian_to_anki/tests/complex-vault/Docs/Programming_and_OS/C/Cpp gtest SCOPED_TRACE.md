---
summary: Causes the current file name, line number, and the given message to be added to failure messages to be added for each assertion failure that occurs in scope.
headings:
  - "[[#Usage]]"
type: note/item
used_by:
  - "[[Cpp gtest Assertions]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
## Usage
  `SCOPED_TRACE(message)` ;;; Adds the current line, number, and message to be added to assertion calls. Useful for when a subroutine is called repeatedly from different sections of code.
