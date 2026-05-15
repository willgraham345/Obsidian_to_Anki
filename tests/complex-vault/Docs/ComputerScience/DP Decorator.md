---
summary: Structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors. Also known as a "wrapper". Done by referencing one object from another.
headings: ["[[#Concepts of Note]]", "[[#Diagrams]]"]
type: note/concept
implements: ["[[PT OOP Composition]]"]
similar: ["[[DP Chain of Responsibility]]", "[[DP Composite]]"]
prev: ["[[DP Composite]]"]
date created: Friday, October 11th 2024, 4:00:07 pm
date modified: Tuesday, November 11th 2025, 2:50:24 pm
diagrams: ["[[decorator.puml]]"]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Decorator](https://refactoring.guru/design-patterns/decorator)

󰙎  Wrapper ;;; Alternative name for the decorator pattern. = #cs/design_pattern/structural/decorator #lang/functions/decorators
- [p] thing

## Concepts of Note

- You may want to extend classes capabilities, without creating a huge dependency tree of implementation classes. (i.e. you don't want 1000 different Notification classes for email, phone, sms, facebook, and twitter notifications).
  - Additionally, this creates inheritance trees which are static and can't be modified at runtime. For you to alter the behavior of an existing object, you'd need to recreate the entire object with another one created from a different subclass.
- Many languages don't let you inherit behaviors from multiple classes at the same time.
  - You can get around this with an aggregation/composition, with the downside that an object _has_ to reference another and delegate some work.
- The decorator is a way to substitute a linked "helper" object with another, changing the behavior of the container at runtime.
  - Your object can have references to multiple objects, and delegate work to them. Aggregation/composition is the key principle behind this, just without worrying about directly writing that within the code.
- A wrapper is an alternative nickname for the decorator pattern.
- You can think of this as a "layered" effect when using functions

## Diagrams

Inheritance is static. You can't alter the behavior of an existing object at runtime. You can only replace the whole object with another one that's just been created.
Subclasses can only have one parent class (in most languages).

Use [[PT OOP Composition]] to delegate work to other objects.
![[DP Decorator.png | 300]]
