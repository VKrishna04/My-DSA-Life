# Partition Array for Maximum Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-partition-array-for-maximum-sum` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-06 |
| Solve Time | 36m 5s |
| Runtime | 151 ms (beats 61.41260000000008%) |
| Memory | 19.1 MB (beats 97.5823%) |

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
*   **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the array and $k$ is the maximum partition size. Each element is visited once in the outer loop, and the inner loop runs up to $k$ times.
*   **Space Complexity:** $O(n)$ to store the `dp` array.

### 2. Correctness
The solution is **correct**. It properly handles:
*   **Small Arrays:** `min(k, i)` ensures it doesn't look back further than the start of the array.
*   **Large $k$:** Correctly calculates the maximum sum if the entire array is one partition.
*   **$k=1$:** Correctly reduces to the sum of the array.

### 3. Optimization
**Space Optimization:** Since `dp[i]` only depends on the previous $k$ values (`dp[i-1]` through `dp[i-k]`), you can reduce the space complexity to **$O(k)$** by using a circular buffer (array of size $k+1$ with modulo indexing) to store only the necessary state.

### 4. Key Algorithmic Pattern
**Linear Dynamic Programming** (specifically the "Partitioning DP" variant), where the optimal solution for a prefix depends on the optimal solutions of preceding subproblems within a window of size $k$.
