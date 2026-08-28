# Binary Search

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-binary-search` |
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

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(\log n)$. The search space is halved in each iteration.
*   **Space Complexity:** $O(1)$. It uses a constant amount of extra memory regardless of input size.

### 2. Correctness
The implementation is correct and robust. 
*   **Empty list:** If `nums` is empty, `right` becomes `-1`, the `while` condition fails immediately, and it correctly returns `-1`.
*   **Single element:** If `nums` has one element, `left` and `right` both equal `0`, the loop runs once, and it correctly identifies or misses the target.
*   **Boundary targets:** It correctly finds the target if it is at the very first or very last index due to the `left <= right` condition.

### 3. Optimization
While this iterative approach is already optimal, you could use Python’s built-in **`bisect` module** (`bisect.bisect_left`) for a more concise and potentially faster solution (as it is implemented in C). 

### 4. Key Algorithmic Pattern
**Binary Search** (a specific type of **Decrease and Conquer**). It relies on the input being sorted to eliminate half of the remaining elements at each step.
