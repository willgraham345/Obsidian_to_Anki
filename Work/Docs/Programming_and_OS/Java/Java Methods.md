---
type: note
---
## Method Definitions
According to Java: **A method declares executable code that can be invoked, passing a fixed number of values as arguments**.

Argument = value that's passed to the method when it is called
Parameter = definition shown in the method declaration
Parameter and argument are often used interchangeably
## Calling a Method
A method is called by naming the method, followed by `()`. A simple example of a method titled `main` is shown below
```java
public class Main {
  static void myMethod() {
    System.out.println("I just got executed!");
  }

  public static void main(String[] args) {
    myMethod();
  }
}

// Outputs "I just got executed!"
```
Another example:
```java
public static void methodName(p1type p1, p2type, p2 {more}) {
 // Method statements
}
```
## Method Overloading
- Method overloading allows multiple methods within a class to have the same name but different parameters. It enables a class to have multiple methods with similar functionality but varying input parameters or argument types.
```csharp
static int plusMethodInt(int x, int y) {
  return x + y;
}

static double plusMethodDouble(double x, double y) {
  return x + y;
}

public static void main(String[] args) {
  int myNum1 = plusMethodInt(8, 5);
  double myNum2 = plusMethodDouble(4.3, 6.26);
  System.out.println("int: " + myNum1);
  System.out.println("double: " + myNum2);
}
```
## Method Parameters
Pass in similarly to C
```java
public class Main {
  static void myMethod(String fname, int age) {
    System.out.println(fname + " is " + age);
  }

  public static void main(String[] args) {
    myMethod("Liam", 5);
    myMethod("Jenny", 8);
    myMethod("Anja", 31);
  }
}

// Liam is 5
// Jenny is 8
// Anja is 31
```


## Return Values
```java
public class Main {
  static int myMethod(int x) {
    return 5 + x;
  }

  public static void main(String[] args) {
    System.out.println(myMethod(3));
  }
}
// Outputs 8 (5 + 3)
```

```java
public class Main {
  static int myMethod(int x, int y) {
    return x + y;
  }

  public static void main(String[] args) {
    System.out.println(myMethod(5, 3));
  }
}
// Outputs 8 (5 + 3)
```