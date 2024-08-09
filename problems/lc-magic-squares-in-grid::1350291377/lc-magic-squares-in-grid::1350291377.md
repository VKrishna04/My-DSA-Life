# Magic Squares In Grid

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-magic-squares-in-grid::1350291377` |
| Topics | Array, Math, Hash Table, Matrix |
| Solved | 2024-08-09 |
| Runtime | 45 ms (beats 6.493499999999996%) |
| Memory | 16.5 MB (beats 100%) |

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
*   **Time:** $O(R \times C)$, where $R$ and $C$ are grid dimensions. We iterate through each possible $3 \times 3$ subgrid exactly once, performing constant-time operations inside.
*   **Space:** $O(1)$. Although subgrids are copied, they are of fixed size ($3 \times 3$), requiring constant auxiliary space.

**2. Correctness**
The logic is correct. It properly validates the range $[1, 9]$, uniqueness, and all 8 sum properties.
*   **Edge Case:** If the grid is smaller than $3 \times 3$, the code returns `magic_count` (0), which is correct. However, the `print("0")` statement is unnecessary and doesn't stop execution (though the loops naturally won't run).

**3. Concrete Optimization**
**Center Property:** In any $3 \times 3$ magic square of numbers 1–9, the center element **must** be 5. You can skip the entire validation if `grid[row+1][col+1] != 5`. Additionally, since the magic sum must be 15, you can replace the chained equality with `== 15` for slight efficiency.

**4. Key Algorithmic Pattern**
**Sliding Window / Brute Force:** It uses a fixed-size ($3 \times 3$) sliding window to check every possible subgrid.
