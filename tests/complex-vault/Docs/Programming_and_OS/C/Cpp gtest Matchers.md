---
summary: Predicates used inside EXPECT_CALL and EXPECT_THAT to constrain argument values or assert on results.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
aliases: [gmock matchers]
concept_of:
  - "[[Cpp GoogleTest]]"
date created: Thursday, March 19th 2026, 12:00:00 pm
date modified: Friday, March 20th 2026, 1:31:03 pm
tags: [lang/test, lang/test/gtest/mocking]
template:
template-version:
used_by:
  - "[[Cpp gTest Mocking Workflow]]"
  - "[[Cpp gtest Mocking]]"
---

# Summary
󰙎 gtest matchers ;;; Predicates used inside `EXPECT_CALL` and `EXPECT_THAT` to constrain argument values or assert on results.

# Additional Background
[Matchers Reference \| GoogleTest](https://google.github.io/googletest/reference/matchers.html)

## Concepts of Note
󰙎 Matcher ;;; A single-argument predicate; composable and reusable across `EXPECT_CALL`, `EXPECT_THAT`, and `ON_CALL`
󰙎 Wildcard ;;; `_` matches any value of any type — the most permissive matcher
󰙎 Composite matcher ;;; Combines matchers with `AllOf()`, `AnyOf()`, `Not()`

## Usage

### Wildcard & Equality
 `_` ;;; Match anything
 `Eq(v)` ;;; Equal to `v` (same as passing `v` directly)
 `Ne(v)` ;;; Not equal to `v`
 `Lt(v)` / `Le(v)` / `Gt(v)` / `Ge(v)` ;;; Ordered comparisons

### Floating Point
 `DoubleEq(v)` ;;; Near-equal for `double` (NaN ≠ NaN)
 `FloatEq(v)` ;;; Near-equal for `float`
 `DoubleNear(v, abs_err)` ;;; Within `abs_err` of `v`

### Strings
  `StrEq(s)` / `StrNe(s)` ;;; Exact string equality/inequality
  `HasSubstr(s)` ;;; Contains substring `s`
  `StartsWith(s)` / `EndsWith(s)` ;;; Prefix / suffix match
  `MatchesRegex(re)` ;;; Full-string regex match
  `ContainsRegex(re)` ;;; Partial regex match
  

### Pointers & References
  `IsNull()` / `NotNull()` ;;; Null-checks a raw pointer
  `Pointee(m)` ;;; Dereferences pointer and applies matcher `m`
  

### Containers
  `IsEmpty()` ;;; Container is empty
  `SizeIs(n)` ;;; Container has size `n` (can itself be a matcher)
  `Contains(m)` ;;; At least one element matches `m`
  `Each(m)` ;;; Every element matches `m`
  `ElementsAre(m1, m2, ...)` ;;; Exact element-by-element match (order matters)
  `UnorderedElementsAre(m1, m2, ...)` ;;; Same elements, any order
  `Pair(m1, m2)` ;;; Matches `std::pair`; first matches `m1`, second `m2`

### Composite
 `AllOf(m1, m2, ...)` ;;; All matchers must pass (logical AND)
 `AnyOf(m1, m2, ...)` ;;; Any matcher passes (logical OR)
 `Not(m)` ;;; Negates matcher `m`

### Standalone assertion
 `EXPECT_THAT(value, matcher)` ;;; Assert `value` satisfies `matcher` outside of mock context
