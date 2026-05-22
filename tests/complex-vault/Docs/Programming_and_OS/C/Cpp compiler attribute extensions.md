---
type: note
tags:
  - programming/cpp
  - programming/c
date created: Tuesday, March 17th 2026, 12:00:00 pm
date modified: Tuesday, March 17th 2026, 12:00:00 pm
---

# Summary
󰙎 `__attribute__((attr))` ;;; GCC/Clang compiler extension that annotates functions, variables, and types with optimization hints, diagnostics, or ABI directives — not standard C++, not supported by MSVC

Related: [[Cpp.compiler.overview]] | [[Cpp.Functions.Inline]] | [[C.Storage_Class_Specifiers]]

# Additional Background

GCC introduced `__attribute__` syntax; Clang adopted it for compatibility. C++11 added `[[attr]]` standard attributes; GCC/Clang expose their extensions under the `gnu::` namespace as `[[gnu::attr]]`. MSVC uses `__declspec(attr)` instead.

## Syntax Forms

| Form | Compiler | Notes |
|---|---|---|
| `__attribute__((attr))` | GCC, Clang | Primary form; double parens required |
| `[[gnu::attr]]` | GCC, Clang (C++11+) | Standard syntax wrapping GCC attrs |
| `[[attr]]` | All (C++11/17/20) | Only standardised attrs (e.g. `[[nodiscard]]`) |
| `__declspec(attr)` | MSVC | MSVC equivalent; different attr names |

## Common Attributes

| Attribute | Applies To | Effect |
|---|---|---|
| `__attribute__((noreturn))` | function | Signals function never returns; enables dead-code elim |
| `__attribute__((deprecated))` | any | Warn on use |
| `__attribute__((deprecated("msg")))` | any | Warn on use with custom message |
| `__attribute__((visibility("default")))` | function/var | Export symbol from shared lib |
| `__attribute__((visibility("hidden")))` | function/var | Hide symbol from shared lib ABI |
| `__attribute__((packed))` | struct/union | Suppress padding; may cause unaligned access |
| `__attribute__((aligned(N)))` | var/type | Force N-byte alignment |
| `__attribute__((always_inline))` | function | Force inlining regardless of heuristics — see [[Cpp.Functions.Inline]] |
| `__attribute__((noinline))` | function | Prevent inlining |
| `__attribute__((pure))` | function | No side effects; may read globals; result reusable |
| `__attribute__((const))` | function | No side effects; reads only args; stronger than `pure` |
| `__attribute__((unused))` | any | Suppress unused-variable/function warnings |
| `__attribute__((format(printf, M, N)))` | function | Enable printf-style format-string checking; M=fmt index, N=args index |
| `__attribute__((constructor))` | function | Run before `main()` |
| `__attribute__((destructor))` | function | Run after `main()` / `exit()` |
| `__attribute__((section("name")))` | function/var | Place in named ELF section |
| `__attribute__((weak))` | function/var | Weak linkage; overridable by strong symbol |

## Usage

### Placement

Attributes attach before or after the declaration depending on what they annotate:

```cpp
// function attribute — before return type or after closing paren
__attribute__((noreturn)) void die(const char* msg);
void die(const char* msg) __attribute__((noreturn));

// C++11 gnu:: form
[[gnu::noreturn]] void die(const char* msg);

// struct attribute
struct __attribute__((packed)) Header { uint8_t a; uint32_t b; };

// variable alignment
int buf[64] __attribute__((aligned(16)));
```

### format attribute

```cpp
// M=2: format string is 2nd arg; N=3: variadic args start at 3rd
void log_error(int level, const char* fmt, ...)
    __attribute__((format(printf, 2, 3)));
```

### constructor / destructor priority

```cpp
__attribute__((constructor(101))) void early_init(void) { /* runs before main */ }
__attribute__((destructor(101)))  void early_fini(void) { /* runs after main */ }
```
Lower priority number = earlier constructor, later destructor.

### weak symbol override

```cpp
// library provides weak default
__attribute__((weak)) void on_error(void) { /* default no-op */ }

// application overrides with strong symbol — no linker conflict
void on_error(void) { abort(); }
```

## Portability

󰠗 How do you guard GCC/Clang attributes for portability? ;; Wrap in `#ifdef __GNUC__` — defined by both GCC and Clang

```cpp
#ifdef __GNUC__
#  define ATTR_NORETURN __attribute__((noreturn))
#  define ATTR_PRINTF(fmt, args) __attribute__((format(printf, fmt, args)))
#else
#  define ATTR_NORETURN
#  define ATTR_PRINTF(fmt, args)
#endif
```

### C++17/20 standard equivalents

| GCC attribute | Standard equivalent |
|---|---|
| `__attribute__((noreturn))` | `[[noreturn]]` (C++11) |
| `__attribute__((deprecated))` | `[[deprecated]]` / `[[deprecated("msg")]]` (C++14) |
| `__attribute__((nodiscard))` | `[[nodiscard]]` (C++17) |
| `__attribute__((maybe_unused))` | `[[maybe_unused]]` (C++17) |
| `__attribute__((likely))` / `((unlikely))` | `[[likely]]` / `[[unlikely]]` (C++20) |

Prefer standard attributes when available; fall back to `__attribute__` for attrs with no standard equivalent (`packed`, `visibility`, `constructor`, `section`, `weak`, `format`).

󰠗 What is the difference between `pure` and `const` attributes? ;; `pure` may read global state; `const` reads only its arguments — `const` is the stronger optimization hint
󰠗 What does `__attribute__((weak))` enable? ;; Weak linkage — another TU can define a strong symbol with the same name and the linker picks it without conflict; used for overridable defaults
