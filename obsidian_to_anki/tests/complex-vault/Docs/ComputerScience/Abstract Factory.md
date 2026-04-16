---
summary: Lets you produce families of related objects. Typically used after having implemented a few factory methods (less complicated).
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Usage]]"
prev:
  - "[[Factory Method]]"
concept_of:
  - "[[DP Creational Patterns]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, March 3rd 2026, 11:57:28 am
images:
  - "[[AbstractFactory.png]]"
  - "[[AbstractFactory2.png]]"
  - "[[DP Abstract-factory.png]]"
implementations:
  - "[[DP Bridge]]"
  - "[[Cpp Class virtual functions]]"
tags:
  - cs/design_pattern/creational/abstract_factory
template:
template-version:
uses:
  - "[[Cpp interface|Cpp abstract classes]]"
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Refactoring template website](https://refactoring.guru/design-patterns/cpp)

## Concepts of Note

### Use cases

- When you have a set of [[Factory Method]]s that blur its primary responsibility.
- When your code needs to work with families of related products, but you don't want it to depend on the concrete classes of these products. They may be known beforehand or you want future extensibility.
  - i.e.: You need a `Chair`, a `Sofa` and a `CoffeeTable` which are related products. They come in styles: `Modern`, `Victorian`, and `ArtDeco`. An abstract factory lets you create these furniture objects so they match other objects of the same family.

1. **Abstract Products** declare interfaces for a set of distinct but related products which make up a product family.
   1. All chair variants can interface with the `Chair` interface, all coffee table variants interface
2. **Concrete Products** are various implementations of abstract products, grouped by variants. Each abstract product (chair/sofa) must be implemented in all given variants (Victorian/Modern).
   1. i.e. `createChair`, `createSofa` `createCoffeeTable`. These methods must return **abstract** product types represented by the interfaces we extracted previously (`Chair`, `Sofa`, `CoffeeTable`)
3. The **Abstract Factory** interface declares a set of methods for creating each of the abstract products.
4. **Concrete Factories** implement creation methods of the abstract factory. Each concrete factory corresponds to a specific variant of products and creates only those product variants.
5. Although concrete factories instantiate concrete products, signatures of their creation methods must return corresponding *abstract* products. This way the client code that uses a factory doesn’t get coupled to the specific variant of the product it gets from a factory. The **Client** can work with any concrete factory/product variant, as long as it communicates with their objects via abstract interfaces.

## Diagrams

![[AbstractFactory.png]]

- Lets you produce families of related objects without specifying their concrete classes

## Why/when would you use this?

Why?

1. Constructors are limited in their control in a creation process.
2. Constructors don't communicate their intention well, as they have to be named after their class --> replacing a constructor with a factory has intention-revealing creation methods
   When?

- Creation of objects involve caching, sharing, or re-using of objects
- Applications that need to maintain object and type counts.
- When the client does not know exactly what type to construct.
  - It's easier to code against a type or interface and then let a factory make this decision for the client (based on parameters or other context)

## Flashcards

󰠗  What are the advantages to using an abstract factory class? ;; More clear intention than a builder/ctor, creation of objects doesn't involve caching/sharing/or re-using of objects, client doesn't need to know exactly what type to construct. =
<!--ID: 1759415941337-->

󰠗 What design pattern should
