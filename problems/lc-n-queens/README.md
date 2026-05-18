# N-Queens

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-n-queens` |
| Topics | Array, Backtracking |
| Solved | 2026-05-03 |
| Runtime | 10 ms (beats 73.5604%) |
| Memory | 19.8 MB (beats 33.8637%) |

## Problem Statement

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

 

**Example 1:**

**Input:** n = 4
**Output:** [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
**Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above

**Example 2:**

**Input:** n = 1
**Output:** [["Q"]]

 

**Constraints:**

	- `1 <= n <= 9`

## Solutions

```Python3
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtract(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtract(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        backtract(0)
        return res
```

## AI Review

### Review

1.  **Complexity**:
    *   **Time**: $O(N!)$ — While the first row has $N$ choices, subsequent rows have fewer due to pruning. The number of solutions is bounded by $N!$.
    *   **Space**: $O(N^2)$ — To store the board state and the recursion stack ($O(N)$). The output storage size depends on the number of valid solutions.

2.  **Correctness**:
    *   **Correct**. The logic using $r+c$ for positive diagonals and $r-c$ for negative diagonals accurately identifies all squares on the same diagonal. It handles $N=1$ and cases with no solutions ($N=2, 3$) correctly.

3.  **Optimization**:
    *   **Bitmasking**: Replace the three `set()` objects with three integers. Use bitwise `OR` to mark positions and `AND` to check constraints. This significantly reduces constant-time overhead and memory usage by avoiding hash set lookups.
    *   *Minor*: Instead of a full board of characters, store only the column indices in an array to save space during recursion, constructing the string representation only when a solution is found.

4.  **Key Algorithmic Pattern**:
    *   **Backtracking** with state-based pruning (Constraint Satisfaction Problem).
