# Search in Rotated Sorted Array

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-search-in-rotated-sorted-array` |
| Topics | Array, Binary Search |
| Solved | 2025-12-31 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.3 MB (beats 100%) |

## Problem Statement

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return _the index of _`target`_ if it is in _`nums`_, or _`-1`_ if it is not in _`nums`.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Example 1:**

**Input:** nums = [4,5,6,7,0,1,2], target = 0
**Output:** 4
**Example 2:**

**Input:** nums = [4,5,6,7,0,1,2], target = 3
**Output:** -1
**Example 3:**

**Input:** nums = [1], target = 0
**Output:** -1

 

**Constraints:**

	- `1 <= nums.length <= 5000`

	- `-104 <= nums[i] <= 104`

	- All values of `nums` are **unique**.

	- `nums` is an ascending array that is possibly rotated.

	- `-104 <= target <= 104`

## Solutions

```Python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1
```

## AI Review

### Analysis

1.  **Complexity**:
    *   **Time**: $O(n)$ — The algorithm performs a linear scan through the array.
    *   **Space**: $O(1)$ — Only a single loop index is stored.

2.  **Correctness**: 
    The logic is correct and will find the target if it exists. It handles edge cases like empty arrays or the target being at the rotation pivot. However, it fails the problem's specific requirement for an $O(\log n)$ runtime.

3.  **Optimization**: 
    Use **Binary Search** to achieve $O(\log n)$. In each step, determine which half is "sorted" by comparing `nums[low]` and `nums[mid]`. 
    *   If `nums[low] <= nums[mid]`, the left side is sorted. Check if the target is within that range to decide which half to discard.
    *   Otherwise, the right side must be sorted.
    This exploits the property that at least one half of a rotated sorted array is always strictly increasing.

4.  **Key Algorithmic Pattern**: 
    **Modified Binary Search**. This pattern is essential for searching in $O(\log n)$ when the standard sorted property is partially disrupted (like rotation).
