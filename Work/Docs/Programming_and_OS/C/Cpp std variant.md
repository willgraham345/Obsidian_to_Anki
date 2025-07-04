---
summary: Type-safe union, useful in situations where the exact data type and/or how you want to handle it is not known until runtime.<br><br>An instance of variant either holds a value of one of its alternative types, or no value. If a variant holds a value of some object `T`, the `T` object is nested within the variant object. Unable to hold references, arrays, and `void`.
headings:
  - "[[#Concepts of Note]]"
type: note/class
similar:
  - "[[Cpp enumeration]]"
  - "[[Cpp std any]]"
  - "[[Cpp union]]"
class_of:
  - "[[Cpp std]]"
date created: Monday, April 14th 2025, 1:57:30 pm
date modified: Thursday, April 17th 2025, 2:23:57 pm
tags:
  - code/cpp/variables/enumerations/variant
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Great for state transitions and finite state machines
- Potential substitute for enums

## Usage
- [p] `std::variant<std::string, int> data` = Declare a variant with two potential data types. `data` can now be cast as either string or an int without issues, and can be recast as either one. = #code/cpp/variables/enumerations/variant
<!--ID: 1751434091513-->

- [p] `auto value =std::get_if<std::string>(&data)` = Get a pointer to the value of `std::variant data` if data holds a string. = #code/cpp/variables/enumerations/variant 
<!--ID: 1751434091516-->
