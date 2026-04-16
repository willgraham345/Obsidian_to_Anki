---
type: note
---
# Background
- Also known as the `moc`
- 

## How does the moc work?
1. The moc ([[QT QTCore Meta Object System Compiler]]) reads a C++ source file. 
	1. If it finds one or more class decorations that contain the [[Qt.QObject.Q_OBJECT]] macro, it produces another C++ source file which contains the meta-data of each of those classes. This generated source file is either included into the class's source file, or usually, compiled and linked with the class's implementation.
Provides features to the `QObject::metaObject()`, `QObject::className()`, `QObject::inherits()`,  

# Usage