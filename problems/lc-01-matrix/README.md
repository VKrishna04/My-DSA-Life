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

### 1. Complexity
*   **Time:** $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. Each cell is visited and processed exactly once.
*   **Space:** $O(M \times N)$ in the worst case to store the `deque` (e.g., a grid where half the cells are zeros).

### 2. Correctness
The code is **correct**. Initializing `1`s to `-1` acts as a "visited" set, and the multi-source BFS ensures that the first time a `-1` cell is reached, it is assigned its minimum distance from any `0`.
*   **Edge Cases:** It handles matrices with only one `0` or all `0`s correctly. Note: LeetCode constraints guarantee at least one `0`.

### 3. Concrete Optimization
Use **Two-Pass Dynamic Programming** to achieve **$O(1)$ auxiliary space** (excluding the input/output matrix).
*   **Pass 1 (Top-Left to Bottom-Right):** For each `mat[r][c] == 1`, set it to `min(top, left) + 1`.
*   **Pass 2 (Bottom-Right to Top-Left):** Update `mat[r][c] = min(mat[r][c], bottom + 1, right + 1)`.
This removes the need for a queue entirely.

### 4. Key Algorithmic Pattern
**Multi-source Breadth-First Search (BFS)**. All "source" nodes (zeros) are added to the queue initially to explore the grid in concurrent radial waves.
