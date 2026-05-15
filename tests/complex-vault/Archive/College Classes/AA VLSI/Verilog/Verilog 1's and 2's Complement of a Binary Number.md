# Background
- 2's complement is a binary representation scheme used to represent both positive and negative integers. It is the most common method of representing fixed point binary values. It is used because:
	- It's simple to add (adding positive and negative numbers is the same as adding their magnitudes and keeping the sign)
	- No separate subtraction, as subtraction can be performed using addition. This simplifies hardware design. 
	- Single representation for both positive and negative numbers
	- Efficient for hardware implementation, as it avoids the need for separate sign bits and complex comparison logic. 
- 2's complement is an operator to find the negative of another given number, so we do only addition. 

## 1's Complement
1's complement of a number is the inversion of that same number. 
## 2's complement
2's complement of a binary number is 1, added to the 1's complement of the binary number

The MSB (most significant bit) represents the sign with a `0` used for plus sign and a `1` used for a minus sign. 
- The remaining bits are used for representing magnitude
	- Positive magnitudes are represented the same way as in the case of sign-bit or 1's complement representation. 
	- Negative magnitudes are represented by the 2's complement of their positive counterparts. 


## Example of Adding 2's Complement