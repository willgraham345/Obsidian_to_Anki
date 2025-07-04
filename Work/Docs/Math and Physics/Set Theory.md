---
summary: Used to define elements and properties of "sets" using symbols. A "set" is often used to define relationships and operations among sets.
headings: ["[[#Concepts of Note]]"]
type: note/concept
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, June 27th 2025, 4:05:13 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] Cardinality = The number of distinct elements within the set, or the "size" of the set. = #term/math
- [I] Sum type (disjoint union) = The cardinality of valid states for the set/type is equal to the sum of valid states. i.e. Restaurant has two members: cuisine, and open on holidays. Open on holidays is a bool, which has two valid states. We'll say that there are 3 types of cuisine: Mexican, Chinese, Italian. The cardinality of this set is (2)+(3) = 5.  ^3fb4e7
- [I] Product type (joint union) = The cardinality of valid states for the set/type is equal to the product of all variant types.
- [I] Isomorphic = One set that *can* carry the same information as another. They can be converted between each other.
- Set notation is used to define elements and properties of sets using symbols.
- A set is used to define relationships and operations among sets

|   |   |
|---|---|
|**Symbol**|**Meaning**|
|∈|‘is a member of’ or ‘is an element of’|
|∉|‘is not a member of’ or ‘is not an element of’|
|{ }|denotes a set|
|**\|**|‘such that’ or ‘for which’|
|:|‘such that’ or ‘for which’|

## How to Denote a Set
- We denote a set by a capital letter, and an element of the set by lower-case letters
- We separate the elements using commas

### Example
Set $A$
$A = \{a, e, i, o, u\}$

## How to Denote Membership in a Set
We use the symbol $\in$ to denote membership in a set

### Examples 
$B = \{x | x \in \mathbb{N}$ and $x \le 5 \}$
- The set of all x such that x is a natural number less than or equal to 5
- another way of representing is $B = \{x:x \in \mathbb{N}$ and $x \le 5\}$ 

## Subsets of a Set
- We can say that set A is a subset of set B when every element of A is also an element of B. The notation is:
	- $A \subset B$
		- A is a subset of B
		- A is contained in B

## Mapping
When we write $f:A \rightarrow B$, we mean that $f$ takes things in $A$ and maps them into a thing in $B$. 
- $f:x\rightarrow y$ means that $f(x)=y$
- 

