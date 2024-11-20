# Find All K-Distant Indices in an Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-all-k-distant-indices-in-an-array` |
| Topics | Array, Two Pointers |
| Solved | 2025-09-07 |
| Runtime | 175 ms (beats 35.10959999999995%) |
| Memory | 18 MB (beats 100%) |

## Problem Statement

You are given a **0-indexed** integer array `nums` and two integers `key` and `k`. A **k-distant index** is an index `i` of `nums` for which there exists at least one index `j` such that `|i - j| <= k` and `nums[j] == key`.

Return _a list of all k-distant indices sorted in **increasing order**_.

 

**Example 1:**

**Input:** nums = [3,4,9,1,3,9,5], key = 9, k = 1
**Output:** [1,2,3,4,5,6]
**Explanation:** Here, `nums[2] == key` and `nums[5] == key.
- For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j` where `|0 - j| <= k` and `nums[j] == key. Thus, 0 is not a k-distant index.
- For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
- For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
- For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
- For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
- For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
- For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
`Thus, we return [1,2,3,4,5,6] which is sorted in increasing order. 

**Example 2:**

**Input:** nums = [2,2,2,2,2], key = 2, k = 2
**Output:** [0,1,2,3,4]
**Explanation:** For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index. 
Hence, we return [0,1,2,3,4].

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`

	- `key` is an integer from the array `nums`.

	- `1 <= k <= nums.length`

## Hints

<details>
<summary>Hint 1</summary>

For every occurrence of key in nums, find all indices within distance k from it.

</details>

<details>
<summary>Hint 2</summary>

Use a hash table to remove duplicate indices.

</details>

## Solutions

```Python3
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        results = set()
        for j in range(len(nums)):
            if nums[j] == key:
                for i in range(max(0, j - k), min(len(nums), j+k+1)):
                    results.add(i)
        return sorted(results)
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \cdot K + N \log N)$. In the worst case (e.g., all elements are `key`), the inner loop iterates $2K+1$ times for every $j$, and the final `sorted()` call takes $O(N \log N)$.
*   **Space Complexity:** $O(N)$ to store indices in the `set`.

### 2. Correctness
The code is **correct**. It accurately identifies all valid indices and handles boundary conditions using `max(0, ...)` and `min(len(nums), ...)`. It correctly avoids duplicates via the `set`.

### 3. Concrete Optimization
You can achieve **$O(N)$ time** by avoiding redundant processing of indices. Keep track of the `last_added_index` to ensure each index is appended to a list only once:

```python
last_added = -1
results = []
for j in range(len(nums)):
    if nums[j] == key:
        start = max(last_added + 1, j - k)
        end = min(len(nums) - 1, j + k)
        for i in range(start, end + 1):
            results.append(i)
            last_added = i
return results
```
This removes the `set` overhead and the final $O(N \log N)$ sort, as indices are added in increasing order.

### 4. Key Algorithmic Pattern
**Greedy Interval Merging / Two Pointers.** The problem involves finding the union of several intervals $[j-k, j+k]$.
