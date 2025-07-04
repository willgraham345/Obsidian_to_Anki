---
type: note
---
# Background
[[PT Shallow Copy vs Deep Copy]]
REMEMBER TO HAVE DESTRUCTORS

# Usage
## Shallow + Deep Copy Constructor
### Shallow
```cpp
#include <iostream>
using namespace std;

class Test
{
    public:
    int a;
    int *p;

    Test (int x)
    {
        a = x;
        p = new int[a];
    }
    Test (Test & t)
    {
        a = t.a;
        p = t.p;
    }
};

int main()
{
    Test t (5);
    t.p[0] = 1;
    Test t2 (t);
    cout << "t: " << t.a << " " << t.p[0] << endl;
    cout << "t2: " << t2.a << " " << t2.p[0] << endl;
}
```
### Deep
```cpp
#include <iostream>
using namespace std;

class Test
{
    public:
    int a;
    int *p;

    Test (int x)
    {
        a = x;
        p = new int[a];
    }
    Test (Test & t)
    {
        a = t.a;
        p = new int[a];
        if (p)
        {
         for (int i = 0; i < a; i++)
         {
             p[i] = t.p[i];
         }
        }
    }
};

int main()
{
    Test t (5);
    t.p[0] = 1;
    Test t2 (t);
    cout << "t: " << t.a << " " << t.p[0] << endl;
    cout << "t2: " << t2.a << " " << t2.p[0] << endl;
}
```