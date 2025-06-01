# Power of Two

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-two::1650968743` |
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
