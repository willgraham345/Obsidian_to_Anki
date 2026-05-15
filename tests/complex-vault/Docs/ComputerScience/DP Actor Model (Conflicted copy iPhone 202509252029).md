---
summary: "Model of concurrent computation, that treats an actor as the basic building block of concurrent computation. In response to a message it receives, an actor can: make local decisions, make more actors, send more messages, and determine how to respond to the next method received. Actors may modify their own private state, but can only affect each other indirectly through messaging (no need for lock-based synchronization)."
headings:
  - "[[#Concepts of Note]]"
type: note/concept
concept_of:
  - "[[DP Concurrency Patterns]]"
date created: Tuesday, April 8th 2025, 2:00:55 pm
date modified: Wednesday, July 16th 2025, 8:53:49 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Actor model - Wikipedia](https://en.wikipedia.org/wiki/Actor_model)
[How the Actor Model works by example](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-the-Actor-Model-works-by-example)

## Concepts of Note
󰙎  Actor Model ;;; A style of software architecture, where the basic unit of computation is called an actor. Actors do not share state, run concurrently, and the location of an actor is transparent. Intended for high-scalability systems. = #cs/design_pattern/concurrent/actor-model  
󰠗  In what situations is the actor model a good design pattern? ;; Complex workflows, streaming apps, concurrent applications, highly available systems. Manufacturing processes that have series of steps is a good example. Multi-user concurrency. = #cs/design_pattern/structural/actor_model 
󰠗  What are the drawbacks to using the actor model? ;; Does not implement a central controller and it is difficult to test and debug. = #cs/design_pattern/structural/actor_model  
