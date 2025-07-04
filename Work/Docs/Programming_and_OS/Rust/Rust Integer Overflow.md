---
summary: Happens when you screw up and create an integer out of scope of your own integer. Handled with 2's complement wrapping.
type: note/concept
concept_of: ["[[Rust DataTypes]]"]
date created: Wednesday, January 8th 2025, 4:49:41 pm
date modified: Wednesday, January 8th 2025, 4:50:38 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

- Integer overflow
	- Rust handles this with 2's complement wrapping. 
	- The program will not panic, but the variable will have a value you aren't expecting. Don't rely on integer overflow wrapping.
	- To handle this:
		- Wrap all modes with the `wrapping_*` methods such as `wrapping_add`
		- Return `None` value if there is overflow with the `checked_*` method