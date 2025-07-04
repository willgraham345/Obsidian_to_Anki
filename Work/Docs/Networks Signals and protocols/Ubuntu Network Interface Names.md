---
type: note/concept
component_of: ["[[Linux Networking and Internet]]"]
concept_of: ["[[Networking]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 11:30:01 am
---
## Interfaces
Names can vary based on the system. 

1. **en0 and eth0:**
    - `en0` is typically used on macOS for Ethernet interfaces.
    - `eth0` is commonly used on Linux for the first Ethernet interface.
	- A physical interface representing Ethernet network card. Used for communication with other computers on the network and on the internet.
2. **lo:**
    - `lo` stands for loopback. It's a virtual network interface that allows network communication with the local host. The IP address for `lo` is usually `127.0.0.1`.
3. **wl01:**
    - The naming convention `wl` is often used for wireless network interfaces. `wl01` could be a specific wireless interface on your system.
4. **docker0:**
    - `docker0` is the default bridge network created by Docker. It allows Docker containers to communicate with each other and the host system.

## Interface Details
`Link encap`
- Shows how packets are encapsulated for transmission. Most interfaces wrap packets in Ethernet frames
`HWaddr` 
- Hardware address of the ethernet interface
- The MAC address
`inet addr`
- IPv4 address assigned to the interface
`Bcast`
- Broadcast address for the interface
`Mask`
- Network mask for the interface
`inet6 addr`
- IPv6 address assigned to the interface
`Scope`
- Scope of IPV6 address. It can be `link-local` or `global`
- Global address is not routable
`UP`
- Indicates that kernel modules related to the interface have been loaded and interface is active
`BROADCAST`
- Indicates that interface is configured to handle broadcast packets, which is required for obtaining IP address via DHCP
`RUNNING`
- Indicates that interface is ready to accept data
`MULTICAST`
- Indicates that interface suppports multicasting
`MTU`
- Maximum transmission unit
- IP datagrams larger than MTU bytes will be fragmented into multiple Ethernet frames
`Metric`
- Determines the cost of using the interface.
- Interfaces with lower cost will have higher priority

## Interface Stats
`RX packets`
- Is a total number of packets received.

`RX errors` 
- Shows a total number of packets received with error. This includes too-long-frames errors, ring-buffer overflow errors, CRC errors, frame alignment errors, fifo overruns, and missed packets.

`RX dropped` 
- Is a number of dropped packets due to unintended VLAN tags or receiving IPv6 frames when interface is not configured for IPv6.

`RX overruns` 
- Is a number of received packets that experienced fifo overruns, caused by rate at which a buffer gets full and kernel isn’t able to empty it.

`RX frame` 
- Is a number of misaligned frames, i.e. frames with length not divisible by 8.

`TX packets` 
- Is total number of packets transmitted.

`TX errors`, `TX dropped` and `TX overruns` 
- Are similar to `RX` equivalents.

`TX carriers` 
- Is a number of packets that experienced loss of carriers. This usually happens when link is flapping.

`TX collisions` 
- Is a number of transmitted packets that experienced Ethernet collisions.

`TX txqueuelen` 
- Is length of transmission queue.

`RX bytes` 
- Is a total number of bytes received over interface.

`TX bytes` 
- Is a total number of bytes transmitted over interface.

## System d Naming Scheme
[Naming Scheme ](https://manpages.ubuntu.com/manpages/focal/man7/systemd.net-naming-scheme.7.html)
Names are generated from the **[systemd-udevd.service](https://manpages.ubuntu.com/manpages/focal/man8/systemd-udevd.service.8.html)**(8) service

| Prefix | Description                        |
| ------ | ---------------------------------- |
| `en`     | Ethernet                           |
| `ib`     | InfiniBand                         |
| `sl`     | Serial line IP (slip)              |
| `wl`     | Wireless local area network (WLAN) |
| `ww`     | Wireless wide area network (WWAN)                                   |

`docker0` is the default bridge created by Docker, allowing the containers to communicate with each other and the host system. 