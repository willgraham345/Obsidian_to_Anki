---
summary: A class/thing that only lets there be one of it, with provided global access.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Workflows]]"
type: note/concept
examples:
  - "[[Cpp Naive Singleton]]"
  - "[[Cpp Thread Safe Singleton]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, June 9th 2025, 12:10:49 pm
concept_of:
  - "[[DP Creational Patterns]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background


## Concepts of Note

### Typical usage cases
- Logging classes (Accessing something over and over again. Not always the right move to make this a singleton.)
- Information flow is one direction
- Access to the resource will be requested from multiple disparate parts of a system. 
- [Five Popular Use Cases to Apply Singleton Pattern To Your Software Project | by Tech Is Beautiful | Medium](https://medium.com/@techisbeautiful/five-popular-use-cases-to-apply-singleton-pattern-to-your-software-project-5145d5841d18)

### Pros:
- You can be sure that a class has only a single instance.
- You gain a global access point to that instance.
- The singleton object is initialized only when it’s requested for the first time.

### Cons
- Violates the _Single Responsibility Principle_. The pattern solves two problems at the time.
- The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other.
- The pattern requires special treatment in a multithreaded environment so that multiple threads won’t create a singleton object several times.
- It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects. Since the constructor of the singleton class is private and overriding static methods is impossible in most languages, you will need to think of a creative way to mock the singleton. Or just don’t write the tests. Or don’t use the Singleton pattern.

## Workflows


1. The **Singleton** class declares the static method `getInstance` that returns the same instance of its own class.
    The Singleton’s constructor should be hidden from the client code. Calling the `getInstance` method should be the only way of getting the Singleton object.
	1. Make the default constructor private, to prevent others from using the `new` operator
		1. Create a static creation method that acts as a constructor. 
		2. Under the hood this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object. 

![[Pasted image 20240515195210.png|600]]

