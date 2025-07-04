---
summary: Use a list, not a one-line thing to create an object.
headings: ["[[#Syntax]]"]
type: note/component
same: []
date created: Tuesday, June 10th 2025, 12:18:32 pm
date modified: Tuesday, June 10th 2025, 12:20:43 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Constructors and member initializer lists - cppreference.com](https://en.cppreference.com/w/cpp/language/constructor)

## Syntax

```
className (parameters...) {
      // body
}
 // Rewritten as...

MyClass::MyClass(int val) : memberVar(val) {};

// or

MyClass::MyClass(int val)
	: memberVar1(),
	memberVar2,
	...
	lastVar()
	
```

Read more about [initializer lists](https://www.geeksforgeeks.org/when-do-we-use-initializer-list-in-c/)
