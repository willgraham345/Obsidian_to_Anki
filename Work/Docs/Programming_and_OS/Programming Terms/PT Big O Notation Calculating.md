---
type: note
---
# Basics
1. Break algorithm/function into individual operations
2. Calculate Big O of each operation
3. Add Big O of each operation together
4. Remove the constants
5. Find the highest order term -- this will be what we consider the Big O of our algorithm/function


# Big O of each operation
1. Assume the worst 
	- Last element in an array
2. Remove constants
	- $O(1+n/2+100)$ -> $O(n)$
3. Use different terms for inputs
	- If we loop over the same array twice, then our Big O is technically $O(2n)$. 
	- Change that to be $O(n^2)$
	- If we have nested loops, we are typically multiplying rather than adding the variables
4. Drop any non dominants
## $O(1)$
- 
## $O(log(n))$
- Divide and conquer algorithms, good complexity for sorting algorithms.
```cpp
for (int i = N/2; i <= N; i++){
	for (int j = 2; j <= N; j = j+2 {
		//statements
	}
}
```
## $O(n)$
## $O(n*m)$
- Nested loop
```cpp
for (int i = 0; i < N; i++){
	for (int j = 0; j < M; j++){
	// statements
	}
}
```
## $O(n^2)$
- Nested loop
## $O(2^n)$