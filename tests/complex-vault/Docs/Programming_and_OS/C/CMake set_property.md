---
summary: 
implements: ["[[CMake properties]]"]
down: ["[[CMake set_target_properties]]"]
date created: Thursday, October 17th 2024, 1:04:45 pm
date modified: Thursday, October 17th 2024, 1:11:19 pm
type: note/function
---
`VIEW[**{summary}**][text(renderMarkdown)]`
[set\_property — CMake 3.31.0-rc2 Documentation](https://cmake.org/cmake/help/latest/command/set_property.html#command:set_property)
![[CMake properties#Property Scope]]

# Usage
```
set_property(<GLOBAL                      |
              DIRECTORY [<dir>]           |
              TARGET    [<target1> ...]   |
              SOURCE    [<src1> ...]
                        [DIRECTORY <dirs> ...]
                        [TARGET_DIRECTORY <targets> ...] |
              INSTALL   [<file1> ...]     |
              TEST      [<test1> ...]
                        [DIRECTORY <dir>] |
              CACHE     [<entry1> ...]    >
             [APPEND] [APPEND_STRING]
             PROPERTY <name> [<value1> ...])
```
First argument determines scope:
- 

