---
summary: 
headings: ["[[#Usage]]"]
type: note/library
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, July 22nd 2025, 9:31:44 am
library_of: ["[[Python]]"]
tags: []
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

Provides access to the BSD socket interface for IPC (inter-process communication)
- When a socket is created, an endpoint for communication becomes available and a corresponding file descriptor is returned
- A file descriptor is an abstract indicator for accessing a file and has `int` values of `0`, `1`, `2` (`stdin`, `stdout`, and `stderr`)

See [[Networking socket]] for more information
[Socket Docs](https://docs.python.org/3/library/socket.html)
[More information on python sockets, and websockets](https://learn-gevent-socketio.readthedocs.io/en/latest/sockets.html)

## Usage
```python
# server.py
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5)

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf)>0:
        print buf

# client.py
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
clientsocket.send('hello')
```