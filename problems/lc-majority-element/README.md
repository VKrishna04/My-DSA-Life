# Majority Element

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-majority-element` |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Counting |
| Solved | 2024-11-10 |
| Runtime | 7 ms (beats 57.99060000000001%) |
| Memory | 18.4 MB (beats 100%) |

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

### Alt approach (Python3) — imported

Submission #1448986088

```Python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return [num for num, count in Counter(nums).items() if count > len(nums)/2][0]
```

## AI Review

### 1. Complexity
*   **Time:** $O(n)$, where $n$ is the length of `nums`. Creating the `Counter` takes $O(n)$ and iterating over its items takes $O(n)$.
*   **Space:** $O(n)$ to store the frequency map in the `Counter` object.

### 2. Correctness
The code is **correct** given the problem's guarantee that a majority element always exists. 
*   **Edge Cases:** If the input list is empty, `max()` would receive an empty sequence and raise a `ValueError`. However, LeetCode constraints typically specify $n \ge 1$.
*   **Note:** Using `max()` is redundant because there can only be one element that appears more than $n/2$ times; `next(...)` would be more idiomatic.

### 3. Optimization
**Boyer-Moore Voting Algorithm:** This optimizes space to **$O(1)$**. 
Instead of a hash map, maintain a `candidate` and a `count`. Iterate through `nums`: if `count` is 0, pick the current number as `candidate`; increment `count` if the number matches `candidate`, otherwise decrement it.

### 4. Key Algorithmic Pattern
**Frequency Counting (Hash Map):** Using a hash table to track occurrences of elements to identify those meeting a specific threshold.
