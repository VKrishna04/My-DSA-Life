# Top K Frequent Elements

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-top-k-frequent-elements::1458507035` |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect |
| Solved | 2024-11-20 |
| Runtime | 3 ms (beats 88.8868%) |
| Memory | 20.3 MB (beats 100%) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

 

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1

**Output:** [1]

**Example 3:**

**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `-104 <= nums[i] <= 104`

	- `k` is in the range `[1, the number of unique elements in the array]`.

	- It is **guaranteed** that the answer is **unique**.

 

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Solutions

```Python3
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        heap = [(-count,value) for value,count in map.items()]
        
        heapq.heapify(heap)
        result = []
        for i in range(k):
            element = heapq.heappop(heap)
            result.append(element[1])
        return result
        
```
