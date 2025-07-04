---
summary: Zero-sized type used to mark things that "act like" they own a `T`. Adding `PhantomData<T>` field to your type tells the compiler that your types as though it stores a value of type `T`, even though it doesn't really. See the
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: 
date created: Monday, June 9th 2025, 12:22:26 pm
date modified: Monday, June 9th 2025, 12:24:33 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[PhantomData - The Rustonomicon](https://doc.rust-lang.org/nomicon/phantom-data.html)

## Concepts of Note
- When working with unsafe code, we often end up in a situation where types/lifetimes are logically associated with a struct, but not actually part of a field. Commonly occurs with lifetimes.

## Usage

|Phantom type|variance of `'a`|variance of `T`|`Send`/`Sync`  <br>(or lack thereof)|dangling `'a` or `T` in drop glue  <br>(_e.g._, `#[may_dangle] Drop`)|
|---|---|---|---|---|
|`PhantomData<T>`|-|**cov**ariant|inherited|disallowed ("owns `T`")|
|`PhantomData<&'a T>`|**cov**ariant|**cov**ariant|`Send + Sync`  <br>requires  <br>`T : Sync`|allowed|
|`PhantomData<&'a mut T>`|**cov**ariant|**inv**ariant|inherited|allowed|
|`PhantomData<*const T>`|-|**cov**ariant|`!Send + !Sync`|allowed|
|`PhantomData<*mut T>`|-|**inv**ariant|`!Send + !Sync`|allowed|
|`PhantomData<fn(T)>`|-|**contra**variant|`Send + Sync`|allowed|
|`PhantomData<fn() -> T>`|-|**cov**ariant|`Send + Sync`|allowed|
|`PhantomData<fn(T) -> T>`|-|**inv**ariant|`Send + Sync`|allowed|
|`PhantomData<Cell<&'a ()>>`|**inv**ariant|-|`Send + !Sync`|allowed|