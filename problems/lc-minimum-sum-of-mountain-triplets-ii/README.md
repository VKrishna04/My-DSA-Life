# Minimum Sum of Mountain Triplets II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-sum-of-mountain-triplets-ii` |
| Topics | Array |
| Solved | 2024-10-27 |
| Runtime | 161 ms (beats 9.209900000000044%) |
| Memory | 32.1 MB (beats 100%) |

## Problem Statement

You are given a **0-indexed** array `nums` of integers.

A triplet of indices `(i, j, k)` is a **mountain** if:

	- `i < j < k`

	- `nums[i] < nums[j]` and `nums[k] < nums[j]`

Return _the **minimum possible sum** of a mountain triplet of_ `nums`. _If no such triplet exists, return_ `-1`.

 

**Example 1:**

**Input:** nums = [8,6,1,5,3]
**Output:** 9
**Explanation:** Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 < 3 < 4
- nums[2] < nums[3] and nums[4] < nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

**Example 2:**

**Input:** nums = [5,4,8,7,10,2]
**Output:** 13
**Explanation:** Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 < 3 < 5
- nums[1] < nums[3] and nums[5] < nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.

**Example 3:**

**Input:** nums = [6,5,4,3,4,5]
**Output:** -1
**Explanation:** It can be shown that there are no mountain triplets in nums.

 

**Constraints:**

	- `3 <= nums.length <= 105`

	- `1 <= nums[i] <= 108`

## Hints

<details>
<summary>Hint 1</summary>

If you fix index `j`, `i` will be the smallest integer to the left of `j`, and `k` the largest integer to the right of `j`.

</details>

<details>
<summary>Hint 2</summary>

To find `i` and `k`, preprocess the prefix minimum array `prefix_min[i] = min(nums[0], nums[1], ..., nums[i])`, and the suffix minimum array `suffix_min[i] = min(nums[i], nums[i + 1], ..., nums[i - 1])`.

</details>

## Solutions

```Python3
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        output = float('inf')
        left = [0]*n
        right = [0]*n

        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(1,n):
            left[i] = min(left[i-1], nums[i])
        for i in range(n-2,-1,-1):
            right[i] = min(right[i+1], nums[i])
        
        for i in range(n-1):
            if left[i] < nums[i] and right[i] < nums[i]:
                output = min(output, left[i]+nums[i]+right[i])
        
        return output if output != float('inf') else -1
```

## AI Review

**1. Complexity**
*   **Time:** $O(n)$ — Three linear passes over the array.
*   **Space:** $O(n)$ — Two auxiliary arrays (`left` and `right`) of size $n$.

**2. Correctness**
The logic is correct. By checking `left[i] < nums[i]` and `right[i] < nums[i]`, you effectively verify that a smaller element exists both to the left (within `nums[0...i-1]`) and to the right (within `nums[i+1...n-1]`). The code handles edge cases like $n < 3$ or "no mountain found" correctly by returning `-1`.

**3. Optimization**
**Reduce Space:** You can eliminate the `left` array. Maintain a `prefix_min` variable and compute it on the fly during the final loop. This reduces space complexity to $O(n)$ for only the `right` (suffix) array.

```python
# Suffix array only
right = [0] * n
right[-1] = nums[-1]
for i in range(n - 2, -1, -1):
    right[i] = min(right[i + 1], nums[i])

prefix_min = nums[0]
for i in range(1, n - 1):
    if prefix_min < nums[i] and right[i + 1] < nums[i]:
        output = min(output, prefix_min + nums[i] + right[i + 1])
    prefix_min = min(prefix_min, nums[i])
```

**4. Key Algorithmic Pattern**
**Prefix/Suffix Precomputation:** Pre-calculating properties (like min, max, or sum) of subarrays ending or starting at each index to answer range queries in $O(1)$.
