# Background
Primarily used for data manipulation within digital designs. Verilog can be used to describe and implement shift registers, but they are not one in the same. 

# Usage
## Shift Operators
| Operator | Description                                               | Syntax                                                                                               |
| -------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `<<`     | Left Shift (Bitwise). LSB padded with zeros.              | `x = x<<2` shifts two places to the left. x might be 1100 before shift, and 0000 after shift.        |
| `>>`     | Right Shift (Bitwise). MSB padded with zeros after shift. |                                                                                                      |
| `>>>`    | Unsigned Right Shift (Bitwise)                            |                                                                                                      |
| `? :`    | Conditional (Ternary) Operator                            | `condition ? value_if_true: value_if_false`                                                          |
| `{}`     | Concatenation                                             | `{co, sum} = a + b + ci` Add `a`, `b`, `c`, and assign overflow to `co`, and result to `sum`. Concat |
| `{{}}`   | Replication                                               | `b = {3{a}}`, replicate `a` 3 times (`{a, a, a}`)                                                    |



Normal shifts shift your input and pad with zeros. The arithmetic shift preserves the sign of the MSB of your variable. 

Shift operations in Verilog



## Example
Shift_operator.v
```verilog
module shift_operator();
	reg [3:0] r_Shift1 = 4'b1000;
	reg signed [3:0] r_Shift2 = 4'b1000;

	initial
		begin
		//left shift
		$display("%b", r_Shift1 <<  1);
      $display("%b", $signed(r_Shift1) <<< 1); // Cast as signed
      $display("%b", r_Shift2 <<< 1); // Declared as signed type // Right Shift $display("%b", r_Shift1 >>  2);
      $display("%b", $signed(r_Shift1) >>> 2); // Cast as signed
      $display("%b", r_Shift2 >>> 2) ;         // Declared as signed type
    end
endmodule
```
Simulation Output
```
0000
0000
0000
0010
1110
1110
```
