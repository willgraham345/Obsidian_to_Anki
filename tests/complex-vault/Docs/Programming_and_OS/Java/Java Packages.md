---
type: note
---
# Background
Types of Packages
- Built-in Packages
	- Packages from the Java API
	- Complete list of classes found here: https://docs.oracle.com/javase/8/docs/api/
- User-defined packages
	- Plenty, found all over Github


# Usage
## Importing a Package
The entire package is imported with ending through the `*` sign. The following will import everything from the `java.util` package
```java
import java.util.*;
```

## User-defined Packages
- Java uses a file system directory to store packages. 
- To create a package, use the `package` keyword:

└── root
  └── mypack
    └── MyPackageClass.java
### MyPackageClass.java
```java
package mypack;
class MyPackageClass {
  public static void main(String[] args) {
    System.out.println("This is my package!");
  }
}
```