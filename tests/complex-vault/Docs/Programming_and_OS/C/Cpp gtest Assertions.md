---
anki_sync:
  4c4c89e3-daa5-4be3-9d24-361662fbc077: 1776707753248
  98bbe025-1b04-466f-b650-f9784206e5d7: 1776707753214
associations:
- '[[Cpp gtest Actions]]'
- '[[Cpp gtest Matchers]]'
- '[[Cpp gtest Mocking]]'
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, March 20th 2026, 1:17:46 pm
headings:
- '[[#Concepts of Note]]'
- '[[#Usage]]'
item_of:
- '[[Cpp GoogleTest|Cpp gtest]]'
similar:
- '[[Cpp gtest Matchers]]'
- '[[Cpp gtest Mocking]]'
summary: The "pass/fail" of a gtest test
tags:
- lang/test/gtest/assertions
template: null
template-version: null
type: note/item
up: '[[Cpp GoogleTest]]'
used_by:
- '[[Cpp gTest Mocking Workflow]]'
- '[[Cpp gtest TEST_P]]'
- '[[Cpp gtest TEST]]'
uses:
- '[[Cpp gtest SCOPED_TRACE]]'
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Macros that resemble function calls, typically done with a failure message.

## Concepts of Note
󰙎 ASSERT_* ;;; Fatal assertion — aborts the current *function* on failure; subsequent checks in that function are skipped
󰙎 EXPECT_* ;;; Non-fatal assertion — records the failure and continues; prefer when you want to gather multiple failures in one run
󰙎 EXPECT_CALL ;;; gmock macro — sets a call expectation on a mock object; verified at end of test scope → [[Cpp gtest Mocking]]
󰠗 When should you use ASSERT vs EXPECT? ;; ASSERT when subsequent checks are meaningless if the first fails (e.g. null-check before deref). EXPECT to gather all failures in one pass.

## Usage
  `ASSERT_*` ;;; Asserts within gtest. Fatal, and will abort the current function



  `EXPECT_*` ;;; Expects, nonfatal failure without aborting current function (within gtest)


  `ASSERT_EQ(condition) << "Failure msg"` ;;; Assert a condition is true, output failure message

  `EXPECT_THAT(var, matcher) << "Test failed"` ;;; Expect that `var` matches `matcher`. If not, insert an error message with the stream insertion operator for gtest.

### Boolean & Null
 - [p] `EXPECT_TRUE(cond)` ;;; Passes if `cond` is true
 - [p] `EXPECT_FALSE(cond)` ;;; Passes if `cond` is false
 - [p] `ASSERT_NE(nullptr, ptr)` ;;; Fatal null-check — safe to dereference `ptr` after this passes
 - [p] `EXPECT_EQ(nullptr, ptr)` ;;; Prefer over `EXPECT_TRUE(ptr == nullptr)` for clearer failure output

### Comparison
 `EXPECT_NE(a, b)` ;;; a != b
 `EXPECT_LT(a, b)` ;;; a < b
 `EXPECT_LE(a, b)` ;;; a <= b
 `EXPECT_GT(a, b)` ;;; a > b
 `EXPECT_GE(a, b)` ;;; a >= b

### Strings (C-strings)
 `EXPECT_STREQ(s1, s2)` ;;; C-string content equality (not pointer equality)
 `EXPECT_STRNE(s1, s2)` ;;; C-string content inequality
 `EXPECT_STRCASEEQ(s1, s2)` ;;; Case-insensitive C-string equality

### Floating Point
 `EXPECT_FLOAT_EQ(a, b)` ;;; Near-equal for `float` (within 4 ULPs)
 `EXPECT_DOUBLE_EQ(a, b)` ;;; Near-equal for `double` (within 4 ULPs)
 `EXPECT_NEAR(a, b, abs_err)` ;;; `|a - b| <= abs_err`

### Exceptions
 `EXPECT_THROW(stmt, ExcType)` ;;; `stmt` must throw `ExcType`
 `EXPECT_NO_THROW(stmt)` ;;; `stmt` must not throw any exception
 `EXPECT_ANY_THROW(stmt)` ;;; `stmt` must throw something

### EXPECT_CALL (gmock)
See [[Cpp gtest Mocking]] for full reference.
 `EXPECT_CALL(obj, Method(matcher))` ;;; Expect `obj.Method` called at least once; arg must match `matcher` → [[Cpp gtest Matchers]]
 `EXPECT_CALL(obj, Method(_)).Times(n)` ;;; Expect exactly `n` calls; `_` matches any argument
 `EXPECT_CALL(obj, Method(_)).Times(testing::AtLeast(1))` ;;; Expect one or more calls
 `EXPECT_CALL(obj, Method(_)).WillOnce(Return(v))` ;;; Stub return value for one call → [[Cpp gtest Actions]]
 `EXPECT_CALL(obj, Method(_)).WillRepeatedly(Return(v))` ;;; Stub return value for all subsequent calls
