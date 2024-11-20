# Minimum Positive Sum Subarray 

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-minimum-positive-sum-subarray` |
| Topics | Array, Sliding Window, Prefix Sum |
| Solved | 2024-11-24 |
| Runtime | 59 ms (beats 28.009900000000048%) |
| Memory | 16.8 MB (beats 100%) |

## Problem Statement

You are given an integer array `nums` and **two** integers `l` and `r`. Your task is to find the **minimum** sum of a **subarray** whose size is between `l` and `r` (inclusive) and whose sum is greater than 0.

Return the **minimum** sum of such a subarray. If no such subarray exists, return -1.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

 

**Example 1:**

**Input:** nums = [3, -2, 1, 4], l = 2, r = 3

**Output:** 1

**Explanation:**

The subarrays of length between `l = 2` and `r = 3` where the sum is greater than 0 are:

	- `[3, -2]` with a sum of 1

	- `[1, 4]` with a sum of 5

	- `[3, -2, 1]` with a sum of 2

	- `[-2, 1, 4]` with a sum of 3

Out of these, the subarray `[3, -2]` has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

**Example 2:**

**Input:** nums = [-2, 2, -3, 1], l = 2, r = 3

**Output:** -1

**Explanation:**

There is no subarray of length between `l` and `r` that has a sum greater than 0. So, the answer is -1.

**Example 3:**

**Input:** nums = [1, 2, 3, 4], l = 2, r = 4

**Output:** 3

**Explanation:**

The subarray `[1, 2]` has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= l <= r <= nums.length`

	- `-1000 <= nums[i] <= 1000`

## Hints

<details>
<summary>Hint 1</summary>

Check every subarray, since constraints are small.

</details>

## Solutions

```Python3
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minsum = float('inf')
        
        for start in range(n):
            currsum = 0
            for end in range(start, n):
                currsum += nums[end]
                length = end - start + 1
                if l <= length <= r and currsum > 0:
                    minsum = min(minsum, currsum)
        
        return minsum if minsum != float('inf') else -1
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. The nested loops iterate through all possible subarrays.
*   **Space Complexity:** $O(1)$, as it only uses a few scalar variables regardless of input size.

### 2. Correctness
The code is **correct** for the given constraints. It exhaustively checks every subarray, verifies if the length is within $[l, r]$, and ensures the sum is strictly positive.
*   **Edge Cases:** Handled correctly (e.g., no positive sum found returns -1; length constraints are inclusive).
*   **Performance Note:** While $O(n^2)$ passes for $n \le 100$ (the constraint for this specific problem), it would fail on larger datasets.

### 3. Optimization
Instead of recalculating sums from every `start` index, use a **Prefix Sum** array or a **Sliding Window** for each fixed length $k \in [l, r]$.
**Concrete Step:** Iterate through each valid length $k$ from $l$ to $r$. For each $k$, use a sliding window to calculate the sum in $O(n)$. This results in $O(n \cdot (r-l+1))$ time, which is more efficient when $r-l$ is small.

### 4. Key Algorithmic Pattern
**Brute Force / Subarray Traversal:** The solution uses nested loops to evaluate all contiguous subarrays within a specific range.
