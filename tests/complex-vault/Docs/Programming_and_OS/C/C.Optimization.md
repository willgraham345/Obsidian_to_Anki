---
type: note
---
# `inline`
- The inline keyword is a suggestion to the compiler, and is not guaranteed that the function will be expanded inline. Essentially, this suggests that the code is "pasted" into all places where it is called rather than forcing the process to jump around and handle inputs/outputs. 
- Can improve performance by avoiding function call overhead, but may increase code size. 
- Usually only defined in header files. When a function is defined in a header file and included in multiple source files, the "inline" keyword helps avoid multiple definitions during linking.
- Most effective for small simple functions.
- Effectiveness will depend on the compiler's optimization settings. 
- Less common nowadays, instead people rely on the compiler to do the optimization.