# Spiral Matrix III

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-spiral-matrix-iii` |
| Topics | Array, Matrix, Simulation |
| Solved | 2026-06-23 |
| Runtime | 15 ms (beats 26.939500000000002%) |
| Memory | 20.6 MB (beats 7.7586999999999975%) |

## Problem Statement

You start at the cell `(rStart, cStart)` of an `rows x cols` grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all `rows * cols` spaces of the grid.

Return _an array of coordinates representing the positions of the grid in the order you visited them_.

 

**Example 1:**

**Input:** rows = 1, cols = 4, rStart = 0, cStart = 0
**Output:** [[0,0],[0,1],[0,2],[0,3]]

**Example 2:**

**Input:** rows = 5, cols = 6, rStart = 1, cStart = 4
**Output:** [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

 

**Constraints:**

	- `1 <= rows, cols <= 100`

	- `0 <= rStart < rows`

	- `0 <= cStart < cols`

## Solutions

```Python3
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i,j = rStart, cStart

        diri, dirj = 0, 1 # directions to move
        twice = 2
        res = []
        moves = 1
        next_moves = 2

        while len(res) < (rows * cols):
            if (-1 < i < rows) and ( -1 < j < cols):
                res.append([i,j])
            
            i += diri
            j += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri # 90 deg Clockwise
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return res
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(\max(R, C)^2)$. The spiral continues expanding until all cells are visited. In the worst case, the spiral's side length grows proportional to the largest dimension of the grid.
*   **Space Complexity:** $O(R \times C)$ to store the resulting coordinates.

### 2. Correctness
The logic is **correct**. It accurately simulates the spiral pattern (Right $\to$ Down $\to$ Left $\to$ Up) where the step length increases every two turns ($1, 1, 2, 2, 3, 3, \dots$). 
*   **Edge Cases:** The code handles $1 \times 1$ grids and starting positions at boundaries correctly because it checks bounds *before* moving and terminates immediately once the result list is full.

### 3. Optimization
**Skip out-of-bounds segments:** Currently, the code iterates one step at a time even when far outside the grid. You can mathematically check if a side of the spiral (from `step_start` to `step_end`) intersects the rectangle $[0, rows-1] \times [0, cols-1]$. If it doesn't, you can update `i, j` and `moves` in a single addition/jump rather than a loop.

### 4. Key Algorithmic Pattern
**Simulation:** The problem is solved by directly simulating the movement rules (traversal with changing directions and incremental step sizes).
