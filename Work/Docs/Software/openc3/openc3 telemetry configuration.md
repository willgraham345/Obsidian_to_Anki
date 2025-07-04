---
summary: Telemetry definition is determined from telemetry fi[s placed in the target's cmd_tlm directory and are processed alphabetically. Telemetry items can be a variety of types (INT, UINT, FLOAT, STRING, BLOCK). All packets require ID items. If you have telemetry files that depend on each other, they can override existing telemetry
type: note/component
date created: Wednesday, March 26th 2025, 9:19:55 am
date modified: Wednesday, March 26th 2025, 9:27:17 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- ID Items
	- Resulting packet is identified by matching the ID fields.
- Variable sized
	- Items have bit sizes of 0. 
- Derived items
	- Telemetry items that don't exist in the binary data, but typically computed based on other telemetry items.
- Received time vs packet time
	- received time is when COSMOS receives the packet. Packet time defaults to received time, but can be set in other ways.
