# Unique Paths

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-unique-paths` |
| Topics | Math, Dynamic Programming, Combinatorics |
| Solved | 2026-04-10 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 22%) |

## Problem Statement

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.

 

**Example 1:**

**Input:** m = 3, n = 7
**Output:** 28

**Example 2:**

**Input:** m = 3, n = 2
**Output:** 3
**Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

 

**Constraints:**

	- `1 <= m, n <= 100`

## Solutions

```Python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            dp.append([1]*n)
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
```

## AI Review

### Review of Unique Paths Solution

**1. Complexity**
*   **Time Complexity:** $O(m \times n)$ — Each cell in the grid is visited and computed exactly once.
*   **Space Complexity:** $O(m \times n)$ — A 2D list of size $m \times n$ is allocated to store path counts.

**2. Correctness**
The solution is **correct**. It properly handles the base cases: if $m=1$ or $n=1$, the nested loops do not execute, and the function correctly returns 1 (the only possible path is a straight line).

**3. Concrete Optimization**
**Space Optimization:** Since the current cell `dp[i][j]` only depends on the cell above it (`dp[i-1][j]`) and the cell to its left (`dp[i][j-1]`), you can reduce space to **$O(n)$** using a 1D array.

*Optimized Snippet:*
```python
dp = [1] * n
for i in range(1, m):
    for j in range(1, n):
        dp[j] += dp[j-1]
return dp[-1]
```

**4. Key Algorithmic Pattern**
**Dynamic Programming (Bottom-Up):** The problem breaks down into overlapping subproblems where the number of ways to reach `(i, j)` is the sum of ways to reach its neighbors `(i-1, j)` and `(i, j-1)`.

## Notes

[ Time taken: 1m 55s ]
