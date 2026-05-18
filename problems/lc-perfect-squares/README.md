# Perfect Squares

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-perfect-squares` |
| Topics | Math, Breadth-First Search, Dynamic Programming |
| Solved | 2026-04-11 |
| Runtime | 1285 ms (beats 81.11419999999951%) |
| Memory | 19.5 MB (beats 46.54509999999999%) |

## Problem Statement

Given an integer `n`, return _the least number of perfect square numbers that sum to_ `n`.

A **perfect square** is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, `1`, `4`, `9`, and `16` are perfect squares while `3` and `11` are not.

 

**Example 1:**

**Input:** n = 12
**Output:** 3
**Explanation:** 12 = 4 + 4 + 4.

**Example 2:**

**Input:** n = 13
**Output:** 2
**Explanation:** 13 = 4 + 9.

 

**Constraints:**

	- `1 <= n <= 104`

## Solutions

```Python3
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        count = 1

        while count ** 2 <= n:
            sq = count ** 2
            for i in range(sq, n + 1):
                dp[i] = min(dp[i - sq] + 1, dp[i])
            count += 1
        return dp[n]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n\sqrt{n})$. The outer loop runs $\sqrt{n}$ times (number of perfect squares $\le n$), and the inner loop iterates up to $n$ times.
*   **Space Complexity:** $O(n)$ to store the `dp` array.

### 2. Correctness
The logic is **correct**. It follows the "Unbounded Knapsack" or "Change-making" pattern. It correctly handles the base case $n=0$ and builds up to $n$. There are no obvious edge cases that would fail within standard integer constraints.

### 3. Concrete Optimization
**Static Memoization:** In a LeetCode environment where the `numSquares` method is called across multiple test cases, you can move the `dp` table to a class-level variable. This prevents re-calculating results for values of $n$ already processed in previous test cases.

```python
class Solution:
    _dp = [0]
    def numSquares(self, n: int) -> int:
        dp = self._dp
        while len(dp) <= n:
            m = len(dp)
            res = float('inf')
            i = 1
            while i * i <= m:
                res = min(res, dp[m - i * i] + 1)
                i += 1
            dp.append(res)
        return dp[n]
```

### 4. Key Algorithmic Pattern
**Dynamic Programming (Bottom-Up)**; specifically, the **Unbounded Knapsack** variation.
