---
type: note
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, April 14th 2025, 11:56:28 am
tags: [code/python/oop, note/python]
---
Specifying types for variables within a class
- [p] `class definition` = Defining a class in python (example in link) = #code/python/oop 
<!--ID: 1751434090697-->


```python
class Projectile(Sprite):
	def __init__(self,
		centerx: int,
		y: int,
		direction: str,
		data_dir: str,
		projectile_type: str) -> None:
	def mark_for_deletion(self) -> None:
		"""Mark the laser for deletion"""
		self.is_alive = False
```