---
type: note
---
# Background
- Getting RAM information can be be accessed from within a program.

# Usage
```cpp
QProcess p;
p.start("sysctl", QStringList() << "kern.version" << "hw.physmem");
p.waitForFinished();
QString system_info = p.readAllStandardOutput();
p.close();
```