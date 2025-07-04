---
type: note/concept
date created: Friday, October 11th 2024, 4:00:07 pm
date modified: Friday, October 11th 2024, 4:08:12 pm
---
[summary:: Structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors. Also known as a "wrapper". Done by referencing one object from another.]
similar:: [[DP Chain of Responsibility]], [[DP Composite]]

[Decorator](https://refactoring.guru/design-patterns/decorator)

Inheritance is static. You can't alter the behavior of an existing object at runtime. You can only replace the whole object with another one that's just been created.
Subclasses can only have one parent class (in most languages). 

Use [[PT OOP Composition]] to delegate work to other objects.
![[DP Decorator.png | 300]]