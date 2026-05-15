---
type: note/library
headings:
similar:
aliases: [Linux netinet, netinet]
date created: Tuesday, March 17th 2026, 12:00:00 pm
date modified: Tuesday, March 17th 2026, 3:36:16 pm
items:
  - "[[C netinet in.h]]"
library_of:
  - "[[Linux network]]"
tags: [programming/c, programming/c/networking]
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[Linux syscall]]"
  - "[[Networking Berkeley Sockets|POSIX sockets]]"
  - "[[NTP server]]"
---

# Summary
󰙎 netinet ;;; POSIX header collection providing socket address structures, protocol constants, and byte-order utilities for IPv4/IPv6 TCP/IP networking in C.

# Additional Background

[\<netinet/in.h\>](https://pubs.opengroup.org/onlinepubs/7908799/xns/netinetin.h.html)
The `netinet/` headers are part of POSIX and ship with glibc on Linux. They sit above the BSD socket API (`sys/socket.h`) and define the concrete address types and protocol constants used when creating, binding, and connecting sockets.

Key headers:
- `<netinet/in.h>` — IPv4/IPv6 address structs, protocol numbers, `INADDR_*` constants, byte-order macros
- `<netinet/tcp.h>` — TCP socket-level options (`TCP_NODELAY`, `TCP_KEEPIDLE`, …)
- `<arpa/inet.h>` — text↔binary conversion (`inet_pton`, `inet_ntop`) and byte-order functions

## Concepts of Note
󰙎 byte order ;;; Network byte order is big-endian. Host byte order may differ. Always convert port and address fields with `htons`/`htonl` before writing them into a `sockaddr_in`.
󰙎 address family ;;; `AF_INET` for IPv4, `AF_INET6` for IPv6. Set in `sin_family` / `sin6_family` of the relevant `sockaddr_*` struct.
󰙎 wildcard address ;;; `INADDR_ANY` (0.0.0.0) binds a socket to all local interfaces; useful for servers.

## Properties

### members

##### sockaddr_in
󰫧 sockaddr_in:
- description: IPv4 socket address passed to `bind`, `connect`, `accept`, etc.
- fields:
  - `sa_family_t sin_family` — always `AF_INET`
  - `in_port_t sin_port` — port in **network** byte order
  - `struct in_addr sin_addr` — IPv4 address in **network** byte order
󰫧 end:

##### sockaddr_in6
󰫧 sockaddr_in6:
- description: IPv6 socket address; extends `sockaddr_in` with flow-info and scope.
- fields:
  - `uint16_t sin6_family` — `AF_INET6`
  - `in_port_t sin6_port` — port, network byte order
  - `uint32_t sin6_flowinfo` — flow label
  - `struct in6_addr sin6_addr` — 128-bit IPv6 address
  - `uint32_t sin6_scope_id` — interface scope
󰫧 end:

##### in_addr
󰫧 in_addr:
- description: Holds a single 32-bit IPv4 address.
- fields:
  - `in_addr_t s_addr` — address in network byte order
󰫧 end:

### variables

#### Protocol constants
##### IPPROTO_TCP
󰫧 :
- description: Protocol number for TCP; passed as third arg to `socket()`.
󰫧 end:

##### IPPROTO_UDP
󰫧 :
- description: Protocol number for UDP.
󰫧 end:

##### INADDR_ANY
󰫧 :
- description: Wildcard IPv4 address `0.0.0.0`; bind to all interfaces.
󰫧 end:

##### INADDR_LOOPBACK
󰫧 :
- description: Loopback address `127.0.0.1`.
󰫧 end:

### functions
#### htons / htonl
##### htons
󰡱 :
- description: Convert 16-bit value from host to network byte order (port numbers).
- args: `uint16_t hostshort`
- calls: —
󰡱 end:

##### htonl
󰡱 :
- description: Convert 32-bit value from host to network byte order (IPv4 addresses).
- args: `uint32_t hostlong`
- calls: —
󰡱 end:

##### ntohs / ntohl
󰡱 :
- description: Inverse of `htons`/`htonl`; network → host byte order.
- args: 16-bit or 32-bit network-order value
- calls: —
󰡱 end:

##### inet_pton / inet_ntop
󰡱 :
- description: Convert a human-readable IP string to binary network address.
- args: `int af, const char *src, void *dst`
- calls: —
- process:
	 start:
	1. Pass `AF_INET` or `AF_INET6` as `af`.
	2. Point `dst` at `sin_addr` (IPv4) or `sin6_addr` (IPv6).
	3. Returns 1 on success, 0 if string is invalid, -1 on error.
	 end:
󰡱 end:

## Usage

Typical IPv4 TCP server setup:
 start:
1. `socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)` — create socket fd
2. Populate `sockaddr_in`: set `sin_family = AF_INET`, `sin_port = htons(port)`, `sin_addr.s_addr = INADDR_ANY`
3. `bind(fd, (struct sockaddr *)&addr, sizeof(addr))`
4. `listen(fd, backlog)` / `accept(fd, ...)`
 end:

```c
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

struct sockaddr_in addr = {
    .sin_family = AF_INET, // AF_INET refers to the protocol family typical for Linux IPv4
    .sin_port   = htons(8080),
    .sin_addr.s_addr = INADDR_ANY,
};

bind(fd, (struct sockaddr *)&addr, sizeof(addr));
```

 `htons(port)` ;;; always wrap port literals — host byte order != network byte order on little-endian systems
 `inet_pton(AF_INET, "192.168.1.1", &addr.sin_addr)` ;;; preferred over deprecated `inet_addr()`

## Flashcards
󰠗 What byte order must `sin_port` and `sin_addr` be stored in? ;; Network byte order (big-endian) — use `htons` for ports and `htonl`/`inet_pton` for addresses.
󰠗 What is the difference between `AF_INET` and `PF_INET`? ;; Historically `AF_*` = address family (used in `sockaddr`), `PF_*` = protocol family (used in `socket()`). On Linux they are identical values.
󰠗 Which header provides `sockaddr_in`? ;; `<netinet/in.h>`
󰠗 How do you disable Nagle's algorithm on a TCP socket? ;; `setsockopt(fd, IPPROTO_TCP, TCP_NODELAY, &one, sizeof(one))` — requires `<netinet/tcp.h>`
