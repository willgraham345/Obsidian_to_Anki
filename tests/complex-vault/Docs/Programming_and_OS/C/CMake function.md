---
summary:
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Properties]]"
  - "[[#Syntax]]"
variables:
  - "[[CMake function#ARGC]]"
  - "[[CMake function#ARGN]]"
  - "[[CMake function#ARGV]]"
  - "[[CMake function#ARGV#]]"
similar:
  - "[[CMake macro]]"
aliases: []
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, March 10th 2026, 3:25:12 pm
id: CMake function
item_of:
  - "[[CMake]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
uses:
  - "[[CMake cmake_parse_arguments]]"
  - "[[CMake option]]"
---

# Summary
󰙎 CMake function ;;; A function that takes in `<arg1>`,... The function opens a new scope (`PARENT_SCOPE`)

# Additional Background
## Concepts of Note

Similar to a function in C or C++. Arguments can be passed in, and they become variables within the function. 

Standard variables like `ARGC`, `ARGV`, `ARGN`, `ARGV0`, and `ARGV1` are supported

### Scope
Function calls have a dynamic scope. 
Within a function, you are in a new scope. All variables defined when the function was called remain defined, but changes to variables only exist within the function. 

### Arguments
When the function is invoked
`ARGC`

### Positional Args vs [[CMake cmake_parse_arguments]]
Positional args best when:
- Argument is required, and always positional (target name, file path)
- You have few args, with obvious order
- Function is simple and stable
`cmake_parse_arguments` is best when:
- Arguments are optional
- You have a variety of args and named keywords
- You want `UNPARSED_ARGUMENTS`/`KEYWRODS_MISSING_VALUES` safety checks
- The function may grow over time

## Syntax
```cmake
function(foo)
	<commands>
endfunction()
```

## Properties
### variables
##### ARGV
󰫧 :
- description: Holds the list of all arguments given to the function
󰫧 end:

##### ARGN
󰫧 :
- description: Holds the list of arguments *past* the last expected argument.
󰫧 end:

##### ARGC
󰫧 :
- description: Number of arguments passed into the function
󰫧 end:

##### ARGV#
󰫧 :
- description: Has the values of args passed in. Facilitates creating functions with optional arguments.
󰫧 end:











