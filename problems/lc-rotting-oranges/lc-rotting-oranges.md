# Rotting Oranges

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-rotting-oranges` |
| Topics | Array, Breadth-First Search, Matrix |
| Solved | 2026-05-10 |
| Solve Time | 19s |
| Runtime | 3 ms (beats 76.1709%) |
| Memory | 19.2 MB (beats 95.95950000000002%) |

## Problem Statement

You are given an `m x n` `grid` where each cell can have one of three values:

	- `0` representing an empty cell,

	- `1` representing a fresh orange, or

	- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return _the minimum number of minutes that must elapse until no cell has a fresh orange_. If _this is impossible, return_ `-1`.

 

**Example 1:**

**Input:** grid = [[2,1,1],[1,1,0],[0,1,1]]
**Output:** 4

**Example 2:**

**Input:** grid = [[2,1,1],[0,1,1],[1,0,1]]
**Output:** -1
**Explanation:** The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

**Example 3:**

**Input:** grid = [[0,2]]
**Output:** 0
**Explanation:** Since there are already no fresh oranges at minute 0, the answer is just 0.

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 10`

	- `grid[i][j]` is `0`, `1`, or `2`.

## Solutions

```Python3
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh:
            time += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2

                    q.append((nr, nc))

                    fresh -= 1
                
        return time if fresh == 0 else -1
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(M \times N)$, where $M$ and $N$ are grid dimensions. Every cell is visited during the initial scan and at most once during the BFS.
*   **Space Complexity:** $O(M \times N)$. In the worst case (e.g., all oranges are rotten), the queue stores all cells.

### 2. Correctness
The solution is **correct** and handles key edge cases:
*   **No fresh oranges:** Returns `0` immediately (the `while` loop condition `fresh` prevents execution).
*   **Impossible to reach:** Returns `-1` correctly as `fresh` never reaches 0.
*   **Empty grid:** Handled by the initial guard clause.
*   **Disconnected components:** BFS naturally handles multiple sources simultaneously.

### 3. Concrete Optimisation
The code is already highly efficient. A minor **performance optimization** would be to use a single loop with `divmod` or 1D indexing to represent coordinates (e.g., `index = r * cols + c`) to slightly reduce tuple creation overhead in the queue, though this sacrifices readability. 

### 4. Key Algorithmic Pattern
**Multisource Breadth-First Search (BFS)**. This allows for the simultaneous expansion of the "rot" from all initial sources, ensuring the `time` variable accurately reflects the shortest path to all reachable fresh oranges.
