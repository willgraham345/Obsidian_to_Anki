---
summary: "A behavioral design pattern which lets you define a subscription mechanism to notify multiple objects about events happening to the object they're observing. "
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Flashcards]]"
type: note/concept
similar:
  - "[[DP Mediator]]"
associations:
  - "[[DP Chain of Responsibility]]"
  - "[[DP Command]]"
concept_of:
  - "[[Behavioral Patterns]]"
date created: Tuesday, November 18th 2025, 10:13:11 am
date modified: Thursday, December 4th 2025, 4:59:50 pm
diagrams:
  - "[[observer.puml]]"
images:
  - "[[observer.svg]]"
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

### Pros:
- Introduce new subscriber classes without having to change publishers code
- Can establish relationships between objects at runtime

### Cons:
- Subscribers are notified in a random order

## Diagrams
![[observer.svg]]
https://refactoring.guru/images/patterns/diagrams/observer/solution2-en-2x.png?id=630cfb84753c258aa4e8500e189c0b65


https://refactoring.guru/images/patterns/diagrams/observer/structure-indexed-2x.png?id=910eec855bc41f05199e510494078926

## Flashcards
STARTI [Basic] What type of design pattern is this? 
![[observer.svg]]
Back: Observer
ENDI

󰠗  When should you use the observer pattern? ;; When changes to the state of one object may require changing other objects, and the actual set of objects is unknown beforehand or dynamically. Also used when some objects must observe other objects, but only for a limited time. = #cs/design_pattern/behavioral/observer
󰠗  What are the pros of the observer model? ;; You can introduce a new subcriber class without having to change the publisher code (and vice versa), and you can establish relations between objects at runtime. #cs/design_pattern/behavioral/observer 
󰠗  What are the cons of the observer model? ;; Subscribers are notified in a random order. = #cs/design_pattern/behavioral/observer 
󰠗  What pattern is the observer very similar to? What's the difference between their goals. ;; The mediator. The mediator wants to eliminate mutual dependencies of system components, instead relying on a single object. A popular implementation of the Mediator relies on the Observer. = #cs/design_pattern/behavioral/observer #cs/design_pattern/behavioral/mediator
