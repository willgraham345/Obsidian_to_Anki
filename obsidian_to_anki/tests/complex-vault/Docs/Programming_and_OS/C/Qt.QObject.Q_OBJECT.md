---
type: note
---
# Background
- You can add this macro to any section of a class definition that declares its own signals and slots or that uses other services provided by Qt's meta-object system
- A macro that is used to enable meta-object features, like dynamic properties, signals, and slots. 

# Usage
## Example usage in a class
```cpp
#include <QObject>

class Counter : public QObject
{
    Q_OBJECT

// Note. The Q_OBJECT macro starts a private section.
// To declare public members, use the 'public:' access modifier.
public:
    Counter() { m_value = 0; }

    int value() const { return m_value; }

public slots:
    void setValue(int value);

signals:
    void valueChanged(int newValue);

private:
    int m_value;
};
```