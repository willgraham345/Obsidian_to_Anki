---
type: note/component
component_of: ["[[Networking socket]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 11:42:12 am
---
# Background
API for Internet sockets and Unix domain sockets
Eventually evolved into the de facto standard within [[Network POSIX]]
- Applies to all sockets that wish to be POSIX compliant
- Designed to be reentrant

# Usage
[Wikipedia on Socket](https://en.wikipedia.org/wiki/Berkeley_sockets)

## Socket API functions
- _socket()_ creates a new socket of a certain type, identified by an integer number, and allocates system resources to it.
- _bind()_ is typically used on the server side, and associates a socket with a socket address structure, i.e. a specified local IP address and a port number.
- _listen()_ is used on the server side, and causes a bound TCP socket to enter listening state.
- _connect()_ is used on the client side, and assigns a free local port number to a socket. In case of a TCP socket, it causes an attempt to establish a new TCP connection.
- _accept()_ is used on the server side. It accepts a received incoming attempt to create a new TCP connection from the remote client, and creates a new socket associated with the socket address pair of this connection.
- _send()_, _recv()_, _sendto()_, and _recvfrom()_ are used for sending and receiving data. The standard functions _write()_ and _read()_ may also be used.
- _close()_ causes the system to release resources allocated to a socket. In case of TCP, the connection is terminated.
- _gethostbyname()_ and _gethostbyaddr()_ are used to resolve host names and addresses. IPv4 only.
- _getaddrinfo()_ and _freeaddrinfo()_ are used to resolve host names and addresses. IPv4, IPv6.
- _select()_ is used to suspend, waiting for one or more of a provided list of sockets to be ready to read, ready to write, or that have errors.
- _poll()_ is used to check on the state of a socket in a set of sockets. The set can be tested to see if any socket can be written to, read from or if an error occurred.
- _getsockopt()_ is used to retrieve the current value of a particular socket option for the specified socket.
- _setsockopt()_ is used to set a particular socket option for the specified socket.