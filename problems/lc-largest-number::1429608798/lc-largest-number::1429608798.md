# Largest Number

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-largest-number::1429608798` |
| Topics | Array, String, Greedy, Sorting |
| Solved | 2024-10-21 |
| Runtime | 3 ms (beats 63%) |
| Memory | 16.4 MB (beats 100%) |

## Problem Statement

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

**Example 1:**

**Input:** nums = [10,2]
**Output:** "210"

**Example 2:**

**Input:** nums = [3,30,34,5,9]
**Output:** "9534330"

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 109`

## Solutions

```Python3
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        nums.sort(key=cmp_to_key(compare))
        
        result = ''.join(nums)
        
        return '0' if result[0] == '0' else result

```
