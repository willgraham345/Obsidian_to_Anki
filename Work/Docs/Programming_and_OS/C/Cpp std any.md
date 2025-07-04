---
summary: Designed for storing values of any type, enabling runtype type storage and retrieval. Very flexible, meant for scenarios where the type isn't known at compile-time.
headings: ["[[#Concepts of Note]]"]
type: note/class
similar: ["[[Cpp std variant]]"]
date created: Monday, April 14th 2025, 2:43:24 pm
date modified: Thursday, April 17th 2025, 2:28:08 pm
function_of: ["[[Cpp Casting]]"]
tags: [code/cpp/variables/casting]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Can store values of any type
- Requires runtime type checks to retrieve the stored value
- Flexible, but less performant than type-safe alternatives like [[Cpp std variant]]
- Slower due to runtime checks, and can throw `bad_any_cast`

## Usage
- [p] `std::any_cast<std::string>(value)` = Storing a string in an "any" type = #code/cpp/variables/casting
<!--ID: 1751434091621-->
