---
summary: Introduced with C++20, they are a language feature intended to share declarations and definitions across translation units. Alternative to some use cases of headers.
type: note/library
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
  - "[[#Syntax]]"
up: "[[Cpp]]"
library_of:
  - "[[Cpp]]"
similar:
  - "[[Cpp.include_and_forward_declaration]]"
associations:
  - "[[Cpp.compiler.overview]]"
  - "[[Cpp.build.tools.overview]]"
  - "[[Cpp.Literals and Macros]]"
  - "[[Cpp.Functions.Inline]]"
implements:
  - "[[Dependency Inversion and Injection]]"
date created: Monday, February 9th 2026, 9:55:36 am
date modified: Friday, March 20th 2026, 12:00:00 pm
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Module Units
- [I] module interface unit ;;; TU declaring `export module name;`. Defines the public API; compiled first, produces a Binary Module Interface (BMI) cached by the build system.
- [I] module implementation unit ;;; TU declaring `module name;` (no `export`). Provides definitions; implicitly imports its own interface.
- [I] named module ;;; Collection of module units sharing a module-name. Replaces the header+source pair pattern.

### Partitions
- [I] module partition ;;; Sub-unit declared `module name:part;`. Splits large modules across files without exposing internal boundaries to importers.
- [I] interface partition ;;; `export module name:part;` — partition that contributes exported names to the primary interface.
- [I] implementation partition ;;; `module name:part;` — visible only within the module, never to importers.
- [p] `import :partition;` ;;; Import a partition *from within the same module only* — cannot be imported externally.

### Global Module Fragment
- [I] global module fragment ;;; Region before `export module name;`, introduced by `module;`. Used to `#include` legacy headers without leaking their macros into the module.
- [p] `module; #include <legacy.h> export module mymod;` ;;; Isolates a legacy `#include` so macros don't contaminate the module's purview.

### Private Module Fragment
- [I] private module fragment ;;; Region after `module : private;` in a primary interface unit. Declarations here are reachable but not visible to importers — hides implementation without a separate `.cpp` file.

### Visibility vs Reachability
- [I] visible ;;; A declaration that can be *named* by an importer — requires `export`.
- [I] reachable ;;; A declaration the compiler can use for semantic purposes (base-class layout, type completeness) even without being directly nameable. Can be reachable but not visible.
- [t] Difference between visible and reachable in C++ modules? ;; Visible = exported, can be named. Reachable = compiler sees the definition for type-checking/layout even if not exported. An unexported base class is reachable but not visible.

### Modules vs Headers
- [I] header unit ;;; `import <header>;` — transitional: treats a header as a module. Macros still leak; not a true named module.
- [t] Key advantages of modules over headers? ;; No macro leakage, no repeated parsing (BMI cached), no include-order sensitivity, explicit dependency graph, faster incremental builds.

## Usage
### Define an Interface Unit
- [p] `export module math;` ;;; Primary module interface unit declaration (file ext: `.cppm`, `.ixx`, or `.mpp` depending on toolchain)
- [p] `export int add(int a, int b);` ;;; Export a single declaration
- [p] `export { int sub(int a, int b); double pi(); }` ;;; Export a block of declarations

### Define an Implementation Unit
- [p] `module math;` ;;; Module implementation unit — implements `math` without re-exporting anything
- [p] `int add(int a, int b) { return a + b; }` ;;; Definition in the implementation unit; no `export` keyword

### Consume a Module
- [p] `import math;` ;;; Import a named module — replaces `#include "math.h"`
- [p] `import <vector>;` ;;; Import a standard library header unit

### Partitions
- [p] `export module math:core;` ;;; Declare an interface partition
- [p] `export import :core;` ;;; Re-export a partition from the primary interface unit
- [p] `import :impl_detail;` ;;; Import an implementation partition (same module, not visible externally)

## Syntax
| Form | Meaning |
|---|---|
| `export module name;` | Primary module interface unit |
| `module name;` | Module implementation unit |
| `export module name:part;` | Interface partition |
| `module name:part;` | Implementation partition |
| `module;` | Start global module fragment |
| `module : private;` | Start private module fragment |
| `export declaration` | Export a single declaration |
| `export { decl-seq }` | Export a block of declarations |
| `import name;` | Import a named module |
| `import :part;` | Import a partition (same module only) |
| `import <header>;` | Import a header unit |