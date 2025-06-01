# Power of Three

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-three::1650980140` |
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

```Python3
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            # print(n)
            n /= 3
        # print(n)
        if n != 1:
            return False
        return True
```
