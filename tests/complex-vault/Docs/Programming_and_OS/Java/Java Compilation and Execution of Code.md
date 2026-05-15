---
type: note
---
# Background
Java text files are converted into an executable program with the [[Java JDK]] compiler. 

Java text segment is converted into bytecode after compilation which carries the `.class` extension. 

## Example
### Write File
#### Java text file `Hello.java`
```java
class Hello{
	public static void main (String[] args) {
		System.out.println("Hello Geek!");
	}
}
```
### Compile
```shell
javac <path_to_hello.java>
```
### Directory Output
A `Hello.class` file is created in the same directory. To run
Run Code
### Run Code
```shell
java Hello
```
- Don't need to include the `.class` to run your code