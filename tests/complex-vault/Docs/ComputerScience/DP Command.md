---
summary: "Behavioral design pattern that turns a request into a stand-alone object that contains all info about the request. This lets you pass requests as args, delay a queue or request execution time, and support undoable operations. "
headings: ["[[#Concepts of Note]]", "[[#Diagrams]]", "[[#Flashcards]]"]
type: note/concept
associations: ["[[DP Memento]]", "[[DP Observer]]"]
concept_of: ["[[Behavioral Patterns]]"]
date created: Thursday, December 4th 2025, 5:00:53 pm
date modified: Thursday, December 4th 2025, 5:10:03 pm
diagrams: ["[[command.puml]]"]
images: ["[[command.svg]]"]
template: "[[base_note_template]]"
template-version: 1.0.0 - "[[Behavioral Patterns]]"
used_by: ["[[DP Memento]]", "[[DP Visitor]]", "[[Prototype]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Use cases
- When you want to parameterize objects with operations.
- When you want to queue operations, schedule execution, or execute them remotely.
- When you want to implement reversible operations.

### Pros/Cons
- Pros:
	- Single responsibility principle, decouples classes that invoke operations from classes that perform the operations
	- Open/closed principle
	- Enables implementing undo/redo
	- Enables deferred execution of code
	- You can compose/aggregate commands into more complicated commands.
- Cons:
	- The code may become more complicated since you're introducing a new layer between senders/receivers.
#TODO/refactor add pros/cons flashcard entries for these...
## Diagrams
![[command.svg]]

## Flashcards
#todo/refactor Needs flashcards added...