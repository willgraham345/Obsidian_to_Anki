---
summary: 
headings: ["[[#Examples]]"]
type: note/workflow
date created: Friday, May 30th 2025, 9:12:27 am
date modified: Friday, June 27th 2025, 10:33:54 am
workflow_of: ["[[Rust bincode]]", "[[Rust serde]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Examples

### Serialization using Bincode
```rust
let mut slice = [0u8; 100];

// You can encode any type that implements `Encode`.
// You can automatically implement this trait on custom types with the `derive` feature.
let input = (
    0u8,
    10u32,
    10000i128,
    'a',
    [0u8, 1u8, 2u8, 3u8]
);

let length = bincode::encode_into_slice(
    input,
    &mut slice,
    bincode::config::standard()
).unwrap();

let slice = &slice[..length];
println!("Bytes written: {:?}", slice);

// Decoding works the same as encoding.
// The trait used is `Decode`, and can also be automatically implemented with the `derive` feature.
let decoded: (u8, u32, i128, char, [u8; 4]) = bincode::decode_from_slice(slice, bincode::config::standard()).unwrap().0;

assert_eq!(decoded, input);
```

### 2
```rust
use bincode::{config, Decode, Encode};

#[derive(Encode, Decode, PartialEq, Debug)]
struct Entity {
    x: f32,
    y: f32,
}

#[derive(Encode, Decode, PartialEq, Debug)]
struct World(Vec<Entity>);

fn main() {
    let config = config::standard();

    let world = World(vec![Entity { x: 0.0, y: 4.0 }, Entity { x: 10.0, y: 20.5 }]);

    let encoded: Vec<u8> = bincode::encode_to_vec(&world, config).unwrap();

    // The length of the vector is encoded as a varint u64, which in this case gets collapsed to a single byte
    // See the documentation on varint for more info for that.
    // The 4 floats are encoded in 4 bytes each.
    assert_eq!(encoded.len(), 1 + 4 * 4);

    let (decoded, len): (World, usize) = bincode::decode_from_slice(&encoded[..], config).unwrap();

    assert_eq!(world, decoded);
    assert_eq!(len, encoded.len()); // read all bytes
}
```