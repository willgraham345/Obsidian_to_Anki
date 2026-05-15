# Background
An encoder converts $M$ input lines to coded $N$ output lines. Various encoders can be designed like decimal-to-binary encoders, octal-to-binary encoders, decimal-to-BCD encoders, etc

Shrinks many input data lines to the output lines. Helpful in reducing input data lines for further processing

Composed of a bunch of OR gates connecting the inputs. 
# I/O
## Input
- $M$
	- Can be decimal, hex, octal, etc
## Output
- $N$
	- 


# Binary Encoder
- Converts $M = 2^n$ input lines to $N = n$ coded binary code. Also known as a digital encoder. 
- A single input line must be high for valid coded output, otherwise the output line will be invalid. The priority encoder prioritizes each input line when multiple output lines are set to high

## 8:3 Binary Encoder
![[binary-encoder.webp]]
![[binary-encoder-truth-table-1024x566.webp]]
![[Pasted image 20231027151004.png]]
### Logical Expresions
$y_2 = D_4 + D_5  + D_6 + D_7$
$y_1 = D_2 + D_3 + D_6 + D_7$
$y_0 = D_1 + D_3 + D_5 + D_7$

### Verilog Code
```verilog
module binary_encoder(
  input [7:0] D,
  output [2:0] y);
  
  assign y[2] = D[4] | D[5] | D[6] | D[7];
  assign y[1] = D[2] | D[3] | D[6] | D[7];
  assign y[0] = D[1] | D[3] | D[5] | D[7];
endmodule
```
##### Testbench
```verilog
module tb;
  reg [7:0] D;
  wire [2:0] y;
  int i;
  
  binary_encoder bin_enc(D, y);
  
  initial begin
    D=8'b1; #1;
    for(i=0; i<8; i++) begin
      $display("D = %h(in dec:%0d) -> y = %0h", D, i, y);
      D=D<<1; #1;
    end
  end
endmodule
```