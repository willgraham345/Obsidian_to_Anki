---
type: note
---
# Background
How Qt deals with object destruction, especially widgets. 

Basic properties
- When an object is destroyed, all of its children are destroyed as well. Calling delete becomes optional in certain cases. 
- All `QObject`s have `findChild` and `findChildren` methods that can be use dto search for children of a given object
- Child widgets in a `QWidget` automatically appear inside the parent widget. 

# Usage
A `QPushButton` inside a `QPushButton`
```cpp
#include <QApplication>
#include <QPushButton>

int main(int argc, char **argv)
{
 QApplication app (argc, argv);

 QPushButton button1 ("test");
 QPushButton button2 ("other", &button1);

 button1.show();

 return app.exec();
}
```
- When application is closed, `button1` which is on the stack, is deallocated. Since `button2` has `button1`, as a parent it is deleted also. 
	- There is no memory leak. 