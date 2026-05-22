---
summary: Frameworks for designing successful messages.
type: note/concept
headings: ["[[#Breadcrumbs]]", "[[#Diagrams]]"]
concepts: ["[[Ack Nak Process]]"]
associations: ["[[Networking Messaging]]", "[[Networking Protocols]]"]
concept_of: ["[[CS]]"]
date created: Monday, September 8th 2025, 1:55:53 pm
date modified: Monday, January 12th 2026, 11:59:48 am
implementations: ["[[CCSDS Packet Transfer Protocol]]", "[[Flatbuffers]]", "[[JSON]]", "[[Protobuf]]", "[[ZMQ]]"]
tags: [cs/design_pattern/messaging/guaranteed, cs/networking/protocols, cs/networking/testing, lang/meta/tokens]
template:
template-version:
used_by:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎  Guaranteed delivery ;;; Once a message is placed into a message channel, the messaging system guarantees that the message will reach the destination even if parts of the application should fail. In general, this looks like writing messages to persistent store before attempting to deliver them to their destination. =
<!--ID: 1758253289686-->

󰙎 IDL ;;; interface description language = 
󰙎 Serialization ;;; Describes a way data can be marshalled into a format, and unmarshalled from a format. Importantly, this doesn't necessarily imply a binary communication method. =
󰙎 Token ;;; Sequence of characters having collective meaning. Individual instance of a type of symbol (i.e. "error" has 3 "r" tokens), or something that serves as a sign of something else. =
󰙎 Fuzzer ;;; An automated software testing technique that provides invalid, unexpected, or random data as inputs to a program.

## Breadcrumbs
```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```

## Diagrams

### Guaranteed Delivery Pattern
![[CS Messaging Frameworks.png | 500]]
