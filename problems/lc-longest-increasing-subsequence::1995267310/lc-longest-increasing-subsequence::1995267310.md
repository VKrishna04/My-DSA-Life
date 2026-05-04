# Longest Increasing Subsequence

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-longest-increasing-subsequence::1995267310` |
| Topics | Array, Binary Search, Dynamic Programming |
| Solved | 2026-05-04 |
| Runtime | 1262 ms (beats 39.49740000000011%) |
| Memory | 19.4 MB (beats 85.3236%) |

## Problem Statement

Given an integer array `nums`, return _the length of the longest **strictly increasing **__**subsequence**_.

 

**Example 1:**

**Input:** nums = [10,9,2,5,3,7,101,18]
**Output:** 4
**Explanation:** The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

**Example 2:**

**Input:** nums = [0,1,0,3,2,3]
**Output:** 4

**Example 3:**

**Input:** nums = [7,7,7,7,7,7,7]
**Output:** 1

 

**Constraints:**

	- `1 <= nums.length <= 2500`

	- `-104 <= nums[i] <= 104`

 

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## Solutions

```Python3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)

```

## AI Review

### Review of LIS Solution

**1. Complexity**
*   **Time Complexity:** $O(N^2)$ due to the nested loops iterating over the input array.
*   **Space Complexity:** $O(N)$ to store the `dp` array.

**2. Correctness**
The logic is correct for standard cases. However:
*   **Edge Case:** If `nums` is empty (e.g., `[]`), `max(dp)` will raise a `ValueError`. While LeetCode constraints often specify $n \ge 1$, a `return max(dp) if dp else 0` is safer.

**3. Optimization**
You can optimize the time complexity to **$O(N \log N)$** using **Binary Search** (Patience Sorting). Instead of a DP table, maintain a list `tails` where `tails[i]` is the smallest ending element of all increasing subsequences of length `i+1`. For each number, use `bisect_left` to find its position in `tails` and update it.

**4. Key Algorithmic Pattern**
**Dynamic Programming (Bottom-Up):** It solves the problem by breaking it into overlapping subproblems (finding the LIS ending at each index `i`) and building the solution iteratively.
