---
type: note
---
# Background
Implicit rules tell `make` how to use customary techniques so you don't have to specify everything in detail when you want to run it. 

For example, C compilation typically takes a `.c` file and makes an `.o` file. 
- `make` applies the implicit rule for C compilation when it sees this combination of file name endings.
- A chain of implicit rules can apply in a sequence.
	- For example, `make` will remake a `.o` file from a `.y` file by way of a `.c` file.


# Usage