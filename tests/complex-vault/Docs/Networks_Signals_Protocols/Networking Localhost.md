---
type: note
---
# Background
Localhost is always your computer. Your computer does not always identify the local host. 
- Can be seen as a server that is used on your computer.

The computer or hostname currently making a request to itself
- In this case, the computer is also the virtual server
- `127.0.0.1:` is "localhost"
	- A host
- The address for **loopback** control
- `localhost` is a protocol, and something has to follow the `:`. That is the port number.

If you use with the live server extension of VSCode, it uses a port `5500` attached to `127.0.0.1` followed by the filename. 