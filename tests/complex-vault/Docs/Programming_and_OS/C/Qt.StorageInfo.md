---
type: note
---
# Background
- Allows you to retrieve info regarding the volume's space, mount point, label, and filesystem name. 
- Can be created by passing the path and the volume's mount point as a constructor parameter, or by using the `setPath` method. Static `mountedVolumes()` can be used to get the list of all mounted filesystems. 
[Docs](https://doc.qt.io/qt-6/qstorageinfo.html)
# Usage

## Public Functions[](https://doc.qt.io/qt-6/qstorageinfo.html#public-functions "Direct link to this headline")

|   |   |
|---|---|
||**[QStorageInfo](https://doc.qt.io/qt-6/qstorageinfo.html#QStorageInfo)**()|
||**[QStorageInfo](https://doc.qt.io/qt-6/qstorageinfo.html#QStorageInfo-1)**(const QString &_path_)|
||**[QStorageInfo](https://doc.qt.io/qt-6/qstorageinfo.html#QStorageInfo-2)**(const QDir &_dir_)|
||**[QStorageInfo](https://doc.qt.io/qt-6/qstorageinfo.html#QStorageInfo-3)**(const QStorageInfo &_other_)|
||**[~QStorageInfo](https://doc.qt.io/qt-6/qstorageinfo.html#dtor.QStorageInfo)**()|
|int|**[blockSize](https://doc.qt.io/qt-6/qstorageinfo.html#blockSize)**() const|
|qint64|**[bytesAvailable](https://doc.qt.io/qt-6/qstorageinfo.html#bytesAvailable)**() const|
|qint64|**[bytesFree](https://doc.qt.io/qt-6/qstorageinfo.html#bytesFree)**() const|
|qint64|**[bytesTotal](https://doc.qt.io/qt-6/qstorageinfo.html#bytesTotal)**() const|
|QByteArray|**[device](https://doc.qt.io/qt-6/qstorageinfo.html#device)**() const|
|QString|**[displayName](https://doc.qt.io/qt-6/qstorageinfo.html#displayName)**() const|
|QByteArray|**[fileSystemType](https://doc.qt.io/qt-6/qstorageinfo.html#fileSystemType)**() const|
|bool|**[isReadOnly](https://doc.qt.io/qt-6/qstorageinfo.html#isReadOnly)**() const|
|bool|**[isReady](https://doc.qt.io/qt-6/qstorageinfo.html#isReady)**() const|
|bool|**[isRoot](https://doc.qt.io/qt-6/qstorageinfo.html#isRoot)**() const|
|bool|**[isValid](https://doc.qt.io/qt-6/qstorageinfo.html#isValid)**() const|
|QString|**[name](https://doc.qt.io/qt-6/qstorageinfo.html#name)**() const|
|void|**[refresh](https://doc.qt.io/qt-6/qstorageinfo.html#refresh)**()|
|QString|**[rootPath](https://doc.qt.io/qt-6/qstorageinfo.html#rootPath)**() const|
|void|**[setPath](https://doc.qt.io/qt-6/qstorageinfo.html#setPath)**(const QString &_path_)|
|QByteArray|**[subvolume](https://doc.qt.io/qt-6/qstorageinfo.html#subvolume)**() const|
|void|**[swap](https://doc.qt.io/qt-6/qstorageinfo.html#swap)**(QStorageInfo &_other_)|
|QStorageInfo &|**[operator=](https://doc.qt.io/qt-6/qstorageinfo.html#operator-eq)**(const QStorageInfo &_other_)|
|QStorageInfo &|**[operator=](https://doc.qt.io/qt-6/qstorageinfo.html#operator-eq-1)**(QStorageInfo &&_other_)|

## mountedVolumes()
```cpp
foreach (const QStorageInfo &storage, QStorageInfo::mountedVolumes()) {
        if (storage.isValid() && storage.isReady()) {
            if (!storage.isReadOnly()) {
                // ...
            }
        }
    }
```