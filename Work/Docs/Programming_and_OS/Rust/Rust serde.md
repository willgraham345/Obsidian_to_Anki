---
summary: Rust serialization/deserialization framework, which describes how the data can be serialized and deserialized. Serde provides the generic interface (with [[Rust trait]]s implemented with [[Rust attributes]]), and relies on another serializer to perform the serializing.<br><br>Serde provides a generic interface that can be used by multiple backends like JSON, YAML, CBOR, and Bincode.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Media]]"
  - "[[#Usage]]"
type: note/library
workflows:
  - "[[Rust serializing a struct]]"
associations:
  - "[[Rust hashmap]]"
  - "[[Rust std String]]"
date created: Thursday, April 17th 2025, 4:36:34 pm
date modified: Friday, June 27th 2025, 10:33:28 am
library_used_in:
  - "[[Rust]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Out of the box, Serde is able to serialize/deserialize common Rust datatypes (`String, &str, usize, Vec<T>, HashMap<K,V>`)

### Data Formats Supported
- [JSON](https://github.com/serde-rs/json), the ubiquitous JavaScript Object Notation used by many HTTP APIs.
- [Postcard](https://github.com/jamesmunns/postcard), a no_std and embedded-systems friendly compact binary format.
- [CBOR](https://github.com/enarx/ciborium), a Concise Binary Object Representation designed for small message size without the need for version negotiation.
- [YAML](https://github.com/dtolnay/serde-yaml), a self-proclaimed human-friendly configuration language that ain't markup language.
- [MessagePack](https://github.com/3Hren/msgpack-rust), an efficient binary format that resembles a compact JSON.
- [TOML](https://docs.rs/toml), a minimal configuration format used by [Cargo](https://doc.rust-lang.org/cargo/reference/manifest.html).
- [Pickle](https://github.com/birkenfeld/serde-pickle), a format common in the Python world.
- [RON](https://github.com/ron-rs/ron), a Rusty Object Notation.
- [BSON](https://github.com/mongodb/bson-rust), the data storage and network transfer format used by MongoDB.
- [Avro](https://docs.rs/apache-avro), a binary format used within Apache Hadoop, with support for schema definition.
- [JSON5](https://github.com/callum-oakley/json5-rs), a superset of JSON including some productions from ES5.
- [URL](https://docs.rs/serde_qs) query strings, in the x-www-form-urlencoded format.
- [Starlark](https://github.com/dtolnay/serde-starlark), the format used for describing build targets by the Bazel and Buck build systems. _(serialization only)_
- [Envy](https://github.com/softprops/envy), a way to deserialize environment variables into Rust structs. _(deserialization only)_
- [Envy Store](https://github.com/softprops/envy-store), a way to deserialize [AWS Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) parameters into Rust structs. _(deserialization only)_
- [S-expressions](https://github.com/rotty/lexpr-rs), the textual representation of code and data used by the Lisp language family.
- [D-Bus](https://docs.rs/zvariant)'s binary wire format.
- [FlexBuffers](https://github.com/google/flatbuffers/tree/master/rust/flexbuffers), the schemaless cousin of Google's FlatBuffers zero-copy serialization format.
- [Bencode](https://github.com/P3KI/bendy), a simple binary format used in the BitTorrent protocol.
- [Token streams](https://github.com/oxidecomputer/serde_tokenstream), for processing Rust procedural macro input. _(deserialization only)_
- [DynamoDB Items](https://docs.rs/serde_dynamo), the format used by [rusoto_dynamodb](https://docs.rs/rusoto_dynamodb) to transfer data to and from DynamoDB.
- [Hjson](https://github.com/Canop/deser-hjson), a syntax extension to JSON designed around human reading and editing. _(deserialization only)_
- [CSV](https://docs.rs/csv), Comma-separated values is a tabular text file format.

### Rust Formats supported 
- [[Rust std String]]
- [[Rust hashmap]]

## Media
[GitHub - serde-rs/serde: Serialization framework for Rust](https://github.com/serde-rs/serde)
[Overview · Serde](https://serde.rs/)

## Usage
- [p] `use serde::{Serialize, Deserialize}` = Declare a local binding to the `Serialize` and `Deserialize` = #code/rust/IO/serial
<!--ID: 1751434090452-->

- [p] `#[derive(Serialize, Deserialize)]` = Declare outer attribute to a struct = #code/rust/attributes/serial
<!--ID: 1751434090456-->


### Things to do before using 
- Add `serde = { version = "1.0", features = ["derive"] }` as a dependency in Cargo.toml.
- Ensure that all other Serde-based dependencies (for example serde_json) are on a version that is compatible with serde 1.0.
- On structs and enums that you want to serialize, import the derive macro as `use serde::Serialize;` within the same module and write `#[derive(Serialize)]` on the struct or enum.
- Similarly import `use serde::Deserialize;` and write `#[derive(Deserialize)]` on structs and enums that you want to deserialize.

### Troubleshooting
`the trait serde::ser::Serialize is not implemented for ___`
- Means that you are using libraries that depend on incompatible versions of Serde. You may be depending on serde 1.0 in your Cargo.toml, but using some other library that depends on serde 0.9.
- Fix: Upgrade/downgrade based on `cargo tree -d`, for finding all duplicate dependencies. 

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
