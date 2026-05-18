# Search Insert Position

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-search-insert-position` |
| Topics | Array, Binary Search |
| Solved | 2024-10-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.3 MB (beats 100%) |

## Problem Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Example 1:**

**Input:** nums = [1,3,5,6], target = 5
**Output:** 2

**Example 2:**

**Input:** nums = [1,3,5,6], target = 2
**Output:** 1

**Example 3:**

**Input:** nums = [1,3,5,6], target = 7
**Output:** 4

 

**Constraints:**

	- `1 <= nums.length <= 104`

	- `-104 <= nums[i] <= 104`

	- `nums` contains **distinct** values sorted in **ascending** order.

	- `-104 <= target <= 104`

## Solutions

```Python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

```

## AI Review

1. **Complexity**:
* **Time**: $O(\log n)$ — Binary search reduces the search space by half each iteration.
* **Space**: $O(1)$ — Only constant extra space is used for pointers.

2. **Correctness**:
The logic is correct and robust. It handles all edge cases:
* **Target exists**: Returns the correct index via the `nums[mid] == target` check.
* **Target missing**: The loop terminates with `left` pointing to the first element greater than the target, which is the correct insertion index.
* **Target outside bounds**: Returns `0` if smaller than all elements and `len(nums)` if larger.
* **Duplicates**: While the problem typically specifies distinct values, this logic returns the leftmost insertion point (the index of the first occurrence).

3. **Optimization**:
While the logic is optimal, you can use Python’s built-in `bisect` module for a cleaner, C-optimized implementation:
```python
import bisect
return bisect.bisect_left(nums, target)
```
In other languages, use `mid = left + (right - left) // 2` to prevent potential integer overflow, though Python handles arbitrarily large integers automatically.

4. **Key Pattern**:
**Binary Search** (specifically, finding the lower bound/insertion point in a sorted sequence).
