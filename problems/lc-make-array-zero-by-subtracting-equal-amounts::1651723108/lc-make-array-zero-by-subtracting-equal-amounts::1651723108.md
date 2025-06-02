# Make Array Zero by Subtracting Equal Amounts

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-make-array-zero-by-subtracting-equal-amounts::1651723108` |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Simulation |
| Solved | 2025-06-02 |
| Runtime | 3 ms (beats 21.767000000000003%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

You are given a non-negative integer array `nums`. In one operation, you must:

	- Choose a positive integer `x` such that `x` is less than or equal to the **smallest non-zero** element in `nums`.

	- Subtract `x` from every **positive** element in `nums`.

Return _the **minimum** number of operations to make every element in _`nums`_ equal to _`0`.

 

**Example 1:**

**Input:** nums = [1,5,0,3,5]
**Output:** 3
**Explanation:**
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

**Example 2:**

**Input:** nums = [0]
**Output:** 0
**Explanation:** Each element in nums is already 0 so no operations are needed.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`

## Solutions

```Python3
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        try:
            nums.remove(0)
        finally:
            return len(nums)

```
