---
summary: Actions are things that mocked functions can do when they are called.
type: note/concept
headings:
  - "[[#Examples]]"
concept_of:
  - "[[Cpp GoogleTest]]"
date created: Thursday, June 12th 2025, 3:07:40 pm
date modified: Thursday, March 19th 2026, 10:27:21 am
tags: []
template:
template-version:
used_by:
  - "[[Cpp gtest TEST]]"
---

# Summary
󰙎 gtest actions ;;; Actions are things that mocked functions can do when they are called.

# Additional Background
## Examples

### Mocking with a lambda, in order to save to a member variable
```cpp
// Assume something like:
class MockFoo : public Foo {
	public: 
		MOCK_METHOD(int)


class TestFixture : MockFoo {

	public:
		void sendMockedCmd()
		{
			EXPECTE_CALL()
		}
}
```