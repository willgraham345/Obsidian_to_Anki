---
type: note/library
classes:
  - "[[Cpp Assertions]]"
  - "[[Cpp GoogleTest Mocking Classes]]"
  - "[[Cpp.GoogleTest Test Definitions]]"
concepts:
  - "[[Cpp GoogleTest Actions]]"
  - "[[Cpp GoogleTest Mocking]]"
  - "[[Cpp gtest fixtures]]"
workflows:
  - "[[Cpp GoogleTest Building with CMake]]"
  - "[[Cpp GoogleTest Install and Setup]]"
  - "[[Cpp GoogleTest Invoking Tests]]"
  - "[[Cpp GoogleTest Running Tests]]"
  - "[[Cpp gTest Mocking Workflow]]"
aliases:
  - Cpp gtest
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, June 25th 2025, 12:34:59 pm
test_for:
  - "[[Cpp]]"
---

# Breadcrumbs

```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```

# Background

- GoogleTest is a testing framework with Google's requirements in mind.
- Why it's good
  - Supports any kind of tests, not just unit tests.
  - GoogleTest groups related tests into suites that can share data and subroutines.
  - Tests are portable and reusable
  - When tests fail, they provide information about the problem. GoogleTest doesn't stop at the first test failure. Instead it only stops the current test and continues with the next.
  - Focuses on housekeeping chores and focus on the test content.
  - Tests are fast

## Basic Concepts/Nomenclature

- Test suite=contains one or many tests.

Start by writing assertions (statements to check a condition's truthfulness)

- Group your tests into test suites that reflect the structure of the tested code.
- When multiple tests in a test suite need to share common objects and subroutines, you can put them into a test fixture class
- A test program can contain multiple test suites
