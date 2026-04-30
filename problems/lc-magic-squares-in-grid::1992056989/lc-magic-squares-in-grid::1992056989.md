# Magic Squares In Grid

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-magic-squares-in-grid::1992056989` |
| Topics | Array, Math, Hash Table, Matrix |
| Solved | 2026-04-30 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 83.38610000000001%) |

## Problem Statement

A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers **from **1** to **9 such that each row, column, and both diagonals all have the same sum.

Given a `row x col` `grid` of integers, how many `3 x 3` magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, `grid` may contain numbers up to 15.

 

**Example 1:**

**Input:** grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
**Output:** 1
**Explanation: **
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.

**Example 2:**

**Input:** grid = [[8]]
**Output:** 0

 

**Constraints:**

	- `row == grid.length`

	- `col == grid[i].length`

	- `1 <= row, col <= 10`

	- `0 <= grid[i][j] <= 15`

## Solutions

```Python3
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            print("0")
        def is_magic(mag):
            flatmag = [item for row in mag for item in row]
            flatmag = [item for item in flatmag if 1 <= item <= 9]
            if len(flatmag) != 9 or set(flatmag) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
            return (sum(mag[0]) == sum(mag[1]) == sum(mag[2]) == 
                    sum(mag[i][0] for i in range(3)) == 
                    sum(mag[i][1] for i in range(3)) == 
                    sum(mag[i][2] for i in range(3)) == 
                    mag[0][0] + mag[1][1] + mag[2][2] == 
                    mag[0][2] + mag[1][1] + mag[2][0])
        
        rowlen = len(grid)
        collen = len(grid[0])
        magic_count = 0
        
        for row in range(rowlen - 2):
            for col in range(collen - 2):
                mag = [grid[row+i][col:col+3] for i in range(3)]
                if is_magic(mag):
                    magic_count += 1
        
        return magic_count
```

## AI Review

**1. Complexity**
*   **Time:** $O(R \times C)$, where $R$ and $C$ are grid dimensions. We iterate over $(R-2) \times (C-2)$ subgrids, performing constant-time ($3 \times 3$) checks for each.
*   **Space:** $O(1)$. While a 3x3 subgrid is extracted, its size is constant and does not scale with input size.

**2. Correctness**
*   **Small Grids:** If $R < 3$ or $C < 3$, the code correctly returns `0` (the `print` statement is redundant but harmless as the loops won't execute).
*   **Uniqueness:** The check `set(flatmag) == {1..9}` correctly ensures each digit 1-9 appears exactly once.
*   **Logic:** Valid. In a 3x3 grid of unique 1-9 digits, if all row/column/diagonal sums are equal, the sum must be 15.

**3. Concrete Optimization**
In any 3x3 magic square containing digits 1-9, the **center element must be 5**. Adding `if grid[row+1][col+1] != 5: continue` at the start of the inner loop avoids expensive subgrid extraction and sum calculations for most cases.

**4. Key Algorithmic Pattern**
**Sliding Window (2D) / Brute Force Search:** Iterating through all possible top-left corners of a fixed-size sub-matrix and validating local properties.
