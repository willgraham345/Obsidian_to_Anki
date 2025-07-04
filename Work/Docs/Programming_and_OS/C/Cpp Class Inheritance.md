---
summary: How Cpp classes inherit from each other.
type: note/example
similar:
  - "[[Cpp Storage Classes and Keywords]]"
concept_of:
  - "[[Cpp Class]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, December 27th 2024, 3:42:35 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
## Media
```cpp
class CPoly { //create base polygon class 
	protected:
		int width, height; 
	public:
		void SetValues(int a, int b) { 
			width=a; height=b;
		} 
}; 
class COutput { // create base output 
	public: // class 
		void Output(int i);	 
 }; 
void COutput::Output (int i) { 
	cout << i << endl;
} 
// CRect inherits SetValues from Cpoly // and inherits Output from COutput
class CRect: public CPoly, public COutput {
	public: 
		int area(void){ 
			return (width * height); 
		} 
}; 
// CTri inherits SetValues from CPoly 
class CTri: public CPoly {
	public:
		int area(void){
			return (width * height / 2); 
		}
};
void main () {
	CRect rect; // declare objects
	CTri tri;
	rect.SetValues (2,9);
	tri.SetValues (2,9);
	rect.Output(rect.area());
	cout<<tri.area()<<endl;
```