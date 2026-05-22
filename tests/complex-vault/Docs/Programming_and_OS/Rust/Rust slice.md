---
summary: A dynamically sized slice, which lets you reference contiguous sequences of elements in a collection rather than the whole collection.
headings:
  - "[[#Concepts of Note]]"
type: note/item
associations:
  - "[[Rust Array]]"
  - "[[Rust sizeof]]"
  - "[[Rust std iter]]"
  - "[[Rust usize]]"
item_of:
  - "[[Rust References and Pointers]]"
  - "[[Rust std]]"
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, June 19th 2025, 5:26:57 pm
processes:
  - "[[Rust type conversions]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
## Concepts of Note
Slices can only be handled through a type of pointer
  `s[0..n]` ;;; Slices from the 1st to the nth element. Slices have a n `i32` type.  = #lang/data/array/index_slice  
ID: 1751997628319



  `&[T]` ;;; Creates a shared slice that is dynamically sized = #lang/data/array/index_slice 
ID: 1751997628324



  `&mut[T]` ;;; Creates a mutable slice that is dynamically sized = #lang/data/array/index_slice  
ID: 1751997628328



  `Box<T>` ;;; Creates an owned slice stored on the heap. = #lang/data/array/index_slice 
ID: 1751997628332





### String Slices
```rust
let string_slice_ref = &string_var[starting_index..ending_index]
```
- `starting_index` is the first position in the slice

- `ending_index` is one more than the last position in the slice
- `[..]` is the whole string
- `0` is first element, `len` is the last element

#### Example
```rust
    let s = String::from("hello world");
    let hello = &s[0..5];
    let world = &s[6..11];

```

### String Slices as Parameters
```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` works on slices of `String`s, whether partial or whole
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` also works on references to `String`s, which are equivalent
    // to whole slices of `String`s
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` works on slices of string literals, whether partial or whole
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Because string literals *are* string slices already,
    // this works too, without the slice syntax!
    let word = first_word(my_string_literal);
}
```

#### Other Slices
```rust
let a = [1, 2, 3, 4, 5];

let slice = &a[1..3];

assert_eq!(slice, &[2, 3]);
```
- The slice has the type `&[i32]` and works the same way as string slices do, by storing a reference to the first element and a length. 
