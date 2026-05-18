# Triangle

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-triangle` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-04-19 |
| Runtime | 0 ms (beats 100%) |
| Memory | 20.2 MB (beats 43.90360000000001%) |

## Problem Statement

Given a `triangle` array, return _the minimum path sum from top to bottom_.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

 

**Example 1:**

**Input:** triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
**Output:** 11
**Explanation:** The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

**Example 2:**

**Input:** triangle = [[-10]]
**Output:** -10

 

**Constraints:**

	- `1 <= triangle.length <= 200`

	- `triangle[0].length == 1`

	- `triangle[i].length == triangle[i - 1].length + 1`

	- `-104 <= triangle[i][j] <= 104`

 

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?

## Solutions

```Python3
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]

        for row in range(len(triangle)-2,-1,-1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col+1])
        return dp[0]
```

## AI Review

### 1. Complexity
*   **Time:** $O(N^2)$, where $N$ is the number of rows. You visit every element in the triangle exactly once.
*   **Space:** $O(N)$ to store the `dp` array (the size of the bottom row).

### 2. Correctness
The solution is **correct**. It correctly implements the bottom-up DP approach, starting from the second-to-last row and moving upwards.
*   **Edge Cases:** It handles single-row triangles correctly (the loops don't execute, and it returns the first element) and handles negative numbers correctly via the `min()` function.

### 3. Concrete Optimization
**In-place Modification:** If you are allowed to mutate the input, you can eliminate the $O(N)$ extra space by modifying the `triangle` list directly. 
```python
for row in range(len(triangle) - 2, -1, -1):
    for col in range(len(triangle[row])):
        triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
return triangle[0][0]
```
This reduces auxiliary space to **$O(1)$**.

### 4. Key Algorithmic Pattern
**Dynamic Programming (Bottom-Up):** It breaks the problem into subproblems (minimum path from current cell to bottom) and uses previous results to compute the current state.
