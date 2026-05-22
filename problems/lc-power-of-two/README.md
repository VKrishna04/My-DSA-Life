# Power of Two

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-two` |
| Topics | Math, Bit Manipulation, Recursion |
| Solved | 2025-06-01 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.7 MB (beats 100%) |

## Problem Statement

Given an integer `n`, return _`true` if it is a power of two. Otherwise, return `false`_.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

 

**Example 1:**

**Input:** n = 1
**Output:** true
**Explanation: **20 = 1

**Example 2:**

**Input:** n = 16
**Output:** true
**Explanation: **24 = 16

**Example 3:**

**Input:** n = 3
**Output:** false

 

**Constraints:**

	- `-231 <= n <= 231 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## Solutions

```Python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n = str(bin(n))[2:]
        # print(n)
    
        # if n[0] != '1':
        #     return False
        
        # for i in range(1,len(n)):
        #     if n[i] != '0':
        #         return False
        # return True

        return n > 0 and str(bin(n)).count('1') == 1
```

## AI Review

### Review of "Power of Two" Solution

**1. Complexity**
*   **Time:** $O(\log n)$. Converting an integer to a binary string and counting characters both scale with the number of bits in $n$.
*   **Space:** $O(\log n)$. The `bin(n)` function creates a new string proportional to the number of bits.

**2. Correctness**
*   The logic is **correct**. It successfully handles $n \le 0$ via the `n > 0` check and correctly identifies that powers of two have exactly one set bit in binary. 
*   **Minor Note:** `str(bin(n))` is redundant; `bin(n)` already returns a string.

**3. Optimization**
Use bitwise manipulation to achieve **$O(1)$ time and space**. A power of two has exactly one bit set. Subtracting 1 flips that bit and all bits to its right. Therefore, `n & (n - 1)` will equal `0`.
*   **Optimized Code:** `return n > 0 and (n & (n - 1)) == 0`

**4. Key Algorithmic Pattern**
**Bit Manipulation.** This problem relies on understanding the binary structure of integers, specifically how powers of two relate to bit counts and bitwise transitions.
