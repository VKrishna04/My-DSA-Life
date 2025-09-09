# Count Number of Pairs With Absolute Difference K

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-count-number-of-pairs-with-absolute-difference-k::1765393180` |
| Topics | Array, Hash Table, Counting |
| Solved | 2025-09-09 |
| Runtime | 115 ms (beats 5.330000000000007%) |
| Memory | 17.7 MB (beats 100%) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return _the number of pairs_ `(i, j)` _where_ `i < j` _such that_ `|nums[i] - nums[j]| == k`.

The value of `|x|` is defined as:

	- `x` if `x >= 0`.

	- `-x` if `x < 0`.

 

**Example 1:**

**Input:** nums = [1,2,2,1], k = 1
**Output:** 4
**Explanation:** The pairs with an absolute difference of 1 are:
- [**1**,**2**,2,1]
- [**1**,2,**2**,1]
- [1,**2**,2,**1**]
- [1,2,**2**,**1**]

**Example 2:**

**Input:** nums = [1,3], k = 3
**Output:** 0
**Explanation:** There are no pairs with an absolute difference of 3.

**Example 3:**

**Input:** nums = [3,2,1,5,4], k = 2
**Output:** 3
**Explanation:** The pairs with an absolute difference of 2 are:
- [**3**,2,**1**,5,4]
- [**3**,2,1,**5**,4]
- [3,**2**,1,5,**4**]

 

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 100`

	- `1 <= k <= 99`

## Solutions

```Python3
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        sorted(nums)
        for i in range(len(nums)):
            count += len([j for j in range(len(nums)) if (nums[i]-k)==nums[j]])
        return count
```
