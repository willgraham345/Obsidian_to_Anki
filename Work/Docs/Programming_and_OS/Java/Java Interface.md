---
type: note
---
# Background
- Blueprint for [[Java Classes]]
- To implement, you must override all methods
- Interfaces cannot constrain a constructor

Why would you use interfaces?
- Security
- Java does NOT support multiple inheritance (a class can only inherit from one superclass). We can achieve this with interfaces, because the class can implement multiple interfaces. 

# Usage
## Multiple Inheritance
```java
// interface
interface Animal {
  public void animalSound(); // interface method (does not have a body)
  public void run(); // interface method (does not have a body)
}
```

```java
interface FirstInterface {
  public void myMethod(); // interface method
}

interface SecondInterface {
  public void myOtherMethod(); // interface method
}

class DemoClass implements FirstInterface, SecondInterface {
  public void myMethod() {
    System.out.println("Some text..");
  }
  public void myOtherMethod() {
    System.out.println("Some other text...");
  }
}

class Main {
  public static void main(String[] args) {
    DemoClass myObj = new DemoClass();
    myObj.myMethod();
    myObj.myOtherMethod();
  }
}
```