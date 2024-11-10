# Most Frequent Even Element

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-most-frequent-even-element::1448999875` |
| Topics | Array, Hash Table, Counting |
| Solved | 2024-11-10 |
| Runtime | 7 ms (beats 99.548%) |
| Memory | 17 MB (beats 100%) |

## Problem Statement

Given an integer array `nums`, return _the most frequent even element_.

If there is a tie, return the **smallest** one. If there is no such element, return `-1`.

 

**Example 1:**

**Input:** nums = [0,1,2,2,4,4,1]
**Output:** 2
**Explanation:**
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

**Example 2:**

**Input:** nums = [4,4,4,9,2,4]
**Output:** 4
**Explanation:** 4 is the even element appears the most.

**Example 3:**

**Input:** nums = [29,47,21,41,13,37,25,7]
**Output:** -1
**Explanation:** There is no even element.

 

**Constraints:**

	- `1 <= nums.length <= 2000`

	- `0 <= nums[i] <= 105`

## Solutions

```Python3
from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = Counter([num for num in nums if num % 2 == 0])
        
        most_frequent_even = -1
        max_count = 0

        for num, count in counts.items():
            if count > max_count or (count == max_count and num < most_frequent_even):
                most_frequent_even = num
                max_count = count

        return most_frequent_even

```
