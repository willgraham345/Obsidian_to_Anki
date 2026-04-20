---
summary: Accepts a single parameter T (trait class), and returns the underlying type of the enum type T. Note, the underlying type of an enum class is `int` unless declared otherwise.
headings:
  - "[[#Examples]]"
type: note/item
date created: Monday, May 19th 2025, 1:57:50 pm
date modified: Monday, October 27th 2025, 11:47:11 am
item_of:
  - "[[Cpp std metaprogramming]]"
template:
template-version:
used_by:
  - "[[Cpp enum (class)]]"
similar:
  - "[[Cpp is_enum]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Examples
```cpp
enum class A : short { x,y,z};

int main() {
	typedef std::underlying_type<A>::type A_under; //will come out to a short type
}
```