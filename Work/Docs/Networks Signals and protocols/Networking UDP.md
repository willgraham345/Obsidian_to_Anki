---
type: note
---
# Background
UDP = user datagram protocol
- Really fast, low overhead, continuous, message stream.
- Enables data transfer before the receiving party provides an agreement. 
- Unreliable and connectionless protocol. 

[More UDP Info](https://www.geeksforgeeks.org/user-datagram-protocol-udp/)

# Components
## Header
8 bytes fixed and simple header (corresponds to 64 bits detailed below)

| Data | Bit Number |
| ---- | ---- |
| Source Port | 16 bits |
| Destination Port | 16 bits |
| Length | 16 bits |
| Checksum | 16 bits |
- Checksum is NOT mandatory
## Ports
The transport layer is where TCP lives and is also known as the internet layer. 

# Usage
[Remote Control Microcontroller with UDP](https://wiki.microblocks.fun/en/wifi/udp)
[Comunication between two ESP32s via UDP](https://www.aranacorp.com/en/communication-between-two-esp32s-via-udp/)