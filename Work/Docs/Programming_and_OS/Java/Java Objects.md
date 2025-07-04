---
type: note
---
- We have to declare and initialize objects within java. 

## Creating an Object in Java
- Use keyword `new`, include the name of the class, followed by parentheses
```java
Car car = new Car();
```
- `Car car` declares the variable
- `new Car()` initializes the variable as an object

## POJO
- POJO = plain old java object
	- comes with lots of boilerplate code. 


## Record Type
- Introduced in JDK 14, and official in JDK 16. 
- Replaces the boilerplate code of the POJO, but to be more restrictive
	- Plain data carriers
- Data that is not meant to be altered.
- Contains only fundamental methods, such as constructors and accessors.
### Example
```java
public record LPAStudent(String id, String name, String dateOfBirth, String classList) {
}
```
- *Record header*: part in parentheses, which consists of record components, in comma separated list
	- Field is declared private and final (can't be modified) 
		- Fields are sometimes referred to as a component field
- For each component in the record header, Java generates a field with the same name and declared type as the record component.
- Java will also generate a toString`toString` method that prints out each attribute in a formatted String. 
- Java also generates a public accessor method for each component. This method has the same name and type of the component, but doesn't have any kind of special prefix (no get, or is, for example)
	- Accessor method for `id` is `id()`