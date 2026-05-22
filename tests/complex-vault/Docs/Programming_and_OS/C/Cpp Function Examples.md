---
summary:
type: 
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
## Variables within Functions
### Regular
```cpp
int count = 10
void example (int i) {
	cout << i;
	i = 30;
}
int main(){
	example(count);
	cout<<count);
	return 0;
}
//Output
10
10
```

### Reference with Reference
```cpp
int count = 10
void example (int &i) {
	cout << i;
	i = 30;
}
int main(){
	example(count);
	cout<<count);
	return 0;
}
//Output
10
30
```
- Use
	- In function parameters and return types

### Reference with Pointer
```cpp
int count = 10
int* pCount = &count;
void example (int &i) {
	cout << *i;
	*i = 30;
}
int main(){
	example(pCount);
	cout<<count);
	return 0;
}
//Output
10
30
```
- Use:
	- If pointer arithmetic is needed (arrays, linked list, tree)
	- If `NULL` is a valid parameter value
