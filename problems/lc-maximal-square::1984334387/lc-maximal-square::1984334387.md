# Maximal Square

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-maximal-square::1984334387` |
| Topics | Array, Dynamic Programming, Matrix |
| Solved | 2026-04-21 |
| Runtime | 92 ms (beats 41.56570000000001%) |
| Memory | 29.3 MB (beats 93.1725%) |

## Problem Statement

Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, _find the largest square containing only_ `1`'s _and return its area_.

 

**Example 1:**

**Input:** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
**Output:** 4

**Example 2:**

**Input:** matrix = [["0","1"],["1","0"]]
**Output:** 1

**Example 3:**

**Input:** matrix = [["0"]]
**Output:** 0

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 300`

	- `matrix[i][j]` is `'0'` or `'1'`.

## Solutions

```Python3
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side = 0
        for i in range(len(matrix)):
            matrix[i][0] = int(matrix[i][0])
            max_side = max(max_side, matrix[i][0])
        for j in range(len(matrix[0])):
            matrix[0][j] = int(matrix[0][j])
            max_side = max(max_side, matrix[0][j])

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                matrix[i][j] = 1 + min(int(matrix[i-1][j]), int(matrix[i-1][j-1]), int(matrix[i][j-1]))
                max_side = max(max_side, matrix[i][j])
        return max_side ** 2
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(M \times N)$ where $M$ and $N$ are the dimensions of the matrix. Each cell is visited twice (once for initialization, once for the DP transition).
*   **Space Complexity:** $O(1)$ *extra* space as it modifies the input matrix in-place.

### 2. Correctness
*   **Empty Matrix:** The code will crash on an empty input (e.g., `[]`) because `matrix[0]` will raise an `IndexError`.
*   **Type Handling:** While it correctly uses `int()` to handle the string-to-integer conversion, calling `int()` repeatedly inside the inner loop is inefficient.
*   **Double Processing:** The cell `matrix[0][0]` is processed twice in the initialization phase, though this does not affect correctness.

### 3. Optimization
**Use 1D DP:** Instead of modifying the input (which is often discouraged in production), use a 1D array of size $N+1$. This reduces space complexity to $O(N)$ and keeps the original data immutable. Additionally, you can eliminate the separate initialization loops by handling boundaries within a single nested loop.

### 4. Key Algorithmic Pattern
**Dynamic Programming (DP):** Specifically, it uses a bottom-up approach where each cell `dp[i][j]` represents the side length of the largest square whose bottom-right corner is at `(i, j)`.
