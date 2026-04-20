---
summary: Debug is an automatically derivable trait, intended to output developer-friendly info about an instance. Typically shows type internals, and can automatically be implemented with `#[derive(Debug)]
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Properties]]", "[[#Usage]]"]
type: note/interface
methods: ["[[#fmt()]]"]
similar: ["[[Rust Display]]"]
associations: ["[[Rust derive attribute macros]]"]
date created: Wednesday, May 21st 2025, 5:43:59 pm
date modified: Thursday, November 20th 2025, 10:21:18 am
item_of: ["[[Rust std fmt]]"]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
  `println!("{0:?}", structVal)` ;;; Debug the `structVal` using `std::fmt::Debug`, which is an attribute coming with standard library = #lang/meta/attributes/debug  = `"{:#?}"` to enable pretty-printing 
ID: 1751997628495




  `impl fmt::Debug for A { ... }` ;;; Manually write the debug implementation for struct `A`. Importantly, the `fn fmt(& self, f: &mut fmt::Formatter) -> fmt::Result { ... }` is likely expected. = #lang/meta/attributes/debug 
ID: 1751997628499
 ^acdb68


- The `Debug` trait can be accessed by using the `{:?}` (or `:#?`) format specifier. 

## Properties
### Methods
#### fmt()
## Usage
### Automatically generate with attributes
- [p] `#[derive(Debug)]`
      `struct myStruct` = Let rust automatically generate an `impl` for `<Debug>`. Allows you to use the `{:#?}` in printing/debugging = #lang/meta/attributes/debug 
```rust
#[derive(Debug)]
struct myStruct() {
	...
}
```

### Manually implementing
- [Rust, How to implement Debug Trait on Enum Type \| by Mike Code \| Medium](https://medium.com/@mikecode/rust-how-to-implement-debug-trait-on-enum-type-01088485390d)
![[#^acdb68]]

## Examples
### Automatically generate with attributes
```rust
#[derive(Debug)]
struct Point {
  x: i32,
  y: i32
}

fn main() {
	let my_point = Point { x: 10, y: 20};
	println!("{:?}", my_point)
}
```
- `Point` is marked with the `#[derive(Debug)]` which automatically generates an `impl` of `Debug` trait for `Point`. Allows you to print by using the `{:?}` formatter.


### Manual implementation
```rust
struct Point {
    x: i32,
    y: i32,
}

impl fmt::Debug for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Point")
         .field("x", &self.x)
         .field("y", &self.y)
         .finish()
    }
}

/// ORRRRR
impl fmt::Debug for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Point [{} {}]", self.x, self.y)
    }
}
```
