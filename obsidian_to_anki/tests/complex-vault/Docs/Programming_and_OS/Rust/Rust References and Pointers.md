---
summary: Granting access to un-owned memory.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
type: note/concept
associations: 
concept_of:
  - "[[Rust]]"
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, July 31st 2025, 12:17:47 pm
item_of:
  - "[[Rust Variables and Type System]]"
items:
  - "[[Rust references]]"
  - "[[Rust slice]]"
  - "[[Rust.References.Dangling]]"
uses:
  - "[[Rust dereference operator]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

 - Rust will not create two mutable references to `s` will fail within the same scope.
	- Rust can prevent data races at compile time.
	- To get around this, you can use curly brackets to create a new scope, allowing for multiple mutable references (just not simultaneous ones)
- You also cannot have a mutable reference while we have an immutable one to the same value.
	- Users of an immutable reference doesn't expect the value to suddenly change out from under them. 
- A reference's scope starts from where it is introduced and continues through the last time that reference is used. 

## Usage
  `&[S]` ;;; Declare a reference to a slice of variable `S` = #lang/data/references 
<!--ID: 1758253288632-->

  `&mut S` ;;; Declare a mutable reference to variable `S` = #lang/data/references/mutable  
<!--ID: 1758253288638-->

󰠗  What is notable about the relationship between mutable references and scope? How can this be avoided? ;; Rust will not create two mutable references within the same scope. You can create a new scope (by using `{}`) to allow for multiple references. Importantly, these can't be simultaneous. = #lang/data/references/mutable 
<!--ID: 1758253288625-->

󰠗  Are shared references shallow or deep operations? ;; Shallow, as they only copy the value of the pointer itself.

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

## Examples
### Mutable Reference in a Function
```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s); //You can only create ONE mutable reference to a value
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

#### Creating Multiple Non-simultaneous Mutable References
```rust
    let mut s = String::from("hello");
    {
        let r1 = &mut s;
    } // r1 goes out of scope here, so we can make a new reference with no problems.
    let r2 = &mut s;
```
