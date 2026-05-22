---
type: note/item
headings:
date created: Tuesday, March 17th 2026, 12:00:00 pm
date modified: Tuesday, March 17th 2026, 11:09:29 am
tags: [cs/linux/networking, cs/linux/networking/syscalls]
template:
template-version:
uses:
  - "[[UNIX File Descriptor]]"
---

[[Linux Kernel Subsystems]] > [[Linux syscall networking]]

# Summary
󰙎 Linux networking syscalls ;;; POSIX/BSD socket API exposed by the Linux kernel; user-space programs create and manipulate sockets via these syscalls to send/receive data over TCP, UDP, or [[UNIX Domain Sockets]]. All sockets are represented as [[UNIX File Descriptor]]s.

# Additional Background
The [[Networking Berkeley Sockets]] API is the canonical interface. Every socket fd flows through the kernel's VFS layer (see [[Linux VFS Overview]]) — `read(2)`/`write(2)` work on connected TCP sockets exactly as they do on files. Error returns set `errno`; see [[Linux process error codes]] for numeric values. Multiplexing readiness across many fds is handled by `select`/[[Linux poll]]/`epoll`.

## Concepts of Note
󰙎 socket domain ;;; Address-family constant passed to `socket()`. `AF_INET` = IPv4, `AF_INET6` = IPv6, `AF_UNIX` = local IPC.
󰙎 socket type ;;; Communication semantics. `SOCK_STREAM` = reliable ordered byte-stream (TCP). `SOCK_DGRAM` = unreliable unordered datagrams (UDP). `SOCK_RAW` = bypass transport layer.
󰙎 backlog ;;; `listen()` argument; maximum length of the pending-connection queue before the kernel starts refusing new SYN packets.
󰙎 sockaddr ;;; Generic address struct; cast to `sockaddr_in` (IPv4), `sockaddr_in6` (IPv6), or `sockaddr_un` (UNIX) at call sites.
󰙎 SO_REUSEADDR ;;; `setsockopt` option; allows rebinding a port that is in `TIME_WAIT`, essential for fast server restarts.
󰙎 MSG_DONTWAIT ;;; Per-call flag making a send/recv non-blocking without setting `O_NONBLOCK` on the fd.
󰙎 EAGAIN / EWOULDBLOCK ;;; `errno` returned when a non-blocking socket has no data ready or send buffer is full; caller must retry.

## Properties
### functions

##### socket
󰡱 `int socket(int domain, int type, int protocol)` :
- description: Creates a new socket; returns an fd or `-1`. `protocol` is usually `0` (kernel selects); set `IPPROTO_TCP` / `IPPROTO_UDP` explicitly when `type` is `SOCK_RAW`.
- args: `domain` — `AF_INET` / `AF_INET6` / `AF_UNIX`; `type` — `SOCK_STREAM` / `SOCK_DGRAM` / `SOCK_RAW`; `type` may be OR'd with `SOCK_NONBLOCK` | `SOCK_CLOEXEC` (Linux 2.6.27+).
- calls: kernel `sys_socket` → allocates `struct socket` in the kernel, returns fd into process fd table.
󰡱 end:

##### bind
󰡱 `int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)` :
- description: Assigns a local address/port to `sockfd`. Required on the server before `listen()`; UDP senders may skip it (kernel auto-assigns ephemeral port).
- args: `addr` — pointer to `sockaddr_in` / `sockaddr_in6` filled with `htons(port)` and `INADDR_ANY` or a specific IP.
- calls: typically precedes `listen()` (TCP server) or the first `sendto()` (UDP server).
󰡱 end:

##### listen
󰡱 `int listen(int sockfd, int backlog)` :
- description: Marks a bound TCP socket as passive (server). Transitions socket to `LISTEN` state. UDP sockets never call this.
- args: `backlog` — kernel clamps to `net.core.somaxconn`; `128` is a common default.
- calls: must follow `bind()`; precedes `accept()`.
󰡱 end:

##### accept / accept4
󰡱 `int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen)` :
- description: Dequeues the first completed connection from the listening socket's accept queue; returns a **new** fd for that connection. Blocks if queue is empty (unless `O_NONBLOCK`). `accept4(2)` adds a `flags` arg (`SOCK_NONBLOCK`, `SOCK_CLOEXEC`) to set attributes atomically.
- args: `addr` / `addrlen` — filled with client address on return; pass `NULL`/`NULL` to discard.
- calls: typically called in a loop; each returned fd is an independent stream to one client.
󰡱 end:

##### connect
󰡱 `int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)` :
- description: Initiates a TCP three-way handshake (`SOCK_STREAM`) or sets the default remote address for a UDP socket (`SOCK_DGRAM`). Blocks until connected or error unless socket is non-blocking (`EINPROGRESS` returned; use `poll`/`epoll` to await completion).
- args: `addr` — remote endpoint filled with server IP + `htons(port)`.
- calls: TCP: triggers SYN → SYN-ACK → ACK. UDP: no packets sent; just records peer address so `send()` can be used instead of `sendto()`.
󰡱 end:

##### send / recv
󰡱 `ssize_t send(int sockfd, const void *buf, size_t len, int flags)` :
- description: Transmit data on a **connected** socket. Returns bytes written (may be less than `len` — caller must loop) or `-1`. For TCP, data enters the kernel send buffer; actual transmission is asynchronous.
- args: `flags` — `0` (common), `MSG_NOSIGNAL` (suppress `SIGPIPE`), `MSG_MORE` (hint more data coming — coalescing). `recv` flags: `MSG_PEEK` (consume nothing), `MSG_WAITALL` (block until full `len` received).
- calls: TCP servers use after `accept()`; UDP after `connect()`.
󰡱 end:

##### sendto / recvfrom
󰡱 `ssize_t sendto(int sockfd, const void *buf, size_t len, int flags, const struct sockaddr *dest_addr, socklen_t addrlen)` :
- description: Send/receive on an **unconnected** UDP socket, specifying/receiving the remote address per-call. `recvfrom` fills `src_addr` with the sender's address. Both degrade to `send`/`recv` if `dest_addr` is `NULL`.
- args: `dest_addr` / `addrlen` — target endpoint; may differ on every call (UDP multicast fan-out, DNS clients, etc.).
- calls: core of connectionless UDP workflows.
󰡱 end:

##### setsockopt / getsockopt
󰡱 `int setsockopt(int sockfd, int level, int optname, const void *optval, socklen_t optlen)` :
- description: Sets per-socket options. `getsockopt` reads them. Options are scoped by `level`: `SOL_SOCKET` (generic), `IPPROTO_TCP`, `IPPROTO_UDP`, `IPPROTO_IP`, `IPPROTO_IPV6`.
- args: key options: `SO_REUSEADDR`, `SO_REUSEPORT`, `SO_RCVBUF` / `SO_SNDBUF` (buffer sizes), `SO_KEEPALIVE`, `TCP_NODELAY` (disable Nagle), `TCP_KEEPIDLE`, `IP_MULTICAST_TTL`.
- calls: call after `socket()`, before `bind()` / `connect()` for address-level options.
󰡱 end:

##### shutdown
󰡱 `int shutdown(int sockfd, int how)` :
- description: Partially or fully closes a TCP connection without releasing the fd. Allows half-close semantics (signal EOF to peer while still reading). `close(2)` releases the fd but only sends FIN when the ref-count drops to zero.
- args: `how` — `SHUT_RD` (stop receiving), `SHUT_WR` (send FIN, stop sending), `SHUT_RDWR` (both).
- calls: precedes or replaces `close()` in graceful teardown.
󰡱 end:

##### epoll_create1 / epoll_ctl / epoll_wait
󰡱 `int epoll_create1(int flags)` / `int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event)` / `int epoll_wait(int epfd, struct epoll_event *events, int maxevents, int timeout)` :
- description: Linux-specific O(1) I/O multiplexer (see [[Linux poll]] for `poll`/`select` context). `epoll_create1` allocates the kernel interest list; `epoll_ctl` adds/modifies/removes fds (`EPOLL_CTL_ADD`, `EPOLL_CTL_MOD`, `EPOLL_CTL_DEL`); `epoll_wait` blocks until events are ready, returning only the **ready** set (vs. `poll`'s linear scan).
- args: `epoll_event.events` — `EPOLLIN`, `EPOLLOUT`, `EPOLLERR`, `EPOLLHUP`, `EPOLLET` (edge-triggered), `EPOLLONESHOT`.
- calls: scales to hundreds of thousands of connections; basis of most async I/O runtimes (libuv, Tokio, etc.).
󰡱 end:

##### getaddrinfo / freeaddrinfo
󰡱 `int getaddrinfo(const char *node, const char *service, const struct addrinfo *hints, struct addrinfo **res)` :
- description: Protocol-agnostic hostname/service resolution; returns a linked list of `addrinfo` structs usable directly with `bind()` / `connect()`. Supersedes `gethostbyname()`. Free result with `freeaddrinfo(res)`.
- args: `node` — hostname or IP string; `service` — port number string or service name (e.g., `"http"`); `hints` — filter by `ai_family`, `ai_socktype`.
- calls: iterate result list, try each until `connect()` succeeds (handles dual-stack).
󰡱 end:

## Usage

### TCP Server Workflow
 start:
1. `socket(AF_INET, SOCK_STREAM, 0)` — create listening fd.
2. `setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, ...)` — allow fast restart.
3. `bind(fd, &addr, sizeof(addr))` — claim port.
4. `listen(fd, backlog)` — enter passive state.
5. `epoll_ctl(epfd, EPOLL_CTL_ADD, fd, ...)` — register with event loop (or `poll`/`select`).
6. `accept4(fd, &client_addr, ...)` on `EPOLLIN` — get client fd.
7. `recv` / `send` on client fd — exchange data (loop until `0` bytes = peer closed).
8. `shutdown(client_fd, SHUT_RDWR)` + `close(client_fd)` — teardown.
 end:

### TCP Client Workflow
 start:
1. `getaddrinfo(host, port, &hints, &res)` — resolve address.
2. `socket(res->ai_family, SOCK_STREAM, 0)` — create fd.
3. `connect(fd, res->ai_addr, res->ai_addrlen)` — three-way handshake (or `EINPROGRESS` if non-blocking).
4. `send` / `recv` — transfer data.
5. `shutdown(fd, SHUT_WR)` — signal EOF; drain remaining `recv`.
6. `close(fd)`.
 end:

### UDP Workflow (connectionless)
 start:
1. **Server**: `socket(AF_INET, SOCK_DGRAM, 0)` → `bind(fd, &addr, ...)`.
2. **Server**: `recvfrom(fd, buf, len, 0, &src_addr, &addrlen)` — blocks for any datagram.
3. **Client**: `socket(AF_INET, SOCK_DGRAM, 0)` (no `bind` needed).
4. **Client**: `sendto(fd, buf, len, 0, &server_addr, sizeof(server_addr))`.
5. **Optional**: `connect(fd, &server_addr, ...)` on client socket → enables `send`/`recv`, filters incoming to that peer only.
6. `close(fd)` on both sides when done.
 end:

## Flashcards
󰠗 What does `accept()` return and why does the server need two fds? ;; A new connected fd for the specific client; the original listening fd remains open to accept further connections. =

󰠗 Why prefer `epoll` over `select` for many concurrent connections? ;; `epoll_wait` returns only ready fds in O(1); `select` scans the entire fd_set in O(n) and has a hard `FD_SETSIZE` limit (typically 1024). 

󰠗 What is the difference between `close()` and `shutdown()` on a TCP socket? ;; `shutdown(SHUT_WR)` sends FIN immediately and prevents further sends while keeping the fd open for reading; `close()` decrements the fd ref-count and only sends FIN when it reaches zero (forked processes share the fd). =

󰠗 What errno is returned when a non-blocking `connect()` is still in progress? ;; `EINPROGRESS`. Use `epoll`/`poll` with `EPOLLOUT` to detect completion, then `getsockopt(SO_ERROR)` to check result. =

󰠗 What is the purpose of `SO_REUSEADDR`? ;; Allows binding a port that has a socket in `TIME_WAIT` state, enabling fast server restarts without waiting the 2×MSL timeout. =

󰠗 When is `sendto()` preferred over `send()`? ;; On unconnected UDP sockets where the destination changes per datagram (e.g., a DNS resolver, UDP echo server). =
