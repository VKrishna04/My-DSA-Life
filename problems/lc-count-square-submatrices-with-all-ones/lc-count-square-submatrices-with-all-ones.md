# Count Square Submatrices with All Ones

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-count-square-submatrices-with-all-ones` |
| Topics | Array, Dynamic Programming, Matrix |
| Solved | 2026-04-20 |
| Runtime | 40 ms (beats 84.35649999999998%) |
| Memory | 22.2 MB (beats 53.76239999999997%) |

## Problem Statement

Given a `m * n` matrix of ones and zeros, return how many **square** submatrices have all ones.

 

**Example 1:**

**Input:** matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
**Output:** 15
**Explanation:** 
There are **10** squares of side 1.
There are **4** squares of side 2.
There is  **1** square of side 3.
Total number of squares = 10 + 4 + 1 = **15**.

**Example 2:**

**Input:** matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
**Output:** 7
**Explanation:** 
There are **6** squares of side 1.  
There is **1** square of side 2. 
Total number of squares = 6 + 1 = **7**.

 

**Constraints:**

	- `1 <= arr.length <= 300`

	- `1 <= arr[0].length <= 300`

	- `0 <= arr[i][j] <= 1`

## Solutions

```Python3
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = 1+ min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])

        return sum(sum(row) for row in matrix)
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. We traverse the matrix once.
*   **Space:** $O(1)$ if modifying the input matrix in-place; otherwise, $O(M \times N)$ for a DP table.

**2. Correctness**
The logic is **correct**. It uses the property that the largest square ending at `(i, j)` has a side length equal to `1 + min(top, left, top-left)`. This side length also represents the number of squares of various sizes ending at that cell.
*   **Edge Cases:** It correctly handles single-row or single-column matrices because the loops (starting at index 1) will be skipped, and the final sum will simply count the existing `1`s.

**3. Optimization**
Accumulate the total count **on the fly** inside the loops. Currently, the code performs an additional $O(M \times N)$ pass with `sum(sum(row)...)`. 
*   **Snippet:** Initialize `total = sum(matrix[0]) + sum(row[0] for row in matrix[1:])` and add `matrix[i][j]` to `total` inside the inner loop.

**4. Key Algorithmic Pattern**
**Dynamic Programming (Tabulation)**. The state `dp[i][j]` represents the side length of the largest square submatrix whose bottom-right corner is at `(i, j)`.
