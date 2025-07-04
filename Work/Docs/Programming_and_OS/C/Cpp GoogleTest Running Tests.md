---
summary: How to run a google test with a filter.
type: note/workflow
date created: Thursday, March 6th 2025, 12:16:04 pm
date modified: Thursday, March 6th 2025, 12:17:21 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- [p] `./<test> --gtest_filter=regx` = Runs tests of a given type with a filter, which can have wildcards. Keep in mind tests are organized by fixtures/test names.