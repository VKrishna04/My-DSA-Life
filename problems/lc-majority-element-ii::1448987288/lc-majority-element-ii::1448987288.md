# Majority Element II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-majority-element-ii::1448987288` |
| Topics | Array, Hash Table, Sorting, Counting |
| Solved | 2024-11-10 |
| Runtime | 3 ms (beats 92.829%) |
| Memory | 18.3 MB (beats 100%) |

## Problem Statement

Given an integer array of size `n`, find all elements that appear more than `&lfloor; n/3 &rfloor;` times.

 

**Example 1:**

**Input:** nums = [3,2,3]
**Output:** [3]

**Example 2:**

**Input:** nums = [1]
**Output:** [1]

**Example 3:**

**Input:** nums = [1,2]
**Output:** [1,2]

 

**Constraints:**

	- `1 <= nums.length <= 5 * 104`

	- `-109 <= nums[i] <= 109`

 

**Follow up:** Could you solve the problem in linear time and in `O(1)` space?

## Solutions

```Python3
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [num for num, count in Counter(nums).items() if count > len(nums)/3]
```
