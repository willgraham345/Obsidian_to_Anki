---
type: note
---
# Logic
## Break
```java
break
```
- When Java reaches a break box, it will break out of the current switch block,. 

## Default
```java
default
```
- Part of the switch case, and will run if there is no case matching. 
## If else
```
if (condition1) {
  // block of code to be executed if condition1 is true
} else if (condition2) {
  // block of code to be executed if the condition1 is false and condition2 is true
} else {
  // block of code to be executed if the condition1 is false and condition2 is false
}
```
## Switch
```java
switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}
```

```java
int day = 4;
switch (day) {
  case 1:
    System.out.println("Monday");
    break;
  case 2:
    System.out.println("Tuesday");
    break;
  case 3:
    System.out.println("Wednesday");
    break;
  case 4:
    System.out.println("Thursday");
    break;
  case 5:
    System.out.println("Friday");
    break;
  case 6:
    System.out.println("Saturday");
    break;
  case 7:
    System.out.println("Sunday");
    break;
}
// Outputs "Thursday" (day 4)
```
## Ternary Operator (Shorthand If/Else)

- consists of 3 operands. The first operand is a condition, the second is returned if true, and the third is returned if false.
- ```variable = (condition) ? expressionTrue :  expressionFalse;```
## Logic tests
`>` 
`==`