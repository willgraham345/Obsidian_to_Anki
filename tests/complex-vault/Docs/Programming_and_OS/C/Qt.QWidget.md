---
type: note
---
# Background
- Widgets are able to respond to events and use parenting system and signals for slot mechanism.
- The `QWidget` contains most properties that are used to describe a window, or a widget, like position and size, mouse cursor, tooltips, etc.

# Usage
## Subclassing
Make a class inherit from `QWidget`
header
```cpp
#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>

class Window : public QWidget
{
 Q_OBJECT // A macro
 public:
  explicit Window(QWidget *parent = 0);

 signals: //a new category of methods
 public slots: //a new category of methods
};

#endif // WINDOW_H
```
src
```cpp
#include "window.h"

Window::Window(QWidget *parent) :
 QWidget(parent) {}
```
main
```cpp
#include <QApplication>
#include "window.h"

int main(int argc, char **argv)
{
 QApplication app (argc, argv);

 Window window;
 window.show();

 return app.exec();
}
```

Things to notice:
- `Q_OBJECT` macro
- `signals` 
	- New category of methods
- `public slots`
- Implementing the window is done in the constructor