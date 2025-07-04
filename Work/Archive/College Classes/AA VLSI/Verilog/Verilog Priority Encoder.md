# Background
A priority encoder can overcome the drawback of a binary encoder that generates invalid output for more than one input line is set to high. 

The priority encoder prioritize each input line and provides an encoder output corresponding to its highest input priority

Used widely in digital applications
- Microprocessor detecting the highest priority input
- Priority encoders are also used in navigation systems, robotics for controlling arm positions, communication systems, etc.

![[priority-encoder-truth-table-1024x563.webp]]
# I/O


# Verilog Code
```verilog
module priority_encoder(
  input [7:0] D,
  output reg [2:0] y);
  
  always@(D) begin
    casex(D)
      8'b1xxx_xxxx: y = 3'b111;
      8'b01xx_xxxx: y = 3'b110;
      8'b001x_xxxx: y = 3'b101;
      8'b0001_xxxx: y = 3'b100;
      8'b0000_1xxx: y = 3'b011;
      8'b0000_01xx: y = 3'b010;
      8'b0000_001x: y = 3'b001;
      8'b0000_0001: y = 3'b000;
      default: $display("Invalid data received");
    endcase
  end
endmodule
```


```verilog
module tb;
  reg [7:0] D;
  wire [2:0] y;
  
  priority_encoder pri_enc(D, y);
  
  initial begin
    $monitor("D = %b -> y = %0b", D, y);
    repeat(5) begin
      D=$random; #1;
    end
  end
endmodule
```