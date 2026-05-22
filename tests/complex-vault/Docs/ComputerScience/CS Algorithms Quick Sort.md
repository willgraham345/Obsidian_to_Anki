---
type: note
---
# Background
- Algorithm on the [[PT Algorithms Divide and Conquer]] which picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array
- The key process is a partition
	- The target of partitions is to place the pivot (any element can be chosen as the pivot) at its correct position in the sorted array and put all smaller elements to the left of the pivot, and all greater elements to the right of the pivot
	- Done recursively so it finally sorts the array
- Choice of pivot will affect the outcome and complexity of your algorithm
- Advantages
	- Makes it easier to solve problems
	- Efficient on large data sets
	- Low overhead, as it only requires a small amount of memory to function
- Disadvantages
	- Has worst-case time complexity of $O(N^2)$, which occurs when the pivot is chosen poorly
	- Not good choice for small data sets
	- Not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved in the sortred output in the case of quick sort, because here we are swapping elements according to the pivot's position.

![[Pasted image 20240305140059.png]]


