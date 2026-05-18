# Number of Islands

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-number-of-islands` |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Solved | 2026-05-09 |
| Runtime | 228 ms (beats 93.70900000000003%) |
| Memory | 21.6 MB (beats 72.3493%) |

## Problem Statement

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

**Example 1:**

**Input:** grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
**Output:** 1

**Example 2:**

**Input:** grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
**Output:** 3

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 300`

	- `grid[i][j]` is `'0'` or `'1'`.

## Solutions

```Python3
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. Each cell is visited at most once.
*   **Space Complexity:** $O(M \times N)$ in the worst case (e.g., a grid full of '1's) due to the recursion stack depth.

### 2. Correctness
The code is **correct** and handles typical edge cases well (empty grids, single-cell grids, no land). 
*   **Note:** It modifies the input grid (`grid[r][c] = '0'`) to track visited cells. In a real-world scenario, you should ask if mutating the input is allowed; otherwise, a `visited` set or boolean matrix is required.

### 3. Optimization
**Iterative BFS/DFS:** On very large grids, deep recursion can trigger a `RecursionError`. Switching to **Breadth-First Search (BFS)** using `collections.deque` or an iterative DFS with a manual stack ensures the solution is more robust against stack overflow.

### 4. Key Algorithmic Pattern
**Graph Traversal / Connected Components:** Specifically using **Depth-First Search (DFS)** to sink (traverse) an entire island once a piece of land is discovered.
