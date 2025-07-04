---
type: note
---
# Background
Adds a custom build rule to the generated build system. 
[Docs](https://cmake.org/cmake/help/latest/command/add_custom_command.html#command:add_custom_command)

# Usage
## Signature for adding a custom command to produce an output
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