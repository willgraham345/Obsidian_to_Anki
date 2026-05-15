---
summary: How to work with Cpp arrays within functions.
headings:
  - "[[#Usage]]"
type: note/process
date created: Thursday, June 19th 2025, 1:50:52 pm
date modified: Monday, July 7th 2025, 9:56:16 am
process_of:
  - "[[Cpp functions]]"
  - "[[Cpp std array]]"
  - "[[Cpp pointers]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage
  `void func(data *a){}` ;;; Declaration to pass a c-style array `a` of type `data` to a function as a pointer. Function has type `void` and has handle `func` = #lang/data/array #lang/functions 
ID: 1751997629749



  `data func(type *a[]){}` ;;; Declaration to pass an unsized c-style array `a` of type `type` to a function. Function is of type `data` and has name `func` = #lang/data/array #lang/functions 
ID: 1751997629753



  `return_type function_name (data_type *array_name[size]){}` ;;; Declaration to pass a sized c-style array to a function. = #lang/data/array #lang/functions 
ID: 1751997629757



#### Pointer Argument
```cpp
void printArrayPointer(int* ptr, int n){
	for (int i = 0; i < n; i++){
		cout << ptr[i] << " ";
	}
}
int main(){
	int arr[] = {10, 20, 30};
	printArrayPointer(arr, 3);
}
```
