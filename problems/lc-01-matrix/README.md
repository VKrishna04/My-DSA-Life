# 01 Matrix

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-01-matrix` |
| Topics | Array, Breadth-First Search, Dynamic Programming, Matrix |
| Solved | 2026-05-18 |
| Solve Time | 6m 30s |
| Runtime | 98 ms (beats 88.91540000000003%) |
| Memory | 21.2 MB (beats 82.1553%) |

## Problem Statement

Given an `m x n` binary matrix `mat`, return _the distance of the nearest _`0`_ for each cell_.

The distance between two cells sharing a common edge is `1`.

 

**Example 1:**

**Input:** mat = [[0,0,0],[0,1,0],[0,0,0]]
**Output:** [[0,0,0],[0,1,0],[0,0,0]]

**Example 2:**

**Input:** mat = [[0,0,0],[0,1,0],[1,1,1]]
**Output:** [[0,0,0],[0,1,0],[1,2,1]]

 

**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 104`

	- `1 <= m * n <= 104`

	- `mat[i][j]` is either `0` or `1`.

	- There is at least one `0` in `mat`.

 

**Note:** This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

## Solutions

```Python3
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return
        q = deque()
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >=cols or mat[nr][nc] != -1:
                    continue
                
                mat[nr][nc] = mat[r][c]+1
                q.append((nr, nc))
        return mat
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(M \times N)$, where $M$ is rows and $N$ is columns. Each cell is processed exactly once.
*   **Space:** $O(M \times N)$ to store the `deque` in the worst case (e.g., a matrix full of zeros).

**2. Correctness**
The code is correct and handles edge cases well:
*   **Empty Matrix:** Handled by the initial check.
*   **All Zeros/Ones:** Works correctly. Per problem constraints, there is always at least one `0`.
*   **In-place modification:** By using `-1` to track unvisited cells, it avoids a separate `visited` set, saving space.

**3. Optimization**
**Two-Pass Dynamic Programming:** You can reduce auxiliary space to $O(1)$ (excluding the result) by using DP. 
*   **Pass 1:** Iterate top-left to bottom-right, checking the top and left neighbors.
*   **Pass 2:** Iterate bottom-right to top-left, checking the bottom and right neighbors.
This removes the need for a queue entirely.

**4. Key Algorithmic Pattern**
**Multi-Source Breadth-First Search (BFS).** By initializing the queue with all `0` coordinates simultaneously, the BFS level-order traversal ensures that the first time a `-1` cell is reached, it is via the shortest possible path from any `0`.
