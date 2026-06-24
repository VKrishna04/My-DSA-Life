# Towers Reaching Both Stations

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-geeks-island-170646` |
| Topics | Depth-First Search, Matrix, Breadth-First Search, Array, Graph, Hash Table |
| Solved | 2026-06-24 |

## Solutions

```python3
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

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(N \times M)$, where $N$ and $M$ are matrix dimensions. Each cell is visited at most once per BFS traversal.
*   **Space Complexity:** $O(N \times M)$ to store the sets (`p`, `a`) and the BFS queues.

**2. Correctness**
The solution is correct. It successfully implements the logic for finding cells that can "flow" to two different boundaries (Top/Left and Bottom/Right) by reversing the problem: starting from the boundaries and moving to cells of equal or greater height. It correctly handles edge cases like $1 \times 1$ or $1 \times N$ matrices.

**3. Concrete Optimisation**
Replace the `set` of tuples with a **2D boolean array** (e.g., `visited = [[False]*m for _ in range(n)]`). Hashing tuples and managing set resizing is significantly slower than direct indexing in a pre-allocated list of lists. Additionally, refactor the BFS logic into a helper function to reduce code duplication.

**4. Key Algorithmic Pattern**
**Multi-source Breadth-First Search (BFS)** starting from the boundaries.
