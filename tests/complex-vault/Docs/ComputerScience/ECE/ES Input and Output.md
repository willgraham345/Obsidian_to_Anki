---
type: note
date created: Tuesday, August 20th 2024, 2:05:32 pm
date modified: Friday, October 11th 2024, 1:23:03 pm
---
- Reconciling two disparate properties of software (sequential) and physical (many things happen at once) is challenging and often the biggest risk in designing an embedded system.

# I/O Hardware
- Embedded processors, typically include a number of I/O mechanisms on a chip, exposed to designers as pins of the chip.
- We develop software for the board using an IDE from the vendor, and load software onto flash memory. Alternatively, software might be loaded through USB interface.

## GPIO (General Purpose I/O)
- When interfacing hardware to GPIO pins, you need to understand the specifications of the device. 
- **Scmitt Triggered** = Hysteresis may be involved
- **Pull-up resistor** = A shared line which brings the voltage of the line up to $V_{DD}$ when all transistors are turned off. If any transistor is turned on, then it will bring the voltage of the entire line down to (near) zero without creating a short circuit with the other GPIO pins. 
	- Assuming active high logic, the logical function being performed is NOR, so such a circuit is called a wired NOR. 
	- ![[Pasted image 20230811181626.png | 500]]
	- GPIO outputs may also be realized with **tristate logic** which means that in addition to producing an output high or low voltage, the pin may be simply turned off. 

## Serial Interfaces
- Serial interfaces efficiently use pins and wires to send information serially as sequences of bits.
- **RS-232** was a standard introduced in 1962 to connect teletypes to modems. It's simple, and defines electrical signals and connector types. Persists due to its simplicity and because of continued prevalence of aging industrial equipment. The standard defines how one device can transmit a bite to another device asynchronously. 
	- Can be slow, and may slow down application software
	- May use a DB-9 connector (huge old-school terrible cords with like 1000 connectors)
- **UART** = universal asynchronous receiver/transmitter converts the contents of an 8-bit register into a sequnce of bits for transmission. 
- The RS-232 mechanism description
	- Sender and receiver agree on transmission rate (this is slow by modern standards)
	- Sender initiates transmission of a byte with a start bit
	- Sender clock out the sequence of bits at the agreed-upon rate, following them up by one or two stop bits
	- Receiver's clock resets upon receiving the start bit and is expected to track the sender's clock closely enough to be able to sample the incoming signal sequential and recover the sequence of bits.
- **USB** supports rates up to 4.8 Gbits/sec
	- Simpler than RS-232 and uses simpler, more robust connections
	- USB defines more than electrical transport of bytes, and more complicated control logic is required to support it. 
- **JTAG** = Joint Test Action Group (IEEE 1149.1 standard)
	- **Boundary scan** allows the state of a logical boundary of a circuit (what would traditionally have been pins accessible to probes) to be read or written serially through pins that are made accessible.
	- JTAG ports are used to provide a debug interface to embedded processors, enabling a PC-hosted debugging environment to examine and control the state of an embedded processor
- **SWD** = Serial wire debug, a newer variant of JTAG with fewer pins.
- There are other serial interfaces like I2C, SPI, PCI Express, FreeWire, MIDI, SCSI

### Parallel Interfaces
- A serial interface sends a sequence of bits sequentially, while parallel uses multiple lines to simultaneously send bits. 
	- Each line of a parallel interface is also a serial interface.
- IEEE-1284 printer is one of the most widely used interfaces. 
- Doesn't necessarily deliver higher performance than serial communication. 

### Buses
- **Bus** = an interface shared among multiple devices, in contrast to point-to-point interconnection linking exactly two devices. 
	- Can be serial interfaces or parallel interfaces
- **SCSI** = small computer system interface. Used to connect hard drives and tape drives to computers
	- Peripheral bus architecture (connecting a computer to peripherals)
- **ISA** = industry standard architecture (used in the IBM PC architecture)
- **PCI** = peripheral component interface
- **Parallel ATA** = parallel advanced technology attachment. 
- **IEEE-488** = Kind of peripheral bus standard. Designed at HP, and widely known as HP-IB and GPIB. M
- Because a bus is shared by many devices, any bus architecture must include a **MAC** protocol to arbitrate competing access. A MAC protocol has a single bus master that interrogates bus slaves.
	- An alternative is a time-triggered bus, where devices are assigned time slots during which they can transmit. 
	- Token ring, is where devices on the same bus must acquire a token before they can use the shared medium
	- Bus arbiter, which is a circuit that handles requests for the bus according to some priorities
	- **CSMA** = carrier sense multiple access, where devices sense the carrier to determine whether the medium is in use before beginning to use it, detect collisions that might occur when they begin to use it, and try again later when a collision occurs

# Sequential Software in a Concurrent World
## Interrupts and Exceptions
- **Interrupt** = a mechanism for pausing execution of whatever a processor is currently doing and executing a pre-defined code sequence called an ISA (interrupt service routine) or interrupt handler
	- Hardware interrupt = external hardware changes the voltage level on an interrupt request line. Program resumes where it left off.
	- Software interrupt = the program that is executing triggers the interrupt by executing an instruction or by writing to a memory-mapped register. Program resumes where it left off
	- Exception = the interrupt is triggered by internal hardware that detects a fault, such as a segmentation fault. Program that triggered the exception is NOT normally resumed, but the program counter is set to some fixed location (the OS may then try to terminate the program)
- Upon occurrence of an interrupt, the hardware must first decide whether to respond. The mechanism for enabling or disabling interrupts varies by processor. Moreover, it may be that some interrupts are enabled and others are not. Interrupts and exceptions generally have priorities, and an interrupt will be serviced only if the processor is not already in the middle of servicing an interrupt with a higher priority. Typically, exceptions have the highest priority and always serviced. 
	- When hardware services an interrupt, it will usually first disable interrupts, push the current program counter and processor status registers onto the stack, and branch to a designated address that will normally contain a jump to an ISR.
- **PIT** = Programmable interval timer, a peripheral device that simply counts down from some value to zero. Initial value is set by writing to a memory-mapped register, and when the value hits zero, the PIT raises an interrupt request.

## Atomicity
## Interrupt Conrollers
- **Interrupt controller** = the logic in the processor that handles interrupts. 
	- Supports some number of interrupts and some number of priority levels. 
- **Interrupt vector** = address of an ISR or an index into an arary called the **interrupt vector table** that contains the addresses of all the ISR's
- **Level triggered** = hardware asserting the interrupt will typically hold voltage on the line until it gets an acknowledgment, which indicates that the interrupt is being handled.
- **Edge triggered** = hardware asserting interrupt changes the voltage for only a short time
- Open collector lines are used in both cases

## Modeling Interrupts
- **FSM** = State machine, which is a model of a system with discrete dynamics that at each reaction maps valuations of the inputs to valuations of the outputs, where the map may depend on its current state. A FSM, is when the set States of the possible states is finite. 
	- ![[Pasted image 20230814145115.png]]
- **Device Driver** = Software that uses mechanisms for interrupts to provide I/O to an external device