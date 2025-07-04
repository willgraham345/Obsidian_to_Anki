A.k.a "Mux"
- Digital element that transfers data from one of the $N$ inputs the the output based on the select singal![[Pasted image 20230922114656.png]]

## Sample Verilog Code
### Using Assign
```verilog
module mux_4to1_assign (input [3:0] a,
					   input [3:0] b,
					   input [3:0] c,
					   input [3:0] d,
					   input [1:0] sel,
					   output [3:0] out);
	assign out = sel[1] ? (sel[0] ? d : c) ? (sel[0] ? b : a);
	// when sel[1] is 0, (sel[0]? b:a) is selected. When sel[1] is 1, (sel[0]? d:c) is taken
					   
					   )
```

More code snippets here [VLSIVerify](https://vlsiverify.com/verilog/verilog-codes/multiplexer):


# Examples
## 2:1 MUX
```verilog
module mux_2_1(
  input sel,
  input i0, i1,
  output y);
  
  assign y = sel ? i1 : i0;
endmodule
```

```verilog
module mux_tb;
  reg i0, i1, sel;
  wire y;
  
  mux_2_1 mux(sel, i0, i1, y);
  initial begin
    $monitor("sel = %h: i0 = %h, i1 = %h --> y = %h", sel, i0, i1, y);
    i0 = 0; i1 = 1;
    sel = 0;
    #1;
    sel = 1;
  end
endmodule
```
## 4:1 MUX
```verilog
module mux_example(
  input [1:0] sel,
  input  i0,i1,i2,i3,
  output reg y);
    
  always @(*) begin
    case(sel)
      2'h0: y = i0;
      2'h1: y = i1;
      2'h2: y = i2;
      2'h3: y = i3;
      default: $display("Invalid sel input");
    endcase
  end
endmodule
```
## 4:1 MUX using 2:1 MUXes
```verilog
module mux_2_1(
  input sel,
  input i0, i1,
  output y);
  
  assign y = sel ? i1 : i0;
endmodule

module mux_4_1(
  input sel0, sel1,
  input  i0,i1,i2,i3,
  output reg y);
  
  wire y0, y1;
  
  mux_2_1 m1(sel1, i2, i3, y1);
  mux_2_1 m2(sel1, i0, i1, y0);
  mux_2_1 m3(sel0, y0, y1, y);
endmodule
```

## Testbench
```verilog
module tb;
  reg sel0, sel1;
  reg i0,i1,i2,i3;
  wire y;
  
  mux_4_1 mux(sel0, sel1, i0, i1, i2, i3, y);
  
  initial begin
    $monitor("sel0=%b, sel1=%b -> i3 = %0b, i2 = %0b ,i1 = %0b, i0 = %0b -> y = %0b", sel0,sel1,i3,i2,i1,i0, y);
    {i3,i2,i1,i0} = 4'h5;

    repeat(6) begin
      {sel0, sel1} = $random;
      #5;
    end
  end
endmodule
```