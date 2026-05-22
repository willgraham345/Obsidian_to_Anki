---
summary: Environment variable, whose value is taken from the calling process environment. May be set to a list of directories specifying prefixes to search when using find_package, find_program, find_library, find_file, and find_path. This might hold a single prfix or a list of prefixes. Typically points towards installed packages.
type: note/item/variable
headings:
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 15th 2026, 3:32:32 pm
template: "[[base_note_template]]"
template-version: 1.0.1
used_by: ["[[CMake find_library]]", "[[CMake find_package]]", "[[CMake find_path]]", "[[CMake find_program]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
CMake variables can be set when creating the initial build, or later on a subsequent invocation of cmake

### Set variable when creating initial build
```shell
mkdir build
$ cd build
$ cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Debug
```

### Set variable on later build
```shell
cd build
$ cmake . -DCMAKE_BUILD_TYPE=Debug
```

### Setting Variables with `-D`
Can create or update (forced) a CMake `CACHE` entry. If `:<type>` portion is given 
```bash
cmake -DMY_CACHE_VAR="command line" -P cache.cmake
```
- The `-P` and `cache.cmake` direct the output to a script file. 

## Unset variables on command line
```shell
cd build
$ cmake . -UMyPackage_DIR
```