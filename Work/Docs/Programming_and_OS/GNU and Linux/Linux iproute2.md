---
summary: Newer command list that lets you interact with the network status of a device.
type: note/library
prev: ["[[Linux net-tools]]"]
date created: Sunday, December 29th 2024, 4:41:43 pm
date modified: Thursday, July 3rd 2025, 1:52:29 pm
tags: []
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- [c] `ip addr` = Displays IP address and property information (abbreviation of address) = #command/linux/networking/ip_queries  = `show dev em1` Display info for only device em1
<!--ID: 1751434090879-->

- [c] `ip link show` = Show all available network interfaces, whether they are active or not = #command/linux/networking/ip_queries  = `show dev em1` Display info only for device em1
<!--ID: 1751434090883-->

      `-s link` Display interface statistics. 
- [c] `ip route` = Display and alter the routing able, and the route entries in the kernel = #command/linux/networking/ip_queries  
<!--ID: 1751434090887-->

- [c] `sudo ip link set up <interface>` = Activate network interface = #command/linux/networking/config
<!--ID: 1751434090891-->

- [c] `sudo ip link set down <interface>` = Dectivate network interface = #command/linux/networking/config
<!--ID: 1751434090895-->


[Linux TCP/IP networking: net-tools vs. iproute2](https://www.xmodulo.com/linux-tcpip-networking-net-tools-iproute2.html)
<iframe src="https://www.xmodulo.com/linux-tcpip-networking-net-tools-iproute2.html" style="width: 100%; height: 600px;"></iframe>