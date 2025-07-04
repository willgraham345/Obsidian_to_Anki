---
type: note
---
# Background
- Project files have all necessary data to build an application using qmake. 
	- Generally, a series of declarations are used in the beginning of the project. 

## Project File Semantics
### Variables
- Inform qmake how to use contents to determine what it should write to a Makefile. 
```qt
HEADERS = mainwindow.h paintwidget.h
SOURCES = main.cpp mainwindow.cpp \
	paintwidget.cpp
CONFIG += console
```

| Variable                                                                    | Contents                                                                                                                                                                             |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [CONFIG](https://doc.qt.io/qt-6/qmake-variable-reference.html#config)       | General project configuration options.                                                                                                                                               |
| [DESTDIR](https://doc.qt.io/qt-6/qmake-variable-reference.html#destdir)     | The directory in which the executable or binary file will be placed.                                                                                                                 |
| [FORMS](https://doc.qt.io/qt-6/qmake-variable-reference.html#forms)         | A list of UI files to be processed by the [user interface compiler (uic)](https://doc.qt.io/qt-6/uic.html).                                                                          |
| [HEADERS](https://doc.qt.io/qt-6/qmake-variable-reference.html#headers)     | A list of filenames of header (.h) files used when building the project.                                                                                                             |
| [QT](https://doc.qt.io/qt-6/qmake-variable-reference.html#qt)               | A list of Qt modules used in the project.                                                                                                                                            |
| [RESOURCES](https://doc.qt.io/qt-6/qmake-variable-reference.html#resources) | A list of resource (.qrc) files to be included in the final project. See the [The Qt Resource System](https://doc.qt.io/qt-6/resources.html) for more information about these files. |
| [SOURCES](https://doc.qt.io/qt-6/qmake-variable-reference.html#sources)     | A list of source code files to be used when building the project.                                                                                                                    |
| [TEMPLATE](https://doc.qt.io/qt-6/qmake-variable-reference.html#template)   | The template to use for the project. This determines whether the output of the build process will be an application, a library, or a plugin.                                         |

### Prepending Variables onto One Another
```
TEMP_SOURCES = $$SOURCES
```

### Whitespaces
Whitespaces separate variables, so enclose things that have whitespaces in double quotes `"`
### Comments
Comments have hashtags in front of them

### Built-in Functions/Control Flow
#### Other Project Files
`include()` takes a filename as an argument, and includes the contents of those files at the place where the `include()` is used. Most commonly used to attach other project files. 

#### Scopes
Scopes behave much like `if` statements in programming languages
```
win32 {
    SOURCES += paintwidget_win.cpp
}
```
# Usage