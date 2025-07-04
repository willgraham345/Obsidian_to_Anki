---
summary: Used when you'd like to define a function/method in a base class, to be implemented in a later class function call.
type: note/concept
implements: ["[[Cpp Polymorphism Run Time]]", "[[Cpp.Polymorphism]]"]
concept_of: ["[[Cpp Class]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, January 7th 2025, 10:37:24 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Why have this abstraction?
- Classes may have virtual members, which are functions that are declared within a base class, and redefined within a derived class.
	- Virtual functions ensure that the correction function is called for an object, regardless of the type of reference (or pointer) used for the function call. 
	- Used to achieve Runtime polymorphism. 
- If the function is redefined in an inherited class, the parent must have the word `virtual` in front of the function definition.
Virtual function Rules
1. Virtual functions cannot be `static`
2. A virtual function can be a friend function of another class
3. Virtual functions should be accessed using a pointer or reference of base class to achieve runtime polymorphism
4. Prototype of virtual functions should be the same in the base as well as the derived class
5. Virtual functions are always defined in the base class and overriden in a derived class. It is **not** mandadtory for the derived class to override (or re-define the virtual function). In that case, the base class version of the function is used. 
6. A class may have a virtual destructor, but it cannot have a virtual constructor. 

# Usage
## Declaring a virtual function in a base class
<iframe src="https://stackoverflow.com/questions/2391679/why-do-we-need-virtual-functions-in-c" style="width: 100%; height: 600px;"></iframe>
