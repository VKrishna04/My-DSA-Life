# Hamming Distance

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-hamming-distance::1651663412` |
| Topics | Bit Manipulation |
| Solved | 2025-06-02 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, return _the **Hamming distance** between them_.

 

**Example 1:**

**Input:** x = 1, y = 4
**Output:** 2
**Explanation:**
1   (0 0 0 1)
4   (0 1 0 0)
       &uarr;   &uarr;
The above arrows point to positions where the corresponding bits are different.

**Example 2:**

**Input:** x = 3, y = 1
**Output:** 1

 

**Constraints:**

	- `0 <= x, y <= 231 - 1`

 

**Note:** This question is the same as  2220: Minimum Bit Flips to Convert Number.

## Solutions

```Python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y)[2:].count("1")

```
