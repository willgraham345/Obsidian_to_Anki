---
summary: Adds a build rule to the build system. There are two signatures (build events or generating files). Not sure what this does.
type: note/function
headings: ["[[#Examples]]", "[[#Usage]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 15th 2026, 2:58:02 pm
tags: [TODO/learn]
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Adds a custom build rule to the generated build system. 
[Docs](https://cmake.org/cmake/help/latest/command/add_custom_command.html#command:add_custom_command)

## Usage


```cmake
add_custom_command(OUTPUT output1 [output2 ...]
                   COMMAND command1 [ARGS] [args1...]
                   [COMMAND command2 [ARGS] [args2...] ...]
                   [MAIN_DEPENDENCY depend]
                   [DEPENDS [depends...]]
                   [BYPRODUCTS [files...]]
                   [IMPLICIT_DEPENDS <lang1> depend1
                                    [<lang2> depend2] ...]
                   [WORKING_DIRECTORY dir]
                   [COMMENT comment]
                   [DEPFILE depfile]
                   [JOB_POOL job_pool]
                   [JOB_SERVER_AWARE <bool>]
                   [VERBATIM] [APPEND] [USES_TERMINAL]
                   [COMMAND_EXPAND_LISTS]
                   [DEPENDS_EXPLICIT_ONLY])
```
- Defines a command to generate specified `OUTPUT` file(s). A created target in the same directory that specifies any output of the custom command as a source file is given a rule to generate the file using the command at build time. 

## Examples
[Example of using add\_custom\_command and add\_custom\_target together in CMake to handle custom build steps with minimal rebuilding: This example untars library headers for an INTERFACE library target · GitHub](https://gist.github.com/socantre/7ee63133a0a3a08f3990)