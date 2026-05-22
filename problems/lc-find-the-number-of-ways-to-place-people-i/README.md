# Find the Number of Ways to Place People I

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-find-the-number-of-ways-to-place-people-i` |
| Topics | Array, Math, Geometry, Sorting, Enumeration |
| Solved | 2024-10-27 |
| Runtime | 15 ms (beats 64.7885%) |
| Memory | 16.6 MB (beats 100%) |

## Problem Statement

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D plane, where `points[i] = [xi, yi]`.

Count the number of pairs of points `(A, B)`, where

	- `A` is on the **upper left** side of `B`, and

	- there are no other points in the rectangle (or line) they make (**including the border**), except for the points `A` and `B`.

Return the count.

 

**Example 1:**

**Input:** points = [[1,1],[2,2],[3,3]]

**Output:** 0

**Explanation:**

There is no way to choose `A` and `B` such that `A` is on the upper left side of `B`.

**Example 2:**

**Input:** points = [[6,2],[4,4],[2,6]]

**Output:** 2

**Explanation:**

	- The left one is the pair `(points[1], points[0])`, where `points[1]` is on the upper left side of `points[0]` and the rectangle is empty.

	- The middle one is the pair `(points[2], points[1])`, same as the left one it is a valid pair.

	- The right one is the pair `(points[2], points[0])`, where `points[2]` is on the upper left side of `points[0]`, but `points[1]` is inside the rectangle so it's not a valid pair.

**Example 3:**

**Input:** points = [[3,1],[1,3],[1,1]]

**Output:** 2

**Explanation:**

	- The left one is the pair `(points[2], points[0])`, where `points[2]` is on the upper left side of `points[0]` and there are no other points on the line they form. Note that it is a valid state when the two points form a line.

	- The middle one is the pair `(points[1], points[2])`, it is a valid pair same as the left one.

	- The right one is the pair `(points[1], points[0])`, it is not a valid pair as `points[2]` is on the border of the rectangle.

 

**Constraints:**

	- `2 <= n <= 50`

	- `points[i].length == 2`

	- `0 <= points[i][0], points[i][1] <= 50`

	- All `points[i]` are distinct.

## Hints

<details>
<summary>Hint 1</summary>

We can enumerate all the upper-left and lower-right corners.

</details>

<details>
<summary>Hint 2</summary>

If the upper-left corner is `(x1, y1)` and lower-right corner is `(x2, y2)`, check that there is no point `(x, y)` such that `x1 <= x <= x2` and `y2 <= y <= y1`.

</details>

## Solutions

```Python3
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0],-x[1]))
        output = 0
        l = len(points)
        for i in range(l):
            start = points[i][0]
            end = float("-inf")
            for j in range(i+1,l):
                if points[j][1] > points[i][1]:
                    continue
                if points[j][1] > end:
                    end = points[j][1]
                    output += 1
        return output
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N^2)$, where $N$ is the number of points. Sorting takes $O(N \log N)$, and the nested loops iterate through all pairs once.
*   **Space Complexity:** $O(N)$ or $O(\log N)$ depending on the implementation of the sorting algorithm in Python.

### 2. Correctness
The solution is **correct**. Sorting by $x$ ascending and $y$ descending ensures that for any pair $(i, j)$ where $j > i$:
*   $x_i \le x_j$ is guaranteed.
*   The condition `points[j][1] <= points[i][1]` ensures $y_j$ is not above $y_i$.
*   Tracking the running maximum `end` ensures no point $k$ exists between $i$ and $j$ such that $y_j \le y_k \le y_i$.

### 3. Optimization
While $O(N^2)$ is optimal for this problem's constraints ($N=50$ for Part I, $N=1000$ for Part II), you can slightly improve performance by using `end = -1e10` (or a known minimum bound) to avoid the overhead of `float("-inf")`.

### 4. Key Algorithmic Pattern
**Sorting + Running Maximum:** By processing points in a specific sorted order, the 2D geometric constraint "no point inside the rectangle" is reduced to a 1D range check using a monotonic property.
