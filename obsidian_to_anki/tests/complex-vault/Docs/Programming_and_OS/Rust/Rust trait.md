---
summary: A collection of associated items (functions, types, constants) that will be used by various types. Does this by using an abstract interface with an implied virtual method table.
type: note/concept
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
concepts:
  - "[[Rust bounds]]"
  - "[[Rust function traits and generics]]"
  - "[[Rust struct traits and generics]]"
similar:
  - "[[Cpp Class virtual functions]]"
  - "[[Cpp interface]]"
  - "[[Python Protocols]]"
next:
  - "[[Rust impl]]"
prev:
  - "[[Rust bounds]]"
date created: Friday, March 21st 2025, 10:32:20 am
date modified: Tuesday, March 3rd 2026, 11:52:04 am
item_of:
  - "[[Rust Items]]"
  - "[[Rust Variables and Type System]]"
tags: [lang/functions/bounds, lang/impl/specific, lang/oop/generics, lang/oop/generics/function, lang/oop/interface_trait, lang/oop/interface_trait/associated-types, lang/oop/interface_trait/bounds, lang/oop/interface_trait/constants, lang/oop/interface_trait/function_method, lang/oop/interface_trait/impl_trait, lang/oop/interface_trait/items/associated-types, lang/oop/interface_trait/trait_object, lang/oop/interface_trait/types]
template:
template-version:
used_by:
  - "[[Rust enum]]"
  - "[[Rust Functions]]"
  - "[[Rust Items]]"
uses:
  - "[[Rust associated items]]"
  - "[[Rust associated types]]"
  - "[[Rust Box]]"
  - "[[Rust dyn]]"
  - "[[Rust impl]]"
---

# Summary
󰙎 Rust trait ;;; A collection of associated items (functions, types, constants) that will be used by various types. Does this by using an abstract interface with an implied virtual method table.

# Additional Background

[Traits - The Rust Reference](https://doc.rust-lang.org/reference/items/traits.html)

## Concepts of Note

- Traits _require_ that the associated items have a [[Rust impl]] statement or a [[Rust derive macros]] that satisfies the trait.
- Traits should be placed in the name of the module/block where they are located.
- Traits define an implicit type param `Self` that refers to the type that implements the interface.

### Terminology

󰙎  Traits ;;; Give you a way to _describe_ related types, which implement shared behavior among different `impl`s. Describes what related types _do_ (by defining their methods, types they must define, and occasionally constants they must use). =

󰙎  Trait object ;;; An opaque value of another type that implements a set of traits. Made up of a dyn compatible base trait plus any number of auto traits. = ^36ef0c
<!--ID: 1758253288298-->

󰙎  Impl trait ;;; A type in rust that provides a way to specify unnamed but concrete types that implement a specific trait. Can appear in an argument position (function args), or the return position (acts as an abstract return type). I _think_ this is the same as a generic constraint but in a more digestible syntax. =
<!--ID: 1758253288305-->

󰙎  Associated constants ;;; Constants which are associated with a type. These declare a signature for associated constant definitions. =
<!--ID: 1758253288311-->

󰙎  Abstract return type (in rust) ;;; Also known as the `impl` Trait in return position. This lets you return an abstract type, where the caller may only use the methods declared by the specified `Trait`. =
<!--ID: 1758253288317-->

󰙎  Abstract trait ;;; Defines interfaces or contracts, but does not provide a default implementation of them. Related to an [[Rust impl#^7fe2e8|abstract implementation]] =
<!--ID: 1758253288323-->

### Handling errors on traits which can't error

- use the [[Rust Infallible]] trait

## Usage

### Associated Types

󰠗  What are the two _varieties_ of associated items? ;; 1. Definitions which contain the actual implementation, 2. Declarations that declare signatures for definitions = ^9617d9
<!--ID: 1758253288218-->

󰠗  What are the two ways to satisfy an associated item for a trait? ;; An `impl` statement or a rust `derive()` macro. =
<!--ID: 1758253288224-->

󰠗  Assume you have a trait with an associated item (i.e. constant, method, type). What is the best way to declare that trait's usage for the struct? ;; An `impl` statement, typically using the `impl <trait> for <type> {//statements}` =
<!--ID: 1758253288230-->

### Trait types and bounds

󰠗  What are the two _types_ of traits? ;; Impl trait (way to specify unnamed but concrete type that specify a specific trait.) and a trait object (value of another type that implements a set of traits). =
<!--ID: 1758253288243-->

  `pub trait A { fn summarize(&self) -> String { println!(“Summary: {self.field}”) }}` ;;; Declares a trait `A` which has a default implementation for its `summarize` method. =
<!--ID: 1758253288283-->

󰠗  How do you typically create a bound for a trait? ;; Through generic parameters passed into the `impl` statement. =
<!--ID: 1758253288252-->

  `fn foo(arg: impl Trait) { }` ;;; Function definition where the argument is an unnamed object that implements the trait `Trait`. =
<!--ID: 1758253288289-->

󰠗  What is nearly identical to an impl trait object? What is the only difference between the two? ;; A generic type parameter. The only difference is that the type for an impl trait is anonymous and doesn't appear in the [[Rust GenericParameters]] list. =
<!--ID: 1758253288260-->

󰠗 What is the difference between these two statements:
  `fn function1<T: Trait>(arg: T) { }`
  `fn function2(arg: impl Trait) { }` = `function1` has the trait as a generic, which will load it into the [[Rust GenericParameters]] list. `function2` uses an impl trait, which will anonymously perform just about the same thing. The caller will not have the option to specify the generic argument for `T` in `function1`.
󰠗  What size is a trait object? ;; It is dynamically sized, and is used behind a type of pointer.
󰠗  What is the difference between `fn f<T: aTrait>(item: &T>` and `fn f(item: &impl aTrait)` ;; None. These are alternative ways of performing the same thing. Notably, the `impl trait` method is helpful when you're trying to have multiple types that implement a similar trait. Makes syntax more concise. =
<!--ID: 1758253288267-->

󰠗  "A trait is generic over its container type" means what? ;; Users of the `trait` must specify _all_ of its generic types. =
<!--ID: 1758253288275-->

![[Rust bounds#^f741de]]
![[Rust bounds#^352403]]

### Ways to implement traits

- [[Rust impl]]
  - [[Rust derive attribute macros]]

### Ways traits are used

- [[Rust Function Parameters]]

## Breadcrumbs %% fold %%

(the graphs were slowing this thing down)

```
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
depth: [0, 3]
show-attributes: [field]
```

```
type: mermaid
field-groups: [ups]
merge-fields: true
sort: field asc
depth: [0, 3]
show-attributes: [field]
```
