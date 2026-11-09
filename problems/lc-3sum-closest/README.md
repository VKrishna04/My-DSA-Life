# 3Sum Closest

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-3sum-closest` |
| Topics | Array, Two Pointers, Sorting |
| Solved | 2026-09-16 |
| Runtime | 407 ms (beats 19.207800000000482%) |
| Memory | 19.4 MB (beats 46.5696%) |

## Problem Statement

You are given an integer array `nums` of length `n` and an integer `target`.

Find three integers at **distinct indices** in `nums` such that the sum is **closest** to `target`.

Return the sum of the three integers.

You may assume that each input would have **exactly** one solution.

 

**Example 1:**

**Input:** nums = [-1,2,1,-4], target = 1
**Output:** 2
**Explanation:** The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

**Example 2:**

**Input:** nums = [0,0,0], target = 1
**Output:** 0
**Explanation:** The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

 

**Constraints:**

	- `3 <= nums.length <= 500`

	- `-1000 <= nums[i] <= 1000`

	- `-104 <= target <= 104`

## Solutions

```Python3
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf') 
        
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i = k + 1
            j = len(nums) - 1
            
            while i < j:
                temp = nums[k] + nums[i] + nums[j]
                
                if temp == target:
                    return temp
                
                if abs(target - temp) < abs(target - closest_sum):
                    closest_sum = temp
                
                if temp < target:
                    i += 1
                else:
                    j -= 1
                    
        return closest_sum
```
