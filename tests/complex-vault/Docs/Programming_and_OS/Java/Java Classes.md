---
type: note
---
# Background
- User-defined blueprint or prototype from which objects are created. 
- General class components
	- Modifiers 
		- [[Java Class Access Modifiers]]
	- Class name
	- Superclass (if any)
		- Name of the class's parent. A class can only extend one parent. 
	- Interfaces (if any)
	- Body (surrounded by braces)



# Usage
## Class Constructors
- Constructors are used to initialize objects, often called when the object of a class is created.
- The constructor name must match the class name, and it cannot have a return type
```java
// Create a Main class
public class Main {
  int x;  // Create a class attribute

  // Create a class constructor for the Main class
  public Main() {
    x = 5;  // Set the initial value for the class attribute x
  }

  public static void main(String[] args) {
    Main myObj = new Main(); // Create an object of class Main (This will call the constructor)
    System.out.println(myObj.x); // Print the value of x
  }
}

// Outputs 5
```
## Declare Class Attributes
- A member of the class
- If you don't want the member to be modified, use the `final` keyword
```java
public class Main {
  final int x = 10;

  public static void main(String[] args) {
    Main myObj = new Main();
    myObj.x = 25; // will generate an error: cannot assign a value to a final variable
    System.out.println(myObj.x);
  }
}
```

