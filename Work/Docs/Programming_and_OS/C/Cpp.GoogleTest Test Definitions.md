---
source:
  - "[[Cpp GoogleTest]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, November 5th 2024, 5:33:26 pm
type: note/class
---
# Background
`TEST()` macro is an ordinary C++ function that doesn't return a value. Test results are determined by the assertions.

Naming rules:
- Should go from general to specific
- First argument is name of the test suite, second argument is the test's name. 

# Usage
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