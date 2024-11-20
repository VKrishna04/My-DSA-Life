# Power of Three

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-three` |
| Topics | Math, Recursion |
| Solved | 2025-06-01 |
| Runtime | 20 ms (beats 14.0719%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

Given an integer `n`, return _`true` if it is a power of three. Otherwise, return `false`_.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.

 

**Example 1:**

**Input:** n = 27
**Output:** true
**Explanation:** 27 = 33

**Example 2:**

**Input:** n = 0
**Output:** false
**Explanation:** There is no x where 3x = 0.

**Example 3:**

**Input:** n = -1
**Output:** false
**Explanation:** There is no x where 3x = (-1).

 

**Constraints:**

	- `-231 <= n <= 231 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## Solutions

### Alt approach (Python3) — imported

Submission #1650981852

```Python3
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # while n >= 3:
        #     # print(n)
        #     n /= 3
        # # print(n)
        # if n != 1:
        #     return False
        # return True

        return n>0 and 3**19%n==0
```

## AI Review

**1. Complexity**
*   **Time:** $O(\log_3 n)$ — The input $n$ is divided by 3 in each iteration.
*   **Space:** $O(1)$ — Only a constant amount of extra space is used.

**2. Correctness**
*   **Edge Cases:** Handles $n \le 0$ and $n = 1$ correctly.
*   **Precision Risk:** Using float division (`n /= 3`) is dangerous for very large integers due to potential floating-point precision errors. It is safer to use integer division (`n //= 3`) and the modulo operator (`n % 3 == 0`).
*   **Efficiency:** The current loop continues even if $n$ is clearly not a power of three (e.g., $n=10$), only stopping when $n < 3$.

**3. Optimisation**
Since 3 is a prime number, the largest power of 3 that fits in a 32-bit signed integer is $3^{19} = 1,162,261,467$. You can achieve **$O(1)$ time** complexity by checking if this maximum value is divisible by $n$:
```python
return n > 0 and 1162261467 % n == 0
```

**4. Key Algorithmic Pattern**
**Iterative Reduction** (specifically, repeated division to reach a base case).
