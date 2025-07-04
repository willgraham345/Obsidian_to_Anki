---
summary: A loop that iterates a given number of times.
type: note/component
headings:
  - "[[#Syntax]]"
date created: Monday, February 24th 2025, 11:57:57 am
date modified: Monday, February 24th 2025, 11:59:00 am
similar:
  - "[[Python enumerate]]"
component_of:
  - "[[Python Control Flow]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Syntax
```python
for <temporary variable> in <list variable>:
	<action statement>
```

### Example
```python
nums = [1,2,3,4,5]
for num in nums: 
  print(num)
```

## `range()`
Can be used to do the same action a specified number of times
```python
for <iterator_name> in range(num_iterations):
	<actions>
```

#### Example
```python
# Print "WARNING" 3 times:
for i in range(3):
  print("WARNING")
```
