---
summary: How to work with Cpp arrays within functions.
headings: ["[[#Usage]]"]
type: note/workflow
date created: Thursday, June 19th 2025, 1:50:52 pm
date modified: Thursday, June 19th 2025, 1:53:08 pm
workflow_of: ["[[Cpp Functions]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage
- [p] `return_type function_name (data_type *array_name){}` = passes an array to a function as a pointer = #code/cpp/variables/array #code/cpp/functions
<!--ID: 1751434091674-->

- [p] `return_type function_name (data_type *array_name[]){}` = passes an unsized array to a function = #code/cpp/variables/array #code/cpp/functions
<!--ID: 1751434091677-->

- [p] `return_type function_name (data_type *array_name[size]){}` = passes a sized array to a function = #code/cpp/variables/array #code/cpp/functions
<!--ID: 1751434091681-->


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