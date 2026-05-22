---
summary: Think of this as a function which generates a different version of itself, for every data type that uses it. Used for implementing generic algorithms (vectors, stacks, queues), and for efficiency. Keep in mind, you can pass functions as types in the object.<br><br>Templates form the basis for the standard library with [[Cpp std vector]], [[Cpp std map (class)]], and [[Cpp std set]].<br>Templates are expanded at compiler time, similar to macros. The compiler does type-checking before template expansion.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Media]]"
  - "[[#Usage]]"
similar:
  - "[[Cpp Class Constructors]]"
  - "[[Cpp macros]]"
associations:
  - "[[Cpp Class Constructors]]"
  - "[[Cpp functions]]"
  - "[[Cpp typename]]"
concept_of:
  - "[[Cpp Class]]"
  - "[[Cpp Variables and Containers]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, April 2nd 2026, 4:12:19 pm
tags: [lang, lang/meta/typing, lang/oop/templates]
template:
template-version:
used_by:
  - "[[Cpp std metaprogramming]]"
  - "[[Cpp Variables and Containers]]"
  - "[[DP Testing Dependency Injection#Template injection]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- A template is a tool that can pass data type as a parameter so that we don't need to write the same code for different data types. 
	- Sorting `int` and `char`

## Concepts of Note
󰙎  Variadic template ;;; Template that can accept zero or more template arguments, potentially of different types

󰙎  Dependent name ;;; A name whose meaning depends on a template parameter — unresolvable at definition time, only at instantiation. Requires [[Cpp typename]] for types, or the `template` keyword for member template calls.

󰙎  `template` disambiguator ;;; Keyword placed before a member template name accessed through a dependent expression. Tells the parser that `<` begins a template argument list, not less-than.

## Usage

  `template <typename... T> entity_definition` ;;; Declare variadic template, which can accept zero or more template arguments of potentially different types `T`. `T` acts as a list of types (it is a parameter pack). `entity_definition` can be a `class` definition, function, or whatever else. Very useful for dependency injection 

 `template <typename T, std::uint16_t a>`
      `class factory<T, a>` ;;; Declare a class class template `factory`, which uses generic class `T` and a `uint16_t` class `a`

 `template <typename T1 = double> class Nerd{ //classdef }` ;;; Declare a templated class which uses `T1` which defaults to being a `double` argument. The class is `Nerd`.

### `this->template` — Dependent Member Template Calls

When calling a member template through a **dependent name**, the parser can't tell whether `<` begins a template argument list or is less-than. The `template` keyword disambiguates.

```cpp
template <typename T>
struct Base {
    template <typename U> void foo() {}
};

template <typename T>
struct Derived : Base<T> {
    void bar() {
        this->template foo<int>();       // 'this' is dependent
        Base<T>::template foo<double>(); // Base<T> is dependent
    }
};
```

 `this->template foo<T>()` ;;; Call member template `foo` on `this` from within a class template. Without `template`, `<` is parsed as less-than — compile error.

 `Base<T>::template bar<U>()` ;;; Call member template through a dependent base. Pair with [[Cpp typename]] when also extracting nested types from the same base.

 `obj.template baz<T>()` ;;; Call member template on `obj` whose type depends on a template parameter.

󰠗 Why does `this->foo<int>()` fail inside a class template? ;; `this` is dependent, so `foo` is a dependent name. Without `template`, `<` parses as less-than. Fix: `this->template foo<int>()`.

󰠗 `template` vs `typename` as disambiguator? ;; `typename` — dependent **type** (`typename Base<T>::value_type`). `template` — dependent **member template call** (`this->template foo<int>()`). Both can appear together: `typename Base<T>::template inner<U>`.

## Media
[More here](https://www.geeksforgeeks.org/templates-cpp/)
 
