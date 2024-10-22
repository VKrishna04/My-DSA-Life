# Two Sum

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-two-sum` |
| Topics | Array, Hash Table |
| Solved | 2024-10-22 |
| Solve Time | 36m 36s |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

You are given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

 

**Example 1:**

**Input:** `nums = [2,7,11,15], target = 9`

**Output:** `[0,1]`

**Explanation:**

The sum of `nums[0]` and `nums[1]` is `2 + 7 = 9`, which equals the target. Therefore, the indices `[0, 1]` are returned.

**Example 2:**

**Input:** `nums = [3,2,4], target = 6`

**Output:** `[1,2]`

**Explanation:**

The sum of `nums[1]` and `nums[2]` is `2 + 4 = 6`, which equals the target. Therefore, the indices `[1, 2]` are returned.

**Example 3:**

**Input:** `nums = [3,3], target = 6`

**Output:** `[0,1]`

**Explanation:**

The sum of `nums[0]` and `nums[1]` is `3 + 3 = 6`, which equals the target. Therefore, the indices `[0, 1]` are returned.

 

**Constraints:**

	- `2 <= nums.length <= 104`

	- `-109 <= nums[i] <= 109`

	- `-109 <= target <= 109`

	- **Only one valid answer exists.**

 

**Follow-up: **Can you come up with an algorithm that is less than `O(n2)` time complexity?

## Solutions

```Python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
```
