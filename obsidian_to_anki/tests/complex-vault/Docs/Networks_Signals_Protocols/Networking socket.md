---
summary: A software structure within a network node of a computer network that serves as the endpoint for sending and receiving data across a network. The basis from which data is passed between each other via the HTTP (TCP) protocol rests upon sockets. Created only during the lifetime of a process of an application running in the node. Most commonly used in the context of the internet protocol suite, and therefore is also referred to as internet socket. Within this context, a socket is externally identified to other hosts by its socket address
headings:
  - "[[#Concepts of Note]]"
type: note/item
similar:
  - "[[Networking port]]"
  - "[[UNIX Domain Sockets]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, September 24th 2025, 1:54:08 pm
implementations:
  - "[[Python socket]]"
  - "[[Rust UdpSocket]]"
item_of:
  - "[[OSI Network Model]]"
items:
  - "[[Networking Berkeley Sockets]]"
used_by:
  - "[[Linux Processes]]"
  - "[[OSI Transport Layer 4]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  What is a TCP connection defined by? ;; Two sockets connected to each other. = #cs/networking/tcp-ip 
<!--ID: 1759154339998-->

󰙎  TCP Connection ;;; Defined by a pair of sockets (address and port). Comprises the destination IP address, destination port, source IP address, and source port number.  = #cs/networking/tcp-ip
<!--ID: 1759154340022-->

󰙎  TCP Socket ;;; An endpoint *instance*, defined by an IP address, port and protocol. An inter-process communicator = #cs/networking/items/socket #cs/networking/tcp-ip  #cs/networking/tcp-ip/layers/transport  #cs/linux/process/IPC/sockets #cs/linux/process/IPC 
<!--ID: 1759154340026-->

󰠗  How is a socket defined? ;; In full: {protocol, local address, local port, remote address, remote port} = #cs/networking/items/socket
<!--ID: 1759154340003-->

󰠗  At what level/layer can a socket be defined in the OSI model? ;; At Layer 2, the data link layer = #cs/networking/osi/layers/data-link #cs/networking/items/socket 
<!--ID: 1759154340008-->


󰠗  What layers does the socket sit between in the TCPIP model? ;; The application layer (1), and the transport layer (2). = #cs/networking/osi/layers/application #cs/networking/osi/layers/transport
<!--ID: 1759154340013-->

󰠗  What are the three categories of sockets? ;; Stream, datagram, and raw socket. = #cs/networking/items/socket 
<!--ID: 1759154340017-->


### Socket definitions
Triad of three things
1. Transport protocol (Transport Layer)
2. IP address
3. Port Number

### Socket types
󰙎  Stream sockets ;;; Most commonly used communication type over TCP/IP. Data pipe is bidirectional, and are delivered in the order they are sent and that computers receive a particular packet only once. If packets arrive out of order on the physical network, the network adapter and host OS ensure they are assembled in the correct sequence.
󰙎  Datagram sockets ;;; A connection-less service. Use UDP protocol to transmit data. Packets are sent independently and there are no guarantees. Size of packets is limited to the size that can be sent in one transaction. There is no disassembly or assembly of packets in datagram sockets.
󰙎  Raw sockets ;;; Type of network socket that enables a software application on the computer to send and receive packets from the network without using the computer's primary operating system. Bypass the normal TCP/IP processing system sending packets straight to application. 
