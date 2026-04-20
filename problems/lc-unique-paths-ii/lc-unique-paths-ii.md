# Unique Paths II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-unique-paths-ii` |
| Topics | Array, Dynamic Programming, Matrix |
| Solved | 2026-04-20 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 63.50730000000001%) |

## Problem Statement

You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.

The testcases are generated so that the answer will be less than or equal to `2 * 109`.

 

**Example 1:**

**Input:** obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
**Output:** 2
**Explanation:** There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

**Example 2:**

**Input:** obstacleGrid = [[0,1],[0,0]]
**Output:** 1

 

**Constraints:**

	- `m == obstacleGrid.length`

	- `n == obstacleGrid[i].length`

	- `1 <= m, n <= 100`

	- `obstacleGrid[i][j]` is `0` or `1`.

## Solutions

```Python3
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for a in range(m):
            if obstacleGrid[a][0] == 1:
                break
            dp[a][0] = 1
        for b in range(n):
            if obstacleGrid[0][b] == 1:
                break
            dp[0][b] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]
```

## AI Review

### 1. Complexity
*   **Time:** $O(m \cdot n)$ — Every cell in the grid is visited once.
*   **Space:** $O(m \cdot n)$ — A 2D DP table of the same dimensions as the input is created.

### 2. Correctness
The code is **correct**. It accurately handles:
*   **Obstacles at boundaries:** The initial loops correctly break when an obstacle is hit, as no further cells in that row/column can be reached.
*   **Obstacle at start/end:** If `obstacleGrid[0][0]` is 1, the DP table remains all zeros, returning 0. If the exit is blocked, the transition `else: dp[i][j] = 0` correctly handles it.

### 3. Concrete Optimisation
**Space Reduction:** You can reduce space complexity to **$O(n)$**. Since the current cell `dp[i][j]` only depends on the cell above (`dp[i-1][j]`) and the cell to the left (`dp[i][j-1]`), you can use a 1D array and update it in-place:
```python
dp = [0] * n
dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
for i in range(m):
    for j in range(n):
        if obstacleGrid[i][j] == 1:
            dp[j] = 0
        elif j > 0:
            dp[j] += dp[j-1]
```

### 4. Key Algorithmic Pattern
**Dynamic Programming (Tabulation)**: It builds a solution bottom-up by solving overlapping subproblems (paths to neighbor cells).
