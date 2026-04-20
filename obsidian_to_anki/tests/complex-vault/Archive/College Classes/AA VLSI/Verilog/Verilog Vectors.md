# Background
- NOT a lexical element, but rather a grouping of things
- Vectors are used to group related signals and make manipulation easier
- Must be declared and typed
	- usually `wire` or `reg`
- Once you declare a vector with a specific endian type (i.e. \[3:0] or \[0:3]), it must always be declared the same way

# Syntax
```verilog
type [upper:lower] vector_name;
```
## Other examples
```verilog
wire [7:0] w;         // 8-bit wire
reg  [4:1] x;         // 4-bit reg
output reg [0:0] y;   // 1-bit reg that is also an output port (this is still a vector)
input wire [3:-2] z;  // 6-bit wire input (negative ranges are allowed)
output [3:0] a;       // 4-bit output wire. Type is 'wire' unless specified otherwise.
wire [0:7] b;         // 8-bit wire where b[0] is the most-significant bit.
```

# Common Issues
## Implicit Nets
- Often a source of hard-to-detect bugs. Net-signals can be implicitly created by an `assign` statement or by attaching something undeclared to the module port. 
```verilog
wire [2:0] a, c;   // Two vectors
assign a = 3'b101;  // a = 101
assign b = a;       // b =   1  implicitly-created wire
assign c = b;       // c = 001  <-- bug
my_module i1 (d,e); // d and e are implicitly one-bit wide if not declared.
                    // This could be a bug if the port was intended to be a vector.
```

### Possible Solution
``` verilog 
`default_nettype none  // Disable implicit nets. Reduces some types of bugs.
```
## Unpacked vs Packed Arrays
The vector indices are written before the vector name. This declares the "packed" dimensions of the array, where the bits are "packed" together into a blob. 
- Unpacked dimensions are declared after the name. Generally used to declare memory arrays. 
```verilog
reg [7:0] mem [255:0];   // 256 unpacked elements, each of which is a 8-bit packed vector of reg.
reg mem2 [28:0];         // 29 unpacked elements, each of which is a 1-bit reg.
```

## Accessing Vector Elements
```verilog
w[3:0]      // Only the lower 4 bits of w
x[1]        // The lowest bit of x
x[1:1]      // ...also the lowest bit of x
z[-1:-2]    // Two lowest bits of z
b[3:0]      // Illegal. Vector part-select must match the direction of the declaration.
b[0:3]      // The *upper* 4 bits of b.
assign w[3:0] = b[0:3];    // Assign upper 4 bits of b to lower 4 bits of w. w[3]=b[0], w[2]=b[1], etc.
```

## Bitwise vs Logical Operators and Vectors
Bitwise operation: Two N-bit vectors have the operation repeated for each bit of the vector and produces an N-bit output. 
Logical Operation: Treats the entire vector as a boolean value and produces a 1-bit output

```verilog
module top_module( 
    input [2:0] a,
    input [2:0] b,
    output [2:0] out_or_bitwise,
    output out_or_logical,
    output [5:0] out_not);
	    assign out_or_bitwise = a | b;
	    assign out_or_logical = (a | b) != 3'b000; // Check if all bits are 0
	    assign out_not[5:3] = ~b;
	    assign out_not[2:0] = ~a;
    
endmodule
```

### Performing a Bitwise Operation on a Vector
```verilog
module top_module( 
    input [3:0] in,
    output out_and,
    output out_or,
    output out_xor
);
    assign out_and = &in; //bitwise and on the vector 
    assign out_or = |in; // bitwise or on the vector
    assign out_xor = ^in; // bitwise Xor on the vector

endmodule
```


## Vector Concatenation Operator