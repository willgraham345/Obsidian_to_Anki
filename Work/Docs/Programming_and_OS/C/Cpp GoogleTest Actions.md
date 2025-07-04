---
summary: Actions are things that mocked functions can do when they are called.
headings:
  - "[[#Examples]]"
type: note/concept
date created: Thursday, June 12th 2025, 3:07:40 pm
date modified: Thursday, June 12th 2025, 3:08:16 pm
concept_of:
  - "[[Cpp GoogleTest]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

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