---
summary: Internet socket address, IPv4 or IPv6. Consist of an IP address, a 16-bit port number.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
type: note/class/enum
date created: Monday, November 10th 2025, 11:20:15 am
date modified: Monday, November 10th 2025, 11:21:39 am
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[SocketAddr in std::net - Rust](https://doc.rust-lang.org/std/net/enum.SocketAddr.html)

## Concepts of Note
## Usage

```rust
#![feature(addr_parse_ascii)]

use std::net::{IpAddr, Ipv4Addr, Ipv6Addr, SocketAddr};

let socket_v4 = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);
let socket_v6 = SocketAddr::new(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1)), 8080);

assert_eq!(SocketAddr::parse_ascii(b"127.0.0.1:8080"), Ok(socket_v4));
assert_eq!(SocketAddr::parse_ascii(b"[::1]:8080"), Ok(socket_v6));
```

## Examples

```rust
pub enum SocketAddr {
    V4(SocketAddrV4),
    V6(SocketAddrV6),
}
```