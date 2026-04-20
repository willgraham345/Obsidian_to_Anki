---
type: note
---
## Static vs Instance Methods
- Static methods: Can't access instance methods and instance variables directly.
	- Usually used for operations that don't require any data from an instance of the class (can't use `this` keyword)
- Instance methods: Can access instance methods directly. 
## Variables
`static` makes variables belong to the class rather than just to the instance/object. Changing one static, will change ALL of the class's static variable. 
- Great for multi-threading

## Import
Static import allows members (fields and methods) defined in a class as public static to be used in Java cod without specifying the class in which the field is defined. 

