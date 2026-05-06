# Partition Array for Maximum Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-partition-array-for-maximum-sum` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-06 |
| Runtime | 151 ms (beats 60.3117000000001%) |
| Memory | 19.1 MB (beats 97.4577%) |

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
*   **Time:** $O(n \cdot k)$, where $n$ is the length of the array. We iterate through the array once and, for each element, look back up to $k$ steps.
*   **Space:** $O(n)$ to store the `dp` array.

### 2. Correctness
The code is **correct** and handles edge cases well:
*   **$k=1$**: Correctly reduces to the sum of the array.
*   **$k \ge n$**: Correctly identifies the global maximum multiplied by $n$.
*   **Small arrays**: The `min(k, i)` bound prevents out-of-bounds errors.

### 3. Concrete Optimization
**Space Complexity:** Since `dp[i]` only depends on the previous $k$ values (`dp[i-1]` through `dp[i-k]`), you can reduce space from $O(n)$ to **$O(k)$** using a circular buffer (array of size $k+1$ with modulo indexing `% (k + 1)`). This is beneficial if $n$ is very large and $k$ is small.

### 4. Key Algorithmic Pattern
**Linear Dynamic Programming (Bottom-Up)**. It uses an optimal substructure where the solution for the first $i$ elements depends on the optimal solutions of smaller prefixes.
