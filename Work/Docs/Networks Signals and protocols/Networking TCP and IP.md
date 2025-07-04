---
type: note
---
# Background
[Good Overview of TCP/IP](https://www.techtarget.com/searchnetworking/definition/TCP-IP)
[Oracle's TCP/IP Admin Guide](https://docs.oracle.com/cd/E19504-01/802-5753/index.html)

## TCP/IP Communication Protocols
![[Pasted image 20240303163958.jpg|350]]
See [[Network OSI Model#Layer Descriptions]] for more info on what is contained in each of the spots. 

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
