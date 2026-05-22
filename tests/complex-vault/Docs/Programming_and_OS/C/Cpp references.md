---
summary: References are an alias for an already existing variable. Implemented by storing the address of an object. Can be thought of as a constant pointer (not necessarily pointing to a constant value) with automatic indirection. The automatic indirection means the compiler will apply the * for you.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
  - "[[#Flashcards]]"
implements:
  - "[[Cpp functions]]"
similar:
  - "[[Cpp pointers]]"
  - "[[Cpp value categories]]"
associations:
  - "[[Cpp Pointers]]"
  - "[[Cpp value categories]]"
concept_of:
date created: Thursday, January 16th 2025, 4:34:38 pm
date modified: Wednesday, March 18th 2026, 1:03:50 pm
item_of:
  - "[[Cpp Memory]]"
keywords:
  - "[[Cpp &]]"
processes:
tags: []
template:
template-version:
used_by:
  - "[[Cpp Memory]]"
  - "[[Cpp Variables and Containers]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

See [[Cpp value categories]] for the full value category taxonomy (lvalue, prvalue, xvalue, glvalue).


󰙎 lvalue reference (`T&`) ;;; alias to a named, addressable object (an lvalue); must be initialized at declaration; cannot be rebound
󰙎 rvalue reference (`T&&`) ;;; binds exclusively to temporaries and expiring values (rvalues); enables move semantics by signalling ownership can be transferred
󰙎 const reference (`const T&`) ;;; read-only alias that can bind to *both* lvalues and rvalues; extends a temporary's lifetime to the reference's scope; idiomatic for large function params to avoid copying
󰙎 universal reference (`T&&` in deduced context) ;;; when `T` is a deduced template parameter, `T&&` can bind to either an lvalue or rvalue — also called a forwarding reference

### lvalue vs rvalue — what can each reference bind to?

| Reference type | Binds to lvalue | Binds to rvalue/temporary |
|---|---|---|
| `T&` | yes | **no** |
| `const T&` | yes | yes (lifetime extended) |
| `T&&` | **no** | yes |
| `T&&` (forwarding ref) | yes (deduced as `T&`) | yes (deduced as `T`) |

```cpp
int a = 10;           // a is an lvalue

int& lref = a;        // OK — lvalue ref binds to lvalue
int& bad  = 42;       // ERROR — cannot bind lvalue ref to rvalue

int&& rref = 20;      // OK — rvalue ref binds to temporary
int&& bad2 = a;       // ERROR — cannot bind rvalue ref to named lvalue

const int& cref = 42; // OK — const ref extends lifetime of temporary
```

### How are they different from pointers?
- Cannot be reassigned.
- Typically cleaner, since the compiler will do the dereferencing for you
- You can use the dot operator with references, rather than the pointer arrow (->)

![[Cpp functions#Pointers and References in Functions]]

### `*` and `&` as _type modifiers_

- `int i` declares an int.
- `int* p` declares a pointer to an int.
- `int& r = i` declares a reference to an int, and initializes it to refer to `i`.
    C++ only. Note that references must be assigned at initialization, therefore `int& r;` is not possible.

Similarly:

- `void foo(int i)` declares a function taking an int (by value, i.e. as a copy).
- `void foo(int* p)` declares a function taking a pointer to an int.
- `void foo(int& r)` declares a function taking an int by reference. (C++ only)

### `*` and `&` as _operators_

- `foo(i)` calls `foo(int)`. The parameter is passed as a copy.
- `foo(*p)` dereferences the int pointer `p` and calls `foo(int)` with the int pointed to by `p`.
- `foo(&i)` takes the address of the int `i` and calls `foo(int*)` with that address.

## Usage
References are initialized when:
1. Naming an [[Cpp value categories]] declared with an initializer
2. When a named [[Cpp rvalue]] variable is declared with an initializer
3. In a function call expression, when the function parameter has reference type
4. In the return statement, when the function returns a reference type.

### LValue
**Correct**:
```cpp
int a = 10;
int &p = a; // Correct
```

**Incorrect**:
```cpp
int &p;
p = a; // Incorrect, since we should declare AND initialize in the same step
```

### Parameter in Function (Pass by reference)

```cpp
void modifyStr(string &str) {
  str += " World!";
}

int main() {
  string greeting = "Hello";
  modifyStr(greeting);
  cout << greeting;
  return 0;
}
```

### Reference Return
It's okay to do this if the lifetime of the object won't end after the call.

A reference *T* can be initialized with an object of type *T*, a function of type *T*, or an object implicitly convertible to *T*. Once initialized, a reference cannot be changed to refer to another object.

## Flashcards

󰠗 Key difference between a reference and a pointer? ;; A reference cannot be null, cannot be rebound, and dereferences automatically — a pointer can be reassigned, can be null, requires explicit `*`/`->`
󰠗 When to prefer a reference over a pointer? ;; When the referent is guaranteed non-null and rebinding is never needed; use a pointer only when null or reassignment is required
󰠗 Can `const T&` bind to an rvalue or temporary? ;; Yes — `const T&` extends the temporary's lifetime to the reference's scope; a non-const `T&` cannot bind to an rvalue
󰠗 What is a dangling reference? ;; A reference whose referent has been destroyed (e.g., returning a ref to a local variable) — undefined behavior on access
󰠗 What is a forwarding/universal reference? ;; `T&&` where `T` is a deduced template parameter — collapses to `T&` for lvalues and `T&&` for rvalues, enabling perfect forwarding
󰠗 What is the difference between `T&&` as an rvalue ref vs a forwarding ref? ;; If `T` is explicitly specified (e.g. `int&&`), it's an rvalue ref; if `T` is deduced (template or `auto&&`), it's a forwarding ref that binds to anything
