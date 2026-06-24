# Pacific Atlantic Water Flow

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-pacific-atlantic-water-flow` |
| Topics | Breadth-First Search, Graph Traversal, Set, Grid |
| Solved | 2026-06-24 |

## Solutions

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
