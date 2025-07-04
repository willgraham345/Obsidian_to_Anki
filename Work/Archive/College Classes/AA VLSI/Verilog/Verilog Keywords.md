Similar to C


| Keyword        | Description                                               |
| -------------- | --------------------------------------------------------- |
| `always`       | Specifies a block of code to be executed continuously.    |
| `always_comb`  | Specifies a combinational logic always block.             |
| `always_ff`    | Specifies a flip-flop-based always block.                 |
| `always_latch` | Specifies a latch-based always block.                     |
| `assign`       | Assigns a value to a wire.                                |
| `begin`        | Begins a block of code.                                   |
| `case`         | Starts a case statement.                                  |
| `defparam`     | Defines a parameter only at compilation time [[Verilog Parameters]]                                                          |
| `default`      | Specifies the default case in a case statement.           |
| `else`         | Specifies an alternative in conditional statements.       |
| `end`          | Ends a block of code.                                     |
| `endcase`      | Ends a case statement.                                    |
| `endfunction`  | Ends a user-defined function.                             |
| `endgenerate`  | Ends code generation.                                     |
| `endmodule`    | Ends the module declaration.                              |
| `for`          | Looping construct.                                        |
| `forever`      | Creates an infinite loop.                                 |
| `function`     | Declares a user-defined function.                         |
| `if`           | Conditional statement.                                    |
| `inout`        | Declares a bidirectional port.                            |
| `input`        | Declares an input port.                                   |
| `localparam`   | Declares a local parameter for a module.                  |
| `module`       | Declares a hardware module. See [[Verilog Module]]        |
| `negedge`      | Specifies the falling edge of a clock signal.             |
| `output`       | Declares an output port.                                  |
| `parameter`    | Declares a parameter for a module. [[Verilog Parameters]] |
| `posedge`      | Specifies the rising edge of a clock signal.              |
| `reg`          | Declares a register for storing values.                   |
| `repeat`       | Looping construct.                                        |
| `wait`         | Pauses simulation.                                        |
| `while`        | Looping construct.                                        |
| `wire`         | Declares a wire for connecting signals.                   |

# Comments
`//` = single line comment
`/* */` = multi-line comment


# Numbers
Can be described in binary, octal, decimal, or hexadecimal format
- Negative numbers are represented in 2's compliment numbers.

`<size> <radix> <value>`
- Size or unsized number is in size
- Radix can be binary, octal, hexadecimal, or decimal

