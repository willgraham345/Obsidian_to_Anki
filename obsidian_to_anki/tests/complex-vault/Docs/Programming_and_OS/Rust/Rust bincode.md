---
summary: Crate for encoding/decoding using binary serialization strategy. This library uses serde as the serialization strategy for struct serialization, and then it performs the serialization.
headings:
  - "[[#Concepts of Note]]"
type: note/library
processes:
  - "[[Rust bincode implementing decode example]]"
  - "[[Rust serializing a struct]]"
associations:
  - "[[Rust UdpSocket]]"
date created: Thursday, May 29th 2025, 4:50:35 pm
date modified: Monday, July 21st 2025, 10:32:37 am
interfaces:
  - "[[Rust Decode]]"
  - "[[Rust Encode]]"
uses:
  - "[[Rust serde]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[bincode - Rust](https://docs.rs/bincode/latest/bincode/)

## Concepts of Note
You'll need to implement these traits on your structures if you want to use bincode:
- Encode
- Decode
󰠗  What are the two traits bincode uses? ;; Encode and decode = #lang/networking/protocol #lang/IO/serialization  
<!--ID: 1758253288989-->

󰠗  What bincode functions should be used for encoding/decoding when working with an `fs::File` or `net::TcpStream`? ;; `encode_into_std_write` for encoding, `decode_from_std_read` for decoding = #lang/networking/protocol 
<!--ID: 1758253288995-->

󰠗  What bincode functions should be used for encoding/decoding when working with an in-memory buffer? ;; `encode_to_vec` for encoding, `decode_from_slice` for decoding = #lang/networking/protocol 
<!--ID: 1758253289002-->

󰠗  What bincode functions should be used for using a custom `Reader` and `Writer`? ;; `encode_into_writer` for encoding, `decode_from_reader` for decoding = #lang/networking/protocol 
<!--ID: 1758253289009-->

󰠗  What bincode functions should be used for using a pre-allocated buffer on an embedded target? ;; `encode_into_slice` for encoding, `decode_from_slice` for decoding = #lang/networking/protocol 
<!--ID: 1758253289016-->

󰠗  What provision must be taken when using bincode with serde in the scope? ;; You need to use `bincode::serde::...` rather than `bincode::...` = #lang/networking/protocol #lang/networking/serde 
<!--ID: 1758253289023-->

