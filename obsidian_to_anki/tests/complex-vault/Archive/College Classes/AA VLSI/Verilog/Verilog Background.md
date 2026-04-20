Hardware description language, used for describing a digital system

Designs, which are described in HDL, are independent of technology, very easy to design and debug, and are normally more useful than schematics, especially for large circuits.


# 3 Major Layers of Abstraction
## Behavior Level
- Concurrent algorithms. Every one is sequential, which means it is a set of instructions that are executed one by one. Functions, tasks, and blocks are the main elements. No regard for structural realization of the design
## Register-transfer Level
- Specify the characteristics of a circuit using operations and the transfer of data between the registers. Any code that is synthesizeable.
## Gate Level
- Within the logical level, the characteristics of a system are described by logical links and their timing properties. All signals are discrete signals, only with definite logical values (`0`, `1`, `X`, `Z`)
- Usable operations are predefined logic primitives (basic gates)
- May not be the right idea for logic design
- Code generated using tools like synthesis tools and netlist is used for gate level simulation and for backend. 

# Order of Operations
## Assign
- The order in which you program `assign` statements does not matter, they are continuous statements.
## Blocking vs Non-blocking
- Blocking operators must evaluate the right hand side of the assignment and complete the assignment without interruption from any other statement, meaning it stops other assignments until it is finished. 
- A non-blocking assignment evaluates the right hand side at the beginning of the time step and waits to assign it until the end, allowing for multiple assignments to be performed in parallel. 
### When should each case be used
- Sequential -> non-blocking
- Combinational -> blocking 


# Design Practices
- Unintentional latches are created when a signal is not assigned to a defined value. This can be done unintentionally by leaving inputs out of the sensitivity list.

