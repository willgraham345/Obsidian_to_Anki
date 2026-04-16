---
type: note
---
The idea behind creating setter methods is that you ensure all data and objects is created through a controlled process, and includes only valid data.

## Get/Set Methods
```java
public class Person {
  private String name; // private = restricted access

  // Getter
  public String getName() {
    return name;
  }

  // Setter
  public void setName(String newName) {
    this.name = newName;
  }
}
```