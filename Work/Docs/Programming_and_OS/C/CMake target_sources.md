---
summary: "Specifies sources to use when building a target and/or its dependents. The target needs to have been created before this. Scope is designated with: `PRIVATE`, `PUBLIC`, or  `INTERFACE`."
implements: ["[[CMake target]]"]
similar: ["[[CMake.target_link_libraries]]"]
date created: Wednesday, October 16th 2024, 11:08:17 am
date modified: Thursday, October 17th 2024, 12:55:26 pm
type: note/function
---
`VIEW[**{summary}**][text(renderMarkdown)]`

- [target\_sources — CMake 3.31.0-rc1 Documentation](https://cmake.org/cmake/help/latest/command/target_sources.html)
- Targets created by [[CMake add_custom_target]] can only be `PRIVATE` in scope
- For file


```cpp
target_sources(<target>
  [<INTERFACE|PUBLIC|PRIVATE>
   [FILE_SET <set> [TYPE <type>] [BASE_DIRS <dirs>...] [FILES <files>...]]...
  ]...)
```