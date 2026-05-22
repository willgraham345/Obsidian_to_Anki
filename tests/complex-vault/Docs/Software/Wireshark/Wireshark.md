---
summary: Foundational network analyzer and packet sniffer.
headings:
  - "[[#Usage]]"
  - "[[#Concepts of Note]]"
type: note/tool
date created: Saturday, November 2nd 2024, 9:50:33 pm
date modified: Wednesday, November 19th 2025, 2:21:41 pm
template: "[[base_note_template]]"
template-version: 1.0.0
---

`VIEW[**{summary}**][text(renderMarkdown)]`

[Learn Wireshark – Computer Networking Tutorial](https://www.freecodecamp.org/news/learn-wireshark-computer-networking/)


[Wireshark Wiki](https://wiki.wireshark.org/)
[Display Filter Reference](https://www.wireshark.org/docs/dfref/)

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Capture options
- Pick whatever interface you're interested in, or whichever has traffic going through it. 

## Concepts of Note
- 


## Usage
### Basic workflow
1. Pick a network
2. Listen on that network
3. Use the display filter to show what you want

### Packet list pane
- Displays short summary of each packet. 
- Source: Address where this packet is coming from
- Destination: Where this packet is going
- Protocol: Name in short version
- Length: Each packet in bytes
- Info: Additional info about packet content, changes according to protocol.

### Packet Details pane
- Displays the above in more detail
- Will show the thing in layers (lowest layer to highest layer)
- When you click on the specific header, you'll pick up the headeryer. 

### Display filter
- `ether <MAC_address>` can be used to isolate traffic. 
- `host IP-address`: This filter limits the captured traffic to and from the IP address
- `net 192.168.0.0/24`: This filter captures all traffic on the subnet
- `dst host IP-address`: Capture packets sent to the specified host
- `port 53`: Capture traffic on port 53 only
- `port not 53 and not arp`: Capture all traffic except DNS and ARP traffic
