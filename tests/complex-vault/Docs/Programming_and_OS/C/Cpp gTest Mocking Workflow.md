---
summary: ""
type: note/process
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
implements:
  - "[[Dependency Inversion and Injection]]"
  - "[[DP Accessor]]"
  - "[[DP Testing Mocking]]"
aliases: []
date created: Tuesday, November 5th 2024, 3:02:11 pm
date modified: Wednesday, April 15th 2026, 4:13:06 pm
process_of:
  - "[[Cpp GoogleTest]]"
  - "[[Cpp gtest Mocking]]"
tags: []
template:
template-version:
uses:
  - "[[Cpp gtest assertions]]"
  - "[[Cpp gtest Matchers|gmock matchers]]"
---

# Summary
# Additional Background

[gMock for Dummies \| GoogleTest](https://google.github.io/googletest/gmock_for_dummies.html#how-to-define-it)

## Concepts of Note
󰙎 Matchers ;;; Answers "What arguments do we expect within this function?". Can be used within `EXPECT_CALL()` when a function is expected
󰙎 Cardinalities ;;; Answers "How many times will it be called?"
󰙎 Actions ;;; Answers "What should it do?"

## Examples
### Normal Class Mocking 
```cpp
class Foo {
 public:
  virtual ~Foo();
  virtual int GetSize() const = 0;
  virtual string Describe(const char* name) = 0;
  virtual string Describe(int type) = 0;
  virtual bool Process(Bar elem, int count) = 0;
};
```
to...
```cpp
#include <gmock/gmock.h>

class MockFoo : public Foo {
 public:
  MOCK_METHOD(int, GetSize, (), (const, override));
  MOCK_METHOD(string, Describe, (const char* name), (override));
  MOCK_METHOD(string, Describe, (int type), (override));
  MOCK_METHOD(bool, Process, (Bar elem, int count), (override));
};
```

### Mocking template
```cpp
template <typename Elem>
class StackInterface {
 public:
  virtual ~StackInterface();
  virtual int GetSize() const = 0;
  virtual void Push(const Elem& x) = 0;
};
```
to...
```cpp
template <typename Elem>
class MockStack : public StackInterface<Elem> {
 public:
  MOCK_METHOD(int, GetSize, (), (const, override));
  MOCK_METHOD(void, Push, (const Elem& x), (override));
};
```
