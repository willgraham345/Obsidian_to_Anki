---
summary: Groups are added to Suites by inheriting from a suite, and calling the `add_group` method.
headings: ["[[#Examples]]"]
type: note/class
class_of: ["[[openc3 python API]]"]
date created: Wednesday, November 12th 2025, 4:18:11 pm
date modified: Wednesday, November 12th 2025, 4:19:14 pm
template: "[[base_note_template]]"
template-version: 1.0.0
uses: ["[[openc3 Group]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Examples

```python
from openc3.script.suite import Suite, Group
class MySuite(Suite):
    def __init__(self):
        self.add_group(ExampleGroup)
    def setup(self):
        print("Suite setup")
    def teardown(self):
        print("Suite teardown")
```