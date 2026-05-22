# Maximum Count of Positive Integer and Negative Integer

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-maximum-count-of-positive-integer-and-negative-integer` |
| Topics | Array, Binary Search, Counting |
| Solved | 2024-10-21 |
| Runtime | 3 ms (beats 32%) |
| Memory | 16.8 MB (beats 100%) |

## Problem Statement

Given an array `nums` sorted in **non-decreasing** order, return _the maximum between the number of positive integers and the number of negative integers._

	- In other words, if the number of positive integers in `nums` is `pos` and the number of negative integers is `neg`, then return the maximum of `pos` and `neg`.

**Note** that `0` is neither positive nor negative.

 

**Example 1:**

**Input:** nums = [-2,-1,-1,1,2,3]
**Output:** 3
**Explanation:** There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

**Example 2:**

**Input:** nums = [-3,-2,-1,0,0,1,2]
**Output:** 3
**Explanation:** There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

**Example 3:**

**Input:** nums = [5,20,66,1314]
**Output:** 4
**Explanation:** There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

 

**Constraints:**

	- `1 <= nums.length <= 2000`

	- `-2000 <= nums[i] <= 2000`

	- `nums` is sorted in a **non-decreasing order**.

 

**Follow up:** Can you solve the problem in `O(log(n))` time complexity?

## Hints

<details>
<summary>Hint 1</summary>

Count how many positive integers and negative integers are in the array.

</details>

<details>
<summary>Hint 2</summary>

Since the array is sorted, can we use the binary search?

</details>

## Solutions

```Python3
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # l = len(nums)
        # if nums[0] > 0 or nums[-1] < 0:
        #     return l

        # pos = 0
        # neg = 0
        # for i in range(l):
        #     if nums[i] < 0:
        #         continue
        #     neg = i
        #     if neg > l/2:
        #         return neg

        #     break
        
        # for i in range(neg+1, l):
        #     if nums[i] == 0:
        #         continue
        # pos = l - i
        # return max(neg, pos)

        neg_count = sum(1 for num in nums if num < 0)
        pos_count = sum(1 for num in nums if num > 0)

        return max(neg_count, pos_count)
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. The code performs two linear passes over the array.
*   **Space Complexity:** $O(1)$, as it only uses a few integer counters (the generator expressions do not create intermediate lists).

### 2. Correctness
The solution is **correct**. It accurately counts strictly positive and strictly negative integers, ignoring zeros as required. It handles edge cases like all zeros, all negatives, or all positives correctly.

### 3. Concrete Optimization
The input `nums` is **sorted**. Instead of a linear scan, use **Binary Search** to find the transition points.
*   Find the first index `i` where `nums[i] >= 0`. The count of negatives is `i`.
*   Find the first index `j` where `nums[j] > 0`. The count of positives is `len(nums) - j`.
This reduces the time complexity from **$O(N)$ to $O(\log N)$**.

### 4. Key Algorithmic Pattern
*   **Current Code:** Linear Scan / Iteration.
*   **Optimal Approach:** Binary Search (leveraging the sorted property of the input).
