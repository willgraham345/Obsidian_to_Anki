---
type: note
---
## Constructor Definition
- Used in the creation of an object, which is an instance of a class
- Has the same name as the class, and doesn't return any values. Don't include a return type on the constructor, but you should control who can access these objects.
- Good practice is to *avoid* calling non-constructor methods from a constructor. This ensures that code is actually being set to the correct member. 

## Example
```java
public class Main {
  int modelYear;
  String modelName;

  public Main(int year, String name) {
    modelYear = year;
    modelName = name;
  }

  public static void main(String[] args) {
    Main myCar = new Main(1969, "Mustang");
    System.out.println(myCar.modelYear + " " + myCar.modelName);
  }
}

// Outputs 1969 Mustang
```
## Constructor Overloading
- Declaring multiple constructors, with different formal parameters. The number of parameters can be different between constructors. If the number of parameters is the same between two constructors, their types or order of the types must differ. 
- Constructor chaining is when one constructor explicitly calls another overloaded constructor
	- You must use the special statement `this()` to execute another constructor, passing it arguments if required. 