# Partition Array for Maximum Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-partition-array-for-maximum-sum` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-06 |
| Runtime | 151 ms (beats 63.60199999999996%) |
| Memory | 19.1 MB (beats 97.57349999999998%) |

## Problem Statement

Given an integer array `arr`, partition the array into (contiguous) subarrays of length **at most** `k`. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return _the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a **32-bit** integer._

 

**Example 1:**

**Input:** arr = [1,15,7,9,2,5,10], k = 3
**Output:** 84
**Explanation:** arr becomes [15,15,15,9,10,10,10]

**Example 2:**

**Input:** arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
**Output:** 83

**Example 3:**

**Input:** arr = [1], k = 1
**Output:** 1

 

**Constraints:**

	- `1 <= arr.length <= 500`

	- `0 <= arr[i] <= 109`

	- `1 <= k <= arr.length`

## Solutions

```Python3
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            cur_max = 0

            for j in range(1, min(k, i) + 1):
                cur_max = max(cur_max, arr[i - j])
                
                chunk_sum = cur_max * j
                dp[i] = max(dp[i], dp[i - j] + chunk_sum)

        return dp[n]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the array. We iterate through the array once and, for each element, look back up to $k$ steps.
*   **Space Complexity:** $O(n)$ to store the `dp` table.

### 2. Correctness
The solution is **correct**. It properly uses dynamic programming to build the maximum sum by considering all possible valid partitions ending at index `i`.
*   **Edge Cases:** It correctly handles $k=1$ (sum of array), $k=n$ (max value * $n$), and small arrays where $i < k$ using `min(k, i)`.

### 3. Optimization
**Space Optimization:** Since `dp[i]` only depends on the previous $k$ values (`dp[i-1]` to `dp[i-k]`), you can reduce the space complexity from **$O(n)$ to $O(k)$** by using a circular buffer (an array of size $k+1$) and the modulo operator `% (k+1)`.

### 4. Key Algorithmic Pattern
**Dynamic Programming (Linear):** Specifically, this is a "look-back" DP where the state at index `i` is determined by iterating over a window of preceding states of size at most $k$.
