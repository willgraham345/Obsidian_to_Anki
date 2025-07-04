---
summary: 
headings:
  - "[[#Usage]]"
type: note/function
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, June 11th 2025, 10:45:39 am
class_of:
  - "[[Cpp GoogleTest]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Macros that resemble function calls, typically done with a failure message.

## Usage
- [p] `ASSERT_*` = Asserts within gtest. Fatal, and will abort the current function = #code/cpp/test/gtest/assertions
<!--ID: 1751434091774-->

- [p] `EXPECT_*` = Expects, nonfatal failure without aborting current function (within gtest) = #code/cpp/test/gtest/assertions
<!--ID: 1751434091779-->

- [p] `ASSERT_EQ(condition) << "Failure msg"` = Assert a condition is true, output failure message = #code/cpp/test/gtest/assertions 
<!--ID: 1751434091784-->

- [p] `EXPECT_EQ(condition) << "Failure msg"` = Assert a condition is true, output failure message = #code/cpp/test/gtest/assertions 
<!--ID: 1751434091789-->


