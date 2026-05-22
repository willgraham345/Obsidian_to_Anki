---
summary: A 5 layer model, coming before the OSI model. It has a much simpler model, as some functions are encompassed in a single layer. Implemented far more than the OSI model.
headings: ["[[#Concepts of Note]]", "[[#Diagrams]]"]
type: note/system
concepts: ["[[Networking TCPIP Cybersecurity]]"]
similar: ["[[OSI Network Model]]"]
aliases: [TCPIP Model]
concept_of: ["[[Networking]]", "[[OSI Network Model]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, October 8th 2025, 11:06:20 am
images: ["[[TCPIP model.jpg]]"]
items: ["[[Networking Application Layer|TCPIP Application Layer 1]]", "[[TCP Protocol Suite]]", "[[TCPIP Hardware Layer 5]]", "[[TCPIP Network Access Layer 3]]", "[[TCPIP Network Interface Layer 4]]", "[[TCPIP Transport Layer 2]]", "[[UDP Protocol Suite]]"]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Good Overview of TCP/IP](https://www.techtarget.com/searchnetworking/definition/TCP-IP)
[Oracle's TCP/IP Admin Guide](https://docs.oracle.com/cd/E19504-01/802-5753/index.html)

## Concepts of Note
### Layers and quick description
[[TCPIP Application Layer 1]]
󰙎  TCPIP Application Layer 1 ;;; Where data originates on the sender’s side. Applications are used to create the data. A web browser, for example, is used to generate the data that gets sent through the rest of the layers, assisted by the Domain Name System (DNS), which associates web domain names with their Internet Protocol (IP) addresses. = #cs/networking/tcp-ip/layers/application
<!--ID: 1759154339969-->


[[TCPIP Transport Layer 2]]
󰙎  TCPIP Transport Layer 2 ;;; Data gets encoded so it can be transported through the internet using either the User Datagram Protocol (UDP) or TCP. = #cs/networking/tcp-ip/layers/transport
<!--ID: 1759154339973-->

[[TCPIP Network Access Layer 3]]
󰙎  TCPIP Network Access Layer 3 ;;; Data gets a header and a trailer, and these tell the data where to go. This information is then conveyed to the network interface layer. = #cs/networking/tcp-ip/layers/network-access
<!--ID: 1759154339979-->

[[TCPIP Network Interface Layer 4]]
󰙎  TCPIP Network Interface Layer 4 ;;; The packet gets formatted and prepared to be transported and routed through the network. = #cs/networking/tcp-ip/layers/network-interface
<!--ID: 1759154339984-->

[[TCPIP Hardware Layer 5]]
󰙎  TCPIP Hardware Layer 5 ;;; The data is turned into something that can be sent and read by a computer or other device. (i.e. IEEE 802.3 converts data into what is used in ethernet connection) = #cs/networking/tcp-ip/layers/hardware
<!--ID: 1759154339989-->

## Diagrams
![[TCPIP model.jpg|750]]

## TCP/IP Communication Protocols

### TCP
What does it do?
- Defines how applications can create channels of communication over a network
How does it work?
- TCP relies on a 3-way handshake:
	- Synchronization, synchronization acknowledgment, and final acknowledgment)

### IP
What does it do?
- Defines how to address and route each packet so it reaches the right destination. 
- IP multicasting allows a host to send a single packet to thousands of hosts across a routed network. 
How does it work?
- A subnet mask tells a computer (or other network device), what portion of the IP address is used to represent the network and what part is used to represent hosts (other computers) on the network.

### NAT
NAT = Network address translation, the virtualization of IP addresses. 
- Helps to improve security and decrease the number of IP addresses an organization needs
- Used mostly for audio (radio) and video distribution
[IP Multicasting Description](http://www.steves-internet-guide.com/introduction-multicasting/)

### TCP/IP working

## TCP/IP Protocols
- These are all considered stateless, meaning that each client request is considered new because it is unrelated to previous request
	- Frees up network paths so they can be used continuously.
	- The transport layer itself *is* stateful
- Use client-server mode of communication (a program sends a request to another program and awaits a response) [Client-server model](https://www.geeksforgeeks.org/client-server-model/)

### HTTP
### HTTP Secure
### File Transfer Protocol
# TCP/IP Components
```
xxx.xxx.xxx.xxx
```

## Types of TCP/IP Networks

| Class | Accomidated Hosts | Shorthand | Submask         | Example                        |
| ----- | ----------------- | --------- | --------------- | ------------------------------ |
| A     | 16,777,214        | /8        | `255.0.0.0`     | `networkpart.host.host.host`   |
| B     | 65,536            | /16       | `255.255.0.0`   | `network.network.host.host`    |
| C     | 254               | /24       | `255.255.255.0` | `network.network.network.host` |

- `255`
	- Used for stuff
- `0`
	- Used for stuff

## Networks to know
- `255.255.255.255`
	- A request sent out, typically from a host to the DHCP to assign it an address
- `192.168.10.x`
	- Private network. Everyone has this on
