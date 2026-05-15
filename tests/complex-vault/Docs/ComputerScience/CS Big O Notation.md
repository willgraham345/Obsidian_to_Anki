---
type: note
---
# Background
- A way to measure an algorithms efficiency
- Two metrics
	- Time complexity
	- Space complexity

# Definition
## Terms
For a problem of size $N$
- Constant-time: 
	- "Order 1" 
	- $O(1)$
- Linear-time
	- "Order N"
	- $O(N)$
- Quadratic
	- "Order N squared"
	- $O(N^2)$


## Problem Definition
- Let $g$ and $f$ be functions from the set of natural numbers to itself
- $f$ is said to be $O(g)$
	- If there is a constant $c > 0$ and a natural number $n_0$ such that $f(n) <= cg(n)$ for all $n >=n_0$

### Useful Properties
Constant multiplication
- If $f(n) = c.g(n)$
	- Then $O(f(n)) = O(g(n))$
	- $c$ = non-zero constant
Polynomial
- If $f(n) = a_0.n + a_1.n + a_2.n^2 + \cdots  + f_m(n)$ 
	- then $O(f(n)) = O(n^m)$
Summation
- If $f(n) = f_1(n) + f_2(n) + \cdots + f_m(n)$ and $f_i(n) <= f_{i+1}(n) \forall i=1$ (for all $i = 1$)
	- Then $O(f(n)) = O(max(f_1(n), f_2(n), \cdots, f_m(n)))$
Logarithmic Function


## Procedure for Analysis
1. Figure out what the input is and what $n$ represents
2. Express the maximum number of operations, the algorithms performs in terms of $n$
3. Eliminate all excluding the highest order of terms
4. Remove all the constant factors

# Best to Worst Performance
## Classification
- A logarithmic algorithm – $O(logn)$
	- Runtime grows logarithmically in proportion to n. 
	- Binary Search. 
- A linear algorithm – $O(n)$ 
	- Runtime grows directly in proportion to n. 
	- Linear Search
- A superlinear algorithm – $O(nlogn)$ 
	- Runtime grows in proportion to n. 
	- Heap sort, Merge Sort
- A polynomial algorithm – $O(nc)$
	- Runtime grows quicker than previous all based on n. 
	- Strassen’s Matrix Multiplication, Bubble Sort, Selection Sort, Insertion Sort, Bucket Sort. 
- A exponential algorithm – $O(cn)$
	- Runtime grows even faster than polynomial algorithm based on n. 
	- Tower of Hanoi
- A factorial algorithm – $O(n!)$ 
	- Runtime grows the fastest and becomes quickly unusable for even small values of n.  
	- Determinant Expansion by Minors, Brute force Search algorithm for Traveling Salesman Problem. 
## Table with Example

| Classes       | n          | _Complexity number of operations (10**)**_ | Execution Time (1 instruction/μsec) |
| ------------- | ---------- | ------------------------------------------ | ----------------------------------- |
| _constant_    | _O(1)_     | _1_                                        | _1 μsec_                            |
| _logarithmic_ | _O(logn)_  | _3.32_                                     | _3 μsec_                            |
| _linear_      | _O(n)_     | _10_                                       | _10 μsec_                           |
| _O(nlogn)_    | _O(nlogn)_ | _33.2_                                     | _33 μsec_                           |
| _quadratic_   | _O(n2)_    | _102_                                      | _100 μsec_                          |
| _cubic_       | _O(n3)_    | _103_                                      | _1msec_                             |
| _exponential_ | _O(2n)_    | _1024_                                     | _10 msec_                           |
| _factorial_   | _O(n!)_    | _10!_                                      | _3.6288 sec_                        |

