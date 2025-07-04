---
tags: note/python
type: note
---
# Terminology
- inner class = nested class
- parent class = root class

A class defined in another class is an inner class

A parent class can have one or more inner classes, but generally inner classes are avoided. It's done to avoid rewriting code and to protect the outside class from the world. 

```python
class Doctors:
	def __init__(self):
		self.name = 'Doctor'
		self.den = self.Dentist()
		self.car = self.Cardiologist()
	def show(self):
		print('In outer class')
		print('Name:', self.name)
	class Dentist:
		def __init__(self):
			self.name = 'Dr. Savita'
			self.degree = 'BDS'
		def display(self):
			print("Name:", self.name)
			print("Degree:", self.degree)
	class Cardiologist:
		def __init__(self):
			self.name = 'Dr. Amit'
			self.degree = 'DM'
		def display(self):
			print("Name:", self.name)
			print("Degree:", self.degree)
```