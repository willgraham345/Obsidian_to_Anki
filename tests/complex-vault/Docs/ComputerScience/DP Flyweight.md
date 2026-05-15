---
type: note/concept
date created: Friday, October 11th 2024, 4:08:56 pm
date modified: Friday, October 11th 2024, 4:13:28 pm
---
[summary:: Structural pattern that lets you fit more objects into available RAM by sharing common parts of state between multiple objects instead of keeping all the data in each object.]

Shows you how to make lots of little objects. [[DP Facade]] shows how to make a single object that contains an entire subsystem. 

[Flyweight](https://refactoring.guru/design-patterns/flyweight)


Intrinsic state: Fields that contains unchanged data duplicated across many objects
Extrinsic state: Fields that contain contextual data unique to each object.

Pros:
- You can save lots of RAM, assuming your project has lots of similar objects
Cons:
- You might be trading RAM over CPU cycles when some of the context data needs to be recalculated each time somebody calls a flyweight method. 
- Code becomes much more complicated. New team members will always be wondering why the state of an entity was separated in such a way. 
![[DP Flyweight.png | 600]]


![[DP Flyweight-1.png | 300]]