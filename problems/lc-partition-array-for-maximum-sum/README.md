# Partition Array for Maximum Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-partition-array-for-maximum-sum` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-06 |
| Runtime | 151 ms (beats 62.974600000000024%) |
| Memory | 19.1 MB (beats 97.71979999999999%) |

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
*   **Time**: $O(N \cdot K)$, where $N$ is the length of `arr`. We iterate through $N$ states, and for each, we look back up to $K$ elements.
*   **Space**: $O(N)$ to store the `dp` table.

### 2. Correctness
The logic is sound. It correctly tracks the maximum element within the current window (`cur_max`) to calculate the potential sum. It handles the window constraint using `min(k, i)`. 
*   **Edge Cases**: $k=1$ (sum of all elements), $k=n$ (one large partition), and $n=1$ are all handled correctly by the loop boundaries.

### 3. Optimization
**Space Complexity**: You can optimize the space from **$O(N)$ to $O(K)$**. 
Since the calculation for `dp[i]` only relies on the previous $K$ values (`dp[i-1]` through `dp[i-k]`), you can use a circular buffer (array of size $K+1$ with modulo indexing) to store only the necessary state history.

### 4. Key Algorithmic Pattern
**Partition Dynamic Programming**: This involves breaking a sequence into contiguous subarrays and using the results of previous partitions to build the global maximum. It is characterized by a state transition like `dp[i] = max(dp[i-j] + cost(i-j, i))` for $1 \le j \le K$.
