# Background
Does the multiplication of 2's complement notation of two signed binary numbers

[More info](https://vlsiverify.com/verilog/verilog-codes/booth-multiplier)

## Pros
- Less complicated
- Faster multiplication
- Consecutive additions are replaced
- Ease in scaling
## Disadvantage
- High power consumption
- Large chip area

# Flow Chart
- $A$ = holds multiplicand
- $B$ = holds multiplier
- $Q = B$
- $Q_0$ = holds 0th bit (LSB) of Q register
- $Q_1$ = 1 bit variable/register
- $A_{cc}$  = Accumulator holds the result of intermediate addition/subtraction
- Count = max(width of multiplicand register, width of multiplied register)
![[Booth-Multiplier-Algorithm.webp]]