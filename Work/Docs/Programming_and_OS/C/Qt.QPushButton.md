---
type: note
---
# Background
[Docs](https://doc.qt.io/qt-6/qpushbutton.html#)
The push button, or command button, is perhaps the most commonly used widget in any graphical user interface. Push (click) a button to command the computer to perform some action, or to answer a question. Typical buttons are OK, Apply, Cancel, Close, Yes, No and Help.

## Signals
A push button emits the signal [clicked](https://doc.qt.io/qt-6/qabstractbutton.html#clicked)() when it is activated by the mouse, the Spacebar or by a keyboard shortcut. Connect to this signal to perform the button's action. Push buttons also provide less commonly used signals, for example [pressed](https://doc.qt.io/qt-6/qabstractbutton.html#pressed)() and [released](https://doc.qt.io/qt-6/qabstractbutton.html#released)().


# Usage
## Public Functions[](https://doc.qt.io/qt-6/qpushbutton.html#public-functions "Direct link to this headline")

|   |   |
|---|---|
||**[QPushButton](https://doc.qt.io/qt-6/qpushbutton.html#QPushButton)**(QWidget *_parent_ = nullptr)|
||**[QPushButton](https://doc.qt.io/qt-6/qpushbutton.html#QPushButton-1)**(const QString &_text_, QWidget *_parent_ = nullptr)|
||**[QPushButton](https://doc.qt.io/qt-6/qpushbutton.html#QPushButton-2)**(const QIcon &_icon_, const QString &_text_, QWidget *_parent_ = nullptr)|
|virtual|**[~QPushButton](https://doc.qt.io/qt-6/qpushbutton.html#dtor.QPushButton)**()|
|bool|**[autoDefault](https://doc.qt.io/qt-6/qpushbutton.html#autoDefault-prop)**() const|
|bool|**[isDefault](https://doc.qt.io/qt-6/qpushbutton.html#default-prop)**() const|
|bool|**[isFlat](https://doc.qt.io/qt-6/qpushbutton.html#flat-prop)**() const|
|QMenu *|**[menu](https://doc.qt.io/qt-6/qpushbutton.html#menu)**() const|
|void|**[setAutoDefault](https://doc.qt.io/qt-6/qpushbutton.html#autoDefault-prop)**(bool)|
|void|**[setDefault](https://doc.qt.io/qt-6/qpushbutton.html#default-prop)**(bool)|
|void|**[setFlat](https://doc.qt.io/qt-6/qpushbutton.html#flat-prop)**(bool)|
|void|**[setMenu](https://doc.qt.io/qt-6/qpushbutton.html#setMenu)**(QMenu *_menu_)|

## Public Slots[](https://doc.qt.io/qt-6/qabstractbutton.html#public-slots "Direct link to this headline")

|      |                                                                                                   |
| ---- | ------------------------------------------------------------------------------------------------- |
| void | **[animateClick](https://doc.qt.io/qt-6/qabstractbutton.html#animateClick)**()                    |
| void | **[click](https://doc.qt.io/qt-6/qabstractbutton.html#click)**()                                  |
| void | **[setChecked](https://doc.qt.io/qt-6/qabstractbutton.html#checked-prop)**(bool)                  |
| void | **[setIconSize](https://doc.qt.io/qt-6/qabstractbutton.html#iconSize-prop)**(const QSize &_size_) |
| void | **[toggle](https://doc.qt.io/qt-6/qabstractbutton.html#toggle)**()                                |
## Signals[](https://doc.qt.io/qt-6/qabstractbutton.html#signals "Direct link to this headline")

|      |                                                                                            |
| ---- | ------------------------------------------------------------------------------------------ |
| void | **[clicked](https://doc.qt.io/qt-6/qabstractbutton.html#clicked)**(bool _checked_ = false) |
| void | **[pressed](https://doc.qt.io/qt-6/qabstractbutton.html#pressed)**()                       |
| void | **[released](https://doc.qt.io/qt-6/qabstractbutton.html#released)**()                     |
| void | **[toggled](https://doc.qt.io/qt-6/qabstractbutton.html#toggled)**(bool _checked_)         |