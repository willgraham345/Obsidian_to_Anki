---
summary: Provides a macro for the standard library `std::error::Error` trait. Does *not* appear in your API, giving you the exact same thing as if you'd written it by hand.
headings: 
type: note/class
similar: ["[[Rust anyhow Error]]"]
date created: Monday, July 14th 2025, 4:35:56 pm
date modified: Monday, July 14th 2025, 4:42:36 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- [p] `#[derive(Error,Debug)]`
      `pub enum ErrorType {`
      `#[error("data store disconnected")]`
      `InvalidLookahead(u32)}` = Declare an `ErrorType` which will not appear in your public API, with a type `InvalidLookahead` that has a u32 returned in the error message. = #lang/control_flow/errors