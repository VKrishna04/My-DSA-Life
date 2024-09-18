# Convert 1D Array Into 2D Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-convert-1d-array-into-2d-array` |
| Topics | Array, Matrix, Simulation |
| Solved | 2024-09-18 |
| Runtime | 688 ms (beats 5.015699999999995%) |
| Memory | 23.4 MB (beats 100%) |

## Problem Statement

You are given a **0-indexed** 1-dimensional (1D) integer array `original`, and two integers, `m` and `n`. You are tasked with creating a 2-dimensional (2D) array with ` m` rows and `n` columns using **all** the elements from `original`.

The elements from indices `0` to `n - 1` (**inclusive**) of `original` should form the first row of the constructed 2D array, the elements from indices `n` to `2 * n - 1` (**inclusive**) should form the second row of the constructed 2D array, and so on.

Return _an _`m x n`_ 2D array constructed according to the above procedure, or an empty 2D array if it is impossible_.

 

**Example 1:**

**Input:** original = [1,2,3,4], m = 2, n = 2
**Output:** [[1,2],[3,4]]
**Explanation:** The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

**Example 2:**

**Input:** original = [1,2,3], m = 1, n = 3
**Output:** [[1,2,3]]
**Explanation:** The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.

**Example 3:**

**Input:** original = [1,2], m = 1, n = 1
**Output:** []
**Explanation:** There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.

 

**Constraints:**

	- `1 <= original.length <= 5 * 104`

	- `1 <= original[i] <= 105`

	- `1 <= m, n <= 4 * 104`

## Solutions

```Python3
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = []
        if len(original) != m*n:
            return arr
        for i in range(m):
            arr.append(original[n * i:n * (i + 1)])
        return arr
```

## AI Review

### 1. Complexity
*   **Time:** $O(m \times n)$ or $O(L)$, where $L$ is the length of `original`. Each element is visited once during slicing.
*   **Space:** $O(m \times n)$ to store the result. Excluding the output, the auxiliary space is $O(1)$ (ignoring temporary slice objects).

### 2. Correctness
The solution is **correct**. It handles the core constraint (`len(original) != m * n`) first and correctly uses Python's slicing bounds to partition the 1D array into rows.
*   **Edge cases:** Correctly handles cases where $m=1$ or $n=1$, and cases where dimensions are incompatible with the input size.

### 3. Concrete Optimisation
Use **List Comprehension**. It is more idiomatic and generally faster in Python than repeated `.append()` calls because it is optimized at the C level:
```python
return [original[i * n : (i + 1) * n] for i in range(m)] if len(original) == m * n else []
```

### 4. Key Algorithmic Pattern
**Array Reshaping/Slicing**: Mapping a 1D index $i$ to 2D coordinates $(r, c)$ using the relationship `index = r * n + c`. In this specific Python implementation, it leverages **interval slicing**.
