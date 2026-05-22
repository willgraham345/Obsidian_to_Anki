---
aliases:
- BSD sockets
- POSIX sockets
- socket.h
anki_sync:
  73effb15-f0fc-4960-8a55-936ffb06bde6: 1776705543077
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, March 17th 2026, 1:42:36 pm
headings:
- '[[#Concepts of Note]]'
- '[[#Flashcards]]'
- '[[#Properties]]'
item_of:
- '[[Networking socket]]'
next:
- '[[Network POSIX]]'
similar: null
summary: API for internet and unix domain sockets. Evolved into Network POSIX, applying
  to all sockets that wish to be POSIX compliant.
tags:
- networking/sockets
- programming/c/networking
template: null
template-version: null
type: note/item
uses:
- '[[C netinet|Linux netinet]]'
- '[[Linux system_data_types]]'
- '[[netdb.h]]'
- '[[sys socket.h]]'
- '[[sys un.h]]'
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

[Wikipedia on Socket](https://en.wikipedia.org/wiki/Berkeley_sockets)

## Concepts of Note
Defined over several header files:
- [[sys socket.h]] — core socket API
- [[C netinet|Linux netinet]] — IPv4/IPv6 address structures
- [[netdb.h]] — hostname/service resolution
- [[sys un.h]] — Unix domain socket addresses

Originated in 4.2BSD (1983). Standardised by POSIX as part of [[Network POSIX]]. The abstraction treats a socket as a file descriptor — enabling `read()`/`write()` alongside socket-specific calls.

### Header Files

| Header | Provides |
|--------|----------|
| `<sys/socket.h>` | `socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `send()`, `recv()`, `setsockopt()`, `getsockopt()`, `struct sockaddr`, `socklen_t`, `AF_*`/`SOCK_*` constants |
| `<netinet/in.h>` | `struct sockaddr_in`, `struct sockaddr_in6`, `INADDR_ANY`, `INADDR_LOOPBACK`, `htons()`/`ntohs()`/`htonl()`/`ntohl()`, `IPPROTO_TCP`/`IPPROTO_UDP` |
| `<arpa/inet.h>` | `inet_pton()`, `inet_ntop()`, `inet_addr()`, `inet_ntoa()` — text↔binary IP address conversion |
| `<netdb.h>` | `getaddrinfo()`, `freeaddrinfo()`, `getnameinfo()`, `struct addrinfo`, `gethostbyname()` (deprecated) |
| `<sys/un.h>` | `struct sockaddr_un` — Unix domain socket addresses |
| `<poll.h>` | `poll()`, `struct pollfd`, `POLLIN`/`POLLOUT`/`POLLERR` |
| `<sys/select.h>` | `select()`, `fd_set`, `FD_SET`/`FD_CLR`/`FD_ISSET`/`FD_ZERO` macros |
| `<sys/epoll.h>` | `epoll_create1()`, `epoll_ctl()`, `epoll_wait()`, `struct epoll_event` (Linux only) |
| `<fcntl.h>` | `fcntl()` with `O_NONBLOCK` — sets non-blocking mode on a socket fd |
| `<errno.h>` | `errno`, `EAGAIN`, `EWOULDBLOCK`, `ECONNREFUSED`, etc. |
| `<string.h>` | `strerror()` for human-readable errno messages |

 `<netinet/in.h>` ;;; defines IPv4/IPv6 address structs and byte-order helpers — always include alongside `<sys/socket.h>`
 `<arpa/inet.h>` ;;; text↔binary IP conversion; `inet_pton`/`inet_ntop` are the modern, AF-agnostic replacements for `inet_addr`/`inet_ntoa`

### Non-Blocking I/O and Multiplexing

| Feature | select | poll | epoll |
|---------|--------|------|-------|
| Max fds | `FD_SETSIZE` (~1024) | unlimited | unlimited |
| Kernel scan | O(nfds) | O(nfds) | O(1) per event |
| Portability | POSIX | POSIX | Linux only |
| State in kernel | no | no | yes (persistent) |
| Edge-triggered | no | no | yes (`EPOLLET`) |

󰙎 `O_NONBLOCK` ;;; set via `fcntl(fd, F_SETFL, flags | O_NONBLOCK)` or `SOCK_NONBLOCK` at creation; blocking calls return `-1`/`EAGAIN` instead
󰙎 `EPOLLET` ;;; edge-triggered mode; notifies on state *change* only — caller must drain the fd completely
󰙎 `EAGAIN` ;;; non-blocking op would block; identical to `EWOULDBLOCK` on Linux

### Error Handling

| errno | Constant | Cause |
|-------|----------|-------|
| 98 | `EADDRINUSE` | Port in use; fix with `SO_REUSEADDR` |
| 111 | `ECONNREFUSED` | Nothing listening at destination |
| 104 | `ECONNRESET` | Peer sent RST |
| 32 | `EPIPE` | Write to closed socket; also raises `SIGPIPE` |
| 11 | `EAGAIN` | Non-blocking op would block |
| 9 | `EBADF` | Invalid fd (use-after-close) |

󰙎 `perror()` ;;; prints `"prefix: strerror(errno)\n"` to stderr
󰙎 `strerror_r()` ;;; thread-safe errno→string; prefer over `strerror()` in threaded code

### TCP Lifecycles

#### Server: socket → bind → listen → accept → read/write → close

 start:
1. `socket(AF_INET, SOCK_STREAM, 0)` — allocate socket fd
2. `setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))` — prevent bind failure on restart
3. `bind(fd, (struct sockaddr*)&addr, sizeof(addr))` — assign local port
4. `listen(fd, backlog)` — mark as passive; `backlog` = max pending connection queue depth
5. `accept(fd, (struct sockaddr*)&peer, &peer_len)` — blocks; returns new fd for each client
6. `read()`/`write()` or `recv()`/`send()` on the accepted fd
7. `close(client_fd)` then eventually `close(listen_fd)`
 end:

```c
// Minimal TCP server pseudocode
int srv = socket(AF_INET, SOCK_STREAM, 0);
int opt = 1;
setsockopt(srv, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

struct sockaddr_in addr = {
    .sin_family = AF_INET,
    .sin_port   = htons(8080),
    .sin_addr.s_addr = INADDR_ANY
};
bind(srv, (struct sockaddr*)&addr, sizeof(addr));
listen(srv, 128);

while (1) {
    struct sockaddr_in peer;
    socklen_t plen = sizeof(peer);
    int cli = accept(srv, (struct sockaddr*)&peer, &plen);
    // handle cli in thread or process
    char buf[4096];
    ssize_t n = read(cli, buf, sizeof(buf));
    write(cli, buf, n);   // echo
    close(cli);
}
```

`listen()` backlog: since Linux 3.20 the kernel silently caps to `/proc/sys/net/core/somaxconn` (default 4096).

#### Client: socket → connect → read/write → close

 start:
1. `socket(AF_INET, SOCK_STREAM, 0)` — allocate socket fd
2. Fill `sockaddr_in` with server IP + port; use `getaddrinfo()` for hostname resolution
3. `connect(fd, (struct sockaddr*)&server, sizeof(server))` — initiates TCP 3-way handshake; blocks until established or error
4. `write()`/`read()` or `send()`/`recv()`
5. `close(fd)` — sends FIN, begins TCP 4-way teardown
 end:

```c
// Minimal TCP client pseudocode
struct addrinfo hints = { .ai_family = AF_UNSPEC, .ai_socktype = SOCK_STREAM };
struct addrinfo *res;
getaddrinfo("example.com", "80", &hints, &res);

int fd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
connect(fd, res->ai_addr, res->ai_addrlen);
freeaddrinfo(res);

const char *req = "GET / HTTP/1.0\r\n\r\n";
write(fd, req, strlen(req));

char buf[4096];
ssize_t n;
while ((n = read(fd, buf, sizeof(buf))) > 0)
    fwrite(buf, 1, n, stdout);

close(fd);
```

See also: [[Networking UDP]] for the connectionless equivalent (`sendto`/`recvfrom`, no `connect`/`accept`).

### Domains and Socket Types

#### Address Families (Domains)

| Constant | Value | Use |
|----------|-------|-----|
| `AF_INET` | 2 | IPv4 internet sockets |
| `AF_INET6` | 10 | IPv6 internet sockets |
| `AF_UNIX` / `AF_LOCAL` | 1 | Unix domain (IPC via filesystem path) |
| `AF_PACKET` | 17 | Raw link-layer access (Linux); requires `CAP_NET_RAW` |
| `AF_UNSPEC` | 0 | Wildcard; used in `getaddrinfo()` hints to accept any family |

󰙎 `AF_PACKET` ;;; bypass TCP/IP stack entirely; used for packet capture, custom protocol implementation; Linux only

#### Socket Types

| Constant | Transport | Properties |
|----------|-----------|------------|
| `SOCK_STREAM` | TCP (or Unix stream) | reliable, ordered, connection-oriented, byte-stream |
| `SOCK_DGRAM` | UDP (or Unix datagram) | unreliable, unordered, connectionless, message-oriented |
| `SOCK_RAW` | raw IP/link | full protocol header control; needs `IPPROTO_*` third arg |
| `SOCK_SEQPACKET` | SCTP / Unix | reliable, ordered, message-preserving (not byte-stream) |
| `SOCK_NONBLOCK` | — | ORed with type to set `O_NONBLOCK` atomically at creation (Linux) |
| `SOCK_CLOEXEC` | — | ORed with type to set `FD_CLOEXEC` atomically at creation (Linux) |

󰙎 `SOCK_SEQPACKET` ;;; like `SOCK_STREAM` but preserves message boundaries; rare in practice; common over `AF_UNIX` for D-Bus
󰙎 `SOCK_STREAM` ;;; provides TCP semantics — connection must be established before data exchange; kernel ensures ordering and retransmission

## Properties
### functions
- _socket()_ creates a new socket of a certain type, identified by an integer number, and allocates system resources to it.
- _bind()_ is typically used on the server side, and associates a socket with a socket address structure, i.e. a specified local IP address and a port number.
- _listen()_ is used on the server side, and causes a bound TCP socket to enter listening state.
- _connect()_ is used on the client side, and assigns a free local port number to a socket. In case of a TCP socket, it causes an attempt to establish a new TCP connection.
- _accept()_ is used on the server side. It accepts a received incoming attempt to create a new TCP connection from the remote client, and creates a new socket associated with the socket address pair of this connection.
- _send()_, _recv()_, _sendto()_, and _recvfrom()_ are used for sending and receiving data. The standard functions _write()_ and _read()_ may also be used.
- _close()_ causes the system to release resources allocated to a socket. In case of TCP, the connection is terminated.
- _gethostbyname()_ and _gethostbyaddr()_ are used to resolve host names and addresses. IPv4 only.
- _getaddrinfo()_ and _freeaddrinfo()_ are used to resolve host names and addresses. IPv4, IPv6.
- _select()_ is used to suspend, waiting for one or more of a provided list of sockets to be ready to read, ready to write, or that have errors.
- _poll()_ is used to check on the state of a socket in a set of sockets. The set can be tested to see if any socket can be written to, read from or if an error occurred.
- _getsockopt()_ is used to retrieve the current value of a particular socket option for the specified socket.
- _setsockopt()_ is used to set a particular socket option for the specified socket.

### Data Structures

󰙎 `sockaddr` ;;; generic socket address; `sa_family` selects type; cast to `struct sockaddr *` for all API calls
󰙎 `sockaddr_in` ;;; IPv4 — `sin_family=AF_INET`, `sin_port` (network byte order via `htons`), `sin_addr.s_addr` (32-bit)
󰙎 `sockaddr_in6` ;;; IPv6 — `sin6_family=AF_INET6`, `sin6_port`, `sin6_addr` (128-bit), `sin6_scope_id`
󰙎 `sockaddr_un` ;;; Unix domain — `sun_path[108]`; abstract namespace: `sun_path[0]='\0'`
󰙎 `addrinfo` ;;; `getaddrinfo()` result; linked list via `ai_next`; `ai_addr` → sockaddr; free with `freeaddrinfo()`
󰙎 `socklen_t` ;;; unsigned int typedef for address length; passed by pointer so kernel can write back actual size
󰙎 `INADDR_ANY` ;;; 0.0.0.0 — bind to all local interfaces
󰙎 `htons()` ;;; host-to-network short; converts port to big-endian network byte order

### Socket Options

󰙎 `SO_REUSEADDR` ;;; allow rebind to port in `TIME_WAIT`; set before `bind()` to prevent "Address already in use" on restart
󰙎 `SO_REUSEPORT` ;;; multiple sockets bind same port; enables multi-process/thread accept balancing (Linux 3.9+)
󰙎 `SO_KEEPALIVE` ;;; kernel sends TCP keep-alive probes on idle connections
󰙎 `SO_LINGER` ;;; `l_linger=0` → RST on `close()`, discards data; `l_linger>0` → `close()` blocks until data flushed
󰙎 `SO_RCVTIMEO` / `SO_SNDTIMEO` ;;; recv/send timeout (`struct timeval`); call returns `EAGAIN` after expiry
󰙎 `SO_ERROR` ;;; retrieve and clear pending socket error (get-only)
󰙎 `TCP_NODELAY` ;;; disable Nagle; transmit immediately — use for latency-sensitive protocols
󰙎 `TCP_CORK` ;;; accumulate until buffer full or cork removed; opposite of `TCP_NODELAY`
󰙎 `TCP_KEEPIDLE` / `TCP_KEEPINTVL` / `TCP_KEEPCNT` ;;; keepalive timing: idle seconds, probe interval, max unanswered probes

## Flashcards

󰠗 What does `bind()` do and which side calls it? ;; Associates a socket with a local address/port. Called by the server before `listen()`. Client rarely calls it — kernel assigns ephemeral port at `connect()`.

󰠗 What is the difference between `SO_REUSEADDR` and `SO_REUSEPORT`? ;; `SO_REUSEADDR` allows rebinding a port in `TIME_WAIT`. `SO_REUSEPORT` allows multiple independent sockets to bind the *same* port simultaneously (load-balancing across threads/processes).

󰠗 Why prefer `getaddrinfo()` over `gethostbyname()`? ;; `getaddrinfo()` handles both IPv4 and IPv6, is thread-safe (returns heap-allocated list), and separates hostname resolution from address-family concerns.

󰠗 What is the `accept()` return value? ;; A new file descriptor representing the individual connection. The original listening socket remains open for further `accept()` calls.

󰠗 What does `listen()`'s backlog argument control? ;; The maximum number of connections the kernel queues (completed 3-way handshake) waiting for `accept()`. Excess connections are dropped or RST'd.

󰠗 select vs epoll — when does epoll win? ;; When managing many concurrent fds. `select` rescans all fds each call (O(n)). `epoll` maintains a kernel-side ready list — O(1) per event regardless of total fd count.

󰠗 What errno is returned by non-blocking `recv()` when no data is available? ;; `EAGAIN` (same value as `EWOULDBLOCK` on Linux). The caller should re-arm the fd in `poll`/`epoll` and retry.

󰠗 What does `TCP_NODELAY` do? ;; Disables the Nagle algorithm. Without it, the kernel buffers small writes until ACK arrives or buffer fills. With it, each `write()`/`send()` is transmitted immediately.

󰠗 What is `socklen_t` and why is it passed by pointer? ;; An unsigned int typedef for address-structure size. Passed by pointer to accept/getsockname so the kernel can write back the *actual* length of the address it filled in.

󰠗 How do you convert "192.168.1.1" to a binary `in_addr`? ;; `inet_pton(AF_INET, "192.168.1.1", &addr.sin_addr)` returns 1 on success, 0 if invalid, -1 on error.
