# Fibonacci Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-fibonacci-number` |
| Topics | Math, Dynamic Programming, Recursion, Memoization |
| Solved | 2024-10-17 |
| Runtime | 35 ms (beats 97.4643%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given `n`, calculate `F(n)`.

 

**Example 1:**

**Input:** n = 2
**Output:** 1
**Explanation:** F(2) = F(1) + F(0) = 1 + 0 = 1.

**Example 2:**

**Input:** n = 3
**Output:** 2
**Explanation:** F(3) = F(2) + F(1) = 1 + 1 = 2.

**Example 3:**

**Input:** n = 4
**Output:** 3
**Explanation:** F(4) = F(3) + F(2) = 2 + 1 = 3.

 

**Constraints:**

	- `0 <= n <= 30`

## Solutions

```Python3
class Solution:
    def fib(self, n: int, memo={}) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)

        return memo[n]
```

## AI Review

### 1. Complexity
*   **Time:** $O(n)$ — Each number from $0$ to $n$ is computed and stored once.
*   **Space:** $O(n)$ — Required for both the recursion stack and the `memo` dictionary.

### 2. Correctness
The logic is correct for $n \ge 0$. However, there is a **Python-specific flaw**:
*   **Mutable Default Argument:** Using `memo={}` is an anti-pattern. In Python, default arguments are evaluated once at definition time. The `memo` dictionary will persist across different calls to `fib()`, which can lead to memory bloat or unexpected side effects in shared environments.

### 3. Concrete Optimisation
Use an **iterative (bottom-up) approach** to reduce space complexity to **$O(1)$**. Instead of a dictionary or recursion, use two variables to track the previous two values:
```python
def fib(self, n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

### 4. Key Algorithmic Pattern
**Dynamic Programming (Top-down with Memoization).**
