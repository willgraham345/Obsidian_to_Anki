---
type: note/concept
headings:
concept_of:
  - "[[Cpp Basics]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, March 18th 2026, 3:12:09 pm
tags: [lang/syntax]
template:
template-version:
used_by:
  - "[[Cpp Class]]"
---

# Summary
󰙎 assignment operator ;;; binds a value to a variable; foundational to all state mutation in C++

# Additional Background

## Syntax

Basic assignment:
```cpp
variable = value;
```

**Compound operators** — shorthand for `var = var OP expr`:

| Operator | Operation        |
| -------- | ---------------- |
| `+=`     | addition         |
| `-=`     | subtraction      |
| `*=`     | multiplication   |
| `/=`     | division         |
| `%=`     | modulus          |
| `&=`     | bitwise AND      |
| `\|=`    | bitwise OR       |
| `^=`     | bitwise XOR      |
| `<<=`    | left shift       |
| `>>=`    | right shift      |

## Concepts of Note

󰙎 copy assignment ;;; copies the resource from another object of the same type (`T& operator=(const T&)`)
󰙎 move assignment ;;; transfers ownership from a temporary/rvalue, leaving source in valid-but-unspecified state (`T& operator=(T&&)`)

## Examples

```cpp
int a = 10;
a += 5;   // a == 15
a >>= 1;  // a == 7

struct Foo {
    Foo& operator=(const Foo& other) = default; // copy
    Foo& operator=(Foo&& other) = default;       // move
};
```
