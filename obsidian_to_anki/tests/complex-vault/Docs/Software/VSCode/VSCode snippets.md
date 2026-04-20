---
type: note
date created: Tuesday, August 27th 2024, 11:25:57 am
date modified: Tuesday, August 27th 2024, 11:27:19 am
---
# Background
- Make sure to turn on tab-autocompletion for snippets on your VSCode settings
- 

# Usage
## Nesting Snippets
- You will need to hit `ctrl+space` to exit at `snippet_test1` to expand it
```json
"Test1": {
        "prefix": "snippet_test1",
        "body": 
            "something"
}
"Test2": {
        "prefix": "snippet_test2",
        "body": 
            "${1:snippet_test1}"
}
```