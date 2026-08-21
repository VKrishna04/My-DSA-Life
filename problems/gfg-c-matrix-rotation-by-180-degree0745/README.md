# C Matrix Rotation By 180 Degree

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-c-matrix-rotation-by-180-degree0745` |
| Topics | Math, Matrix, Array |
| Solved | 2026-06-24 |

## Problem Statement

Given a 2D square matrix **mat**[][] of size **n x n**, rotate it by **180** **degrees** without using extra space.

**Note:** You must rotate the matrix** in place **and modify the input matrix directly.

**Examples:**

**Input: **mat[][] =** **[[1, 2],
                [3, 4]]
**Output: **[[4, 3], 
        [2, 1]]
**Input: ** mat[][] = [[1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9]]
**Output: **[[9, 8, 7], 
        [6, 5, 4], 
        [3, 2, 1]]

**Constraints:**
1 &le; n &le; 500
0 &le; mat[i][j] &le; 104

## Solutions

```python3
class Solution:
    def rotateMatrix(self, mat):
        mat[:] = mat[::-1]

        for row in mat:
            row[:] = row[::-1]

        return mat
        
```

## AI Review

1. **Complexity**:
* **Time**: $O(N \times M)$ where $N$ is rows and $M$ is columns. Every element is visited twice.
* **Space**: $O(N + M)$ auxiliary space. Although you are using slice assignment (`mat[:] = ...`), the expression `mat[::-1]` and `row[::-1]` creates a temporary shallow copy of the list before the assignment.

2. **Correctness**:
The logic is sound. Rotating $180^\circ$ is mathematically equivalent to a vertical flip (reverse rows) followed by a horizontal flip (reverse elements within rows). It handles rectangular matrices and empty inputs correctly.

3. **Optimization**:
To achieve true **$O(1)$ auxiliary space** (addressing your recurring space complexity flag), avoid slicing. Instead, use a single loop to swap elements from the start and end of the matrix:
```python3
total = rows * cols
for i in range(total // 2):
    r1, c1 = divmod(i, cols)
    r2, c2 = divmod(total - 1 - i, cols)
    mat[r1][c1], mat[r2][c2] = mat[r2][c2], mat[r1][c1]
```

4. **Key Algorithmic Pattern**:
**Matrix Transformation** via Row/Column reversal.
