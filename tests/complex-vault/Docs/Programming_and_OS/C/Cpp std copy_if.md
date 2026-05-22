---
summary: Similar to the `std::ranges::copy()`, but accepts a third argument as a conditional. Will only execute if that returns true.
headings: ["[[#Concepts of Note]]"]
type: note/function
similar: ["[[Cpp std range copy]]"]
date created: Thursday, June 5th 2025, 10:58:31 am
date modified: Saturday, November 8th 2025, 12:06:00 pm
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

  `std::ranges::copy_if(Source, Destination.begin(), isEven)` ;;; Copies every element from `Source` to a `Destination` based on a conditional lambda fn (`IsEven` in this example. = #lang/data/vector  



