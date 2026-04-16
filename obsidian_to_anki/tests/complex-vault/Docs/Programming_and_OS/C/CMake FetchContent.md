---
type: note/library/module
tags:
  - programming/cmake
date created: 2026-03-18
date modified: 2026-03-18
up: "[[CMake modules]]"
uses:
  - "[[CMake ExternalProject]]"
  - "[[CMake add_subdirectory]]"
  - "[[CMake find_package]]"
---

# Summary
󰙎 FetchContent ;;; CMake module that populates external dependencies at configure time, making targets immediately available to the build

# Additional Background
Built on [[CMake ExternalProject]] but runs at configure time (not build time), so populated targets are usable in [[CMake add_subdirectory]], [[CMake include]], and [[CMake file]] within the same configure pass.

Key invariants:
- Declare details before populating — separate `_Declare` from `_MakeAvailable`/`_Populate`
- First population wins — subsequent calls reuse the result; higher-level projects override lower-level declarations
- Pinning by full commit hash is strongly preferred over branch names or version tags

## Concepts of Note

### Population hierarchy
Parent projects override child declarations for the same dependency name. Declare all deps at the top level when override control matters.

### find_package integration
`FIND_PACKAGE_ARGS` / `OVERRIDE_FIND_PACKAGE` let FetchContent act as a fallback or replacement for [[CMake find_package]], transparently routing `find_package(Foo)` calls through FetchContent.

### Populated vs. added
`FetchContent_Populate` only downloads/extracts — it does not call `add_subdirectory`. `FetchContent_MakeAvailable` does both. Use `_Populate` + manual `add_subdirectory` only when you need to customise subdirectory options (e.g. `EXCLUDE_FROM_ALL`).

## Usage

### FetchContent_Declare

```cmake
FetchContent_Declare(
  <name>
  <contentOptions>...      # same options as ExternalProject_Add
  [EXCLUDE_FROM_ALL]       # don't include in ALL target when add_subdirectory'd
  [SYSTEM]                 # treat headers as system headers (suppress warnings)
  [OVERRIDE_FIND_PACKAGE]  # redirect find_package(<name>) to use this declaration
  [FIND_PACKAGE_ARGS args...]  # args passed to find_package before falling back to fetch
)
```

Common `<contentOptions>`:

| Option | Purpose |
|---|---|
| `GIT_REPOSITORY <url>` | Clone from git |
| `GIT_TAG <hash\|branch\|tag>` | Ref to checkout; **use full SHA for reproducibility** |
| `GIT_SHALLOW TRUE` | Shallow clone (depth 1); faster, no history |
| `GIT_SUBMODULES ""` | Disable submodule population |
| `URL <url>` | Download archive |
| `URL_HASH <algo>=<hash>` | Verify download integrity |
| `PATCH_COMMAND <cmd>` | Run after download/checkout; apply patches |
| `SOURCE_DIR <path>` | Override local source directory |
| `DOWNLOAD_NO_EXTRACT TRUE` | Download only, no extract (useful with `PATCH_COMMAND`) |

### FetchContent_MakeAvailable

```cmake
FetchContent_MakeAvailable(<name1> [<name2>...])
```

For each name: populates if not already done, then calls `add_subdirectory` (if a `CMakeLists.txt` is found). Preferred over manual `_Populate` + `add_subdirectory` in most cases.

### FetchContent_Populate (lower-level)

```cmake
# Modern form — uses declaration stored by FetchContent_Declare
FetchContent_Populate(<name>)

# Legacy standalone form (deprecated in 3.28)
FetchContent_Populate(
  <name>
  <contentOptions>...
)
```

After calling, sets variables in the calling scope:
- `<lowercaseName>_SOURCE_DIR`
- `<lowercaseName>_BINARY_DIR`
- `<lowercaseName>_POPULATED` → `TRUE`

Use when you need manual control over `add_subdirectory` (e.g. pass `EXCLUDE_FROM_ALL` or skip entirely for header-only deps).

### FetchContent_GetProperties

```cmake
FetchContent_GetProperties(<name>
  [SOURCE_DIR <srcDirVar>]
  [BINARY_DIR <binDirVar>]
  [POPULATED <isPopulated>]
)
```

Query population state for `<name>`. Useful in guard patterns:

```cmake
FetchContent_GetProperties(googletest)
if(NOT googletest_POPULATED)
  FetchContent_Populate(googletest)
  add_subdirectory(${googletest_SOURCE_DIR} ${googletest_BINARY_DIR} EXCLUDE_FROM_ALL)
endif()
```

### FIND_PACKAGE_ARGS / OVERRIDE_FIND_PACKAGE

```cmake
# Try find_package(Catch2 3 REQUIRED) first; fetch if not found
FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG        v3.5.2
  FIND_PACKAGE_ARGS 3 REQUIRED
)
FetchContent_MakeAvailable(Catch2)

# Force all find_package(mylib) calls to resolve through FetchContent
FetchContent_Declare(
  mylib
  GIT_REPOSITORY ...
  OVERRIDE_FIND_PACKAGE
)
```

## Concepts of Note — Best Practices

- Pin `GIT_TAG` to a full commit SHA, not a branch
- Use `GIT_SHALLOW TRUE` for large repos when history is not needed
- Declare all deps near the top of the root `CMakeLists.txt` before any `FetchContent_MakeAvailable` call
- Prefer `FetchContent_MakeAvailable` over the manual `_Populate` + `add_subdirectory` pattern unless customisation is required
- Use `FIND_PACKAGE_ARGS` to allow system-installed packages to satisfy the dependency without fetching

## Flashcards

󰠗 What is the difference between `FetchContent_Populate` and `FetchContent_MakeAvailable`? ;; `_Populate` downloads only; `_MakeAvailable` downloads + calls `add_subdirectory`
󰠗 How do you prevent FetchContent from re-fetching if already populated? ;; `FetchContent_GetProperties` + guard on `<name>_POPULATED`
󰠗 Why pin `GIT_TAG` to a full SHA? ;; Branch names and tags are mutable; a SHA guarantees a reproducible build
󰠗 What does `OVERRIDE_FIND_PACKAGE` do? ;; Redirects all `find_package(<name>)` calls in the project to resolve through the FetchContent declaration instead
