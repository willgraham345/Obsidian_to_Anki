# Background
- Multiple-input, multiple-output logic circuit for converting coded inputs into coded outputs where input and output codes are different. 
	- The input generally has fewer bits than the output code, and there is one-to-one mapping from input code words into output code words. 
 - Outputs on the 
- A 4:16 decoder decodes four binary weighted address inputs (A0 to A3) to sixteen mutually exclusive outputs (Y0 to Y15). 
- The reverse of an encoder
![[binary-decoder-truth-table.webp]]
## Most common Version 
- For $n$ inputs, it gives $2^n$ outputs
	- The input code lines select which output is active. The remaining output lines are disabled. 
	- Intended to provide a binary code to other circuits (such as a memory circuit)
- A decoder is mainly composed of an NAND circuit. 
# Verilog Code

## Binary Decoder Using Verilog Code
```verilog
module binary_decoder(
  input [2:0] D,
  output reg [7:0] y);
  
  always@(D) begin
    y = 0;
    case(D)
      3'b000: y[0] = 1'b1;
      3'b001: y[1] = 1'b1;
      3'b010: y[2] = 1'b1;
      3'b011: y[3] = 1'b1;
      3'b100: y[4] = 1'b1;
      3'b101: y[5] = 1'b1;
      3'b110: y[6] = 1'b1;
      3'b111: y[7] = 1'b1;
      default: y = 0;
    endcase
  end
endmodule
```
### Testbench
```
module tb;
  reg [2:0] D;
  wire [7:0] y;
  
  binary_decoder bin_dec(D, y);
  
  initial begin
    $monitor("D = %b -> y = %0b", D, y);
    repeat(5) begin
      D=$random; #1;
    end
  end
endmodule
```