---
type: note
---
## Final Modifier
If you don't want the ability to override existing attribute values, declare attributes as `final`
```java
public class Main {
  final int x = 10;
  final double PI = 3.14;

  public static void main(String[] args) {
    Main myObj = new Main();
    myObj.x = 50; // will generate an error: cannot assign a value to a final variable
    myObj.PI = 25; // will generate an error: cannot assign a value to a final variable
    System.out.println(myObj.x);
  }
}
```


The final modifier will also keep other classes from inheriting that specific class
```java
final class Vehicle {
  ...
}

class Car extends Vehicle {
  ...
}
// Outputs error: Main.java:9: error: cannot inherit from final Vehicle
```