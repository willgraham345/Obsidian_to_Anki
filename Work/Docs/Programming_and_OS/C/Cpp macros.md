---
summary: Variables with fixed values that can't be changed, typically written in all caps. Once they're defined, they remain constant throughout the execution of the program. Generally stored as read-only tokens in the code segment of the memory of the program.
type: note/concept
similar:
  - "[[Cpp templates]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, January 14th 2025, 2:41:24 pm
concept_of:
  - "[[Cpp Variables and Containers]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
`const` vs `constexpr`
Similar, but `constexpr` are initialized at compiler time.

# Usage
Constant using `const` keyword
```cpp
const DATATYPE variable_name = value;
```

Constant using the `constexpr` keyword
```cpp
constexpr DATATYPE variable_name = value;
```

Constant using `#define` preprocessor
- Known as "macro constants"
These will work as an alias for the value which is substituted during the preprocessing. 
```cpp
#define MACRO_NAME replacement_value
```

## Bad examples
```cpp
const int var;
const int var;
var = 5
```