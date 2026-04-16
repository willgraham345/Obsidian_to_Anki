---
summary: Different types of storage, and their protocols/connections.
type: note/item
headings:
date created: Saturday, December 28th 2024, 1:20:51 pm
date modified: Wednesday, April 8th 2026, 9:10:32 am
item_of:
  - "[[Networking Protocols]]"
items:
  - "[[Networking NVME]]"
  - "[[Networking PCIe]]"
  - "[[Networking SATA]]"
tags: []
template:
template-version:
used_by:
  - "[[CS Memory Types]]"
  - "[[CS Memory]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Additional types of hard drive connection
- PATA (old)
	- Molex power
	- PATA data
	- 10 MB/s max
- SATA (serial ATA)
	- SATA power
	- SATA data (smaller than the last ribbon cable)
	- 600 MB/s max
	- There’s also mSATA drives (mini SATA)
- SSD
	- No spinning disk
	- Same connectors as SATA
	- 220 MB/s
	- More expensive
- micro SD
- PCIe
	- For graphics cards and other stuff
