---
summary:
type: note/item
headings:
  - "[[#Concepts of Note]]"
concept_of:
  - "[[openc3 configuration]]"
date created: Monday, August 11th 2025, 5:17:44 pm
date modified: Friday, March 20th 2026, 9:43:52 am
item_of:
  - "[[openc3 interfaces]]"
items:
  - "[[openc3 accessors]]"
tags: [tools/openc3/interfaces/protocols]
template:
template-version:
used_by:
  - "[[openc3 interfaces]]"
  - "[[openc3 plugins]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Protocols \| OpenC3 Docs](https://docs.openc3.com/docs/configuration/protocols)

## Concepts of Note
󰙎  Protocols ;;; Process data on behalf of an "Interface". Can read, write or both with modifications.


- Typically used to define logic to delineate packets and manipulate data as it is written to and read from Interfaces. 
- COSMOS includes interfaces for TCP/IP Client, TCP/IP Server, Udp Client / Server, and serial connections.
	- These likely won't require changes, and all unique behavior should be defined within [[openc3 protocols]].
