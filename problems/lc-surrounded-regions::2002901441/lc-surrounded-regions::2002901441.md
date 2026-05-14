# Surrounded Regions

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-surrounded-regions::2002901441` |
| Topics | Array, Breadth-First Search, Depth-First Search, Matrix, Union-Find |
| Solved | 2026-05-14 |
| Runtime | 3 ms (beats 84.6562%) |
| Memory | 22.5 MB (beats 40.83939999999998%) |

## Problem Statement

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

	- **Connect**: A cell is connected to adjacent cells horizontally or vertically.

	- **Region**: To form a region **connect every** `'O'` cell.

	- **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed **by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

 

**Example 1:**

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

**Explanation:**

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

**Example 2:**

**Input:** board = [["X"]]

**Output:** [["X"]]

 

**Constraints:**

	- `m == board.length`

	- `n == board[i].length`

	- `1 <= m, n <= 200`

	- `board[i][j]` is `'X'` or `'O'`.

## Solutions

```Python3
import sys
sys.setrecursionlimit(2000)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board: return
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return

            board[r][c] = 'T'

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for c in range(cols):
            if board[0][c] == 'O': dfs(0, c)
            if board[rows - 1][c] == 'O': dfs(rows - 1, c)
            
        for r in range(1, rows - 1):
            if board[r][0] == 'O': dfs(r, 0)
            if board[r][cols - 1] == 'O': dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. Every cell is visited at most twice (once during DFS/boundary checks and once during the final scan).
*   **Space Complexity:** $O(M \times N)$ in the worst case for the recursion stack (e.g., a board filled with 'O's in a snake-like pattern).

### 2. Correctness
The logic is correct: identifying boundary-connected 'O's ensures only internal 'O's are flipped. 
**Edge Case Risk:** The `sys.setrecursionlimit(2000)` is dangerous. LeetCode constraints are often $200 \times 200$; a single path could reach a depth of $40,000$. This code will crash with a `RecursionError` on large, complex inputs.

### 3. Optimization
**Use BFS or Iterative DFS:** Replace the recursive function with a `collections.deque` (BFS) or a manual stack (Iterative DFS). This eliminates the dependency on the recursion limit and prevents stack overflow errors while maintaining the same time complexity.

### 4. Key Algorithmic Pattern
**Flood Fill (from boundaries):** Instead of identifying surrounded regions directly, the algorithm uses "reverse thinking" to mark reachable (non-surrounded) regions starting from the edges.
