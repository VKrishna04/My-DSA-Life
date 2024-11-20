# Search in Rotated Sorted Array II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-search-in-rotated-sorted-array-ii` |
| Topics | Array, Binary Search |
| Solved | 2025-12-31 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true`_ if _`target`_ is in _`nums`_, or _`false`_ if it is not in _`nums`_._

You must decrease the overall operation steps as much as possible.

 

**Example 1:**

**Input:** nums = [2,5,6,0,0,1,2], target = 0
**Output:** true
**Example 2:**

**Input:** nums = [2,5,6,0,0,1,2], target = 3
**Output:** false

 

**Constraints:**

	- `1 <= nums.length <= 5000`

	- `-104 <= nums[i] <= 104`

	- `nums` is guaranteed to be rotated at some pivot.

	- `-104 <= target <= 104`

 

**Follow up:** This problem is similar to Search in Rotated Sorted Array, but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

## Solutions

```Python3
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in nums:
            if i == target:
                return True
        return False


```

## AI Review

### Review of Python3 Solution

**1. Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of elements. The loop iterates through the list once.
*   **Space Complexity:** $O(1)$, as it uses no additional data structures.

**2. Correctness**
*   **Verdict:** Correct but inefficient.
*   **Edge Cases:** It handles all cases (empty lists, single elements, duplicates) because it checks every element. However, it fails to leverage the "sorted" property, which is the core challenge of the problem.

**3. Optimization**
Use **Modified Binary Search** to achieve an average time complexity of $O(\log N)$.
*   Check if `nums[mid] == target`.
*   If `nums[left] == nums[mid] == nums[right]`, increment `left` and decrement `right` (to handle duplicates).
*   Otherwise, determine which half is sorted:
    *   If `nums[left] <= nums[mid]`, the left half is sorted. Check if the target lies within it.
    *   Else, the right half is sorted. Check if the target lies within it.

**4. Key Algorithmic Pattern**
**Binary Search** on a rotated sorted property. Specifically, handling the worst-case $O(N)$ scenario introduced by duplicates.
