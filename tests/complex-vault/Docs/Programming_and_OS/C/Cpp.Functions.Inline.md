---
type: note
---
# Background
A way to reduce function call overhead, and a function that happens in the line it is called. They have weird include statements, see [[Cpp.include_and_forward_declaration]]
![[Pasted.image.20240227151719.png]]
The compiler can ignore the request for inlining
**The compiler may not perform inlining in such circumstances as:** 
1. If a function contains a loop. (_for, while and do-while_) 
2. If a function contains static variables. 
3. If a function is recursive. 
4. If a function return type is other than void, and the return statement doesn’t exist in a function body. 
5. If a function contains a switch or goto statement.

Why are inline functions used

Advantages
1. Function call overhead doesn’t occur. 
2. It also saves the overhead of push/pop variables on the stack when a function is called. 
3. It also saves the overhead of a return call from a function. 
4. When you inline a function, you may enable the compiler to perform context-specific optimization on the body of the function. Such optimizations are not possible for normal function calls. Other optimizations can be obtained by considering the flows of the calling context and the called context. 
5. An inline function may be useful (if it is small) for embedded systems because inline can yield less code than the function called preamble and return.

Disadvantages
1. The added variables from the inlined function consume additional registers, After the in-lining function if the variable number which is going to use the register increases then they may create overhead on register variable resource utilization. This means that when the inline function body is substituted at the point of the function call, the total number of variables used by the function also gets inserted. So the number of registers going to be used for the variables will also get increased. So if after function inlining variable numbers increase drastically then it would surely cause overhead on register utilization. 
2. If you use too many inline functions then the size of the binary executable file will be large, because of the duplication of the same code. 
3. Too much inlining can also reduce your instruction cache hit rate, thus reducing the speed of instruction fetch from that of cache memory to that of primary memory. 
4. The inline function may increase compile time overhead if someone changes the code inside the inline function then all the calling location has to be recompiled because the compiler would be required to replace all the code once again to reflect the changes, otherwise it will continue with old functionality. 
5. Inline functions may not be useful for many embedded systems. Because in embedded systems code size is more important than speed. 
6. Inline functions might cause thrashing because inlining might increase the size of the binary executable file. Thrashing in memory causes the performance of the computer to degrade. The following program demonstrates the use of the inline function.