# Minimum Index of a Valid Split

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-index-of-a-valid-split` |
| Topics | Array, Hash Table, Sorting |
| Solved | 2024-11-13 |
| Runtime | 67 ms (beats 52.792100000000026%) |
| Memory | 33.2 MB (beats 65.48230000000001%) |

## Problem Statement

An element `x` of an integer array `arr` of length `m` is **dominant** if **more than half** the elements of `arr` have a value of `x`.

You are given a **0-indexed** integer array `nums` of length `n` with one **dominant** element.

You can split `nums` at an index `i` into two arrays `nums[0, ..., i]` and `nums[i + 1, ..., n - 1]`, but the split is only **valid** if:

	- `0 <= i < n - 1`

	- `nums[0, ..., i]`, and `nums[i + 1, ..., n - 1]` have the same dominant element.

Here, `nums[i, ..., j]` denotes the subarray of `nums` starting at index `i` and ending at index `j`, both ends being inclusive. Particularly, if `j < i` then `nums[i, ..., j]` denotes an empty subarray.

Return _the **minimum** index of a **valid split**_. If no valid split exists, return `-1`.

 

**Example 1:**

**Input:** nums = [1,2,2,2]
**Output:** 2
**Explanation:** We can split the array at index 2 to obtain arrays [1,2,2] and [2]. 
In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3. 
In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split. 
It can be shown that index 2 is the minimum index of a valid split. 

**Example 2:**

**Input:** nums = [2,1,3,1,1,1,7,1,2,1]
**Output:** 4
**Explanation:** We can split the array at index 4 to obtain arrays [2,1,3,1,1] and [1,7,1,2,1].
In array [2,1,3,1,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
In array [1,7,1,2,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
Both [2,1,3,1,1] and [1,7,1,2,1] have the same dominant element as nums, so this is a valid split.
It can be shown that index 4 is the minimum index of a valid split.

**Example 3:**

**Input:** nums = [3,3,3,3,7,2,2]
**Output:** -1
**Explanation:** It can be shown that there is no valid split.

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `1 <= nums[i] <= 109`

	- `nums` has exactly one dominant element.

## Hints

<details>
<summary>Hint 1</summary>

Find the dominant element of nums by using a hashmap to maintain element frequency, we denote the dominant element as x and its frequency as f.

</details>

<details>
<summary>Hint 2</summary>

For each index in [0, n - 2], calculate f1, x’s frequency in the subarray [0, i] when looping the index. And f2, x’s frequency in the subarray [i + 1, n - 1] which is equal to f - f1. Then we can check whether x is dominant in both subarrays.

</details>

## Solutions

```Python3
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def count_elements(nums):
            counter = {}
            for num in nums:
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1
            return counter

        full_counter = count_elements(nums)
        dominant_element = max(full_counter, key=full_counter.get)
        
        dominant_count = full_counter[dominant_element]
        
        left_count = 0
        for i in range(len(nums)):
            if nums[i] == dominant_element:
                left_count += 1
            right_count = dominant_count - left_count
            
            if left_count > (i + 1) // 2 and right_count > (len(nums) - i - 1) // 2:
                return i
        return -1

```

## AI Review

### 1. Complexity
*   **Time:** $O(n)$, where $n$ is the length of `nums`. We traverse the list twice (once for frequency counting, once for the split check).
*   **Space:** $O(n)$ to store the `full_counter` dictionary.

### 2. Correctness
The logic is **correct**. For a split to be valid with the same dominant element, that element *must* also be the dominant element of the entire array. The conditions `left_count * 2 > (i + 1)` and `right_count * 2 > (len(nums) - i - 1)` are correctly implemented using floor division logic.

### 3. Concrete Optimization
Use the **Boyer-Moore Voting Algorithm** to find the dominant element in $O(1)$ space and `collections.Counter` for cleaner code. Additionally, avoid the `max()` call on the dictionary to save a full pass.

```python
# Optimized snippet for finding dominant_element
cand, count = None, 0
for x in nums:
    if count == 0: cand = x
    count += 1 if x == cand else -1
dominant_element = cand
# Total count still needs one pass: dominant_count = nums.count(cand)
```

### 4. Key Algorithmic Pattern
**Frequency Counting / Prefix Sums:** Tracking the cumulative frequency of a specific candidate element while iterating to evaluate subarray properties in constant time.
