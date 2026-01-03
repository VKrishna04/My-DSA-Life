# Intersection of Two Arrays

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-intersection-of-two-arrays::1873478355` |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Solved | 2026-01-03 |
| Runtime | 1 ms (beats 38.4239%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return _an array of their intersection_. Each element in the result must be **unique** and you may return the result in **any order**.

 

**Example 1:**

**Input:** nums1 = [1,2,2,1], nums2 = [2,2]
**Output:** [2]

**Example 2:**

**Input:** nums1 = [4,9,5], nums2 = [9,4,9,8,4]
**Output:** [9,4]
**Explanation:** [4,9] is also accepted.

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 1000`

	- `0 <= nums1[i], nums2[i] <= 1000`

## Solutions

```Python3
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for n in nums1:
            if n not in d:
                d[n] = True
        out = []
        for n in nums2:
            if n in d and d[n]:
                d[n] = False
                out.append(n)
        return out
```
