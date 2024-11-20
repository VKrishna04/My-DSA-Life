# Power of Two

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-two` |
| Topics | Math, Bit Manipulation, Recursion |
| Solved | 2025-06-01 |
| Runtime | 4 ms (beats 5.668899999999994%) |
| Memory | 17.8 MB (beats 100%) |

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

### Alt approach (Python3) — imported

Submission #1650968743

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

**1. Complexity**
*   **Time:** $O(\log n)$ — converting an integer to a binary string and iterating through its bits requires logarithmic time relative to the value of $n$.
*   **Space:** $O(\log n)$ — the string representation of the binary number is stored in memory.

**2. Correctness**
The logic is **correct**. It correctly identifies that a power of two in binary starts with '1' followed exclusively by '0's.
*   **Edge cases:** 
    *   `n = 0`: Returns `False` (Correct).
    *   `n < 0`: `bin(-2)` is `'-0b10'`; the slice `[2:]` results in `'b10'`. Since `'b' != '1'`, it returns `False` (Correct).

**3. Optimization**
Use bitwise operators to achieve **$O(1)$ time and space** without string conversion:
```python
return n > 0 and (n & (n - 1)) == 0
```
This works because a power of two (e.g., `1000`) and its predecessor (e.g., `0111`) share no common set bits, so their bitwise AND is always zero.

**4. Key Algorithmic Pattern**
**Bit Manipulation** (specifically checking the Hamming weight or bit properties of an integer).
