---
summary: Parsing library for parsing a stream of Rust tokens into a syntax tree of Rust source code.
headings:
  - "[[#Concepts of Note]]"
type: note/library
library_of:
  - "[[Rust]]"
used_by:
  - "[[Rust derive macros]]"
items:
  - "[[Rust syn DeriveInput]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
## Concepts of Note
  `let ast: DeriveInput ``=`` syn::parse(input).unwrap()` ;;; Splits an input `TokenStream` `input` into one of 3 possible structs, a `struct`, `enum`, or `union`. This also removes the `Result<>`. = #lang/meta/attributes/derive #lang/macros/procedural 
<!--ID: 1758253288337-->

󰠗  What structure from the `syn` library can split an incoming `TokenStream` into a `struct`, `enum`, or `union`? ;; `syn::DeriveInput` = #lang/meta/attributes/derive #lang/macros/procedural 
<!--ID: 1758253288331-->


### Concepts in Syn
1. Data structures provided in syn
	- Syntax tree is rooted at `syn::File` which represents a full source file.
		- Other entry points include:
			- `syn::Item`
			- `syn::Expr`
			- `syn::Type`
2. Derives
	- `syn::DeriveInput`, which is any of the 3 legal input terms to a derive macro
3. Parsing
	- Built around parsing functions.
4. Location info
	- Each token parsed by Syn is associated with a `Span` that tracks the line/column information back to the source code of that token. Allows procedural macro to display detailed error messages pointing to all the right places in the user's code. 
