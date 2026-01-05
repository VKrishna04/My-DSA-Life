# Binary Search

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-binary-search::1875796252` |
| Topics | Array, Binary Search |
| Solved | 2026-01-05 |
| Runtime | 0 ms (beats 100%) |
| Memory | 13.3 MB (beats 37.21339999999999%) |

## Problem Statement

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Example 1:**

**Input:** nums = [-1,0,3,5,9,12], target = 9
**Output:** 4
**Explanation:** 9 exists in nums and its index is 4

**Example 2:**

**Input:** nums = [-1,0,3,5,9,12], target = 2
**Output:** -1
**Explanation:** 2 does not exist in nums so return -1

 

**Constraints:**

	- `1 <= nums.length <= 104`

	- `-104 < nums[i], target < 104`

	- All the integers in `nums` are **unique**.

	- `nums` is sorted in ascending order.

## Solutions

```Python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left , right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
```
