# Pascal's Triangle

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-pascals-triangle` |
| Topics | Array, Dynamic Programming |
| Solved | 2025-06-01 |
| Runtime | 0 ms (beats 100%) |
| Memory | 18 MB (beats 100%) |

## Problem Statement

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

 

**Example 1:**

**Input:** numRows = 5
**Output:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
**Example 2:**

**Input:** numRows = 1
**Output:** [[1]]

 

**Constraints:**

	- `1 <= numRows <= 30`

## Solutions

```Python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # new = [[0], [1], [0]]
        
        # for i in range(numRows):
        #     new.append(list(new[i-1] + new[i]) for i in range(len(new)))
        
        
        if numRows == 1:
            return [[1]]
        
        prev = self.generate(numRows-1)
        pre = prev[-1]
        cur = [1]

        for i in range(1, numRows-1):
            cur.append(pre[i-1] + pre[i])
        
        cur.append(1)
        prev.append(cur)

        return prev


        return ans


```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n^2)$, where $n$ is `numRows`. Each element in the triangle is calculated exactly once through a simple addition.
*   **Space Complexity:** $O(n^2)$ to store the output. The recursion stack adds $O(n)$ auxiliary space.

### 2. Correctness
*   **Edge Cases:** The code fails for `numRows = 0` (resulting in infinite recursion/`RecursionError`), although LeetCode constraints typically specify $n \ge 1$.
*   **Logic:** The logic is sound for $n \ge 1$. It correctly builds the current row using the previous row's values.

### 3. Optimization
**Iterative Approach:** Replace recursion with a nested loop. This eliminates the $O(n)$ recursion stack overhead and prevents potential stack overflow for large inputs.
```python
res = [[1]]
for i in range(1, numRows):
    row = [1]
    for j in range(1, i):
        row.append(res[-1][j-1] + res[-1][j])
    row.append(1)
    res.append(row)
```

### 4. Key Algorithmic Pattern
**Dynamic Programming:** Specifically, this uses the **Tabulation** logic (even though implemented recursively), where the solution to a subproblem (row $i$) is used to construct the solution for the next state (row $i+1$).
