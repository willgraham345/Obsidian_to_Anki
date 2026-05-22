---
summary: Performs conversions between pointers to related classes. No safety check is performed during runtime to check if the object being converted is a full object of the destination type.
type: note/function
headings:
implements:
  - "[[Cpp Casting]]"
date created: Friday, December 27th 2024, 5:32:32 pm
date modified: Thursday, January 15th 2026, 1:14:16 pm
function_of:
  - "[[Cpp Casting]]"
template:
template-version:
similar:
  - "[[Cpp dynamic_cast]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

```cpp
class CBase {};
class CDerived: public CBase {};
CBase * a = new CBase;
CDerived * b = static_cast<CDerived*>(a);
```