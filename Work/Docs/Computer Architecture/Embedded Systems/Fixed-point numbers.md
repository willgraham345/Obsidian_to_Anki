---
type: note
---
Many embedded processors provide hardware for integer arithmetic only. Integer arithmetic,
however, can be used for non-whole numbers, with some care. Given, say, a 16-
bit integer, a programmer can imagine a binary point, which is like a decimal point,
except that it separates bits rather than digits of the number. For example, a 16-bit integer
can be used to represent numbers in the range 􀀀1:0 to 1:0 (roughly) by placing a
(conceptual) binary point just below the high-order bit of the number, as shown below:
![[Pasted image 20230810184234.png]]

Without the binary point, a number represented by the 16 bits is a whole number $x \in \{-2^{15}, \cdots , 2^{15} - 1\}$  (assuming the twos-complement binary representation, which has
become nearly universal for signed integers). With the binary point, we interpret the
16 bits to represent a number y = x=215. Hence, y ranges from 􀀀1 to 1􀀀2􀀀15. This is
known as a fixed-point number. The format of this fixed-point number can be written
1.15, indicating that there is one bit to the left of the binary point and 15 to the right.
When two such numbers are multiplied at full precision, the result is a 32-bit number.
The binary point is located as follows:
![[Pasted image 20230810184243.png]]


The location of the binary point follows from the law of conservation of bits. When
multiplying two numbers with formats n:m and p:q, the result has format $(n+p)*(m+
q)$ Processors often support such full-precision multiplications, where the result goes
into an accumulator register that has at least twice as many bits as the ordinary data
registers. To write the result back to a data register, however, we have to extract 16
bits from the 32 bit result. If we extract the shaded bits on page 235, then we preserve
the position of the binary point, and the result still represents a number roughly in the
range -1 to 1.
There is a loss of information, however, when we extract 16 bits from a 32-bit result.
First, there is a possibility of overflow, because we are discarding the high-order bit.
Suppose the two numbers being multiplied are both 􀀀1, which has binary representation
in twos complement as follows:
![[Pasted image 20230810184306.png]]