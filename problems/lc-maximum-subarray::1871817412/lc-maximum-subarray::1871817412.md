# Maximum Subarray

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-maximum-subarray::1871817412` |
| Topics | Array, Divide and Conquer, Dynamic Programming |
| Solved | 2026-01-02 |
| Runtime | 94 ms (beats 5.176500000000063%) |
| Memory | 30 MB (beats 99.99520000000001%) |

## Problem Statement

Given an integer array `nums`, find the subarray with the largest sum, and return _its sum_.

 

**Example 1:**

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

**Example 2:**

**Input:** nums = [1]
**Output:** 1
**Explanation:** The subarray [1] has the largest sum 1.

**Example 3:**

**Input:** nums = [5,4,-1,7,8]
**Output:** 23
**Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `-104 <= nums[i] <= 104`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Solutions

```Python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = ans = nums[0]

        for x in nums[1:]:
            curr = max(x, curr + x)
            ans = max(ans, curr)
        return ans
```
