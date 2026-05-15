---
summary: "C++11 keyword that instructs the compiler to deduce a variable's type from its initializer expression; replaces the old C89 storage-class meaning of auto."
type: note/keyword
similar:
  - "[[Cpp.Variables.Primitive Data Types]]"
date created: Monday, March 23rd 2026, 12:00:00 pm
date modified: Monday, March 23rd 2026, 12:00:00 pm
tags:
  - programming/cpp
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] type deduction ;;; Compiler infers the variable's type from its initializer; the variable is still strongly typed — type is fixed at compile time, not runtime
- [I] `auto` copies ;;; Plain `auto` always copies; use `auto&` for mutable references or `const auto&` to avoid copying non-trivial types
- [I] trailing return type ;;; C++11 syntax `auto f() -> T` — return type appears after `->`, enabling it to reference parameter names or use `decltype`
- [I] return type deduction ;;; C++14: compiler deduces return type from the `return` expression; all return paths must deduce to the same type
- [I] generic lambda ;;; C++14: `[](auto x)` makes the lambda templated — `x` is deduced independently at each call site

## Syntax
- [p] `auto x = expr;` ;;; deduce type from `expr` — must have an initializer
- [p] `auto& x = expr;` ;;; deduce reference type; `expr` must be an lvalue
- [p] `const auto& x = expr;` ;;; deduce const reference — zero-copy, safe to bind to temporaries
- [p] `auto f() -> ReturnType { }` ;;; trailing return type (C++11)
- [p] `auto f() { return expr; }` ;;; return type deduction (C++14); all returns must agree

## Usage
### Variable Declarations
- [p] `auto i = 42;` ;;; deduces `int`
- [p] `auto d = 3.14;` ;;; deduces `double`
- [p] `auto s = std::string{"hello"};` ;;; deduces `std::string` — **not** `auto s = "hello"` which gives `const char*`
- [p] `auto p = std::make_unique<int>(5);` ;;; deduces `std::unique_ptr<int>`

### Iterators
- [p] `auto it = vec.begin();` ;;; replaces verbose `std::vector<int>::iterator it = vec.begin()`
- [p] `auto it = m.find(key);` ;;; type is `std::map<K,V>::iterator`

### Range-Based For
- [p] `for (auto x : v)` ;;; copy each element — fine for primitives, expensive for large objects
- [p] `for (auto& x : v)` ;;; mutable reference — modify elements in-place
- [p] `for (const auto& x : v)` ;;; const reference — preferred for read-only iteration over non-trivial types

### Lambdas
- [p] `auto f = [](int x) { return x * 2; };` ;;; `f`'s type is a compiler-generated closure type; only `auto` can hold it without `std::function`
- [p] `auto f = [](auto x) { return x * 2; };` ;;; generic lambda (C++14) — deduces `x` per call site

### Trailing Return Type
- [p] `auto add(int a, int b) -> int { return a + b; }` ;;; C++11 — equivalent to `int add(int a, int b)`; useful for readability in complex signatures
- [p] `template<class T, class U> auto add(T a, U b) -> decltype(a + b) { return a + b; }` ;;; C++11 template — return type depends on parameter types via `decltype`

## Flashcards
- [t] What does `auto s = "hello";` deduce? ;; `const char*`, not `std::string` — use `auto s = std::string{"hello"}` for a string object
- [t] When was function return type deduction introduced? ;; C++14 — C++11 requires a trailing `-> ReturnType`
- [t] Why use `const auto&` in a range-for loop? ;; Avoids copying the element while preventing accidental mutation
