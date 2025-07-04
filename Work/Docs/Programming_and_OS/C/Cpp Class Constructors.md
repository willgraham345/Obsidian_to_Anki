---
summary: Method that's invoked at the time of object creation. These can be overloaded, morphed, and deleted if necessary.
headings: ["[[#Concepts of Note]]"]
type: note
concepts: ["[[Cpp Class Delegated Constructors]]", "[[Cpp.Class.Overloading_Constructors]]", "[[Cpp.Class.Overloading_Operators]]"]
components: ["[[Cpp Class Copy Constructors]]", "[[Cpp Class Move Constructors]]", "[[Cpp Class Parameterized Constructors]]", "[[Cpp default constructor]]"]
similar: ["[[Cpp Input Output]]", "[[Cpp Storage Classes and Keywords]]", "[[Cpp templates]]"]
associations: ["[[Cpp std move]]", "[[Cpp templates]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, June 26th 2025, 9:53:39 am
function_of: ["[[Cpp Class]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

## More Background
Method that is invoked automatically at the time of object creation. Used to initialize the data members of new objects. 
[More info here](https://www.geeksforgeeks.org/constructors-c/)
Constructors can be defined inside of the class (typically in the `public:` access), but can also be defined outside of the class. 
- 

# Usage
## Concepts of Note
### Constructor types
#### Default
```
className() {
    // body_of_constructor
}
```

#### Designated Initializers

#### Parameterized
- ![[Cpp Class Parameterized Constructors#Syntax]]

#### Copy
- ![[Cpp Class Copy Constructors#Syntax]]

#### Move
- ![[Cpp Class Move Constructors#Syntax]]

#### Delegated Constructors #TODO
[[Cpp Class Delegated Constructors]]

#### Overloaded Constructors #TODO 
[[Cpp.Class.Overloading_Constructors]]

#### Overloaded Operators #TODO 
[[Cpp.Class.Overloading_Operators]]

#### Destructors #TODO
```
ClassName (ClassName&)
```