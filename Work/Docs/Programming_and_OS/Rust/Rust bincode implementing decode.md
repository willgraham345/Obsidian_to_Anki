---
summary: How to implement the decode trait onto an entity/struct.
headings: 
type: note/workflow
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background

[Decode in bincode::de - Rust](https://docs.rs/bincode/latest/bincode/de/trait.Decode.html)
```rust
struct Entity {
    pub x: f32,
    pub y: f32,
}



impl<Context> bincode::Decode<Context> for Entity {
    fn decode<D: bincode::de::Decoder<Context = Context>>(
        decoder: &mut D,
    ) -> core::result::Result<Self, bincode::error::DecodeError> {
        Ok(Self {
            x: bincode::Decode::decode(decoder)?,
            y: bincode::Decode::decode(decoder)?,
        })
    }
}
impl<'de, Context> bincode::BorrowDecode<'de, Context> for Entity {
    fn borrow_decode<D: bincode::de::BorrowDecoder<'de, Context = Context>>(
        decoder: &mut D,
    ) -> core::result::Result<Self, bincode::error::DecodeError> {
        Ok(Self {
            x: bincode::BorrowDecode::borrow_decode(decoder)?,
            y: bincode::BorrowDecode::borrow_decode(decoder)?,
        })
    }
}

```