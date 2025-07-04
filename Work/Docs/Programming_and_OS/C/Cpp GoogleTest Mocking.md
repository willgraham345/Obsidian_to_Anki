---
summary: How to implement the same interface as a real object, but lets you specify at runtime how it will be used and what it should do. The separation between "fake" objects and mocked objects is that fake objects have no expectations/programming.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/concept
workflows: ["[[Cpp gTest Mocking Workflow]]"]
similar: ["[[Cpp GoogleTest Mocking Classes]]"]
concept_of: ["[[Cpp GoogleTest]]"]
date created: Tuesday, November 5th 2024, 5:53:20 pm
date modified: Tuesday, June 17th 2025, 10:24:33 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Mocking Reference \| GoogleTest](https://google.github.io/googletest/reference/mocking.html#macros)

## Concepts of Note
- [I] Uninteresting calls = are calls that don't have a single `EXPECT_CALL(x, Y(...))` set = #term/cpp/testing
- [I] Unexpected call = If there are *some* `EXPECT_CALL(x, Y(...))` but none of them match the call. = #term/cpp/testing
- [I] Nice mock = Suppresses the uninteresting call warnings = #term/cpp/testing
- [I] Strict mock = Turns all uninteresting call warnings into errors.  = #term/cpp/testing
- [I] Actions = Things you'd like to do when a mocked function is called = #term/cpp/testing 

## Usage
- [p] `.WillOnce()` = Sets a cardinality (how many times) on a Gtest Macro for one time. See actions for adding what you want this thing to do. = #code/cpp/test/gtest/macros/cardinality 
<!--ID: 1751434091649-->

- [p] `.WillRepeatedly()` = Sets a cardinality (how many times) on a Gtest Macro for repeatedly. See Actions for how to add what you want this thing to do. = #code/cpp/test/gtest/macros/cardinality
<!--ID: 1751434091652-->

- [p] `NiceMock<MockFoo> nice_foo` = Sets a mock which ignores all uninteresting calls = #code/cpp/test/gtest/mocking
<!--ID: 1751434091656-->

