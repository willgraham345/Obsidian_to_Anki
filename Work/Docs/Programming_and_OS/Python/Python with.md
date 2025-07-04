---
summary: Runtime context allows you to run a group of statements together.
headings: 
type: note/concept
concept_of: ["[[Python Context Managers]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, April 23rd 2025, 12:55:31 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Examples
```python
# Python program creating a
# context manager

class ContextManager():
	def __init__(self):
		print('init method called')
		
	def __enter__(self):
		print('enter method called')
		return self
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		print('exit method called')

with ContextManager() as manager:
	print('with statement block')
```

## Media
- [With statement](https://realpython.com/python-with-statement/)