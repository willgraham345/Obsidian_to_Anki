---
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
similar:
  - "[[Python Mock]]"
date created: Wednesday, March 4th 2026, 3:33:49 pm
date modified: Wednesday, March 4th 2026, 3:49:34 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
concept_of:
  - "[[Python pytest]]"
---

# Summary
󰙎 Python pytest monkeypatch ;;; A way to dynamically modify a module, class, or function behavior at runtime without changing its original source code. Primarily used for testing and mocking (dependencies, temporary changes, and/or 3rd party libs)

# Additional Background
## Concepts of Note
- By definition, monkeypatching breaks the abstraction barrier. May be brittle.

### monkeypatch vs mock vs pytest-mock

| Library       | Pros                                                                                                                                                                                               | Cons                                                                                                                                     |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `monkeypatch` | - Comes with pytest<br>- Simple, no `MagicMock`, no call tracking<br>                                                                                                                              | - It is a fixture, and scope can be broader than expected. Can lead to "leaking" into other fixtures<br>- Less battle tested than `mock` |
| `mock`        | - Python3: Comes with standard library<br>- More features than monkeypatch (call tracking, MagicMock, assertion framework)<br>- Tight control over mocked context with context managers/decorators | - If on python2, you may need a backport<br>- MagicMock is "crazy magic"                                                                 |
| `pytest-mock` | -                                                                                                                                                                                                  |                                                                                                                                          |

## Usage

## Examples
```python
import os

class UnixFS:
    @staticmethod
    def rm(filename):
        os.remove(filename)
def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')

```
