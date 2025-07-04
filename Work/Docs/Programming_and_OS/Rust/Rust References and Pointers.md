---
summary: Granting access to un-owned memory.
type: note/concept
components:
  - "[[Rust slice]]"
associations:
  - "[[Rust Generics]]"
concept_of:
  - "[[Rust]]"
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Monday, March 31st 2025, 11:58:49 am
---
### References & Pointers

Granting access to un-owned memory. Also see section on Generics & Constraints.

|Example|Explanation|
|---|---|
|`&S`|Shared **reference** [BK](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html "See this topic in 'The Rust Programming Language'.") [STD](https://doc.rust-lang.org/std/primitive.reference.html "See this topic in 'The Rust Standard Library'.") [NOM](https://doc.rust-lang.org/nightly/nomicon/references.html "See this topic in 'The Rustonomicon'.") [REF](https://doc.rust-lang.org/stable/reference/types.html#pointer-types "See this topic in 'The Rust Reference'.") (type; space for holding _any_ `&s`).|
|`&[S]`|Special slice reference that contains (`address`, `count`).|
|`&str`|Special string slice reference that contains (`address`, `byte_length`).|
|`&mut S`|Exclusive reference to allow mutability (also `&mut [S]`, `&mut dyn S`, …).|
|`&dyn T`|Special **trait object** [BK](https://doc.rust-lang.org/book/ch17-02-trait-objects.html#using-trait-objects-that-allow-for-values-of-different-types "See this topic in 'The Rust Programming Language'.") reference that contains (`address`, `vtable`).|
|`&s`|Shared **borrow** [BK](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html "See this topic in 'The Rust Programming Language'.") [EX](https://doc.rust-lang.org/stable/rust-by-example/scope/borrow.html "See this topic in 'Rust by Example'.") [STD](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "See this topic in 'The Rust Standard Library'.") (e.g., addr., len, vtable, … of _this_ `s`, like `0x1234`).|
|`&mut s`|Exclusive borrow that allows **mutability**. [EX](https://doc.rust-lang.org/stable/rust-by-example/scope/borrow/mut.html "See this topic in 'Rust by Example'.")|
|`*const S`|Immutable **raw pointer type** [BK](https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html#dereferencing-a-raw-pointer "See this topic in 'The Rust Programming Language'.") [STD](https://doc.rust-lang.org/std/primitive.pointer.html "See this topic in 'The Rust Standard Library'.") [REF](https://doc.rust-lang.org/stable/reference/types.html#raw-pointers-const-and-mut "See this topic in 'The Rust Reference'.") w/o memory safety.|
|`*mut S`|Mutable raw pointer type w/o memory safety.|
|`&raw const s`|Create raw pointer w/o going through ref.; _c_. `ptr:addr_of!()` [STD](https://doc.rust-lang.org/std/ptr/macro.addr_of.html "See this topic in 'The Rust Standard Library'.") 🚧 🝖|
|`&raw mut s`|Same, but mutable. 🚧 Needed for unaligned, packed fields. 🝖|
|`ref s`|**Bind by reference**, [EX](https://doc.rust-lang.org/stable/rust-by-example/scope/borrow/ref.html "See this topic in 'Rust by Example'.") makes binding reference type. 🗑️|
|`let ref r = s;`|Equivalent to `let r = &s`.|
|`let S { ref mut x } = s;`|Mut. ref binding (`let x = &mut s.x`), shorthand destructuring [↓](https://cheats.rs/#pattern-matching "On this site, below.") version.|
|`*r`|**Dereference** [BK](https://doc.rust-lang.org/book/ch15-02-deref.html "See this topic in 'The Rust Programming Language'.") [STD](https://doc.rust-lang.org/std/ops/trait.Deref.html "See this topic in 'The Rust Standard Library'.") [NOM](https://doc.rust-lang.org/nightly/nomicon/vec-deref.html "See this topic in 'The Rustonomicon'.") a reference `r` to access what it points to.|
|`*r = s;`|If `r` is a mutable reference, move or copy `s` to target memory.|
|`s = *r;`|Make `s` a copy of whatever `r` references, if that is `Copy`.|
|`s = *r;`|Won't work 🛑 if `*r` is not `Copy`, as that would move and leave empty.|
|`s = *my_box;`|Special case[🔗](https://old.reddit.com/r/rust/comments/b4so6i/what_is_exactly/ej8xwg8 "Third-party site (mainly used in conjunction with other symbols).") for **`Box`**[STD](https://doc.rust-lang.org/std/boxed/index.html "See this topic in 'The Rust Standard Library'.") that can move out b'ed content not `Copy`.|
|`'a`|A **lifetime parameter**, [BK](https://doc.rust-lang.org/book/ch10-00-generics.html "See this topic in 'The Rust Programming Language'.") [EX](https://doc.rust-lang.org/stable/rust-by-example/scope/lifetime.html "See this topic in 'Rust by Example'.") [NOM](https://doc.rust-lang.org/nightly/nomicon/lifetimes.html "See this topic in 'The Rustonomicon'.") [REF](https://doc.rust-lang.org/stable/reference/items/generics.html#type-and-lifetime-parameters "See this topic in 'The Rust Reference'.") duration of a flow in static analysis.|
|`&'a S`|Only accepts address of some `s`; address existing `'a` or longer.|
|`&'a mut S`|Same, but allow address content to be changed.|
|`struct S<'a> {}`|Signals this `S` will contain address with lt. `'a`. Creator of `S` decides `'a`.|
|`trait T<'a> {}`|Signals any `S`, which `impl T for S`, might contain address.|
|`fn f<'a>(t: &'a T)`|Signals this function handles some address. Caller decides `'a`.|
|`'static`|Special lifetime lasting the entire program execution.|
