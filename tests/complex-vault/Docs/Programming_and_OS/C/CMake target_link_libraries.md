---
summary: Will add a target/flag as a dependency for that target, making it aware of the symbols (e.g. functions/classes/variables) within that library.
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
implements:
  - "[[CMake target]]"
  - "[[CMake visibility]]"
prev:
  - "[[CMake target_sources]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, March 18th 2026, 8:42:01 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
used_by:
  - "[[CMake Libraries]]"
  - "[[CMake target]]"
  - "[[Cpp include]]"
  - "[[Cpp include|C include]]"
---

# Summary
󰙎 target_link_libraries ;;; CMake's way of associating output artifacts with each other (dependency mapping)

# Additional Background

## Concepts of Note
### Linkable items
1. Library target name — full path to the linkable file; target must exist via [[CMake add_library]] or as an imported target
2. Full path to a library file — re-links `<target>` if the file changes
3. Plain library name — linker searches for it (e.g. `-lfoo`)
4. Link flag — passed directly to the linker
5. [[CMake generator expression]]

### Visibility keywords
See [[CMake visibility]] for full semantics.

| Keyword | Compile definitions/includes propagate to... | Link propagates to... |
|---|---|---|
| `PUBLIC` | `<target>` and consumers | `<target>` and consumers |
| `PRIVATE` | `<target>` only | `<target>` only |
| `INTERFACE` | consumers only | consumers only |

󰙎 PUBLIC ;;; dependency needed to build and use `<target>` — propagates to all consumers
󰙎 PRIVATE ;;; dependency needed only to build `<target>` — not exposed to consumers
󰙎 INTERFACE ;;; dependency not used by `<target>` itself but required by consumers (e.g. header-only libs)

### Chaining libraries
```cmake
add_library(another STATIC another.cpp another.h)
target_link_libraries(another PUBLIC one)
```
- If `one` is a CMake target, adds the full transitive dependency. If not, links a library named `one` from the path.
- Prefer target names over plain library names — enables transitive dependency propagation.

## Usage
 `target_link_libraries(<target> PUBLIC <item>)` ;;; Define an `item` that `target` depends on. Also specify that the compile definitions and link will propagate to `target` and all of it's consumers.
 `target_link_libraries(<target> PRIVATE <item>)` ;;; Define an `item` that `target` depends on. Also specify that nothing other than the `target` will propagate to `target` only. 
 `target_link_libraries(<target> ... <item>...)` ;;; legacy positional form — no visibility keyword; inherits caller's propagation rules

```cmake
target_link_libraries(<target> <PRIVATE|PUBLIC|INTERFACE> <item>...)


target_link_libraries(<target>
  <PRIVATE|PUBLIC|INTERFACE> <item>...
  [<PRIVATE|PUBLIC|INTERFACE> <item>...]...)
```
