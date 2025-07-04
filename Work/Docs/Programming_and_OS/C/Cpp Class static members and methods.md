---
summary: Static variables are the same throughout all instances of a class. Signifies that the function/field belongs to the class -- not to the instance. Very useful for mutex situations.
headings: ["[[#Usage]]"]
type: note/component
implements: ["[[Cpp Storage Classes and Keywords]]", "[[Cpp.Storage.Classes.static]]"]
source: ["[[Cpp Class]]"]
class_of: ["[[Cpp Storage Classes and Keywords]]"]
component_of: ["[[Cpp static]]"]
concept_of: ["[[Cpp Class]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, June 26th 2025, 8:23:24 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage
- [p] `public:`<br>`static void funFun()` = Declares a static method that is the same across all installations of the class. Useful for mutex/matrix situations and cli handlers. = #code/cpp/functions 
<!--ID: 1751434091731-->

- [p] `public:`<br>`static int variable` = Declares a static variable that is the same across all installations of the class. Very useful for having a mutex that is to be used by all instances. = #code/cpp/variables/static 
<!--ID: 1751434091735-->


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