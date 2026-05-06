# Partition Array for Maximum Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-partition-array-for-maximum-sum` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-06 |
| Solve Time | 1m 49s |
| Runtime | 151 ms (beats 64.1557000000001%) |
| Memory | 19.1 MB (beats 97.4895%) |

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

1.  **Time Complexity:** O(N\*K)
    *   The outer loop runs `N` times.
    *   The inner loop runs up to `K` times (or `i` times, whichever is smaller).
    *   Operations inside the inner loop are O(1).
    *   **Space Complexity:** O(N)
    *   A DP array of size `N+1` is used.

2.  **Correctness:** Correct.
    *   The `dp[i]` state correctly stores the maximum sum for the prefix `arr[0...i-1]`.
    *   The base case `dp[0]=0` is implicitly handled.
    *   The transitions correctly iterate through all possible lengths `j` (from `1` to `k`) for the last partition ending at `i-1`, efficiently calculating its sum (`cur_max * j`) and combining it with the maximum sum of the preceding subarray (`dp[i-j]`).
    *   Edge cases like `k=1`, `k>=n`, and small `n` are handled.

3.  **One concrete optimisation:**
    No significant asymptotic optimization (reducing O(N\*K)) is apparent for this problem. The current approach efficiently maintains `cur_max` within the inner loop, which is already optimal for the current DP structure.

4.  **Key algorithmic pattern used:** Dynamic Programming (bottom-up approach).
