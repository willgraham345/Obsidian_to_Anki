---
type: note
---
# Background
QT is a cross-platform framework that is typically used for GUI development

Main Concepts of GUI programming
- **Window:** A top level window frame that host other widgets inside itself.
- **Button:** A clickable button that have some event associated with its click.
- **Label:** Simple read-only text
- **Checkbox**: Box that provide the options to be on or off.
- **Radio Button:** Box that provide the options to be on or off but we can only choose one radio button in a group.
- **Dropdown/Combo Box**: Opens a dropdown menu when clicked. Only one item can be displayed in the non-opened form.
- **Textbox:** Editable Text area.
- **Listbox:** The box with multiple items and a scroll bar to go through all of them.
- **Slider:** A navigation widget used to move around the application.
- **Menu:** Shown at the top, menu provides different options to the application user.
- **Dialog Box:** A box that is displayed on the top of a window. Sometimes to display the notification.
- **Grid:** Used for the Layout Management of the UI.

## [[Qt.Class.Hierarchy]]

## Modules in Qt
- **QtCore** =  a base library that provides containers, thread management, event management, and much more
- **QtGui** and **QtWidgets** =  a GUI toolkit for Desktop, that provides a lot of graphical components to design applications.
- **QtNetwork** =  that provides a useful set of classes to deal with network communications
- **QtWebkit** =  the webkit engine, that enable the use of web pages and web apps in a Qt application.
- **QtSQL** =  a full featured SQL RDBM abstraction layer extensible with own drivers, support for ODBC, SQLITE, MySQL and PostgreSQL is available out of the box
- **QtXML** =  support for simple XML parsing (SAX) and DOM
- **QtXmlPatterns** =  support for XSLT, XPath, XQuery and Schema validation

## How Qt Program is Compiled
For small projects, its easy to compile everything by hand. 
`qmake` is the build system that comes with Qt, and it generates makefiles for you. Qt uses meta-objects to extend C++ functionalities, and qmake is responsible for preparing a makefile that contains this meta-object extraction phase. 



## Terms in Qt
`TEMPLATE` = describes the type to build. Can be an application, a library, or subdirectories
`TARGET` = name of the app or library
`QT` = used to indicate which libraries/Qt modules are being used in the project. 

Headers and sources can be added manually with: 
```cpp
HEADERS += first_file.h second_file.h
SOURCES += first_file.cpp second_file.cpp
```