---
summary: Design pattern that lets you split a large class or set of closely related classes into two separate hierarchies (abstraction and implementation), which can be developed independently of each other.
headings: ["[[#Concepts of Note]]", "[[#Flashcards]]"]
type: note/item
implements: "[[Abstract Factory]]"
concept_of: ["[[DP Structural Patterns]]"]
date created: Friday, October 11th 2024, 3:52:47 pm
date modified: Monday, September 29th 2025, 10:39:30 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Switches from [[CS OOP Inheritance|Inheritance]] to [[PT OOP Composition|Composition]].
- Usually designed up-front, letting you develop parts of an application independently of each other.
- [[DP Adapter]] is commonly used with existing apps.

[Bridge](https://refactoring.guru/design-patterns/bridge)
- Has code examples in a bunch of different languages. 

## Flashcards
󰠗  What design pattern makes sense when you are trying to extend classes in two independent dimensions (i.e. Form/color, GUI elements, different APIs), and don't want inheritance problems? ;; The bridge = #cs/design_pattern/structural/bridge
<!--ID: 1759377309214-->

󰠗  How does the bridge solve class hierarchy "explosion"? ;; By transforming one potentially-complicated hierarchy into two separate hierarchies. = #cs/design_pattern/structural/bridge 
<!--ID: 1759377309218-->
