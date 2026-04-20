---
type: note
---
# Background
- A class which provides access to directory structures and their contents. 
- Can be used to:
	- Manipulate path names
	- Access information on reading paths and files
	- Manipulate underlying file system
	- Access Qt's resource system. 
- Uses "/" as a universal directory separator.

# Usage
## Get files and directory contents
```
QDir directory("Documents/Letters");
QString path = directory.filePath("contents.txt");
QString absolutePath = directory.absoluteFilePath("contents.txt");
```

### Current directory and other special Paths

|QDir|[QString](https://doc.qt.io/qt-6/qstring.html)|Return Value|
|---|---|---|
|[current](https://doc.qt.io/qt-6/qdir.html#current)()|[currentPath](https://doc.qt.io/qt-6/qdir.html#currentPath)()|The application's working directory|
|[home](https://doc.qt.io/qt-6/qdir.html#home)()|[homePath](https://doc.qt.io/qt-6/qdir.html#homePath)()|The user's home directory|
|[root](https://doc.qt.io/qt-6/qdir.html#root)()|[rootPath](https://doc.qt.io/qt-6/qdir.html#rootPath)()|The root directory|
|[temp](https://doc.qt.io/qt-6/qdir.html#temp)()|[tempPath](https://doc.qt.io/qt-6/qdir.html#tempPath)()|The system's temporary directory|

## Member Type Documentation 
### `enum QDir:: Filter` and `flags QDir::Filters`
Describes the filtering options available to the `QDir`.

See full list of filters [here](https://doc.qt.io/qt-6/qdir.html#Filter-enum)

### `enum QDir::SortFlag` and `flags QDir::SortFlags`
Describes sort options available to the `QDir` for `entryList()` and `entryInfoList()`