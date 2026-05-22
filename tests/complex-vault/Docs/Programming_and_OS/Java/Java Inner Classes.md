---
type: note
---
In java, you can nest classes (class within a class). The idea is that you'd be able to group classes together, making things more maintainable and readable. 


## Accessing Outer Classes from an Inner Class
```java
class OuterClass {
  int x = 10;

  class InnerClass {
    public int myInnerMethod() {
      return x;
    }
  }
}

public class Main {
  public static void main(String[] args) {
    OuterClass myOuter = new OuterClass();
    OuterClass.InnerClass myInner = myOuter.new InnerClass();
    System.out.println(myInner.myInnerMethod());
  }
}

// Outputs 10
```