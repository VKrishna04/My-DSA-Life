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

## AI Review

1. **Complexity:** $O(n^2)$ time complexity due to the nested traversal and two-pointer scan after sorting. $O(1)$ or $O(n)$ space complexity depending on the sorting algorithm's implementation.

2. **Correctness:** The solution is correct. It successfully handles duplicates to skip redundant work and properly bounds the closest sum update. No edge cases fail (handles negative numbers and arrays of length 3 correctly).

3. **Optimisation:** You can add an early exit: if the smallest possible sum with `nums[k]` exceeds `target` (e.g., `nums[k] + nums[k+1] + nums[k+2] > target`), you can break out of the outer loop because subsequent sums will only be larger. Conversely, if the largest possible sum with `nums[k]` is less than `target` (e.g., `nums[k] + nums[-2] + nums[-1] < target`), you can safely `continue` to the next `k`.

4. **Pattern:** Two Pointers combined with Sorting.
