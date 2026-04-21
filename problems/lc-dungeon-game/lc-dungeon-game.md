# Dungeon Game

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-dungeon-game` |
| Topics | Array, Dynamic Programming, Matrix |
| Solved | 2026-04-21 |
| Runtime | 3 ms (beats 82.65110000000001%) |
| Memory | 20.1 MB (beats 33.98299999999999%) |

## Problem Statement

The demons had captured the princess and imprisoned her in **the bottom-right corner** of a `dungeon`. The `dungeon` consists of `m x n` rooms laid out in a 2D grid. Our valiant knight was initially positioned in **the top-left room** and must fight his way through `dungeon` to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to `0` or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only **rightward** or **downward** in each step.

Return _the knight's minimum initial health so that he can rescue the princess_.

**Note** that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

**Example 1:**

**Input:** dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
**Output:** 7
**Explanation:** The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

**Example 2:**

**Input:** dungeon = [[0]]
**Output:** 1

 

**Constraints:**

	- `m == dungeon.length`

	- `n == dungeon[i].length`

	- `1 <= m, n <= 200`

	- `-1000 <= dungeon[i][j] <= 1000`

## Solutions

```Python3
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0]*n+[float('inf')] for _ in range(m)]
        dp.append([float('inf')]*(n+1))
        dp[-2][-1] = 1
        dp[-1][-2] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]
```

## AI Review

### Analysis

1.  **Complexity**:
    *   **Time**: $O(m \times n)$ where $m$ is the number of rows and $n$ is columns, as we visit each cell once.
    *   **Space**: $O(m \times n)$ to store the `dp` table.

2.  **Correctness**:
    *   **Logic**: Correct. Calculating from bottom-right to top-left is the standard approach because the health requirement at any cell depends on future needs.
    *   **Edge Cases**: The code handles $1 \times 1$ grids and large health boosters/drains correctly. The padding with `inf` and the dual `1` initialization for `dp[-2][-1]` and `dp[-1][-2]` elegantly handles the base case for the princess's cell.

3.  **Optimization**:
    *   **Space Complexity**: You can reduce space to **$O(n)$** (or $O(\min(m, n))$). Since `dp[i][j]` only depends on `dp[i+1][j]` and `dp[i][j+1]`, you only need a 1D array to store the "next" row's values and update it in place.

4.  **Key Algorithmic Pattern**:
    *   **Bottom-up Dynamic Programming** (specifically, **Reverse DP**). By working backward from the destination, you ensure the knight always has at least 1 HP upon entering any cell.
