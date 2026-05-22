---
summary:
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Flashcards]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
implements:
  - "[[Cpp functions]]"
similar:
  - "[[Cpp references]]"
  - "[[Cpp std memory shared_ptr|Cpp shared_ptr]]"
  - "[[Cpp std memory unique_ptr|Cpp unique_ptr]]"
  - "[[Cpp std memory weak_ptr|Cpp weak_ptr]]"
associations:
  - "[[Cpp references]]"
  - "[[Cpp std array]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, April 13th 2026, 12:45:50 pm
implementations:
  - "[[Cpp const]]"
item_of:
  - "[[Cpp Memory]]"
  - "[[Cpp std array]]"
items:
  - "[[Cpp std memory shared_ptr]]"
  - "[[Cpp std memory unique_ptr]]"
  - "[[Cpp std memory weak_ptr]]"
processes:
  - "[[Cpp function array arguments]]"
tags: []
template:
template-version:
used_by:
  - "[[Cpp Memory]]"
uses:
  - "[[CS Dynamic dispatch|CS Virtual dispatch]]"
---

# Summary
󰙎 pointers ;;; A variable that "points" to a location in memory. Hugely useful, as they often require much less memory than the data they point towards. Used extensively within arrays and functions. Notably, for use within functions, they can be a nullpointer signifying that they do not point to a valid location in memory. This can't be performed with references.

# Additional Background

## Concepts of Note

󰙎 pointer ;;; (`T*`) variable storing a memory address of type `T`; declared as `T* p;`
󰙎 reference ;;; (`T&`) variable storing a reference (non-reassignable, non-nullable)
󰙎 address-of (`&`) ;;; unary operator returning the address of a variable; `int* p = &x;`. This is how you'd pass a pointer into a function expecting a pointer.
󰙎 dereference (`*`) ;;; unary operator accessing the value at a pointer's address; `int val = *p;`
󰙎 nullptr ;;; C++11 keyword for a null pointer constant; safer than `NULL` or `0`; signals pointer holds no valid address
󰙎 pointer arithmetic ;;; incrementing a pointer advances it by `sizeof(T)` bytes, not by 1
󰙎 pointer to const (`const T*`) ;;; pointer is mutable; pointed-to value is immutable — `*p` cannot be assigned
󰙎 const pointer (`T* const`) ;;; pointer address is immutable; pointed-to value is mutable — `p` cannot be reassigned

- Arrays are contiguous locations in memory, so C-style pointers pass an array pointer with the length in order to resolve this challenge

![[Cpp functions#Pointers and References in Functions]]

### Double Pointers (`T**`)
󰙎 double pointer ;;; a pointer whose value is the address of another pointer; i.e. `T**` points to a `T*`

Classic use: `int main(int argc, char** argv)` — `argv` is an array of C strings. Each element is a `char*` (pointer to the first char of a string); `char**` points to the first element of that array. `char* argv[]` is equivalent syntax in a function parameter context.

```
argv ──► [ argv[0] ]──► "program\0"
         [ argv[1] ]──► "--flag\0"
         [ argv[2] ]──► "value\0"
         [ NULL    ]
```

### Smart Pointers
RAII wrappers in `<memory>` that manage lifetime automatically. Prefer over raw `new`/`delete`.
󰙎 unique_ptr ;;; sole ownership — non-copyable, movable; destroyed when out of scope → [[Cpp std memory unique_ptr]]
󰙎 shared_ptr ;;; shared ownership via reference count; destroyed when the last owner releases → [[Cpp std memory shared_ptr]]
󰙎 weak_ptr ;;; non-owning observer of a `shared_ptr`; used to break reference cycles → [[Cpp std memory weak_ptr]]

## Syntax

```cpp
int x = 42;

int* p = &x;       // declare pointer, init with address-of
int val = *p;      // dereference — val == 42
*p = 99;           // write through pointer — x is now 99

int* q = nullptr;  // null pointer
if (q != nullptr) { // always check before deref
    *q;
}

const int* pc = &x;  // pointer to const — *pc = 1 is illegal
int* const cp = &x;  // const pointer   — cp = &y is illegal
```

## Usage
- [[Cpp const]]
- [[Cpp function array arguments]]
- [[Cpp function pointers and references]]

## Flashcards

󰠗 What is the key difference between a pointer and a reference? ;; A pointer can be null (`nullptr`) and reassigned; a reference must be bound at declaration and is never null
󰠗 What does `const int* p` vs `int* const p` mean? ;; `const int*` — pointed-to value is immutable; `int* const` — pointer address is immutable
󰠗 What does `char** argv` mean in `main`? ;; A pointer to the first element of an array of `char*`; each `char*` is a null-terminated C string
󰠗 Why use `nullptr` instead of `0` or `NULL`? ;; `nullptr` is type-safe (`std::nullptr_t`); `0`/`NULL` can silently convert to `int`, causing ambiguous overload resolution
