---
summary: A common idealized method for explaining how networks work, defined by the International Standards Organization. Protocol-independent model, coming after the TCP IP model. Has not been implemented as well as the TCPIP model in high stress and high traffic networks.
type: note/system
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
concepts:
  - "[[Network IP Multicasting]]"
  - "[[Networking Communication]]"
  - "[[Networking OSI Cybersecurity]]"
  - "[[Networking UDP]]"
  - "[[TCP-IP Model]]"
similar:
  - "[[TCP-IP Model]]"
associations:
  - "[[Networking Protocols]]"
concept_of:
  - "[[Networking]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, March 31st 2026, 10:32:07 am
images:
  - "[[Network OSI Model.png]]"
  - "[[OSI Network Model 2.jpg]]"
  - "[[OSI Network Model.png]]"
items:
  - "[[Networking Application Layer]]"
  - "[[Networking LAN Technologies]]"
  - "[[Networking Link Layer 2]]"
  - "[[Networking network driver]]"
  - "[[Networking Network Layer 3]]"
  - "[[Networking Physical Layer 1]]"
  - "[[Networking port]]"
  - "[[Networking proxy server]]"
  - "[[Networking reverse proxy]]"
  - "[[Networking Session Layer 5]]"
  - "[[Networking socket]]"
  - "[[OSI Transport Layer 4]]"
tags: []
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- 

### Layers %% fold %% 
#### [[Networking Application Layer]] - Data
#### [[OSI Presentation Layer 6]] - Data
#### [[OSI Session Layer 5]] - Data
#### [[OSI Transport Layer 4]] - Segments

#### [[OSI Network Layer 3]] - Packets

#### [[OSI Data Link Layer 2]] - Frames
- Establishes and terminates a connection between two physically-connected nodes on a network. 
- Breaks up packets and sends them from source to destination. 

- Comprises two parts:
	- Logical Link Control (LLC) = identifies network protocols, performs 
	- Media Access Control (MAC) = uses MAC addresses to connect devices and define permissions to transmit and receive data.

#### [[OSI Physical Layer 1]] - Bits
- Physical cable or wireless connection between network nodes.
- Defines connector, electrical cable/wireless tech, and is responsible for transmission of raw data (1s and 0s) while taking care of bit rate control.T

## Diagrams
- ![[OSI Network Model.png | 900]]
- ![[OSI Network Model 2.jpg|300]]
- ![[Network OSI Model.png | 300]]



