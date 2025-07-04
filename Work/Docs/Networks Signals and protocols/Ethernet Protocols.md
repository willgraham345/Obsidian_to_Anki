---
type: note/component
components:
  - "[[Ethernet Frame Overview]]"
  - "[[Ethernet IEEE 802 3]]"
  - "[[Fast Ethernet IEEE 802 3u]]"
concept_of:
  - "[[Networking]]"
---
[Tutorial website](https://www.lantronix.com/resources/networking-tutorials/ethernet-tutorial-networking-basics/)
After a physical connection has been made, network protocols define the standards that allow computers to communicate. 
- A protocol will define how computers identify one another on a network, the form the data should take in transit, and how this information is processed once it reaches its final destination. 
- Main types of protocols in use today:
	- TCP/IP
		- UNIX, Windows NT, Windows 95
	- IPX
		- Novell NetWare
	- DECnet
	- AppleTalk
		- Macintosh

# Standard Ethernet Code
**Guide to Ethernet Coding**
Basically how fast the ethernet is...

|            |                                                          |
| ---------- | -------------------------------------------------------- |
| **10**     | at the beginning means the network operates at 10Mbps.   |
| **BASE**   | means the type of signaling used is baseband.            |
| **2 or 5** | at the end indicates the maximum cable length in meters. |
| **T**      | the end stands for twisted-pair cable.                   |
| **X**      | at the end stands for full duplex-capable cable.         |
| **FL**     | at the end stands for fiber optic cable.                 |

Example: 100BASE-TX indicates a Fast Ethernet connection (100MBps) that uses a twisted pair capable of full-duplex transmission.

# Medium
Major types of media in use today
1. Thickwire (for 10BASE5 networks)
2. Thin coax (for 10BASE2 networks)
3. Unshielded twisted pair (UTP) (for 10BASE-T networks)
4. Fiber optic Inter-Repeater Link (FOIRL) (for 10Base-FL networks)

Most popular wiring schemes are 10BASE-T and 100BASE-TX
- Uses UTP cable, and comes in a variety of grades.