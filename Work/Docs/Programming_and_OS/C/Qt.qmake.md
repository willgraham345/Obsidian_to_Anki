---
type: note
---
# Background
- A utility that automates the generation of [[GNU make.makefile]]s. Makefiles are used by the program to build executable programs from source code, therefore qmake is a make-makefile tool. 
- Automates the creation of moc (meta object compiler) and rcc (resource compiler) sources which are used in Qt's meta-object system and in the integration of binary resources (e.g. pictures)

# Usage
## qmake Language
Many qmake project files describe the sources and headers used by the project. qmake has other features which can help process info. 

[Using the qmake language]([qmake Language | qmake Manual (qt.io)](https://doc.qt.io/qt-5/qmake-language.html))

### Variable Expansion
Use two `$$` in front of a variable to access it

QMake uses [its own syntax for variable references](http://qt-project.org/doc/qt-4.8/qmake-advanced-usage.html#variables).
- `VAR = foobar` => Assign value to variable when qmake is run
- `$$VAR` => QMake variable's value at the time qmake is run
- `$${VAR}` => QMake variable's value at the time qmake is run (identical but enclosed to separate from surrounding text)
- `$(VAR)` => Contents of an Environment variable at the time Makefile (not qmake) is run
- `$$(VAR)` =>Contents of an Environment variable at the time qmake (not Makefile) is run