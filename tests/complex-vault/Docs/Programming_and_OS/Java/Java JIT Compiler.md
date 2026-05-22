---
type: note
---
# Background
- Essential part of the [[Java JRE]] responsible for performance optimization of java based applications during run time. 
- The greater degree of optimization the more time a JIT compiler spends in the execution stage.
## Bytecode
- Bytecodes have to be interpreted or compiled to proper machine instructions depending on the ISA. These can be directly executed in the ISA as bytecode-based.
- Interpreting the bytecode affects the speed of execution
- JIT compilers interact with the JVM at runtime and compile suitable bytecode sequences into native machine code. 

![[Pasted image 20240317170649.png]]