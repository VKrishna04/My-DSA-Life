# Binary Search

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-binary-search` |
| Topics | Array, Binary Search, Two Pointers |
| Solved | 2026-09-15 |
| Runtime | 0 ms (beats 100%) |
| Memory | 20.4 MB (beats 95.71430000000001%) |

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

```Python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

## AI Review

### Review

1. **Complexity:**
   * **Time Complexity:** $O(\log n)$ because the search space is halved in each step.
   * **Space Complexity:** $O(1)$ auxiliary space as it only uses a few variables.

2. **Correctness:** 
   The solution is fully correct. It handles all edge cases perfectly, including single-element arrays, empty arrays (if permitted by constraints), targets at the extreme boundaries, and missing elements. The search interval shrinks correctly without infinite loops.

3. **Optimization:**
   The code is already highly optimal. A minor Python-specific micro-optimization is to use `mid = (left + right) // 2`. Since Python dynamically manages arbitrarily large integers, integer overflow is not a concern, and this avoids one subtraction operation per iteration.

4. **Pattern:**
   Binary Search (Two Pointers).
