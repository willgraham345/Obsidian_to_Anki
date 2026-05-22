---
summary: TEST() is a provided macro from gtest that doesn't return a value. The test results are determined by the assertions contained within the macro.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
type: note/item
source: ["[[Cpp GoogleTest]]"]
similar: ["[[Cpp gtest TEST_P]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, September 16th 2025, 9:22:42 am
uses: ["[[Cpp gtest assertions]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
- `TEST()` macro is an ordinary C++ function that doesn't return a value. Test results are determined by the assertions.
- It'

### Naming Conventions:
- Should go from general to specific
- First argument is name of the test suite, second argument is the test's name. 
󰙎  Value-parameterized test ;;; Allows you to test code with different parameters without writing multiple copies of the same test. = #lang/test/gtest/create-a-test #lang/test/gtest 
<!--ID: 1758253289886-->


## Usage
- [p] `TEST(TestSuiteName, TestName) {`
      `... test body ... `
      `{` = Creates a google test named `TestName`, within the suite `TestSuiteName` in gtest. Note, the names cannot contain underscores. = #lang/test/gtest/macros #lang/test/gtest/create-a-test

```
TEST(TestSuiteName, TestName) {
... test body ...
}
```

## Examples


### Testing a factorial
```cpp
// Tests factorial of 0.
TEST(FactorialTest, HandlesZeroInput) {
  EXPECT_EQ(Factorial(0), 1);
}

// Tests factorial of positive numbers.
TEST(FactorialTest, HandlesPositiveInput) {
  EXPECT_EQ(Factorial(1), 1);
  EXPECT_EQ(Factorial(2), 2);
  EXPECT_EQ(Factorial(3), 6);
  EXPECT_EQ(Factorial(8), 40320);
}
```
