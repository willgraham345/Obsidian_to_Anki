---
summary: Ties libraries or flags to whatever target your target. Has scope for rules on its dependents. Will add that library as a dependency for that target, making it aware of the symbols (e.g. functions/classes/variables) within that library.
implements: ["[[CMake target]]"]
concepts: ["[[Cmake target link scopes]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, November 4th 2024, 5:08:28 pm
type: note/function
---

[Docs](https://cmake.org/cmake/help/latest/command/target_link_libraries.html#command:target_link_libraries "target_link_libraries")

# Scope
# Usage
```cmake
`target_link_libraries(<target> ... <item>... ...)`
```

## Chaining Libraries
```cmake
add_library(another STATIC another.cpp another.h)
target_link_libraries(another PUBLIC one)
```
`target_link_libraries()` is the most useful command in CMake.
- It takes a target (`another` in this example), and adds a dependency if a target is given. 
- If no target of that name (`one` in this example) exists, then it adds a link to a library (called `one` in this example) on your path. 
- You can give it a full path, a linker flag, or anything. CMake also lets you skip the keyword selection of `PUBLIC`. 
- Try to use targets as much as possible. 

What can targets include?
- Directories
- Linked libraries (or linked targets)
- Compile options
- Compile definitions
- Compile features

You can often get targets (and always make targets) to represent all the libraries you use. 