---
summary: 
headings: ["[[#Concepts of Note]]"]
type: note/item
date created: Monday, August 11th 2025, 5:32:26 pm
date modified: Saturday, November 8th 2025, 11:45:01 am
item_of: ["[[openc3 protocols]]"]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰙎  Accessors ;;; Low-level code acting on behalf of a protocol, which knows how to read and write into and out of buffers. These handle the serialization formats (i.e. CCSDS, JSON, CBOR, XML, HTML). The buffer data is then written out in an interface which uses protocols to potentially changes the data. = #tools/openc3/interfaces/protocols
