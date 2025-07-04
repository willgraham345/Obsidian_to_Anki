---
summary: "Model of concurrent computation, that treats an actor as the basic building block of concurrent computation. In response to a message it receives, an actor can: make local decisions, make more actors, send more messages, and determine how to respond to the next method received. Actors may modify their own private state, but can only affect each other indirectly through messaging (no need for lock-based synchronization)."
headings: 
type: note/concept
concept_of: ["[[DP Concurrent Computation]]"]
date created: Tuesday, April 8th 2025, 2:00:55 pm
date modified: Tuesday, April 8th 2025, 2:03:22 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Actor model - Wikipedia](https://en.wikipedia.org/wiki/Actor_model)