---
summary: Set of statements that takes input, does something, and produces output. Has various rules regarding parameter passing and variable usage.
headings: ["[[#Concepts of Note]]", "[[#Syntax]]"]
type: note/concept
examples: ["[[Cpp Function Examples]]"]
concepts: ["[[Cpp const Member Functions]]", "[[Cpp functors]]", "[[Cpp Lambda Capture]]", "[[Cpp Variadic Functions]]"]
workflows: ["[[Cpp function array arguments]]", "[[Cpp function pointers and references]]"]
similar: ["[[Python Functions]]"]
associations: ["[[Cpp explicit]]", "[[Cpp std optional (class)]]", "[[Cpp templates]]"]
concept_of: ["[[Cpp]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, June 19th 2025, 2:27:15 pm
implementations: ["[[Cpp pointers]]", "[[Cpp references]]"]
tags: [term/cpp/functions]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- 
- You can have functions which take another function as an argument (i.e. [[DP Functional Programming]])
- [I] Function prototype = Declaration of function's name, return type, and params without the function body (blueprint for compiler before definition) = #term/cpp/functions
- [I] Function implementation = Definition of a function and what it does = #term/cpp/functions

## Syntax
```cpp
//declaration
return_type functionName(param_type paramName);

//definition
functionName(param_type paramName);
{
	//Implementation
}
```

See [[Cpp function pointers and references]] for more examples/usage cases
