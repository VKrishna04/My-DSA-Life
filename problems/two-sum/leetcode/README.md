# Two Sum

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-two-sum` |
| Topics | Array, Hash Table |
| Solved | 2024-10-22 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

 

**Example 1:**

**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

**Example 3:**

**Input:** nums = [3,3], target = 6
**Output:** [0,1]

 

**Constraints:**

	- `2 <= nums.length <= 104`

	- `-109 <= nums[i] <= 109`

	- `-109 <= target <= 109`

	- **Only one valid answer exists.**

 

**Follow-up: **Can you come up with an algorithm that is less than `O(n2)` time complexity?

## Hints

<details>
<summary>Hint 1</summary>

A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions just for completeness. It is from these brute force solutions that you can come up with optimizations.

</details>

<details>
<summary>Hint 2</summary>

So, if we fix one of the numbers, say `x`, we have to scan the entire array to find the next number `y` which is `value - x` where value is the input parameter. Can we change our array somehow so that this search becomes faster?

</details>

<details>
<summary>Hint 3</summary>

The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

</details>

## Solutions

```Python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
```

## AI Review

### Analysis

1.  **Complexity**:
    *   **Time**: $O(n)$ – The list is traversed once; dictionary lookups and insertions are $O(1)$ on average.
    *   **Space**: $O(n)$ – In the worst case, the dictionary stores $n-1$ elements.

2.  **Correctness**: 
    The logic is correct and robust. By checking for the `complement` *before* adding the current element to the dictionary, it prevents using the same index twice. It correctly handles negative numbers, zeros, and duplicate values.

3.  **Optimization**: 
    This is the optimal one-pass approach for time complexity. To optimize **space** to $O(1)$, you could sort the array and use the **Two-Pointer technique**, but this would increase time complexity to $O(n \log n)$ due to sorting and is only applicable if you can return values instead of original indices (sorting loses index positions unless tracked).

4.  **Key Algorithmic Pattern**: 
    **Hash Map (One-Pass)** – Using a dictionary to trade space for a constant-time lookup of a previously seen value.
