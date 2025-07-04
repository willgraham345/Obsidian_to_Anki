---
summary: Similar to the `std::ranges::copy()`, but accepts a third argument as a conditional. Will only execute if that returns true.
headings: ["[[#Concepts of Note]]"]
type: note/function
similar: ["[[Cpp std range copy]]"]
date created: Thursday, June 5th 2025, 10:58:31 am
date modified: Thursday, June 5th 2025, 11:02:46 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

- [p] `std::ranges::copy_if(Source, Destination.begin(), isEven)` = Copies every element from a source range to a new destination. The destination where elements will be copied is the second argument. In this example, `isEven` is a lambda function taking in an `x` parameter and returning true/false = #code/cpp/variables/copying #code/cpp/variables/vectors 
<!--ID: 1751434091610-->

