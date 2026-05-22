---
summary: "Model of concurrent computation, that treats an actor as the basic building block of concurrent computation. In response to a message it receives, an actor can: make local decisions, make more actors, send more messages, and determine how to respond to the next method received. Actors may modify their own private state, but can only affect each other indirectly through messaging (no need for lock-based synchronization)."
headings: ["[[#Concepts of Note]]"]
type: note/concept
concept_of: ["[[DP Concurrent Computation]]"]
date created: Tuesday, April 8th 2025, 2:00:55 pm
date modified: Monday, September 29th 2025, 7:59:57 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Actor model - Wikipedia](https://en.wikipedia.org/wiki/Actor_model)
[How the Actor Model works by example](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-the-Actor-Model-works-by-example)

## Concepts of Note
󰙎  Actor Model ;;; A style of software architecture, where the basic unit of computation does not share state, run concurrently, and the location of each unit is transparent. Intended for high-scalability systems. = #cs/design_pattern/concurrent/actor-model  
<!--ID: 1759154610070-->


󰠗  In what situations is the actor model a good design pattern? ;; Complex workflows, streaming apps, concurrent applications, highly available systems. Manufacturing processes that have series of steps is a good example. Multi-user concurrency. = #cs/design_pattern/structural/actor_model 
<!--ID: 1758253289650-->

󰠗  What are the drawbacks to using the actor model? ;; Does not implement a central controller and it is difficult to test and debug. = #cs/design_pattern/structural/actor_model  
<!--ID: 1758253289656-->

