---
summary: Debug is an automatically derivable trait, intended to output developer-friendly info about an instance. Typically shows type internals, and can automatically be implemented with `#[derive(Debug)]
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
type: note/interface
similar: ["[[Rust Display (trait)]]"]
associations: ["[[Rust derive attribute macros]]"]
component_of: ["[[Rust std fmt]]"]
date created: Wednesday, May 21st 2025, 5:43:59 pm
date modified: Wednesday, May 21st 2025, 6:03:36 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [p] `println!("{0:?}", structVal)` = Debug the `structVal` using `std::fmt::Debug`, which is an attribute coming with standard library = #code/rust/attributes/debug  = `"{:#?}"` to enable pretty-printing
<!--ID: 1751434090576-->

- [p] `impl fmt::Debug for A { ... }` = Manually write the debug implementation for struct `A`. Importantly, the `fn fmt(& self, f: &mut fmt::Formatter) -> fmt::Result { ... }` is likely expected. = #code/rust/attributes/debug  ^c1eac8
<!--ID: 1751434090580-->

- The `Debug` trait can be accessed by using the `{:?}` (or `:#?`) format specifier. 

## Usage
### Automatically generate with attributes
- [p] `#[derive(Debug)]`
      `struct myStruct` = Let rust automatically generate an `impl` for `<Debug>`. Allows you to use the `{:#?}` in printing/debugging = #code/rust/attributes/debug #code/rust/format/debug
```
#[derive(Debug)]
struct myStruct() {
	...
}
```

### Manually implementations
- [Rust, How to implement Debug Trait on Enum Type \| by Mike Code \| Medium](https://medium.com/@mikecode/rust-how-to-implement-debug-trait-on-enum-type-01088485390d)
![[#^c1eac8]]
## Examples
```
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
