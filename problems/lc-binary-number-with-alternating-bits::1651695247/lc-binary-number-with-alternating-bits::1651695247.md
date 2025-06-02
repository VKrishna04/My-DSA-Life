# Binary Number with Alternating Bits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-binary-number-with-alternating-bits::1651695247` |
| Topics | Bit Manipulation |
| Solved | 2025-06-02 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

**Example 1:**

**Input:** n = 5
**Output:** true
**Explanation:** The binary representation of 5 is: 101

**Example 2:**

**Input:** n = 7
**Output:** false
**Explanation:** The binary representation of 7 is: 111.

**Example 3:**

**Input:** n = 11
**Output:** false
**Explanation:** The binary representation of 11 is: 1011.

 

**Constraints:**

	- `1 <= n <= 231 - 1`

## Solutions

```Python3
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x+1)) == 0
```
