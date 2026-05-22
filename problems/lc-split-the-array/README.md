# Split the Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-split-the-array` |
| Topics | Array, Hash Table, Counting |
| Solved | 2024-11-10 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.7 MB (beats 100%) |

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

```Python3
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return len(nums) % 2 == 0 and max(Counter(nums).values()) < 3

```

## AI Review

### Analysis

1.  **Complexity**:
    *   **Time**: $O(n)$ where $n$ is the length of `nums`. Counting elements takes linear time, and finding the maximum value in the frequency map also takes $O(n)$ in the worst case.
    *   **Space**: $O(n)$ to store the frequency counts in the `Counter` dictionary.

2.  **Correctness**:
    *   The logic is **correct**. To split an array into two sets of distinct elements, no single value can appear more than twice. If a value appears 3 times, it is impossible to distribute them without one set receiving at least two.
    *   **Edge Case**: The problem constraints usually specify $n$ is even, but `len(nums) % 2 == 0` provides an extra layer of safety.

3.  **Optimisation**:
    *   **Early Exit**: Instead of counting the entire array and then checking the maximum, iterate through the numbers and return `False` immediately if any frequency reaches 3. This avoids processing the full list if a violation is found early.
    ```python
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > 2: return False
    return True
    ```

4.  **Key Pattern**:
    *   **Frequency Counting / Hashing**: Using a hash map to track occurrences to satisfy distinctness constraints.
