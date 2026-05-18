# Minimum Path Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-path-sum` |
| Topics | Array, Dynamic Programming, Matrix |
| Solved | 2026-04-20 |
| Runtime | 11 ms (beats 56.491400000000006%) |
| Memory | 21.8 MB (beats 25.873700000000007%) |

## Problem Statement

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

 

**Example 1:**

**Input:** grid = [[1,3,1],[1,5,1],[4,2,1]]
**Output:** 7
**Explanation:** Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1 minimizes the sum.

**Example 2:**

**Input:** grid = [[1,2,3],[4,5,6]]
**Output:** 12

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 200`

	- `0 <= grid[i][j] <= 200`

## Solutions

```Python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[0][1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
```

## AI Review

### 1. Complexity
*   **Time:** $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. Each cell is visited once.
*   **Space:** $O(M \times N)$ to store the `dp` table.

### 2. Correctness
The solution is **correct**. The initialization `dp[0][1] = 0` (while all other cells in the first row/column are $\infty$) is a clever way to ensure the starting cell `grid[0][0]` correctly evaluates to its own value without needing separate loops for the first row and column.

### 3. Optimization
**Space Complexity:** You can reduce space to **$O(N)$** by using a 1D array, as calculating the current row only requires values from the previous row and the element to the left. 
*Example:* `dp[j] = grid[i][j] + min(dp[j], dp[j-1])`.
Alternatively, if allowed, modify the `grid` in-place for **$O(1)$** auxiliary space.

### 4. Key Algorithmic Pattern
**Dynamic Programming (Tabulation)**: It builds a solution bottom-up by breaking the problem into overlapping subproblems (the minimum path to any cell $(i, j)$).
