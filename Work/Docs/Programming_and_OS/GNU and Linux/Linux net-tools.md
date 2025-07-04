---
summary: Accesses and changes kernel network config via procfs (`/proc`) and `ioctl` system call. More heavyweight than the netlink interface, and used in older linux systems.
type: note/library
up:
  - "[[Linux Networking and Internet]]"
next:
  - "[[Linux iproute2]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
Network resources (e.g. link, IP address, route, tunnel, etc.) are defined with `object` abstraction, and you can manage different objects using consistent syntax. Still under active development. 

# Usage
- [p] `ifconfig` = Show a list of all available network interfaces = #command/linux/networking 
<!--ID: 1751434090851-->


