---
summary: If hit, the execution will immediately exit the while loop or the for loop it is placed, before the loop has finished. Will only exit the loop in which it is placed.
type: note/function
date created: Monday, February 24th 2025, 12:01:38 pm
date modified: Monday, February 24th 2025, 12:03:47 pm
function_of:
  - "[[Python for loop]]"
  - "[[Python while loop]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
```python
# Example: Searching for an element in a list

a = [1, 3, 5, 7, 9, 11]
val = 7

for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print(f"not found")

```
## Concepts of Note
### Nested loops
A break statement will exit the loop in which it is placed directly. To exit multiple levels of nested loops, you'd need to create a flag variable or another user-defined structure.