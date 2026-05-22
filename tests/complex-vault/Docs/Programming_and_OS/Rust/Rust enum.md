---
summary: Rust's way of handling variants. Any variant which is valid as a `struct` is also valid in an `enum`. Notably, enums have an underlying type determined by the `[repr()]` compiler flag.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/concept
concept_of: ["[[Rust Items]]"]
date created: Wednesday, May 7th 2025, 2:01:53 pm
date modified: Wednesday, November 5th 2025, 4:40:16 pm
implementations: ["[[Rust Enum Generics]]"]
item_of: ["[[Rust Items]]"]
template:
template-version:
uses: ["[[Rust data layout]]", "[[Rust impl]]", "[[Rust match]]", "[[Rust trait]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Enums - Rust By Example](https://doc.rust-lang.org/rust-by-example/custom_types/enum.html)

## Concepts of Note
󰠗  What types can variants be in an enum? ;; Unit-like, tuple-struct like, or struct-like structures. = #lang/data/enumeration/variant #lang/data/enumeration   
  `enum E { A, B(), C{} }` ;;; Declares enum `E` with unit variant `A`, tuple-like variant `B`, and struct-like variant `C` = #lang/data/enumeration/variant  
<!--ID: 1758253288801-->

  `enum E { A=1 }` ;;; Declares enum `E` with variant `A`, with a set discriminant of 1. = #lang/data/enumeration/variant  
<!--ID: 1758253288805-->

  `E::C {x:y}` ;;; Creates an enum variant `C` with struct value `x` of type `y` away from typical enum definition block. = #lang/data/enumeration/variant  
<!--ID: 1758253288808-->

## Examples

```rust
// Create an `enum` to classify a web event. Note how both
// names and type information together specify the variant:
// `PageLoad != PageUnload` and `KeyPress(char) != Paste(String)`.
// Each is different and independent.
enum WebEvent {
    // An `enum` variant may either be `unit-like`,
    PageLoad,
    PageUnload,
    // like tuple structs,
    KeyPress(char),
    Paste(String),
    // or c-like structures.
    Click { x: i64, y: i64 },
}

// A function which takes a `WebEvent` enum as an argument and
// returns nothing.
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("page loaded"),
        WebEvent::PageUnload => println!("page unloaded"),
        // Destructure `c` from inside the `enum` variant.
        WebEvent::KeyPress(c) => println!("pressed '{}'.", c),
        WebEvent::Paste(s) => println!("pasted \"{}\".", s),
        // Destructure `Click` into `x` and `y`.
        WebEvent::Click { x, y } => {
            println!("clicked at x={}, y={}.", x, y);
        },
    }
}

fn main() {
    let pressed = WebEvent::KeyPress('x');
    // `to_owned()` creates an owned `String` from a string slice.
    let pasted  = WebEvent::Paste("my text".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let load    = WebEvent::PageLoad;
    let unload  = WebEvent::PageUnload;

    inspect(pressed);
    inspect(pasted);
    inspect(click);
    inspect(load);
    inspect(unload);
}

```
