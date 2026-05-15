---
type: note
---
# Background
CAN = Controller Area Network
- 2-wire serial bus specified by Bosch CAN specification
- Has a flexible data-rate specification and ISO 11898-1:2003 standard
- CAN is used extensively in the automotive industry but also in home and industrial automation
	- e
## ISO 11898-1:2003
![[can_timing.svg]]
A single bit is split into four segements:
- Sync_Seg: The nodes synchronize at the edge of the Sync_Seg. It is always one time quantum in length.
- Prop_Seg: The signal propagation delay of the bus and other delays of the transceiver and node.
- Phase_Seg1 and Phase_Seg2 :Define the sampling point. The bit is sampled at the end of Phase_Seg1.

Timing parameters are set within zephyr from the device-tree and can be changed at run-time from the timing API

CAN uses so-called identifiers to identify the frame instead of address to identify a node. 
- Identifiers can have 11-bit width (standard or basic), or 29-bit in an extended frame
	- Zephyr supports both concurrently

Masking techniques are used to ensure that only relevant identifiers of interest are given to a specific node. An identifier that doesn't match any filter is ignored. 
- Most CAN controllers implement a limited number of filters in hardware
- Number of filters is also limited in Kconfig to save memory
## Applications
- Passenger vehicles, trucks, buses (combustion vehicles and electric vehicles)
- Agricultural equipment
- Electronic equipment for aviation and navigation
- Industrial automation and mechanical control
- Elevators, escalators
- Building automation
- Medical instruments and equipment
- [Pedelecs](https://en.wikipedia.org/wiki/Pedelec "Pedelec")
- [Model railways](https://en.wikipedia.org/wiki/Model_railway "Model railway")/railroads
- Ships and other maritime applications
- Lighting control systems
- 3D Printers
- Robotics/Automation

## Lines within CAN
Wires use logic levels whereas the bus-level is interpreted differentially between CAN H and CAN L. The bus can be either in the recessive (logical one), or dominant (logical zero) state. 
- CAN H = CAN High
- CAN L = CAN Low
- CAN TX = transmit wire from controller to transceiver
- CAN RX = receive wire from controller to transceiver



# Usage
[[Zephyr Networking CAN Sending Data]]
[[Zephyr Networking CAN Receiving Data]]