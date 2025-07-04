---
summary: All scripts should be part of an [[openc3 plugin]]. Organization can be done with `targets/TARGET_NAME/lib` and `targets/TARGET_NAME/procedures`. Put each activity into a distinct method.
headings: ["[[#Architecture]]", "[[#Concepts of Note]]", "[[#Examples]]"]
type: note/concept
concept_of: ["[[openc3 scripting API]]"]
date created: Monday, April 14th 2025, 5:02:47 pm
date modified: Monday, April 14th 2025, 5:13:30 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Classes
	- If you have code that works on a shared state, across methods, use a class. If you have something that happens multiple times in a script without copying/pasting, it probably does not need to be in a class.
- Convention
	- `TARGET/lib/target.py` which is named after the `TARGET` name and contains a class called `Target`. 

## Architecture
| Folder                         | Description                                                               |
| ------------------------------ | ------------------------------------------------------------------------- |
| `targets/TARGET_NAME/lib`        | Place script files containing reusable target specific methods here       |
| `targets/TARGET_NAME/procedures` | Place simple procedures that are centered around one specific target here |

## Examples
```python
class Gimbal:
    def __init__(self):
        self.gimbal_steps = 0

    def move(self, steps_to_move):
        # Move the gimbal
        self.gimbal_steps += steps_to_move

    def home_gimbal(self):
        # Home the gimbal
        self.gimbal_steps = 0

def perform_common_math(x, y):
    return x + y

gimbal = Gimbal()
gimbal.home_gimbal()
gimbal.move(100)
gimbal.move(200)
print(f"Moved gimbal {gimbal.gimbal_steps}")
result = perform_common_math(gimbal.gimbal_steps, 10)
print(f"Math:{result}")
```