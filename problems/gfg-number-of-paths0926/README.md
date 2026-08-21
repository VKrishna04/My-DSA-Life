# Number Of Paths

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-number-of-paths0926` |
| Topics | Dynamic Programming, Math, Array |
| Solved | 2026-06-24 |

## Problem Statement

Given two integers **m** and **n** representing the number of rows and columns of a grid, respectively, find the number of distinct paths from the top-left cell (0, 0) to the bottom-right cell (m - 1, n - 1). From any cell, you can move only right or down.

**Note:** The answer is guaranteed to fit within a 32-bit integer.

**Examples:**

**Input**: m = 2, n = 3
**Output**: 3
**Explanation**: There are three distinct paths from the top-left cell to the bottom-right cell.
 
**Input**: m = 1, n = 4
**Output:** 1
**Explanation**: There is only one possible path from the top-left cell to the bottom-right cell.

**Constraints:**
1 &le; m &le; 100
1 &le; n &le; 100

## Solutions

```python3
class Solution:
    def numberOfPaths(self, m, n):
        dp = []
        for _ in range(m):
            dp.append([1]*n)
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
```

## AI Review

### Analysis
1. **Complexity**: 
   - **Time**: $O(m \times n)$ as every cell in the grid is visited once.
   - **Space**: $O(m \times n)$ to store the 2D `dp` table.

2. **Correctness**: The solution is logically sound. It correctly handles the base cases (where $m=1$ or $n=1$) because the nested loops will not execute, returning the initialized value of `1`.

3. **Optimization**: Addressing your recurring flag for **space complexity**, this can be optimized to **$O(n)$**. You only need the current row and the previous row to calculate the next values. Even better, you can use a single 1D array of size $n$ and update it in place: `dp[j] += dp[j-1]`.

4. **Pattern**: Dynamic Programming (Tabulation).

### Summary
While the DP approach is standard, the $O(m \times n)$ space is a common bottleneck in your history. For this specific problem, a mathematical approach using Combinatorics—calculating $\binom{m+n-2}{m-1}$—would achieve $O(\min(m, n))$ time and $O(1)$ space.
