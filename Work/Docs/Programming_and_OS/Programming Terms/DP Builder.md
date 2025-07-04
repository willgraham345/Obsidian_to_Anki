---
type: note/concept
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Friday, October 11th 2024, 3:50:29 pm
---
[summary:: When piecewise object construction is complicated, provide an API for doing it succinctly. Basically, build something that builds other stuff step-by-step. ]
down:: [[DP Fluent Builder]], [[Groovy Style Builder]], [[Builder Facets]], [[Life without Builder]]
examples:: [[DP Builder Example Code]]

Why?
- You can't create an infinite amount of subclasses.
	- If you do, the constructors get really yucky. 
- Gets rid of the MASSIVE overloaded constructor sequencing (see below):
```cpp
class Pizza {
    Pizza(int size) { ... }
    Pizza(int size, boolean cheese) { ... }
    Pizza(int size, boolean cheese, boolean pepperoni) { ... }
    // ...
```
- Construct objects step-by-step, defer construction steps, or run it recursively
- Single responsibility
- You can reuse the same construction code when building various representations of products

Lets you construct complex objects step by step. Lets you produce different types and representations of an object using the same construction code. 

# Example
![[Pasted image 20240515191716.png | 500]]
1. The **Builder** interface declares product construction steps that are common to all types of builders.
	1. Decompose construction into a series of steps, and use builders in the construction process
    
2. **Concrete Builders** provide different implementations of the construction steps. Concrete builders may produce products that don’t follow the common interface.
	1. i.e. (`buildWalls`, `buildDoor`, `buildWindows`) for `House`
	2. Can be extended to construct a product into a separate class called *director*.
		1. Isn't necessary, but might be good so you can reuse this across the program. The director also completely hides the details of product construction from the client code. The client only needs to associate a builder with a director, launch the construction with the director, and get the result from the builder.
    
3. **Products** are resulting objects. Products constructed by different builders don’t have to belong to the same class hierarchy or interface.
    
4. The **Director** class defines the order in which to call construction steps, so you can create and reuse specific configurations of products.
[[DP]] 
    
5. The **Client** must associate one of the builder objects with the director. Usually, it’s done just once, via parameters of the director’s constructor. Then the director uses that builder object for all further construction. However, there’s an alternative approach for when the client passes the builder object to the production method of the director. In this case, you can use a different builder each time you produce something with the director.


