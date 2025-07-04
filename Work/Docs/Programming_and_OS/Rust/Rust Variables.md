---
summary: Variables by default are immutable. Rust would like you to initialize and use each variable. Structs are data types and memory locations defined with keywords.
headings: ["[[#Concepts of Note]]", "[[#Types]]"]
type: note/concept
concepts: ["[[Rust never type]]", "[[Rust Variable Scope]]", "[[Rust vector]]"]
functions: ["[[Rust impl]]", "[[Rust Self]]"]
associations: ["[[Rust DataTypes]]", "[[Rust Scoping Rules]]"]
concept_of: ["[[Rust]]"]
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Tuesday, April 29th 2025, 4:37:16 pm
tags: [code/rust/data/array/instance, code/rust/data/array/slice, code/rust/data/array/type, code/rust/data/enum, code/rust/data/primitive/unit, code/rust/data/range/exclusive, code/rust/data/range/from, code/rust/data/range/full, code/rust/data/range/inclusive, code/rust/data/range/to, code/rust/data/range/to_inclusive, code/rust/data/struct, code/rust/data/struct/tuple_struct, code/rust/data/struct/unit, code/rust/data/tuple, code/rust/data/tuple/type, code/rust/definition/const, code/rust/definition/enum, code/rust/definition/enum/discriminant, code/rust/definition/enum/uninhabited, code/rust/definition/enum/variants, code/rust/definition/let, code/rust/definition/let/mutable, code/rust/definition/static, code/rust/definition/struct, code/rust/definition/struct/tuple, code/rust/definition/struct/unit, code/rust/definition/union, code/rust/syntax/assignment, code/rust/syntax/expression, code/rust/syntax/field_access/named, code/rust/syntax/field_access/tuple, code/rust/syntax/indexing, code/rust/syntax/indexing/range]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
### Variables
To fix unused variable earning, prepend the variable with an underscore
- I.e. `y: i32;` -> `_y: i32;`
Change a variable to mutable:
```rust
let mut x: i32 = 5;
x =+ 1;
```

### Shadowing variables 


### Types of Structs
There are 3 types of structures that can be created using the `struct` keyword
- Tuple structs (named tuples)
- Classic C structs
- Unit structs, which are field-less, are useful for generics

## Types
- [p] `S { x: y }` = Create `struct S {}` or `use`'d `enum E::S {}` with field `x` set to `y`. = #code/rust/data/struct  
<!--ID: 1751434090005-->

- [p] `S { x }` = Same, but use local variable `x` for field `x`. = #code/rust/data/struct  
<!--ID: 1751434090009-->

- [p] `S { ..s }` = Fill remaining fields from `s`, especially useful with `Default::default()`. = #code/rust/data/struct  
<!--ID: 1751434090014-->

- [p] `S { 0: x }` = Like `S(x)` below, but set field `.0` with struct syntax. = #code/rust/data/struct/tuple_struct  
<!--ID: 1751434090018-->

- [p] `S(x)` = Create `struct S(T)` or `use`'d `enum E::S()` with field `.0` set to `x`. = #code/rust/data/struct/tuple_struct  
<!--ID: 1751434090022-->

- [p] `S` = If `S` is unit `struct S;` or `use`'d `enum E::S`, create value of `S`. = #code/rust/data/struct/unit  
<!--ID: 1751434090026-->

- [p] `E::C { x: y }` = Create enum variant `C`. Other methods above also work. = #code/rust/data/enum  
<!--ID: 1751434090031-->

- [p] `()` = Empty tuple, both literal and type, aka **unit**. = #code/rust/data/primitive/unit  
<!--ID: 1751434090036-->

- [p] `(x)` = Parenthesized expression. = #code/rust/syntax/expression  
<!--ID: 1751434090040-->

- [p] `(x,)` = Single-element **tuple** expression. = #code/rust/data/tuple  
<!--ID: 1751434090044-->

- [p] `(S,)` = Single-element tuple type. = #code/rust/data/tuple/type  
<!--ID: 1751434090048-->

- [p] `[S]` = Array type of unspecified length, i.e., **slice**. Can't live on stack. = #code/rust/data/array/slice  
<!--ID: 1751434090052-->

- [p] `[S; n]` = **Array type** of fixed length `n` holding elements of type `S`. = #code/rust/data/array/type  
<!--ID: 1751434090059-->

- [p] `[x; n]` = **Array instance** (expression) with `n` copies of `x`. = #code/rust/data/array/instance  
<!--ID: 1751434090063-->

- [p] `[x, y]` = Array instance with given elements `x` and `y`. = #code/rust/data/array/instance  
<!--ID: 1751434090066-->

- [p] `x[0]` = Collection indexing, here with `usize`. Implemented via `Index`, `IndexMut`. = #code/rust/syntax/indexing  
<!--ID: 1751434090070-->

- [p] `x[..]` = Same, via range (here _full range_), also `x[a..b]`, `x[a..=b]`, etc. = #code/rust/syntax/indexing/range  
<!--ID: 1751434090077-->

- [p] `a..b` = **Right-exclusive range** creation, e.g., `1..3` means `1, 2`. = #code/rust/data/range/exclusive  
<!--ID: 1751434090083-->

- [p] `..b` = Right-exclusive **range to** without starting point. = #code/rust/data/range/to  
<!--ID: 1751434090088-->

- [p] `..=b` = **Inclusive range to** without starting point. = #code/rust/data/range/to_inclusive  
<!--ID: 1751434090092-->

- [p] `a..=b` = **Inclusive range**, e.g., `1..=3` means `1, 2, 3`. = #code/rust/data/range/inclusive  
<!--ID: 1751434090096-->

- [p] `a..` = **Range from** without ending point. = #code/rust/data/range/from  
<!--ID: 1751434090100-->

- [p] `..` = **Full range**, usually means _the whole collection_. = #code/rust/data/range/full  
<!--ID: 1751434090103-->

- [p] `s.x` = Named **field access**, might try to `Deref` if `x` not part of type `S`. = #code/rust/syntax/field_access/named  
<!--ID: 1751434090107-->

- [p] `s.0` = Numbered field access, used for tuple types `S(T)`. = #code/rust/syntax/field_access/tuple  
<!--ID: 1751434090111-->


- [p] `struct S {}` = Define a **struct** with named fields. = #code/rust/definition/struct
<!--ID: 1751434090116-->

- [p] `struct S { x: T }` = Define struct with named field `x` of type `T`. = #code/rust/definition/struct
<!--ID: 1751434090120-->

- [p] `struct S(T);` = Define "tupled" struct with numbered field `.0` of type `T`. = #code/rust/definition/struct/tuple
<!--ID: 1751434090125-->

- [p] `struct S;` = Define **zero-sized** unit struct. Occupies no space, optimized away. = #code/rust/definition/struct/unit
<!--ID: 1751434090129-->

- [p] `enum E {}` = Define an **enum**. = #code/rust/definition/enum
<!--ID: 1751434090133-->

- [p] `enum E { A, B(), C {} }` = Define variants of enum; unit-`A`, tuple-`B()`, and struct-like `C{}`. = #code/rust/definition/enum/variants
<!--ID: 1751434090137-->

- [p] `enum E { A = 1 }` = Enum with **discriminant values**, useful for FFI. = #code/rust/definition/enum/discriminant
<!--ID: 1751434090141-->

- [p] `enum E {}` = Enum with no variants is **uninhabited**, can't be instantiated. = #code/rust/definition/enum/uninhabited
<!--ID: 1751434382632-->

- [p] `union U {}` = Define an unsafe **union** for FFI compatibility. = #code/rust/definition/union = unsa
<!--ID: 1751434090147-->

- [p] `static X: T = T();` = Define a **global static variable** with `'static` lifetime. = #code/rust/definition/static
<!--ID: 1751434090151-->

- [p] `const X: T = T();` = Define a **constant**, copied into a temporary when used. = #code/rust/definition/const
<!--ID: 1751434090155-->

- [p] `let x: T;` = Allocate `T` on stack, bound to `x`, immutable by default. = #code/rust/definition/let
<!--ID: 1751434090159-->

- [p] `let mut x: T;` = Like `let`, but mutable. = #code/rust/definition/let/mutable
<!--ID: 1751434090163-->

- [p] `x = y;` = Move `y` into `x`; invalidates `y` if not `Copy`, otherwise copies. = #code/rust/syntax/assignment
<!--ID: 1751434090167-->

