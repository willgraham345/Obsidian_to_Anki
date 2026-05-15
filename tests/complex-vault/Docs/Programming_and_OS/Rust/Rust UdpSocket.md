---
summary: Creates a UDP socket from a given address.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Methods]]"
  - "[[#Properties]]"
  - "[[#Usage]]"
type: note/class
methods:
  - "[[Rust UdpSocket#.bind()]]"
  - "[[Rust UdpSocket#.recv_from()]]"
associations:
  - "[[Rust bincode]]"
class_of:
  - "[[Rust std net]]"
date created: Thursday, May 29th 2025, 3:46:32 pm
date modified: Monday, November 10th 2025, 11:06:18 am
template:
template-version:
uses:
  - "[[Rust SocketAddr]]"
implements:
  - "[[Networking socket]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note


## Properties
### Methods
#### .bind()
  `socket ``=`` UdpSocket::bind<A: ToSocketAddrs>(addr: A)` ;;; Creates a UDP socket `socket` in Rust from address `A`. = #lang/networking/udp
- Creates a UDP socket from the given address
- Declares the scope of your network.

#### .recv_from()
	- [p] `.recv_from(&self, buf: &mut [u8]))` = Receives a single datagram message on socket from a UDP socket, returning number of bytes read and the origin. Excess bytes may be discarded. = #lang/networking/udp 

## Usage
