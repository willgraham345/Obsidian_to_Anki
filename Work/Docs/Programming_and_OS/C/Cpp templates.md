---
summary: Think of this as a function which generates a different version of itself, for every data type that uses it. Used for implementing generic algorithms (vectors, stacks, queues), and for efficiency. Keep in mind, you can pass functions as types in the object.<br><br>Templates form the basis for the standard library with [[Cpp std vector]], [[Cpp std map (class)]], and [[Cpp std set]].<br>Templates are expanded at compiler time, similar to macros. The compiler does type-checking before template expansion.
headings: ["[[#Concepts of Note]]", "[[#Media]]"]
type: note/concept
similar: ["[[Cpp Class Constructors]]", "[[Cpp macros]]"]
associations: ["[[Cpp Class Constructors]]", "[[Cpp Functions]]", "[[Cpp typename]]"]
concept_of: ["[[Cpp Class]]", "[[Cpp Variables and Containers]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, June 10th 2025, 3:53:15 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- A template is a tool that can pass data type as a parameter so that we don't need to write the same code for different data types. 
	- Sorting `int` and `char`

## Concepts of Note
- [I] Variadic template = Template that can accept zero or more template arguments, potentially of different types = #term/cpp 
- [p] `template <typename... T> entity_definition` = Declare variadic template, which can accept zero or more template arguments of potentially different types. `T` acts as a list of types (it is a parameter pack). `entity_definition` can be a `class` definition, function, or whatever else. Very useful for dependency injection = #code/cpp/templates
<!--ID: 1751434091453-->


## Media
[More here](https://www.geeksforgeeks.org/templates-cpp/)
<iframe src="https://www.geeksforgeeks.org/templates-cpp/" style="width: 100%; height: 600px;"></iframe>
 