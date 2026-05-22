---
summary: Access for python to the serial port. Provides backends for running on Windows, OSX, Linux, BSD, and IronPython.
type: note/library
date created: Wednesday, February 5th 2025, 1:38:39 pm
date modified: Wednesday, February 5th 2025, 1:39:37 pm
classes:
  - "[[Python Serial (class)]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Features
- Same class based interface on all supported platforms.
- Access to the port settings through Python properties.
- Support for different byte sizes, stop bits, parity and flow control with RTS/CTS and/or Xon/Xoff.
- Working with or without receive timeout.
- File like API with “read” and “write” (“readline” etc. also supported).
- The files in this package are 100% pure Python.
- The port is set up for binary transmission. No NULL byte stripping, CR-LF translation etc. (which are many times enabled for POSIX.) This makes this module universally useful.
- Compatible with [`io`](https://docs.python.org/3/library/io.html#module-io "(in Python v3.11)") library
- RFC 2217 client (experimental), server provided in the examples.

## Media
[pySerial — pySerial 3.4 documentation](https://pyserial.readthedocs.io/en/latest/pyserial.html)