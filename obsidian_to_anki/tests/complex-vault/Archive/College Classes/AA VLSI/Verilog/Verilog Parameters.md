A constant value that you can define within a Verilog module or design file that makes code more flexible and configurable. 

Different types of parameters
- Compile time `defparam`
- Module parameters
	- Can be used to override parameter definitions within a module. 

## Module Parameter Syntax
```verilog
module an_example #(parameter PAR_A, PAR_B, PAR_C) 
	( input port_in, output port_out ); 
//module body endmodule
```
## Instantiation of Parameterized Modules
```verilog
A_module #( .A_PARAMETER(a_constant_value), .ANOTHER_PARAMETER(7) ) 
	an_instance_name ( .a_port(a_wire), .another_port(another_wire_or_constant) )
```


## Using Parameters with Generate Statements
