---
summary: Metadata applied to a module, create, or item. There are a few typical use cases, described in the components. Attributes can take arguments, but do not have to.
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
type: note/concept
items:
  - "[[Rust std attribute macros]]"
associations:
  - "[[Rust derive attribute macros]]"
concept_of:
  - "[[Rust Generics]]"
  - "[[Rust procedural macros]]"
date created: Tuesday, March 25th 2025, 9:19:42 pm
date modified: Friday, May 30th 2025, 9:45:58 am
libraries:
  - "[[Rust std attribute macros]]"
tags:
  - lang/meta/attributes
  - lang
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

󰙎  Attribute ;;; Metadata for the item/module/struct/crate. Varying use cases (unit testing, diagnostics, deriving new code, code generation, type system) = #lang 


󰙎  Attribute macro ;;; An outer attribute which can be attached to items. See attribute for more info = #lang 



### Scope

- Can be applied at the module/crate level, or the item level. See [[Rust Organization and Dependencies]] for more info
- Attribute consists of:
  - Path to the attribute
  - (Optional) delimited token tree
  - Attributes other than macro attributes also allow the input to be an `=`

### Safety

- Attributes may be unsafe. To avoid this, certain obligations that can't be checked by the compiler should be met. To assert this, wrap the attribute in `unsafe(..)`

## Usage

  `#![attribute]` ;;; Apply an attribute to the crate/module level = #lang/meta/attributes 
ID: 1751997628559



  `#[attribute]` ;;; Apply an attribute to the item = #lang/meta/attributes 
ID: 1751997628563



  `#[repr(u8)]` ;;; Tells the compiler to represent the enum in memory using a `u8` rather than the default `isize` = #lang/data/enumeration/discriminant #lang/data/enumeration #lang/meta/attributes/repr 
ID: 1751997628567




### Examples

```
#[attribute = "value"]
#[attribute(key = "value")]
#[attribute(value)]
```

## Breadcrumbs

```breadcrumbs
type: mermaid
field-groups: [downs, sames]
merge-fields: true
sort: field asc
show-attributes: [field]
```
