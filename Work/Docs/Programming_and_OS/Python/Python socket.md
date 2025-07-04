---
tags: note/python
type: note
---
# Background
Provides access to the BSD socket interface for IPC (inter-process communication)
- When a socket is created, an endpoint for communication becomes available and a corresponding file descriptor is returned
- A file descriptor is an abstract indicator for accessing a file and has `int` values of `0`, `1`, `2` (`stdin`, `stdout`, and `stderr`)

See [[Networking socket]] for more information
[Socket Docs](https://docs.python.org/3/library/socket.html)
[More information on python sockets, and websockets](https://learn-gevent-socketio.readthedocs.io/en/latest/sockets.html)

# Usage
## Example Server Socket and Client Socket sending messages to each other
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