---
tags: note/python
type: note
---
For Array Functions, see [[Python Numpy.Array]]

### Vector Math

| Vector Math                 | Description                                                            |
| --------------------------- | ----------------------------------------------------------- |
| `np.add(arr1,arr2)`         | Elementwise add arr2 to arr1                                |
| `np.subtract(arr1,arr2)`    | Elementwise subtract arr2 from arr1                         |
| `np.multiply(arr1,arr2)`    | Elementwise multiply arr1 by arr2                           |
| `np.divide(arr1,arr2)`      | Elementwise divide arr1 by arr2                             |
| `np.power(arr1,arr2)`       | Elementwise raise arr1 raised to the power of arr2          |
| `np.array_equal(arr1,arr2)` | Returns True if the arrays have the same elements and shape |
| `np.sqrt(arr)`              | Square root of each element in the array                    |
| `np.sin(arr)`               | Sine of each element in the array                           |
| `np.log(arr)`               | Natural log of each element in the array                    |
| `np.abs(arr)`               | Absolute value of each element in the array                 |
| `np.ceil(arr)`              | Rounds up to the nearest int                                |
| `np.floor(arr)`             | Rounds down to the nearest int                              |
| `np.round(arr)`             | Rounds to the nearest int                                   |

### Scalar Math

| Scalar Math Function        | Description                                                          |
| -------------------- | -------------------------------------------------------------------- |
| `np.add(arr,1)`      | Add 1 to each array element                                          |
| `np.subtract(arr,2)` | Subtract 2 from each array element                                   |
| `np.multiply(arr,3)` | Multiply each array element by 3                                     |
| `np.divide(arr,4)`   | Divide each array element by 4 (returns np.nan for division by zero) |
| `np.power(arr,5)`    | Raise each array element to the 5th power                            |

### Statistics 

| Statistics Function   | Description                                                |
| --------------------- | ----------------------------------------------- |
| `np.mean(arr,axis=0)` | Returns mean along specific axis                |
| `arr.sum()`           | Returns sum of arr                              |
| `arr.min()`           | Returns minimum value of arr                    |
| `arr.max(axis=0)`     | Returns maximum value of specific axis          |
| `np.var(arr)`         | Returns the variance of array                   |
| `np.std(arr,axis=1)`  | Returns the standard deviation of specific axis |
| `arr.corrcoef()`      | Returns correlation coefficient of array        |