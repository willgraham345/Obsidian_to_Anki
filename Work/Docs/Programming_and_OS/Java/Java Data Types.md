---
type: note
---
# Primitive Data types
| Type    | Description             | Default | Size    | Example Literals                            | Range of values                                                        |
| ------- | ----------------------- | ------- | ------- | ------------------------------------------- | ---------------------------------------------------------------------- |
| boolean | true or false           | false   | 1 bit   | true, false                                 | true, false                                                            |
| byte    | twos-complement integer | 0       | 8 bits  | (none)                                      | -128 to 127                                                            |
| char    | Unicode character       | \u0000  | 16 bits | ‘a’, ‘\u0041’, ‘\101’, ‘\\’, ‘\’, ‘\n’, ‘β’ | characters representation of ASCII values<br><br>0 to 255              |
| short   | twos-complement integer | 0       | 16 bits | (none)                                      | -32,768 to 32,767                                                      |
| int     | twos-complement intger  | 0       | 32 bits | -2,-1,0,1,2                                 | -2,147,483,648 <br><br>to <br><br>2,147,483,647                        |
| long    | twos-complement integer | 0       | 64 bits | -2L,-1L,0L,1L,2L                            | -9,223,372,036,854,775,808 <br><br>to<br><br>9,223,372,036,854,775,807 |
| float   | IEEE 754 floating point | 0.0     | 32 bits | 1.23e100f , -1.23e-100f , .3f ,3.14F        | upto 7 decimal digits                                                  |
| double  | IEEE 754 floating point | 0.0     | 64 bits | 1.23456e300d , -123456e-300d , 1e1d         | upto 16 decimal digits                                                 |

## Creating new variables
Just like C programming, with a specifier at the end:
```java
float myFloatNum = 5f;
int myInt = 5;
double myDoubleNum = 5d;
char myChar = 'B';
```


# Non-Primitive Data Types
```java
String greeting = "Hello";
```