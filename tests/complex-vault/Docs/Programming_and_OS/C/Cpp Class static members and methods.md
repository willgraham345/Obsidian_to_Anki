---
summary: Static variables are the same throughout all instances of a class. Signifies that the function/field belongs to the class -- not to the instance. Very useful for mutex situations.
headings:
  - "[[#Usage]]"
type: note/item
implements:
  - "[[Cpp Storage Classes and Keywords]]"
source:
  - "[[Cpp Class]]"
concept_of:
  - "[[Cpp Class]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, September 4th 2025, 1:33:11 pm
uses:
  - "[[Cpp static]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage
  `public:`<br>`static void funFun()` ;;; Declares a static method that is the same across all installations of the class. Useful for mutex/matrix situations and cli handlers. = #lang/functions  
ID: 1751997629807



  `public:`<br>`static int variable` ;;; Declares a static variable that is the same across all installations of the class. Very useful for having a mutex that is to be used by all instances. = #lang/data/static  
ID: 1751997629812

### Initialize a static object in the class scope
```cpp
#include <string>
class A
{
	static inline std::string str = "string";
	static inline int x = 900;
};
```
- See also [[Cpp.Functions.Inline]]
