# Power of Three

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-three` |
| Topics | Math, Recursion |
| Solved | 2025-06-01 |
| Runtime | 4 ms (beats 84.63830000000002%) |
| Memory | 17.8 MB (beats 100%) |

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

### 1. Complexity
*   **Time Complexity:** $O(1)$. The exponentiation and modulo operations take constant time for fixed-width integers.
*   **Space Complexity:** $O(1)$. No additional memory is allocated.

### 2. Correctness
The solution is **correct** for the range of a 32-bit signed integer. 
*   **Edge Cases:** $n \le 0$ is handled by `n > 0`.
*   **Logic:** Since 3 is a prime number, the only divisors of $3^{19}$ are $3^0, 3^1, \dots, 3^{19}$. $3^{19}$ ($1,162,261,467$) is the largest power of three that fits in a 32-bit signed integer. Therefore, any $n > 0$ that divides $3^{19}$ must be a power of three.

### 3. Optimization
Replace the expression `3**19` with the literal integer value `1162261467`. This avoids recalculating the power at runtime, though Python's interpreter may already optimize this.

```python
return n > 0 and 1162261467 % n == 0
```

### 4. Key Algorithmic Pattern
**Mathematical Property of Prime Bases:** Using the constraints of the data type (32-bit integer) and the properties of prime numbers to solve in constant time without iteration or recursion.
