---
type: note
---
# Background
- You can change what operators do within classes through operator overloading
- 
## Operators we can overload
| Operators that can be overloaded              | Examples                 |
| --------------------------------------------- | ------------------------ |
| Binary Arithmetic                             | +, -, *, /, %            |
| Unary Arithmetic                              | +, -, ++, —              |
| Assignment                                    | =, +=,*=, /=,-=, %=      |
| Bitwise                                       | & , \| , << , >> , ~ , ^ |
| De-referencing                                | (->)                     |
| Dynamic memory allocation,  <br>De-allocation | New, delete              |
| Subscript                                     | [ ]                      |
| Function call                                 | ()                       |
| Logical                                       | &,  \| \|, !             |
| Relational                                    | >, < , = =, <=, >=       |

# Example
## Basic
```cpp
// C++ Program to Demonstrate
// Operator Overloading
#include <iostream>
using namespace std;

class Complex {
private:
	int real, imag;

public:
	Complex(int r = 0, int i = 0)
	{
		real = r;
		imag = i;
	}

	// This is automatically called when '+' is used with
	// between two Complex objects
	Complex operator+(Complex const& obj)
	{
		Complex res;
		res.real = real + obj.real;
		res.imag = imag + obj.imag;
		return res;
	}
	void print() { cout << real << " + i" << imag << '\n'; }
};

int main()
{
	Complex c1(10, 5), c2(2, 4);
	Complex c3 = c1 + c2;
	c3.print();
}
```

## Input/Output Operator Overloading
```cpp
#include <iostream>
using namespace std;
 
class Distance {
   private:
      int feet;             // 0 to infinite
      int inches;           // 0 to 12
      
   public:
      // required constructors
      Distance() {
         feet = 0;
         inches = 0;
      }
      Distance(int f, int i) {
         feet = f;
         inches = i;
      }
      friend ostream &operator<<( ostream &output, const Distance &D ) { 
         output << "F : " << D.feet << " I : " << D.inches;
         return output;            
      }

      friend istream &operator>>( istream  &input, Distance &D ) { 
         input >> D.feet >> D.inches;
         return input;            
      }
};

int main() {
   Distance D1(11, 10), D2(5, 11), D3;

   cout << "Enter the value of object : " << endl;
   cin >> D3;
   cout << "First Distance : " << D1 << endl;
   cout << "Second Distance :" << D2 << endl;
   cout << "Third Distance :" << D3 << endl;

   return 0;
}
```

[Example](https://www.tutorialspoint.com/cplusplus/input_output_operators_overloading.htm)