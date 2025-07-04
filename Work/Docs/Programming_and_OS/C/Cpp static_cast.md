---
summary: Performs conversions between pointers to related classes. No safety check is performed during runtime to check if the object being converted is a full object of the destination type.
type: note/function
date created: Friday, December 27th 2024, 5:32:32 pm
date modified: Friday, December 27th 2024, 5:35:38 pm
function_of:
  - "[[Cpp Casting]]"
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