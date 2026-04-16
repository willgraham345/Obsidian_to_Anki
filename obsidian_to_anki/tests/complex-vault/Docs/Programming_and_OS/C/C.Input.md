---
type: note
---

# `getchar()`
- If you want to read a single character from the keyboard in ASCII format, then use `getchar()`
- Takes no argument, and returns an `int` value which happens to b the ASCII value of the key pressed
- `int a = getchar();` 
	- Program will hang until you press a key followed by pressing the enter key

# `scanf()`
- Standard library function that allows you to read input from standard in
- You can read in both characters and numbers from the keyboard
## Reading a number
```c
int age;
printf("Enter your age: ");
scanf("%d", &age); 
//%d specifies that it will read it in as an integer
//&age is the address it puts the input
```
## Reading a character
```c
int age;
printf("Enter your age: ");
scanf("%c", &ch); 
//%d specifies that it will read it in as an character
//&ch is the address it puts the input
```