# Find Greatest Common Divisor of Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-greatest-common-divisor-of-array::1967589570` |
| Topics | Array, Math, Number Theory |
| Solved | 2026-04-03 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 80.2024%) |

## Problem Statement

Given an integer array `nums`, return** **_the **greatest common divisor** of the smallest number and largest number in _`nums`.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

 

**Example 1:**

**Input:** nums = [2,5,6,9,10]
**Output:** 2
**Explanation:**
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

**Example 2:**

**Input:** nums = [7,5,6,8,3]
**Output:** 1
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

**Example 3:**

**Input:** nums = [3,3]
**Output:** 3
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

 

**Constraints:**

	- `2 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`

## Solutions

```Python3
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min(nums)
        l = max(nums)

        while (l != 0):
            s, l = l, s % l
        return s

        # Using built in functions
        # from math import gcd
        # return gcd(min(nums), max(nums))

```
