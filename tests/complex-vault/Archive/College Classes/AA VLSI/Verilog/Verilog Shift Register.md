# Background
$N$ flip flops connected in order to store $n$ bits of data
- A register is a device that is used to store such information, 
Used to store and shift data
- Can be used for data storage, serial-to-parallel conversion, or creating delays
## Applications
- Temporary data storage
- Data transfer and data manipulation
- SISO and PIPO used to produce time delay to digital circuits
- SIPO used to convert serial data into parallel data
	- Communication lines where demultiplexing of a data line into several parallel lines is required
- PISO used to convert parallel data to serial data


# Shift Operator in Verilog
Not the same thing as this. See [[Verilog Shift Operators]]

# Examples of Shift Registers
## Types of Shift Registers
- Serial In Serial Out (SISO)
	- ![[Pasted image 20230922112608.png]]
- Serial In Parallel Out (SIPO)
	- ![[Pasted image 20230922112631.png]]
- Parallel In Serial Out  (PISO)
	- ![[Pasted image 20230922112638.png]]
- Parallel In Parallel Out (PIPO)
	- ![[Pasted image 20230922112644.png]]
- Bidirectional Shift Register
	- ![[Pasted image 20230922112650.png]]
- Universal Shift Register
	- ![[Pasted image 20230922112655.png]]
- Shift Register Counter
	- Ring Counter
	- Johnson Coutner

