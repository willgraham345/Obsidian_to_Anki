---
type: note
---
# Background
- Stores a string of 16bit [[Qt.QtCore.QChar]]s
- Behind the scenes, QString implicitly shares (copy-on-write). 
- An alternative to this class is the [[Qt.QtCore.QByteArray]]

# Usage
## Initializing a String
Pass a `const char *` to its constructro
```cpp
QString str = "Hello";
```

## See if a QString contains another QString
```cpp
bool QString::contains(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
//or
bool QString::contains(QChar ch, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
```

### Example
```
QString str = "Peter Pan";
str.contains("peter", Qt::CaseInsensitive);
```