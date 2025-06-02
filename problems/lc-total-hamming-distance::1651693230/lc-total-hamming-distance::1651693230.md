# Total Hamming Distance

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-total-hamming-distance::1651693230` |
| Topics | Array, Math, Bit Manipulation |
| Solved | 2025-06-02 |
| Runtime | 114 ms (beats 91.95130000000006%) |
| Memory | 20.1 MB (beats 100%) |

## Problem Statement

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array `nums`, return _the sum of **Hamming distances** between all the pairs of the integers in_ `nums`.

 

**Example 1:**

**Input:** nums = [4,14,2]
**Output:** 6
**Explanation:** In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

**Example 2:**

**Input:** nums = [4,14,4]
**Output:** 4

 

**Constraints:**

	- `1 <= nums.length <= 104`

	- `0 <= nums[i] <= 109`

	- The answer for the given input will fit in a **32-bit** integer.

## Solutions

```Python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return  sum(i.count('1') * i.count('0') for i in zip(*map('{:032b}'.format,nums)))

```
