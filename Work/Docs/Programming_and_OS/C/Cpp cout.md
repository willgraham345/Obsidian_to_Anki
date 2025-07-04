---
summary: Print to standaard out with this.
headings: ["[[#Usage]]"]
type: note/function
associations: ["[[Cpp endl]]", "[[Cpp iostream cerr]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, April 15th 2025, 9:35:35 am
function_of: ["[[Cpp Input Output]]", "[[Cpp.iostream]]"]
tags: [code/cpp/IO/std]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

- Object of class [[Cpp ostream]] that is the standard output stream with type `char`. Corresponds to [[Cpp stdio stout]]
- The standard output stream is the default destination of characters determined by the environment. The destination may be shared with more standard objects ([[Cpp iostream cerr]] or [[Cpp.iostream.clog]])

## Usage
- [p] `std::cout << "string" << "\n";` = Output to stdout with a newline = #code/cpp/IO/std
<!--ID: 1751434091701-->
