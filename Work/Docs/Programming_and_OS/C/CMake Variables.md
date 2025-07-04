---
summary: 
type: note/concept
down: ["[[CMake INTERFACE_SOURCES]]", "[[CMake SOURCES]]"]
concepts: ["[[CMake Variables Scope]]"]
functions: ["[[CMake.set]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, April 14th 2025, 4:35:48 pm
---
# Background
[CMake Variables Manual](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7))

> [!WARNING]
> Avoiding naming variables `CMAKE_`, as CMake already does that with a bunch of them. All CMake variables are stored internally as strings.

# Usage

## Accessing Variables
```cmake
	set(Foo a b c)    # 3 unquoted args -> value is "a;b;c"
	command(${Foo})   # unquoted arg replaced by a;b;c
	                  # and expands to three arguments
	command("${Foo}") # quoted arg value is "a;b;c"
	set(Foo "")       # 1 quoted arg -> value is empty string
	command(${Foo})   # unquoted arg replaced by empty string
	                  # and expands to zero arguments
	command("${Foo}") # quoted arg value is empty string
```

## Checking if a Variable has been Set
```cmake
	if(NOT DEFINED ${VAR_NAME})
```