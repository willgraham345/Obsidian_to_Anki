---
summary: Sniffer and packet analyzer
date created: Saturday, November 2nd 2024, 9:50:33 pm
date modified: Sunday, November 3rd 2024, 10:08:50 am
type: 
---
`VIEW[**{summary}**][text(renderMarkdown)]`

[Learn Wireshark – Computer Networking Tutorial](https://www.freecodecamp.org/news/learn-wireshark-computer-networking/)


[Wireshark Wiki](https://wiki.wireshark.org/)
[Display Filter Reference](https://www.wireshark.org/docs/dfref/)
# Usage
Capture options
- Pick whatever interface you're interested in, or whichever has traffic going through it. 

## Packet list pane
- Displays short summary of each packet. 
- Source: Address where this packet is coming from
- Destination: Where this packet is going
- Protocol: Name in short version
- Length: Each packet in bytes
- Info: Additional info about packet content, changes according to protocol.

## Packet Details pane
- Displays the above in more detail
- Will show the thing in layers (lowest layer to highest layer)
- When you click on the specific header, you'll pick up the headeryer. 

## Display filter
- `ether <MAC_address>` can be used to isolate traffic. 
- `host IP-address`: This filter limits the captured traffic to and from the IP address
- `net 192.168.0.0/24`: This filter captures all traffic on the subnet
- `dst host IP-address`: Capture packets sent to the specified host
- `port 53`: Capture traffic on port 53 only
- `port not 53 and not arp`: Capture all traffic except DNS and ARP traffic
