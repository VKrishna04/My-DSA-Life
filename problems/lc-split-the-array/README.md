# Split the Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-split-the-array` |
| Topics | Array, Hash Table, Counting |
| Solved | 2024-11-10 |
| Runtime | 1 ms (beats 48.0769%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

You are given an integer array `nums` of **even** length. You have to split the array into two parts `nums1` and `nums2` such that:

	- `nums1.length == nums2.length == nums.length / 2`.

	- `nums1` should contain **distinct **elements.

	- `nums2` should also contain **distinct** elements.

Return `true`_ if it is possible to split the array, and _`false` _otherwise__._

 

**Example 1:**

**Input:** nums = [1,1,2,2,3,4]
**Output:** true
**Explanation:** One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

**Example 2:**

**Input:** nums = [1,1,1,1]
**Output:** false
**Explanation:** The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `nums.length % 2 == 0 `

	- `1 <= nums[i] <= 100`

## Hints

<details>
<summary>Hint 1</summary>

It’s impossible if the same number occurs more than twice. So just check the frequency of each value.

</details>

## Solutions

### Alt approach (Python3) — imported

Submission #1448744782

```Python3
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return len(nums) % 2 == 0 and max(Counter(nums).values()) < 3

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. We iterate through the array once to count frequencies and once through the unique values.
*   **Space Complexity:** $O(n)$ to store the frequency map (`Counter`).

### 2. Correctness
The solution is **correct**. To split an array into two subarrays with distinct elements, no single value can appear more than twice. If a value appears three times, at least one subarray must contain a duplicate. Since the total length is $n$ (even), and no count exceeds 2, we can always distribute elements to fill two $n/2$ arrays.

### 3. Optimization
Instead of building the entire `Counter` and then iterating, you can check the condition **inline** to potentially return `False` early:
```python
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
    if counts[x] > 2:
        return False
return True
```
This saves time in cases where the condition is violated early in the input.

### 4. Key Algorithmic Pattern
**Frequency Counting / Hash Map:** Using a dictionary or hash table to track occurrences of elements to satisfy frequency-based constraints.
