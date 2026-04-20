---
summary: Conditional control loop in CMake
type: note/function
headings: ["[[#Usage]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 29th 2026, 5:04:50 pm
tags: [lang/control_flow/if]
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[if()](https://cmake.org/cmake/help/latest/command/if.html#command:if "if")

## Usage
```
if(<condition>)
  <commands>
elseif(<condition>) # optional block, can be repeated
  <commands>
else()              # optional block
  <commands>
endif()
```

### Existence Checks
 `if (COMMAND getTacoBell)` ;;; CMake conditional depending on the existence of a `getTacoBell` command.
 `if (POLICY a)` ;;; CMake conditional depending on the existence of a policy `a`.
 `if (TARGET bigTarget)` ;;; CMake conditional that is true if a target `bigTarget` exists.





