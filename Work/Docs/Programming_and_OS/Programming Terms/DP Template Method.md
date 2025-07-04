---
type: note/concept
date created: Friday, October 11th 2024, 5:12:59 pm
date modified: Friday, October 11th 2024, 5:20:37 pm
---
[summary:: Makes use of polymorphism and a template method, and defines the skeleton of an algorithm in a superclass. Lets a subclass override specific steps of an algorithm without changing its structure. You break down an algorithm into a series of steps and turn these steps into methods. ]
similar:: [[DP Template Method]]

[Template Method](https://refactoring.guru/design-patterns/template-method)

Possible uses:
- Logging
- Console output
- Debug printing
- Based on inheritance.

Basic workflow
1. Analyze the target algorithm to see whether you can break it into steps. Consider which steps are common to all subclasses and which ones will always be unique.
2. Create the abstract base class and declare the template method and a set of abstract methods representing the algorithm’s steps. Outline the algorithm’s structure in the template method by executing corresponding steps. Consider making the template method `final` to prevent subclasses from overriding it.
3. It’s okay if all the steps end up being abstract. However, some steps might benefit from having a default implementation. Subclasses don’t have to implement those methods.
4. Think of adding hooks between the crucial steps of the algorithm.
5. For each variation of the algorithm, create a new concrete subclass. It _must_ implement all of the abstract steps, but _may_ also override some of the optional ones.

Pros:
- You can let clients override only certain parts of a large algorithm, making them less affected by changes that happen to other parts of the algorithm. 
- You can pull the duplicate code into a superclass.
Cons:
- Some clients may be limited by the provided skeleton of algorithm. 
- You might violate the Liskov Substitution principle by suppressing a default step implementation via a subclass.
- Template methods tend to be harder to maintain the more steps they have. 


![[DP Template Method.png | 500]]