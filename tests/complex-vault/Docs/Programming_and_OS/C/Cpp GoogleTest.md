---
summary: Test framework that supports any kind of tests (not just unit), and groups test into related suites that can share data & subroutines.
type: note/library
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
concepts:
  - "[[Cpp gtest Actions]]"
  - "[[Cpp gtest fixtures]]"
  - "[[Cpp gtest Matchers]]"
  - "[[Cpp gtest Mocking]]"
aliases:
  - Cpp gtest
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, March 20th 2026, 9:17:22 am
items:
  - "[[Cpp gtest Assertions]]"
  - "[[Cpp gtest GTEST_SKIP]]"
  - "[[Cpp gtest SCOPED_TRACE]]"
  - "[[Cpp gtest TEST_F]]"
  - "[[Cpp gtest TEST_P]]"
  - "[[Cpp gtest TEST]]"
processes:
  - "[[Cpp GoogleTest Building with CMake]]"
  - "[[Cpp gtest Invoking Tests]]"
  - "[[Cpp gTest Mocking Workflow]]"
tags:
  - lang/test/gtest
template:
template-version:
test_for:
  - "[[Cpp]]"
down:
  - "[[Cpp gtest Assertions]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰙎  Test suite ;;; A group of one or more tests within gtest. = 

Start by writing assertions (statements to check a condition's truthfulness)

- Group your tests into test suites that reflect the structure of the tested code.
- When multiple tests in a test suite need to share common objects and subroutines, you can put them into a test fixture class
- A test program can contain multiple test suites

## Usage
  `./<test> --gtest_filter=regx` ;;; Runs tests of a given type with a filter, which can have wildcards. Keep in mind tests are organized by fixtures/test names.

## Breadcrumbs
```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```



