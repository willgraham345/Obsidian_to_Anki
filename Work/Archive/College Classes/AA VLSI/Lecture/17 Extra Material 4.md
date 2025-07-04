# SOC
A system built on the same silicon substrate, composed of active parts which are usually found on other packages
What is the difference between a microprocessor and a microcontroller
- A microprocessor is just a CPU
- A microcontroller has memory, peripherals and a CPU

We built a microprocessor composed of:
- CPU core
- Register file


## Architecture, what should we know
There are many different types

What's important to know is to have a solid general background on everything
- The same parallel can be made in the research world
	- Architecture
		- What kind of cache, hardware acccelerator, and all that stuff. But they don't know how to make a chip. 
		- They model stuff with C and Python
	- SOC
		 - They may know a bit about architecture, but they aren't the best
	- VLSI
		 - No idea how to build a chip
- ARM or Intel
	- Microprocessor microarchitecture
	- ISA extension
- L3Harris
	- How do we build a good DSP?
- ARM
	- CPU Intellectual Property

Get the depth once you get into a career
- 


# Hardware Accelerator
What accelerators do?
Everything that you want to do in a better way (faster, energy)
## Examples
A multiply unit counts as an accelerator
- You can emulate multiplication with basic shifts and addition
Regular multiplications vs floating point multiplications
- On a CPU
- Floating point multiplier
	- A piece of hardware that gets two pieces of data
	- A specialized piece of silicon that can multiply in one clock cycle
Other Examples
- There are convolution accelerators
- Signal processing FLIR

# Difference between CPU and GPU
- Microarchitecture is different than VLSI perspective

DSPs
- CPUs optimized for vector math
- Single instruction operating on multiple data

GPU is the same as a DSP but on steroids
- Thousands of small ALUs that work on a chunk of data at the same time

The compiler has to know that it has this processor within the system. 


# How does a compiler work, and a Hardware Accelerator?
How is it done?
- One of the instructions introduced in x86 by intel
	- SIMD instructions
	- There are instructions for the compiler
	- Compilers are capable of 
- Use Libraries
	- CUDA in GPUs
	- Specific programming language for Nvidia GPUs
		- `a*b` can be translate into Nvidia who roped the DMA and instruction to run the stuff
What if I have a custom?
- How do you make your crap work with the MMX instruction


Very likely, you'll need to control the accelerator from a piece of embedded software
- We've removed FSM and now we use CPUs
- A hardware-software codesign problem
	- Similar to what we do in embedded systems
	- A software play that requires a ton of knowledge about the hardware


For CE, EE and lots of CS you need to learn with C
- C -> C++ for object oriented
	- Garbage collection and stuff like that is important
- Bash used to be the scripting language
- A little bit of web-based language (GUIs and other crap)

# Direction of the Field
We will keep abstracting things
- The future is heading towards: Translate a piece of C code into Verilog
	- We aren't there yet, because the tools aren't there yet

Bypass intermediate steps that used to exist
- We went through verilog, because you need to know how that works. 
	- It's unlikely that we will write Verilog for our career, but it is likely that we will need to understand it at a basic level and we WILL read it a lot.
 - In software, we can make the same parallel
	 - In software, it is easier because its just binding libraries
		 - Hardware is more difficult
	- 

# When we buy IPs what do we get?
Soft IP = RTL and that's it
Hard macros = actual layout
For something simple like an ARM, you can synthesize the stuff yourself
- If you are a person like Apple, then they'll send you 50 ARM Engineers to get it figured out. 

You'd buy the RTL so you can get timing specific stuff nailed down. 


# If you graduated right now, what would you try to do?
Go into design?
AI-based stuff is hyped right now

# Why is it a waste to go into industry?
1. You're kind of wasting your time for a couple of years
2. It's hard to come back to studying
You start faster on a career path once you've had a masters
- Hard to deal with that once you have a PhD


Hardware likes PhDs, software does not
- There's a high number of people with grad studies