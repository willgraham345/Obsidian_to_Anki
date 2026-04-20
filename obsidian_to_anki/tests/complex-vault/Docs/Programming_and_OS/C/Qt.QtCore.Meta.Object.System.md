---
type: note
---
# Background
- Qt's meta-object system provides the signals and slots for inter-object communication, run-time type information, and dynamic property system. 
- Based on 3 things:
	1. [[Qt.QtCore.QObject]] class provides base class for objects that can take advantage of the meta-object class system
	2. [[Qt.QObject.Q_OBJECT]] macro is used to enable meta-object features
	3. [[QT.QTCore.Meta.Object.System.Compiler]] supplies each `QObject` subclass with the necessary code to implement meta-object features

## How does it work?
See [[QT.QTCore.Meta.Object.System.Compiler#How does the moc work?|How does the moc work?]] for more information

## What features does it give access to?
# Usage
- [QObject::metaObject](https://doc.qt.io/qt-6/qobject.html#metaObject)() returns the associated [meta-object](https://doc.qt.io/qt-6/qmetaobject.html) for the class.
- [QMetaObject::className](https://doc.qt.io/qt-6/qmetaobject.html#className)() returns the class name as a string at run-time, without requiring native run-time type information (RTTI) support through the C++ compiler.
- [QObject::inherits](https://doc.qt.io/qt-6/qobject.html#inherits)() function returns whether an object is an instance of a class that inherits a specified class within the [QObject](https://doc.qt.io/qt-6/qobject.html) inheritance tree.
- [QObject::tr](https://doc.qt.io/qt-6/qobject.html#tr)() translates strings for [internationalization](https://doc.qt.io/qt-6/internationalization.html).
- [QObject::setProperty](https://doc.qt.io/qt-6/qobject.html#setProperty)() and [QObject::property](https://doc.qt.io/qt-6/qobject.html#property)() dynamically set and get properties by name.
- QMetaObject::newInstance() constructs a new instance of the class.