---
summary:
headings:
type: note/item
similar: ["[[Networking socket]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, September 24th 2025, 1:39:30 pm
items: ["[[Networking Commonly Used ports]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎  Port ;;; A virtualization identifier defining a service endpoint (distinct from a service *instance* endpoint a.k.a. session identifier). A logical construct for separating processes. In the broadest sense, a point of ingress or egress. = #cs/networking/items/port #
<!--ID: 1759154340037-->

󰠗  What are the numbers a port can be? ;; Between 1 and 65535. = #cs/networking/items/port 
<!--ID: 1759154340033-->

A number uniquely assigned to identify a connection endpoint and to direct data to a specific service. 
- Within an OS, a port is a logical construct that identifies a specific process or a type of a network service. 
	- Where network connections start and end. 
- A port number is always associated with a network address of a host (such as an IP address), and the type of transport protocol used for communication. 
	- Completes the destination or origination address of a message. 
		- Port numbers 
- Ports provide a multiplexing service for multiple services or multiple communication sessions at one network address.
	- In the client-server model, multiple simultaneous communication sessions may be initiated for the same service

Also see [[Networking socket]]

## Emhemeral Ports
- Ports available for general use by applications. 
- Provide 
