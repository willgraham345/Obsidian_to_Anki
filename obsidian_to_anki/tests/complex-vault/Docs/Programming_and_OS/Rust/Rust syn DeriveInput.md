---
summary: Data structure in the syn library, typically representing the output of `syn::parse().unwrap()`. Has 3 big fields, the
headings: ["[[#Diagrams]]", "[[#Properties]]"]
type: note/item
date created: Friday, August 22nd 2025, 2:57:48 pm
date modified: Tuesday, September 2nd 2025, 1:34:32 pm
diagrams: ["[[derive-input.puml]]"]
images: "[[derive-input.svg]]"
item_of: ["[[Rust syn]]"]
members: ["[[#attrs]]", "[[#data]]", "[[#generics]]", "[[#ident]]", "[[#vis]]"]
used_by: ["[[Rust derive macros]]"]
uses: ["[[Rust quote]]", "[[Rust syn data]]", "[[Rust syn Ident]]", "[[Rust syn Visibility]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Properties
### attrs
`pub attrsVec<Attribute>`

### vis
`pub vis: Visibility`

### ident
`pub ident: Ident`

### generics
`pub generics: Generics`

### data
`pub data: Data`

## Diagrams
### Example workflow
![[derive-input.svg | 1000]]