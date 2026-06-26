# Pacific Atlantic Water Flow

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-pacific-atlantic-water-flow` |
| Topics | Graph, Breadth-First Search, Depth-First Search |
| Solved | 2026-06-24 |

## Problem Statement

You are given a matrix **mat[][]** of dimensions **n x m**, where mat[i][j] represents the **height of a cell** in a rectangular grid island. The **Pacific Ocean** touches the island's **left and top** borders, and the **Atlantic Ocean** touches the island's **right and bottom** borders. Rainwater can flow from a cell to its neighbouring cells in the directions North, South, East, and West, but only if the **neighbouring cell has a height less than or equal to the current cell's height**.

The task is to determine **all coordinates (x, y)** such that water can flow from the cell (x, y) to **both** the Pacific Ocean and the Atlantic Ocean. Water can flow from any adjacent cell directly into an ocean.

**Examples:**

**Input: **mat[][] = [[1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4]]
**Output:** 7
**Explanation:** In the given matrix, there are 7 coordinates through which the water can flow to both the Oceans. They are  (0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), and (4, 0).
**Input: **arr[][] = [[2, 2], 
               [2, 2]]
**Output:** 4
**Explanation:** In the following example, all cells allow water to flow to both the Oceans.
**Constraints:**
1 ≤ number of rows, number of columns ≤ 103
1 ≤ arr[i][j] ≤ 103

## Solutions

### Approach 1 (python3)

Synced from submissions table — 2026-06-24 07:51:20

```Python3
from collections import deque
class Solution:
    def countCoordinates(self, mat):
        n, m = len(mat), len(mat[0])
        p, a = set(), set()
        pq, aq = deque(), deque()
        for r in range(n):
            pq.append((r, 0)); p.add((r, 0))
            aq.append((r, m-1)); a.add((r, m-1))
        for c in range(m):
            pq.append((0, c)); p.add((0, c))
            aq.append((n-1, c)); a.add((n-1, c))
        while pq:
            r, c = pq.popleft()
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in p and mat[nr][nc] >= mat[r][c]:
                    p.add((nr, nc)); pq.append((nr, nc))
        while aq:
            r, c = aq.popleft()
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in a and mat[nr][nc] >= mat[r][c]:
                    a.add((nr, nc)); aq.append((nr, nc))
        return len(p & a)
```

## AI Review

1.  **Time complexity (Big-O) and space complexity**
    Time complexity: O(N*M), where N is the number of rows and M is the number of columns. Two BFS traversals each visit every cell and edge at most once. Set intersection is also O(N*M).
    Space complexity: O(N*M) for storing the `p` and `a` sets and the `pq`, `aq` deques, which can hold up to all grid coordinates.

2.  **Correctness — any edge cases that could fail?**
    The core approach of performing two reverse BFS traversals from the Pacific and Atlantic borders is correct for identifying cells that can reach each ocean. The flow condition `mat[nr][nc] >= mat[r][c]` for reverse traversal is also correct.
    **However, the solution fails to meet the problem's output requirement.** It returns `len(p & a)` (an integer count) instead of `list(p & a)` (a list of coordinates `[r, c]`). This is a critical error.

3.  **One concrete optimisation if applicable**
    The primary "optimization" is correcting the return type from `len(p & a)` to `list(p & a)` to match the problem's expected output. The two-BFS approach is already optimal for this problem.

4.  **Key algorithmic pattern used**
    Breadth-First Search (BFS), Graph Traversal.
