Lexical conventions are close to the C++ language.
- Comments are `//` and `/* */`
- Spaces are important in that they delimit tokens in the language

## Traditional form
```verilog
<size><base format><number>
```
- `<size>` = decimal digits that specify size of the constant in number of bits
	- Optional
- `<base format>` = Single character ' followed by one of the following numbers `b`, `d`, `o`, `h`.
- `<number>` = Digits which are legal for the `<base format>`
## Program Structure
```verilog
module <modulename> (<port list>);
<declares>
<module items>
endmodule
```