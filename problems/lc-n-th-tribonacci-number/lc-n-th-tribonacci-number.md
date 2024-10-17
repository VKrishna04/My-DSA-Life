# N-th Tribonacci Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-n-th-tribonacci-number` |
| Topics | Math, Dynamic Programming, Memoization |
| Solved | 2024-10-17 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.7 MB (beats 100%) |

## Problem Statement

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given `n`, return the value of Tn.

 

**Example 1:**

**Input:** n = 4
**Output:** 4
**Explanation:**
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

**Example 2:**

**Input:** n = 25
**Output:** 1389537

 

**Constraints:**

	- `0 <= n <= 37`

	- The answer is guaranteed to fit within a 32-bit integer, ie. `answer <= 2^31 - 1`.

## Solutions

```Python3
class Solution:
    def tribonacci(self, n: int, memo={}) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = self.tribonacci(n - 1, memo) + self.tribonacci(n - 2, memo) + self.tribonacci(n-3, memo)

        return memo[n]
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(n)$ — Each value from $0$ to $n$ is calculated once.
*   **Space:** $O(n)$ — Required for the recursion stack and the `memo` dictionary.

**2. Correctness & Edge Cases**
*   **Persistent Mutable Default:** Using `memo={}` as a default argument is a "Python gotcha." The dictionary persists across different calls to `tribonacci`, which can lead to unexpected behavior in a long-running process (though it often speeds up LeetCode tests).
*   **Recursion Limit:** For very large $n$, this would hit Python's recursion limit, but since the problem limits $n \le 37$, it functions correctly.
*   **Base Cases:** Correctly handles $n=0, 1, 2$.

**3. Optimization**
**Iterative Bottom-Up (Space Optimization):**
You can reduce space from $O(n)$ to $O(1)$ by using three variables to track only the last three values, eliminating the dictionary and recursion stack.
```python
a, b, c = 0, 1, 1
for _ in range(n):
    a, b, c = b, c, a + b + c
return a
```

**4. Key Algorithmic Pattern**
**Dynamic Programming** (Top-down approach with Memoization).
