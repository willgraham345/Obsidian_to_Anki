---
summary: A type alias. Basically creates a new name for an existing data type, making code reuse much better.
type: note/concept
associations: ["[[Cpp using]]"]
date created: Thursday, January 16th 2025, 12:37:49 pm
date modified: Monday, February 10th 2025, 4:37:38 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

[typedef specifier - cppreference.com](https://en.cppreference.com/w/cpp/language/typedef)

An alternative method, is to use [[Cpp using]]

# Additional Background
## Media
```cpp
typedef std::map<class1, class2> mappymap;
```
- Defines `mappymap` as a new class/structure which will make it easier to use in the code
- Uses `std::map`
	- `std::map<class1, class2>` is an associative container that maps keys of type `class1` to values of type `class2`.
	- This means `class1` should have a valid **comparison operator (`<`)** because `std::map` requires it to order keys.