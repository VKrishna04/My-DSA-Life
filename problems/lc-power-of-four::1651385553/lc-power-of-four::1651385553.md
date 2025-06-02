# Power of Four

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-four::1651385553` |
| Topics | Math, Bit Manipulation, Recursion |
| Solved | 2025-06-02 |
| Runtime | 2 ms (beats 17.511499999999998%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

Given an integer `n`, return _`true` if it is a power of four. Otherwise, return `false`_.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4x`.

 

**Example 1:**

**Input:** n = 16
**Output:** true
**Example 2:**

**Input:** n = 5
**Output:** false
**Example 3:**

**Input:** n = 1
**Output:** true

 

**Constraints:**

	- `-231 <= n <= 231 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## Solutions

```Python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       
        if n not in [4**i for i in range(int(math.log(2**31,4))+1)]:
            return False
        return True

        # return n>0 and (n & (n-1)==0) and (n % 3 == 1)
```
