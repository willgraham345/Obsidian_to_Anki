---
summary: Rust serialization/deserialization framework, which describes how the data can be serialized and deserialized. Serde provides the generic interface (with [[Rust trait]]s implemented with [[Rust attributes]]), and relies on another serializer to perform the serializing.<br><br>Serde provides a generic interface that can be used by multiple backends like JSON, YAML, CBOR, and Bincode.
headings: []
type: note/library
processes:
  - "[[Rust serializing a struct]]"
associations:
  - "[[Rust hashmap]]"
  - "[[Rust std String]]"
date created: Thursday, April 17th 2025, 4:36:34 pm
date modified: Monday, September 29th 2025, 8:03:18 am
items:
library_of:
  - "[[Rust]]"
members:
used_by:
  - "[[Rust bincode]]"
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[GitHub - serde-rs/serde: Serialization framework for Rust](https://github.com/serde-rs/serde)
[Overview · Serde](https://serde.rs/)

## Concepts of Note

- Serde "maps" every struct into one of 29 possible "types" that serde uses. Each method of the `Serializer` trait corresponds to one of the types in the data model.
- Out of the box, Serde is able to serialize/deserialize common Rust datatypes (`String, &str, usize, Vec<T>, HashMap<K,V>`)

- Supported datatypes
	- [[Rust std String]]
	- [[Rust hashmap]]

## Diagrams

![[serde.svg]]

## Usage

  `use serde::{Serialize, Deserialize}` ;;; Import the `Serialize` and `Deserialize` traits to be bound to objects. Note, does not implement the traits with this command. = #lang/IO/serialization

- [p] `#[derive(Serialize, Deserialize)]`
  `struct a {}` = Use a derive macro to implement `serde` on the `struct a`. = #lang/meta/attributes/serialization

  `#[serde(rename ;;; "new_name")]` = Use a different name when serializing a container in serde. = #lang/networking/protocol/container
<!--ID: 1759154339824-->

  `#[serde(rename_all ;;; "...")` = Rename all the fields (if struct), or variants (if enum) according to the case convention. Conventions include: `"lowercase"`, `"UPPERCASE"`, `"PascalCase"`, `"camelCase"`, `"snake_case"`, `"SCREAMING_SNAKE_CASE"`, `"kebab-case"`, `"SCREAMING-KEBAB-CASE"` = #lang/networking/protocol/container 
<!--ID: 1759154339828-->

  `#[serde(rename_all_fields ;;; "...")` = Apply a `rename_all` on every struct variant of an enum according to the given case convention. Conventions include: `"lowercase"`, `"UPPERCASE"`, `"PascalCase"`, `"camelCase"`, `"snake_case"`, `"SCREAMING_SNAKE_CASE"`, `"kebab-case"`, `"SCREAMING-KEBAB-CASE"` = #lang/networking/protocol/container 
<!--ID: 1759154339832-->

  `#[serde(deny_unknown_fields)` ;;; Always error during deserialization when encountering unknown fields. = #lang/networking/protocol/container 
<!--ID: 1759154339836-->

  `#[serde(skip_serializing)]` ;;; Skips this field when serializing in serde. = #lang/networking/protocol/container 
<!--ID: 1759154339840-->

  `#[serde(skip_serializing_if ;;; "function")]` = Skip serializing for functions, and serialize everything that isn't a function. = #lang/networking/protocol/container 
<!--ID: 1759154339845-->

  `#[serde(skip_serializing_if ;;; "Option::is_none")]` = Skip serializing for Options, only if none. Serialize everything that isn't a function. = #lang/networking/protocol/container 

## Examples

```rust
use serde::{Serialize, Deserialize}
#[derive(Serialize, Deserialize, Debug)]
struct Point {
	x: i32,
	y: i32,
}

fn main() {
	let point = Point { x: 1, y: 2};
	let serialized = serde_json::to_string(&point).unwrap();
}
```

## Properties

### Traits

#### Serialize

#### Deserialize

## Questions

󰠗  What should you do to customize the behavior of the `Serialize` and `Deserialize` traits? ;; Use the attributes serde provides = #lang/IO/serialization #lang/networking/serde
<!--ID: 1759154339819-->

## Troubleshooting

`the trait serde::ser::Serialize is not implemented for ___`

- Means that you are using libraries that depend on incompatible versions of Serde. You may be depending on serde 1.0 in your Cargo.toml, but using some other library that depends on serde 0.9.
- Fix: Upgrade/downgrade based on `cargo tree -d`, for finding all duplicate dependencies.

