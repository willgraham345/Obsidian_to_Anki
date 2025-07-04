---
summary: Creates a UDP socket from a given address.
headings: ["[[#Methods]]"]
type: note/class
associations: ["[[Rust bincode]]"]
date created: Thursday, May 29th 2025, 3:46:32 pm
date modified: Wednesday, June 18th 2025, 3:07:33 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Methods
- [E] [[Rust UdpSocket]] = `.recv_from(&self, buf: &mut [u8]))` = Receives a single datagram message on socket, returning number of bytes read and the origin. Excess bytes may be discarded.
- [E] [[Rust UdpSocket]] = `.bind<A: ToSocketAddrs>(addr: A)` = Binds to a socket
