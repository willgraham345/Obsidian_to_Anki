---
summary: Crate for encoding/decoding using binary serialization strategy. This library uses serde as the serialization strategy for struct serialization.
headings: ["[[#Concepts of Note]]"]
type: note/library
functions: 
workflows: ["[[Rust bincode implementing decode]]", "[[Rust serializing a struct]]"]
associations: ["[[Rust serde]]", "[[Rust UdpSocket]]"]
date created: Thursday, May 29th 2025, 4:50:35 pm
date modified: Friday, May 30th 2025, 11:09:40 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[bincode - Rust](https://docs.rs/bincode/latest/bincode/)

## Concepts of Note
You'll need to implement these traits on your structures if you want to use this...
- Encode
- Decode
