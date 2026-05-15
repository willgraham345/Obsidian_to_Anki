# Wire
- Used to represent a physical wire, and used for connection of gates or modules.  Can be read or assigned but no values are stored in them. They need to be driven by either continuous assign statement or from a port of a module. 
	- Can only be read and not assigned in a function or block. 
	- Cannot store value, but is always driven by a continuous assignment statement or by connecting wire to output of a gate/module
	- Wires in Verilog are directional, and data can only flow in one direction. 
## Syntax
```verilog
assign left_side = right_side; //This assigns the right side to CONTINUALLY be updated to the wire on the left side. Not a one-time event.
```
## Example in Instance
- **Wand (wired-AND)** − here value of Wand is dependent on logical AND of all the device drivers connected to it.
- **Wor (wired-OR)** − here value of a Wor is dependent on logical OR of all the device drivers connected to it.
- **Tri (three-state)** − here all drivers connected to a tri must be z, except only one (which determines value of tri).

## Example in Code
```verilog
Example: 
   Wire [msb:lsb] wire_variable_list; 
   Wirec // simple wire Wand d; 
   
   Assign d = a; // value of d is the logical AND of Assign d = b; // a and b Wire [9:0] A; // a cable (vector) of 10 wires. Wand [msb:lsb] wand_variable_list; 
   Wor [msb:lsb] wor_variable_list; 
   Tri [msb:lsb] tri_variable_list;
```

