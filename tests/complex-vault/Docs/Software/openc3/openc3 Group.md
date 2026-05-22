---
summary: Contains methods used to run test or operations. Methods starting with `script`, `op`, or `test` which are implemented within a Group class are automatically included as scripts to run.
headings:
  - "[[#Examples]]"
type: note/class
date created: Wednesday, November 12th 2025, 4:14:51 pm
date modified: Wednesday, November 12th 2025, 4:16:17 pm
template: "[[base_note_template]]"
template-version: 1.0.0
class_of:
  - "[[openc3 python API]]"
used_by:
  - "[[openc3 Suite]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎  Group ;;; Class you use within openc3 to contain methods used to run test or operations. = #tools/openc3/api

## Examples

```python
from openc3.script.suite import Suite, Group
class ExampleGroup(Group):
    def setup(self):
        print("setup")
    def script_1(self):
        print("script 1")
    def teardown(self):
        print("teardown")
```
