---
type: note
similar:
  - "[[Rust trait]]"
---
# Background
C++ has no built-in concept of interfaces. You can implement using abstract classes, which contain only virtual functions. 


# Usage
## Syntax
```cpp
class Interface
{
public:
	Interface(){}
	virtual ~Interface(){}
	virtual void method1() = 0; //"=0" makes this method pure virtual, and
	virtual void method2() = 0; // also makes this class abstract
};
class Concrete : public Interface
{
private:
	int myMember;
public:
	Concrete(){}
	~Concrete(){}
	void method1();
	void method2();
}
void Concrete::method1()
{
	// stuff goes here
}
void Concrete::method2()
{
	//other stuff here
}
int main(void)
{
	Interface *f = new Concrete();
	f->method1();
	f->method2();
	delete f;
	return 0;
}
```

## Example Usage