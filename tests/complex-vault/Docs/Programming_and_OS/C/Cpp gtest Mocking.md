---
summary: How to implement the same interface as a real object, but lets you specify at runtime how it will be used and what it should do. The separation between "fake" objects and mocked objects is that fake objects have no expectations/programming.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
similar:
  - "[[Cpp GoogleTest Mocking Classes]]"
  - "[[Cpp gtest Assertions]]"
aliases:
  - gtest mocking
concept_of:
  - "[[Cpp GoogleTest]]"
date created: Tuesday, November 5th 2024, 5:53:20 pm
date modified: Monday, April 13th 2026, 11:53:10 am
processes:
  - "[[Cpp gTest Mocking Workflow]]"
tags:
  - lang/test
  - lang/test/gtest/macros/cardinality
  - lang/test/gtest/mocking
template:
template-version:
associations:
  - "[[Cpp gtest Assertions]]"
uses:
  - "[[Cpp gtest Matchers|gmock matchers]]"
---

# Summary
󰙎 gtest mocking ;;; How to implement the same interface as a real object, but lets you specify at runtime how it will be used and what it should do. The separation between "fake" objects and mocked objects is that fake objects have no expectations/programming.

# Additional Background
[Mocking Reference \| GoogleTest](https://google.github.io/googletest/reference/mocking.html#macros)

## Concepts of Note
󰙎 Uninteresting calls ;;; are calls that don't have a single `EXPECT_CALL(x, Y(...))` set.
󰙎 Unexpected call ;;; If there are *some* `EXPECT_CALL(x, Y(...))` but none of them match the call.
󰙎 Nice mock ;;; Suppresses the uninteresting call warnings
󰙎 Strict mock ;;; Turns all uninteresting call warnings into errors.
󰙎 Actions ;;; Things you'd like to do when a mocked function is called in gtest.

󰙎 MOCK_METHOD ;;; Macro to declare a mock method **inside a mock class**. Signature: `MOCK_METHOD(ReturnType, MethodName, (args...), (specifiers...))` — the 4th arg is optional and accepts `const`, `override`, `Calltype(...)`, or combinations.

- You can mock using a class: [Mocking Reference \| GoogleTest](https://google.github.io/googletest/reference/mocking.html#classes)

## Usage

 `.WillOnce()` ;;; Sets a cardinality (how many times) on a Gtest Macro as one time. See actions for adding what you want this thing to do.


 `.WillRepeatedly()` ;;; Sets a cardinality (how many times) on a Gtest Macro for repeatedly. See Actions for how to add what you want this thing to do.


 `NiceMock<MockFoo> foo` ;;; Created a mock `foo` which ignores all uninteresting calls.

 `EXPECT_CALL(obj, Method(matcher))` ;;; Set expectation on `obj`'s `Method`; matcher can be a value, `_` (any), or a [[Cpp gtest Matchers|matcher]]
 `EXPECT_CALL(obj, Method(_)).Times(n)` ;;; Expect exactly `n` calls
 `EXPECT_CALL(obj, Method(_)).Times(testing::AtLeast(1))` ;;; Expect one or more calls
 `EXPECT_CALL(obj, Method(_)).WillOnce(Return(v)).WillRepeatedly(Return(d))` ;;; Return `v` first call, `d` on all subsequent
 `auto mock = std::make_unique<MockFoo>(); sut.Init(std::move(mock));` ;;; Inject mock via unique_ptr; set `EXPECT_CALL` **before** moving

### Declare Mock Methods
 `MOCK_METHOD(ReturnType, MethodName, (args...))` ;;; Declare a mock method — arity inferred automatically, no numbered suffix needed
 `MOCK_METHOD(ReturnType, MethodName, (args...), (const))` ;;; Use when the interface method is `const`-qualified — compiler enforces `const` on `*this` during the call
 `MOCK_METHOD(ReturnType, MethodName, (args...), (override))` ;;; Verifies at compile time that the method exists with this exact signature in the base class — always recommended
 `MOCK_METHOD(ReturnType, MethodName, (args...), (const, override))` ;;; Const virtual that must match the base class signature — use for all `const` virtuals
 `MOCK_METHOD(ReturnType, MethodName, (args...), (Calltype(STDMETHODCALLTYPE)))` ;;; Sets the calling convention — needed for Windows COM interfaces (`STDMETHODCALLTYPE`, `WINAPI`, etc.)
 `MOCK_METHOD(ReturnType, MethodName, (args...), (const, Calltype(STDMETHODCALLTYPE)))` ;;; Const COM method — combine `const` and `Calltype` when both apply
󰠗 When do you need the 4th arg to MOCK_METHOD? ;; When the method has specifiers: `const`, `override`, `noexcept`, or a calling convention via `Calltype(...)`. Omit the 4th arg entirely for a plain non-const method.
󰠗 Why always add `override` to MOCK_METHOD? ;; If the base class signature changes, the compiler errors on the mock — without `override`, the mock silently stops overriding the virtual and tests pass falsely.

## Examples
```cpp
TEST(UnitTest, DoThing) {
	auto mock_dep = make_unique<Mock
	EXPECT_CALL(*mock_dep, doThing())
}

```
