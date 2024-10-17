# Climbing Stairs

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-climbing-stairs` |
| Topics | Math, Dynamic Programming, Memoization |
| Solved | 2024-10-17 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.8 MB (beats 100%) |

## Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

 

**Example 1:**

**Input:** n = 2
**Output:** 2
**Explanation:** There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

**Example 2:**

**Input:** n = 3
**Output:** 3
**Explanation:** There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 

**Constraints:**

	- `1 <= n <= 45`

## Solutions

```Python3
class Solution:
    def climbStairs(self, n, memo={}):
        if n <= 1:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

        return memo[n]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$. Each value from $1$ to $n$ is computed and stored exactly once.
*   **Space Complexity:** $O(n)$. This accounts for both the recursion stack depth and the `memo` dictionary.

### 2. Correctness & Edge Cases
*   **Critical Bug:** The use of a **mutable default argument** (`memo={}`) is a major Python anti-pattern. The dictionary persists across different test cases/calls to `climbStairs`. While this might pass on LeetCode, it causes data leakage and potential side effects in production environments.
*   **Edge Cases:** Handles $n=1$ correctly. For $n=0$, it returns $1$, which is standard for combinatorial problems (one way to stay at the start).

### 3. Optimization
**Iterative Bottom-Up (Space Optimization):**
Instead of recursion, use two variables to track the previous two steps. This reduces space complexity from **$O(n)$ to $O(1)$**.
```python
a, b = 1, 1
for _ in range(n):
    a, b = b, a + b
return a
```

### 4. Key Algorithmic Pattern
**Dynamic Programming (Top-down with Memoization).** The problem is mathematically equivalent to generating the **Fibonacci sequence**.
