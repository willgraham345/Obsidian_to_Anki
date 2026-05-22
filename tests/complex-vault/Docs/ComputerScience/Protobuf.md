---
summary: "Google's take on a messaging frameworks that is platform independent, and can be used for sending data or messages serially. "
headings:
  - "[[#Concepts of Note]]"
  - "[[#Flashcards]]"
type: note/system
implements:
  - "[[CS Messaging and Serialization]]"
similar:
  - "[[Flatbuffers]]"
date created: Friday, November 7th 2025, 11:39:44 am
date modified: Thursday, November 20th 2025, 12:02:17 pm
template: "[[base_note_template]]"
template-version: 1.0.0
item_of:
  - "[[Serial Protocols]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
https://protobuf.dev/getting-started/cpptutorial/

## Concepts of Note
### Pros
- Small binary size, strong schema evolution, and great language support (gRPC).

### Cons
- Requires a compilation step
- Not "zero-copy" (requires decoding step)

## Flashcards
󰠗  What are the pros/cons of the Protobuf serialization protocol? ;; Pros: has as small binary size, strong schema evolution, great language support. Cons: requires compilation step, not zero-copy (requires decoding). = #cs/networking/protocols/serial 
