---
type: reference
headings:
date created: Wednesday, March 18th 2026, 12:00:00 pm
date modified: Wednesday, March 18th 2026, 11:01:32 am
item_of:
  - "[[C syntax]]"
  - "[[Docs/Programming_and_OS/C/C]]"
items:
  - "[[c_type_array]]"
  - "[[c_type_bool]]"
  - "[[c_type_char]]"
  - "[[c_type_complex]]"
  - "[[c_type_double]]"
  - "[[c_type_enum]]"
  - "[[c_type_float]]"
  - "[[c_type_int]]"
  - "[[c_type_long_double]]"
  - "[[c_type_long_long]]"
  - "[[c_type_long]]"
  - "[[c_type_pointer]]"
  - "[[c_type_ptrdiff_t]]"
  - "[[c_type_short]]"
  - "[[c_type_size_t]]"
  - "[[c_type_stdint]]"
  - "[[c_type_struct]]"
  - "[[c_type_typedef]]"
  - "[[c_type_union]]"
  - "[[c_type_unsigned]]"
  - "[[c_type_void]]"
tags: []
template:
template-version:
---

# Summary
󰙎 C datatypes ;;; All built-in and standard-library types available in C; governs storage size, alignment, and value range for every variable and expression.

# Additional Background
C's type system is static and weakly typed. Sizes of primitive types are platform-dependent except where fixed-width types (`<stdint.h>`) are used. C99 and C11 extended the original K&R set with booleans, complex numbers, and guaranteed-width integers.

## Concepts of Note

󰠗 What determines the size of `int` on a given platform? ;; The ABI/data model (e.g. LP64 vs ILP32), not the C standard — only minimum widths are mandated.

󰠗 Which header provides guaranteed-width integers? ;; `<stdint.h>` (C99+), e.g. `int32_t`, `uint64_t`.

## Usage

### Primitive Types

| Type | Category | Min width | Notes |
|---|---|---|---|
| `[[c_type_char]]` | Integer | 8 bit | May be signed or unsigned; used for characters and small integers |
| `[[c_type_short]]` | Integer | 16 bit | `short int`; rarely preferred over `int` |
| `[[c_type_int]]` | Integer | 16 bit | Default integer; typically 32 bit on modern platforms |
| `[[c_type_long]]` | Integer | 32 bit | 32 bit (Windows) or 64 bit (Linux LP64) |
| `[[c_type_long_long]]` | Integer | 64 bit | C99+; at least 64 bit |
| `[[c_type_unsigned]]` | Integer modifier | — | Applied to any integer type; removes sign, doubles positive range |
| `[[c_type_float]]` | Floating-point | 32 bit | IEEE 754 single precision |
| `[[c_type_double]]` | Floating-point | 64 bit | IEEE 754 double precision; default FP type |
| `[[c_type_long_double]]` | Floating-point | 80/128 bit | Platform-dependent extended precision |
| `[[c_type_void]]` | Special | — | No value; used for typeless pointers and functions with no return |
| `[[c_type_bool]]` | Integer | 8 bit | C99+; `<stdbool.h>`; values `true`/`false` |

### Derived / Aggregate Types

| Type | Description |
|---|---|
| `[[c_type_pointer]]` | Holds memory address of another object; `T*` syntax |
| `[[c_type_array]]` | Contiguous block of same-type elements; fixed or VLA size |
| `[[c_type_struct]]` | Named aggregate of heterogeneous fields; fields laid out sequentially |
| `[[c_type_union]]` | Overlapping storage for multiple interpretations of the same bytes |
| `[[c_type_enum]]` | Named integer constants; underlying type is `int` by default |
| `[[c_type_typedef]]` | Alias for any type; does not create a new type, only a new name |

### C99 / C11 Standard-Library Types

| Type | Header | Description |
|---|---|---|
| `[[c_type_stdint]]` | `<stdint.h>` | Fixed-width integers: `int8_t` … `uint64_t`, `intmax_t`, `uintmax_t` |
| `[[c_type_size_t]]` | `<stddef.h>` | Unsigned type for object sizes; result of `sizeof` |
| `[[c_type_ptrdiff_t]]` | `<stddef.h>` | Signed type for pointer differences |
| `[[c_type_complex]]` | `<complex.h>` | C99+; complex floating-point: `float _Complex`, `double _Complex` |

## Syntax

 `sizeof(type)` ;;; returns `size_t` count of bytes occupied by type; evaluated at compile time for all non-VLA types

 `(type)expr` ;;; explicit cast; converts `expr` to `type`; no runtime check, programmer responsibility

 `unsigned int x` ;;; `unsigned` modifier shifts range from `[-2^(n-1), 2^(n-1)-1]` to `[0, 2^n-1]`

```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```
