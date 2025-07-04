---
summary: Visual representations of the relationships and interactions between entities within a codebase. There are nodes, edges, and colors. Direction implies dependency (A -> B; implies that A depends on B).
type: note/concept
implements: ["[[PT OOP Composition]]", "[[PT OOP Inheritance]]"]
date created: Friday, January 3rd 2025, 3:38:56 pm
date modified: Friday, February 7th 2025, 12:44:31 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

![[Doxygen Collaboration Graphs.png]]

Colors
- Arrows
	- Blue = `public` [[PT OOP Inheritance|Inheritance]], or include relation (for include dependency graph)
	- Green = `protected` [[PT OOP Inheritance|Inheritance]]
	- Red = `private` [[PT OOP Inheritance|Inheritance]]
	- Purple dashed = [[PT OOP Association|Association]] (should have label with what is accessible)
	- Yellow dashed = Relationship with a template class it was instantiated from. 
		- I *think* the yellow solid line is showing a template relationship as part of another class
- Box Colors
	- Black box = documented class/struct
	- Filled gray box = Class graph being generated 
	- Gray box border = Undocumented struct/class
	- Red box border = Documented struct/class for which not all inheritance/containment relations are shown. Sign of truncation

`Inherited` = filled gray box = The class's graph being generated
