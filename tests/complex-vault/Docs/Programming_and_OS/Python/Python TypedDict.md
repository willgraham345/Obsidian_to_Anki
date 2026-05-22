---
summary: Class that can define any number of items, conditional upon `dict` objects only contaiing keys of type `str`. Values that are a member of the set of a TypedDict type must be instances of `dict` itself, not a subclass. Created as a way to give structure to a dictionary.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/class
prev:
  - "[[Python Dict]]"
class_of:
  - "[[Python typing]]"
date created: Thursday, December 4th 2025, 11:58:50 am
date modified: Monday, December 8th 2025, 11:55:03 am
tags:
  - lang/data/dict
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
 Open `TypedDict` ;; A `TypedDict` that *can* accept additional keys beyond what is originally declared. 
󰠗 Are `TypedDict`s in Python defaulted to open or closed? What does that mean? ;; They default to be closed, which means they *can't* accept any additional keys that aren't declared.

[The varying strictness of TypedDict](https://snarky.ca/the-varying-strictness-of-typeddict/)

## Usage
 `a: tdType = {"input": 3, "op": "add"}` ;;; Instantiate (do not define) `a`, which is custom type of `tdType` that inherits from `TypedDict`. `tdType` should have fields `input` set to 3, and `op` set to `"add"`.

 `class A(TypedDict)` ;;; Create `A`, a structured dictionary that *can* accept keys beyond what is initially declared. 
 `class A(TypedDict, closed=False)` ;;; Create `A`, a structured dictionary that *can* accept keys beyond what is initially declared. 
 `class A(TypedDict, closed=False, total=False)` ;;; Create `A`, a structured dictionary that *can* accept keys beyond what is initially declared, and doesn't require all arguments to be created. 

