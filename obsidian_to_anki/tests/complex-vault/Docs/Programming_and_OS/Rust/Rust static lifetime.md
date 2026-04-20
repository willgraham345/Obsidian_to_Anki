---
summary: "`'static` indicates that the data apointed to by the reference lives for the remaining lifetime of the running program.<br><br>Two ways to create this: Make a constant with static declaration, or make a string literal with the type `&'static str`."
headings: 
type: note/concept
associations:
  - "[[Rust static items]]"
class_of:
  - "[[Rust lifetimes]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
## Concepts of Note

You don't want to create a reference, and *then* promote it to the static lifetime. 
Instead, create a box, which contains a reference to a value on the heap.

## Diagrams
```mermaid
graph LR
	T
	box["Box< T >"]
	static["&'static"]
	T --> box
	box --> static
	T <-.- T_comment
	box <-.- box_comment
	static <-.- static_comment
	T_comment@{shape: comment, label: "Memory:Stack\nOwned"}
	box_comment@{shape: comment, label: "Memory: Heap\nOwned"}
	static_comment@{shape: comment, label: "Memory: Heap\nNot Owned"}
```