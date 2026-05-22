---
summary: Keyword which creates variables for the "lifetime" of the translation unit they are defined in. If namespaced, these variables cannot be accessed by any other translation unit. Additionally, static member functions can be called without an instance of the class. Static functions "belong" to the class definition.
type: note/keyword
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
similar: ["[[Python classmethod]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 15th 2026, 11:38:26 am
implementations: ["[[Cpp.memory.static_pointer_cast]]"]
item_of: ["[[Cpp keywords]]"]
keyword_of: ["[[Cpp keywords]]"]
template:
template-version:
used_by: ["[[Cpp Class Constructors]]", "[[Cpp Class static members and methods]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Static variables exist for the "lifetime" of the translation unit it is defined in
	- If in a namespace scope, then it can't be accessed from any other translation unit. 

## Usage
### Static Variables
- Static class variables exist as 1 for each class
	- they exist for the lifetime of the translation unit, which is typically a cpp file where the class is defined

### Static Functions
- Can be called without an instance of the class.
- Cannot access non-static members of the class, as it has no instance.
