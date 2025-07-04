---
summary: Can be called on an lvalue to produce an rvalue that can be "smuggled" into an rvalue reference. The new implicit variable will be created, the rvalue reference will actaully refer to the lvalue passed into `std::move()`.<br><br>It changes an expression from being an lvalue (i.e. named variable) to being an xvalue (which tells the compiler it will be destroyed soon). You are letting the compiler cannibalize whatever is inside of `std::move()`
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/function
associations:
  - "[[Cpp value categories]]"
  - "[[Cpp Class Constructors]]"
date created: Wednesday, April 30th 2025, 4:08:48 pm
date modified: Tuesday, June 10th 2025, 12:11:22 pm
function_of:
  - "[[Cpp std]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Used to move resources from one object to another instead of copying (i.e. swapping two objects with less copying)
	- Used when you're writing constructor, operator methods, or wherever objects are created + destroyed a lot. 
	- Under the hood `std::move()` copies the internal pointer to data into the moved object. 

## Usage
Tyic