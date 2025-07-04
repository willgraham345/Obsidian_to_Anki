---
summary: Unwraps valid values, or returns erroneous values, propagating them to the call function.
headings: 
type: note/keyword
associations: ["[[Rust match]]", "[[Rust turbofish]]"]
date created: Thursday, May 8th 2025, 10:11:30 am
date modified: Friday, June 27th 2025, 4:23:43 pm
keyword_of: ["[[Rust error handling]]"]
used_by: ["[[Rust std result]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- [p] `match operand {`<br>`Ok(x) => x`<br>`Err(e) => return Err(From::from(e)),` = How to think of the `?` in Rust, or what it actually is doing = #code/rust/result 
<!--ID: 1751434090466-->
