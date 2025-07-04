---
summary: Lets you define what namespace you are using things from. Can be used from a namespace or block scope, or within a class. Can also be used as a more flexible alternative to typedef for creating aliases for various datatypes.
type: note/component
associations: ["[[Cpp Scope Operator]]", "[[Cpp typedef]]"]
component_of: ["[[Cpp Scope and Namespace]]"]
date created: Thursday, January 16th 2025, 12:15:53 pm
date modified: Thursday, January 16th 2025, 12:42:58 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Concept
Using within a class can expose a protected member of base as public or derived.

## Usage
- [p] `using std::string` = Example use case for namespacing a function/class in your code = #code/cpp/scope/using
<!--ID: 1751434091448-->

### Nested name specifier 
```cpp
using std::string
```

### Declarator list
Comma separated list of one or more declarations of the typename thing. Look at the website below to learn more about this, don't understand it myself.

### Bad Example
```cpp
using namespace std
```
DO NOT USE THIS. Will use namespace std at a global level if it is included in a header file.
### Typedef alternative
```cpp
using int_array2D = int[4][4]
```

## Media
[Using-declaration - cppreference.com](https://en.cppreference.com/w/cpp/language/using_declaration)
<iframe src="https://en.cppreference.com/w/cpp/language/using_declaration" style="width: 100%; height: 600px;"></iframe>

# Additional Background