---
summary: Variables by default are immutable. Rust would like you to initialize and use each variable. Structs are data types and memory locations defined with keywords.
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/concept
functions:
  - "[[Rust impl]]"
  - "[[Rust Self]]"
classes:
  - "[[Rust std String]]"
concepts:
  - "[[Rust Dynamically Sized Types]]"
  - "[[Rust Integer Overflow]]"
  - "[[Rust Variable Scope]]"
processes:
  - "[[Rust type conversions]]"
associations:
  - "[[Rust Scoping Rules]]"
concept_of:
  - "[[Rust]]"
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Saturday, November 8th 2025, 12:33:48 pm
items:
  - "[[Rust Array]]"
  - "[[Rust char]]"
  - "[[Rust closures]]"
  - "[[Rust function pointers]]"
  - "[[Rust Functions]]"
  - "[[Rust never type]]"
  - "[[Rust References and Pointers]]"
  - "[[Rust slice]]"
  - "[[Rust str]]"
  - "[[Rust trait]]"
  - "[[Rust Tuples]]"
  - "[[Rust Vec]]"
keywords:
  - "[[Rust constant items]]"
  - "[[Rust let]]"
  - "[[Rust mut]]"
tags: []
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
󰠗  There are 6 groupings of types in rust. What are they? ;; Primitive types (`bool`, `i32`, `char`, `str`, `!`), Sequence types (tuple, array, slice), User-defined (`struct`, `enum`, union), function types (`fn`, closures), pointer types (references, raw pointers, function pointers), and trait types (trait objects, impl trait)
󰙎  Shadowing variables ;;; When an inner variable has the same name as an "outer" variable. Any reference to the "inner" variable only references the "inner" variable. = #lang/data  
<!--ID: 1758253288190-->

## Breadcrumbs %% fold %% 
```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
depth: [0, 2]
show-attributes: [field]
```

## Usage
  `S { x: y }` ;;; Create `struct S {}` with field `x` set to `y`. = #lang/oop/struct   
ID: 1751997627868



  `S { x }` ;;; Create `struct S {}`, using local variable `x` for field `x`. = #lang/oop/struct   
ID: 1751997627873



  `S { ..s }` ;;; Fill remaining fields in a strict from `s`, especially useful with `Default::default()`. = #lang/oop/struct   
ID: 1751997627877



  `S { 0: x }` ;;; Create `struct S(T)`, but set field `.0` to `x` with struct syntax. = #lang/oop/struct/tuple_struct   
ID: 1751997627881



  `S(x)` ;;; Create `struct S(T)` with field `.0` set to local variable `x`. = #lang/oop/struct/tuple_struct   
ID: 1751997627886



  `E::C { x: y }` ;;; Create enum variant `C`. Other methods above als work. = #lang/data/enumeration   
ID: 1751997627895



  `()` ;;; Empty tuple, both literal and type, aka **unit**. = #lang/data/tuple   
ID: 1751997627899



  `(x)` ;;; Parenthesized expression. = #lang/syntax/expression   
ID: 1751997627904



  `(x,)` ;;; Single-element **tuple** expression. = #lang/data/tuple   
ID: 1751997627909



  `(S,)` ;;; Single-element tuple type. = #lang/data/tuple
ID: 1751997627913



  `[S]` ;;; Array type of unspecified length, i.e., **slice**. Can't live on stack. = #lang/data/array/index_slice   
ID: 1751997627917



  `[S; n]` ;;; **Array type** of fixed length `n` holding elements of type `S`. = #lang/data/array/type   
ID: 1751997627922



  `[x; n]` ;;; **Array instance** (expression) with `n` copies of `x`. = #lang/data/array
ID: 1751997627926



  `[x, y]` ;;; Array instance with given elements `x` and `y`. = #lang/data/array
ID: 1751997627930



  `x[0]` ;;; Collection indexing, here with `usize`. Implemented via `Index`, `IndexMut`. = #lang/syntax/indexing   
ID: 1751997627935



  `x[..]` ;;; Same, via range (here _full range_), also `x[a..b]`, `x[a..=b]`, etc. = #lang/syntax/indexing/range   
ID: 1751997627939



  `a..b` ;;; **Right-exclusive range** creation, e.g., `1..3` means `1, 2`. = #lang/data/range/exclusive   
ID: 1751997627944



  `..b` ;;; Right-exclusive **range to** without starting point. = #lang/data/range/to   
ID: 1751997627949



  `..=b` ;;; **Inclusive range to** without starting point. = #lang/data/range/to_inclusive   
ID: 1751997627954



  `a..=b` ;;; **Inclusive range**, e.g., `1..=3` means `1, 2, 3`. = #lang/data/range/inclusive   
ID: 1751997627959



  `a..` ;;; **Range from** without ending point. = #lang/data/range/from   
ID: 1751997627963



  `..` ;;; **Full range**, usually means _the whole collection_. = #lang/data/range/full   
ID: 1751997627967



  `s.x` ;;; Named **field access**, might try to `Deref` if `x` not part of type `S`. = #lang/syntax/field_access/named   
ID: 1751997627972



  `s.0` ;;; Numbered field access, used for tuple types `S(T)`. = #lang/syntax/field_access/tuple   
ID: 1751997627977




  `struct S {}` ;;; Define a **struct** with named fields. = #lang/oop/struct 
ID: 1751997627981



  `struct S { x: T }` ;;; Define struct with named field `x` of type `T`. = #lang/oop/struct 
ID: 1751997627987



  `struct S(T);` ;;; Define "tupled" struct with numbered field `.0` of type `T`. = #lang/oop/struct/tuple 
ID: 1751997627991



  `struct S;` ;;; Define **zero-sized** unit struct. Occupies no space, optimized away. = #lang/oop/struct/unit 
ID: 1751997627995



  `enum E {}` ;;; Define an **enum**. = #lang/data/enumeration 
ID: 1751997628000



  `enum E { A, B(), C {} }` ;;; Define variants of enum; unit-`A`, tuple-`B()`, and struct-like `C{}`. = #lang/data/enumeration/variant 
ID: 1751997628005



  `enum E { A ``=`` 1 }` ;;; Enum with **discriminant values**, useful for FFI. = #lang/data/enumeration/discriminant 
ID: 1751997628009



  `enum E {}` ;;; Enum with no variants is **uninhabited**, can't be instantiated. = #lang/data/enumeration/uninhabited 


  `union U {}` ;;; Define an unsafe **union** for FFI compatibility. = #lang/data/union = unsa 
ID: 1751997628015



  `static X: T ``=`` T();` ;;; Define a **global static variable** with `'static` lifetime. = #lang/data/static 
ID: 1751997628020



  `const X: T ``=`` T();` ;;; Define a **constant**, copied into a temporary when used. = #lang/data/const 
ID: 1751997628024



  `let x: T;` ;;; Allocate `T` on stack, bound to `x`, immutable by default. = #lang/memory/stack 
ID: 1751997628028



  `let mut x: T;` ;;; Like `let`, but mutable. = #lang/data/mutable 
ID: 1751997628032



  `x ``=`` y;` ;;; Move `y` into `x`; invalidates `y` if not `Copy`, otherwise copies. = #lang/syntax/assignment 
ID: 1751997628037



