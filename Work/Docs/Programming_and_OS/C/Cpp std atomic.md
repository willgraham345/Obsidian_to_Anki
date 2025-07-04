---
summary: 
headings: ["[[#Concepts of Note]]"]
type: 
date created: Tuesday, June 10th 2025, 9:12:41 am
date modified: Tuesday, June 10th 2025, 9:15:11 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] Memory ordering (memory barrier) = Barrier instruction that causes a CPU/compiler to enforce ordering constraint on memory operations issued before/after the barrier instruction. Typically means that operations issued prior to the barrier are guaranteed to be performed before operations issued after the barrier.
- [I] Barrier = Type of synchronization method, means that any thread/process must stop at this point and cannot proceed until all other threads/processes reach this barrier.