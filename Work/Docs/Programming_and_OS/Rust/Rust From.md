---
summary: Used to do value-to-value conversions while consuming the input value for infallible conversions. The reciprocal of [[Rust Into]]. This one is better to implement, as `From` will automatically provide a blanket implementation of `Into`.
headings:
  - "[[#Concepts of Note]]"
type: 
date created: Friday, May 30th 2025, 9:58:56 am
date modified: Friday, May 30th 2025, 10:00:27 am
same:
  - "[[Rust Into]]"
concept_of:
  - "[[Rust type conversions]]"
similar:
  - "[[Rust TryFrom]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [p] `From<T> for U` = Converts from `T` into `U`. Can also be performed with `U::from(t)` = #code/rust/type_conversion 
<!--ID: 1751434090568-->
