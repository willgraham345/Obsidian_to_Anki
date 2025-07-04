---
type: note
---
# Background
It isn't necessary to spell out recipes for compiling individual C source files, because `make` can figure them out.
- There is an implicit rule for updating a `.o` file from a correspondingly named `.c` file using a `cc -c` command. 
For more information, see [[GNU make implicit rules]] and [Using Implicit Rules Link](https://www.gnu.org/software/make/manual/html_node/Implicit-Rules.html)