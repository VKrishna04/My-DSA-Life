# Minimum Cost Tree From Leaf Values

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-cost-tree-from-leaf-values` |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Solved | 2026-04-28 |
| Runtime | 119 ms (beats 14.4144%) |
| Memory | 19.5 MB (beats 31.831899999999997%) |

## Problem Statement

Given an array `arr` of positive integers, consider all binary trees such that:

	- Each node has either `0` or `2` children;

	- The values of `arr` correspond to the values of each **leaf** in an in-order traversal of the tree.

	- The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.

Among all possible binary trees considered, return _the smallest possible sum of the values of each non-leaf node_. It is guaranteed this sum fits into a **32-bit** integer.

A node is a **leaf** if and only if it has zero children.

 

**Example 1:**

**Input:** arr = [6,2,4]
**Output:** 32
**Explanation:** There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

**Example 2:**

**Input:** arr = [4,11]
**Output:** 44

 

**Constraints:**

	- `2 <= arr.length <= 40`

	- `1 <= arr[i] <= 15`

	- It is guaranteed that the answer fits into a **32-bit** signed integer (i.e., it is less than 231).

## Solutions

```Python3
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[float('inf')]*len(arr) for _ in range(len(arr))]

        for i in range(len(arr)):
            dp[i][i] = 0
        
        for i in range(len(arr)-1, -1, -1):

            for j in range(i+1, len(arr)):

                for k in range(i, j):
                    rcost = max(arr[i:k+1]) * max(arr[k+1:j+1])
                    tcost = rcost + dp[i][k] + dp[k+1][j]
                    dp[i][j] = min(dp[i][j], tcost)
        return dp[0][-1]
```

## AI Review

1. **Complexity**: 
   - **Time**: $O(n^4)$. The triple-nested loops contribute $O(n^3)$, and the `max(arr[i:k+1])` slicing/searching adds an $O(n)$ factor inside the innermost loop.
   - **Space**: $O(n^2)$ to store the `dp` table.

2. **Correctness**: 
   The logic is correct and follows the optimal subtree property. It correctly handles the base case (`dp[i][i] = 0`). No specific edge cases fail, though it is inefficient for large $n$.

3. **Optimization**: 
   Precompute the maximum leaf values for every range `[i, j]` into a 2D array in $O(n^2)$ time before the main loops. Replacing the inner `max()` calls with this lookup reduces the time complexity to **$O(n^3)$**.
   *(Note: The most optimal solution uses a **Monotonic Stack** to achieve $O(n)$ time.)*

4. **Key Algorithmic Pattern**: 
   **Interval Dynamic Programming** (specifically the Matrix Chain Multiplication pattern). It builds the solution by calculating the minimum cost for increasingly larger subarrays (intervals).
