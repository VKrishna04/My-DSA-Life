# Count the Number of Fair Pairs

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-count-the-number-of-fair-pairs::1761545599` |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Solved | 2025-09-06 |
| Runtime | 267 ms (beats 50.544000000000096%) |
| Memory | 32.2 MB (beats 100%) |

## Problem Statement

Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and `upper`, return _the number of fair pairs_.

A pair `(i, j)` is **fair **if:

	- `0 <= i < j < n`, and

	- `lower <= nums[i] + nums[j] <= upper`

 

**Example 1:**

**Input:** nums = [0,1,7,4,4,5], lower = 3, upper = 6
**Output:** 6
**Explanation:** There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

**Example 2:**

**Input:** nums = [1,7,9,2,5], lower = 11, upper = 11
**Output:** 1
**Explanation:** There is a single fair pair: (2,3).

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `nums.length == n`

	- `-109 <= nums[i] <= 109`

	- `-109 <= lower <= upper <= 109`

## Solutions

```Python3
from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # if len(nums) == 1:
        #     return 0
        # nums.sort()
        # ans = 0
        # for l in range(len(nums)-1):
        #     for r in range(l+1,len(nums)):
        #         if lower<=(nums[l]+nums[r])<=upper:
        #             ans += 1
        #             print(f"{nums[l]}, {nums[r]}")
        # return ans

        nums.sort()
        count = 0
        for i in range(len(nums)):
            left = bisect_left(nums, lower - nums[i], i+1)
            right = bisect_right(nums, upper - nums[i], i+1)
            count += right - left
        return count
```
