---
type: note
---
# Background
`QObject` is the most basic class, and provides the following capabilities:
- Object name, parenting system, signals and slots, event management
- All functions in this class are reentrant (can be called simultaneously from multiple threads, but only if each thread uses its own data)
# Usage
- `QObject::connect()` is used to connect a signal to a signla 
## Connecting signal to a slot
```cpp
FooObjectA *fooA = new FooObjectA();
FooObjectB *fooB = new FooObjectB();

QObject::connect(fooA, SIGNAL (bared()), fooB, SLOT (baz()));
```
- This assumes that `FooObjectA` has a `bared` signal, and `FooObjectB` has a `baz` slot
- You need to write the two macros `SIGNAL` and `SLOT`

# Docs
[Docs Link](https://doc.qt.io/qt-6/qobject.html)
## Public Functions[](https://doc.qt.io/qt-6/qobject.html#public-functions "Direct link to this headline")

|   |   |
|---|---|
||**[QObject](https://doc.qt.io/qt-6/qobject.html#QObject)**(QObject *_parent_ = nullptr)|
|virtual|**[~QObject](https://doc.qt.io/qt-6/qobject.html#dtor.QObject)**()|
|QBindable<QString>|**[bindableObjectName](https://doc.qt.io/qt-6/qobject.html#objectName-prop)**()|
|bool|**[blockSignals](https://doc.qt.io/qt-6/qobject.html#blockSignals)**(bool _block_)|
|const QObjectList &|**[children](https://doc.qt.io/qt-6/qobject.html#children)**() const|
|QMetaObject::Connection|**[connect](https://doc.qt.io/qt-6/qobject.html#connect-2)**(const QObject *_sender_, const char *_signal_, const char *_method_, Qt::ConnectionType _type_ = Qt::AutoConnection) const|
|bool|**[disconnect](https://doc.qt.io/qt-6/qobject.html#disconnect-2)**(const char *_signal_ = nullptr, const QObject *_receiver_ = nullptr, const char *_method_ = nullptr) const|
|bool|**[disconnect](https://doc.qt.io/qt-6/qobject.html#disconnect-3)**(const QObject *_receiver_, const char *_method_ = nullptr) const|
|void|**[dumpObjectInfo](https://doc.qt.io/qt-6/qobject.html#dumpObjectInfo)**() const|
|void|**[dumpObjectTree](https://doc.qt.io/qt-6/qobject.html#dumpObjectTree)**() const|
|QList<QByteArray>|**[dynamicPropertyNames](https://doc.qt.io/qt-6/qobject.html#dynamicPropertyNames)**() const|
|virtual bool|**[event](https://doc.qt.io/qt-6/qobject.html#event)**(QEvent *_e_)|
|virtual bool|**[eventFilter](https://doc.qt.io/qt-6/qobject.html#eventFilter)**(QObject *_watched_, QEvent *_event_)|
|T|**[findChild](https://doc.qt.io/qt-6/qobject.html#findChild)**(QAnyStringView _name_, Qt::FindChildOptions _options_ = Qt::FindChildrenRecursively) const|
|`(since 6.7)` T|**[findChild](https://doc.qt.io/qt-6/qobject.html#findChild-1)**(Qt::FindChildOptions _options_ = Qt::FindChildrenRecursively) const|
|QList<T>|**[findChildren](https://doc.qt.io/qt-6/qobject.html#findChildren)**(QAnyStringView _name_, Qt::FindChildOptions _options_ = Qt::FindChildrenRecursively) const|
|`(since 6.3)` QList<T>|**[findChildren](https://doc.qt.io/qt-6/qobject.html#findChildren-1)**(Qt::FindChildOptions _options_ = Qt::FindChildrenRecursively) const|
|QList<T>|**[findChildren](https://doc.qt.io/qt-6/qobject.html#findChildren-2)**(const QRegularExpression &_re_, Qt::FindChildOptions _options_ = Qt::FindChildrenRecursively) const|
|bool|**[inherits](https://doc.qt.io/qt-6/qobject.html#inherits)**(const char *_className_) const|
|void|**[installEventFilter](https://doc.qt.io/qt-6/qobject.html#installEventFilter)**(QObject *_filterObj_)|
|`(since 6.4)` bool|**[isQuickItemType](https://doc.qt.io/qt-6/qobject.html#isQuickItemType)**() const|
|bool|**[isWidgetType](https://doc.qt.io/qt-6/qobject.html#isWidgetType)**() const|
|bool|**[isWindowType](https://doc.qt.io/qt-6/qobject.html#isWindowType)**() const|
|void|**[killTimer](https://doc.qt.io/qt-6/qobject.html#killTimer)**(int _id_)|
|virtual const QMetaObject *|**[metaObject](https://doc.qt.io/qt-6/qobject.html#metaObject)**() const|
|bool|**[moveToThread](https://doc.qt.io/qt-6/qobject.html#moveToThread)**(QThread *_targetThread_)|
|QString|**[objectName](https://doc.qt.io/qt-6/qobject.html#objectName-prop)**() const|
|QObject *|**[parent](https://doc.qt.io/qt-6/qobject.html#parent)**() const|
|QVariant|**[property](https://doc.qt.io/qt-6/qobject.html#property)**(const char *_name_) const|
|void|**[removeEventFilter](https://doc.qt.io/qt-6/qobject.html#removeEventFilter)**(QObject *_obj_)|
|void|**[setObjectName](https://doc.qt.io/qt-6/qobject.html#setObjectName)**(const QString &_name_)|
|`(since 6.4)` void|**[setObjectName](https://doc.qt.io/qt-6/qobject.html#setObjectName-1)**(QAnyStringView _name_)|
|void|**[setParent](https://doc.qt.io/qt-6/qobject.html#setParent)**(QObject *_parent_)|
|bool|**[setProperty](https://doc.qt.io/qt-6/qobject.html#setProperty)**(const char *_name_, const QVariant &_value_)|
|`(since 6.6)` bool|**[setProperty](https://doc.qt.io/qt-6/qobject.html#setProperty-1)**(const char *_name_, QVariant &&_value_)|
|bool|**[signalsBlocked](https://doc.qt.io/qt-6/qobject.html#signalsBlocked)**() const|
|int|**[startTimer](https://doc.qt.io/qt-6/qobject.html#startTimer)**(int _interval_, Qt::TimerType _timerType_ = Qt::CoarseTimer)|
|int|**[startTimer](https://doc.qt.io/qt-6/qobject.html#startTimer-1)**(std::chrono::milliseconds _interval_, Qt::TimerType _timerType_ = Qt::CoarseTimer)|
|QThread *|**[thread](https://doc.qt.io/qt-6/qobject.html#thread)**() const|

## Public Slots[](https://doc.qt.io/qt-6/qobject.html#public-slots "Direct link to this headline")

|   |   |
|---|---|
|void|**[deleteLater](https://doc.qt.io/qt-6/qobject.html#deleteLater)**()|

## Signals[](https://doc.qt.io/qt-6/qobject.html#signals "Direct link to this headline")

|   |   |
|---|---|
|void|**[destroyed](https://doc.qt.io/qt-6/qobject.html#destroyed)**(QObject *_obj_ = nullptr)|
|void|**[objectNameChanged](https://doc.qt.io/qt-6/qobject.html#objectNameChanged)**(const QString &_objectName_)|

## Static Public Members[](https://doc.qt.io/qt-6/qobject.html#static-public-members "Direct link to this headline")

|   |   |
|---|---|
|QMetaObject::Connection|**[connect](https://doc.qt.io/qt-6/qobject.html#connect)**(const QObject *_sender_, const char *_signal_, const QObject *_receiver_, const char *_method_, Qt::ConnectionType _type_ = Qt::AutoConnection)|
|QMetaObject::Connection|**[connect](https://doc.qt.io/qt-6/qobject.html#connect-1)**(const QObject *_sender_, const QMetaMethod &_signal_, const QObject *_receiver_, const QMetaMethod &_method_, Qt::ConnectionType _type_ = Qt::AutoConnection)|
|QMetaObject::Connection|**[connect](https://doc.qt.io/qt-6/qobject.html#connect-3)**(const QObject *_sender_, PointerToMemberFunction _signal_, const QObject *_receiver_, PointerToMemberFunction _method_, Qt::ConnectionType _type_ = Qt::AutoConnection)|
|QMetaObject::Connection|**[connect](https://doc.qt.io/qt-6/qobject.html#connect-4)**(const QObject *_sender_, PointerToMemberFunction _signal_, Functor _functor_)|
|QMetaObject::Connection|**[connect](https://doc.qt.io/qt-6/qobject.html#connect-5)**(const QObject *_sender_, PointerToMemberFunction _signal_, const QObject *_context_, Functor _functor_, Qt::ConnectionType _type_ = Qt::AutoConnection)|
|bool|**[disconnect](https://doc.qt.io/qt-6/qobject.html#disconnect)**(const QObject *_sender_, const char *_signal_, const QObject *_receiver_, const char *_method_)|
|bool|**[disconnect](https://doc.qt.io/qt-6/qobject.html#disconnect-1)**(const QObject *_sender_, const QMetaMethod &_signal_, const QObject *_receiver_, const QMetaMethod &_method_)|
|bool|**[disconnect](https://doc.qt.io/qt-6/qobject.html#disconnect-4)**(const QMetaObject::Connection &_connection_)|
|bool|**[disconnect](https://doc.qt.io/qt-6/qobject.html#disconnect-5)**(const QObject *_sender_, PointerToMemberFunction _signal_, const QObject *_receiver_, PointerToMemberFunction _method_)|
|const QMetaObject|**[staticMetaObject](https://doc.qt.io/qt-6/qobject.html#staticMetaObject-var)**|
|QString|**[tr](https://doc.qt.io/qt-6/qobject.html#tr)**(const char *_sourceText_, const char *_disambiguation_ = nullptr, int _n_ = -1)|