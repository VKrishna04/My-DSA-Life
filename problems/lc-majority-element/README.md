# Majority Element

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-majority-element` |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Counting |
| Solved | 2024-11-10 |
| Runtime | 7 ms (beats 57.99060000000001%) |
| Memory | 18.5 MB (beats 100%) |

## Problem Statement

Given an array `nums` of size `n`, return _the majority element_.

The majority element is the element that appears more than `&lfloor;n / 2&rfloor;` times. You may assume that the majority element always exists in the array.

 

**Example 1:**

**Input:** nums = [3,2,3]
**Output:** 3
**Example 2:**

**Input:** nums = [2,2,1,1,1,2,2]
**Output:** 2

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5 * 104`

	- `-109 <= nums[i] <= 109`

	- The input is generated such that a majority element will exist in the array.

 

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## Solutions

```Python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return [num for num, count in Counter(nums).items() if count > len(nums)/2][0]
```

## AI Review

### Review of Majority Element Solution

**1. Complexity**
*   **Time Complexity:** $O(n)$ — Requires one pass to build the frequency map and one pass to iterate through its keys.
*   **Space Complexity:** $O(n)$ — In the worst case (no element occurs more than once except for the majority), the hash map stores approximately $n/2$ unique keys.

**2. Correctness**
*   **Logic:** Correct. It strictly follows the definition of a majority element ($> n/2$).
*   **Edge Cases:** Handles single-element arrays correctly ($1 > 0.5$). However, if the input list is empty or lacks a majority element, it will raise an `IndexError`. The problem constraints usually guarantee a majority element exists.

**3. Optimization**
Use **Boyer-Moore Voting Algorithm** to reduce space complexity to **$O(1)$**. This algorithm tracks a candidate and a counter, incrementing for matches and decrementing for mismatches, avoiding the need for a hash map.

**4. Key Algorithmic Pattern**
*   **Frequency Counting / Hash Mapping:** Leveraging a hash table (`collections.Counter`) to track occurrences of elements.
