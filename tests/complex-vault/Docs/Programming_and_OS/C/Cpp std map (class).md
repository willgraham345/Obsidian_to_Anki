---
summary: Maps are associative containers formed by a combination of a key value and a mapped value (types for key and mapped value don't have to match). The key values are generally used to map and identify the elements. Internally, the elements in a map are always sorted by its key following a specific "strict weak ordering" criterion indicated by its internal `Compare` object.<br><br>Similar to a list<pair<>>, but has more lookup options.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/class
classes: ["[[Cpp std map (library)]]"]
similar: ["[[Cpp std pair (class)]]", "[[Cpp std unordered_map]]"]
class_of: ["[[Cpp std map (library)]]"]
date created: Monday, January 6th 2025, 10:41:03 am
date modified: Monday, October 20th 2025, 4:05:08 pm
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Generally slower than `unordered_map`
- Container properties
	- **Associative** = Elements in associative containers are referenced by their _key_ and not by their absolute position in the container.
	- **Ordered** = The elements in the container follow a strict order at all times. All inserted elements are given a position in this order.
	- **Map** = Each element associates a _key_ to a _mapped value_: Keys are meant to identify the elements whose main content is the _mapped value_.
	- **Unique keys** = No two elements in the container can have equivalent _keys_.
	- **Allocator-aware** = The container uses an allocator object to dynamically handle its storage needs.

## Usage

  `myMP->try_emplace(a, obj)` ;;; Build an object `obj` at index `a` in a map `myMap` which is accessed as a `unique_ptr` by directly building within the object. = #lang/data/map #lang/IO/std 


`Key` Type of the keys, aliased as member type `map::key_type`
`T` Type of the mapped value. Each element in a `map` stores some data as its mapped value.
`Compare` Binary predicate that takes two element keys and returns a `bool`.  The `map` uses this expression to determine whether two keys are equivalent. No two elements in a `map` container can have equivalent keys.

[Map in C++ Standard Template Library (STL) - GeeksforGeeks](https://www.geeksforgeeks.org/map-associative-containers-the-c-standard-template-library-stl/)
