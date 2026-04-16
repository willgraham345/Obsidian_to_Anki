---
type: note
---
# Background
- The array is split into a sorted and unsorted part. 
- Values from the unsorted part are picked and placed in the correct position in the sorted parg
	- To sort an array of size $N$ in ascending order, iterate over the array and compare the current element (key) to its predecessor.
		- If the key element is smaller than its predecessor, compare it to the elements before. 
		- Move greater elements one position up to make space for the swapped element
![[Pasted image 20240305135911.png]]
# Usage
## C++ Implementation
```cpp
// C++ program for insertion sort

#include <bits/stdc++.h>
using namespace std;

// Function to sort an array using
// insertion sort
void insertionSort(int arr[], int n)
{
	int i, key, j;
	for (i = 1; i < n; i++) {
		key = arr[i];
		j = i - 1;

		// Move elements of arr[0..i-1],
		// that are greater than key, 
		// to one position ahead of their
		// current position
		while (j >= 0 && arr[j] > key) {
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = key;
	}
}

// A utility function to print an array
// of size n
void printArray(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
}

// Driver code
int main()
{
	int arr[] = { 12, 11, 13, 5, 6 };
	int N = sizeof(arr) / sizeof(arr[0]);

	insertionSort(arr, N);
	printArray(arr, N);

	return 0;
}
// This is code is contributed by rathbhupendra

```