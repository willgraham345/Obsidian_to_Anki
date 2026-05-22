---
summary: The "mail trucks" of the networking toolchain. These handle delivering messages, but not the serialization or writing into buffers.
type: note/item
headings:
associations:
  - "[[CS Messaging and Serialization]]"
  - "[[Networking Topology]]"
date created: Thursday, November 20th 2025, 11:38:45 am
date modified: Tuesday, March 31st 2026, 10:34:20 am
implementations:
  - "[[gRPC]]"
  - "[[MPI]]"
  - "[[NNN]]"
  - "[[quic]]"
  - "[[ZMQ]]"
item_of:
  - "[[Networking]]"
items:
tags: [cs/networking/message-frameworks]
template: "[[base_note_template]]"
template-version: 1.0.0
uses:
  - "[[Networking CRC]]"
  - "[[Networking network driver]]"
  - "[[Networking port]]"
  - "[[Networking Protocols]]"
  - "[[Networking proxy server]]"
  - "[[Networking socket]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎  Message broker ;;; Piece of software which enables services and apps to communicate with each other using messages. Message structure is formally defined and independent from the services that send them. 
