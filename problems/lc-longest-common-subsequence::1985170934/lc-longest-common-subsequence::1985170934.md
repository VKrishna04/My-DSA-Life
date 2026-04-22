# Longest Common Subsequence

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-longest-common-subsequence::1985170934` |
| Topics | String, Dynamic Programming |
| Solved | 2026-04-22 |
| Runtime | 353 ms (beats 63.31260000000027%) |
| Memory | 44.3 MB (beats 57.71480000000023%) |

## Problem Statement

Given two strings `text1` and `text2`, return _the length of their longest **common subsequence**. _If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

	- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

 

**Example 1:**

**Input:** text1 = "abcde", text2 = "ace" 
**Output:** 3  
**Explanation:** The longest common subsequence is "ace" and its length is 3.

**Example 2:**

**Input:** text1 = "abc", text2 = "abc"
**Output:** 3
**Explanation:** The longest common subsequence is "abc" and its length is 3.

**Example 3:**

**Input:** text1 = "abc", text2 = "def"
**Output:** 0
**Explanation:** There is no such common subsequence, so the result is 0.

 

**Constraints:**

	- `1 <= text1.length, text2.length <= 1000`

	- `text1` and `text2` consist of only lowercase English characters.

## Solutions

```Python3
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
```

## AI Review

### Review of LCS Python Solution

**1. Complexity**
*   **Time Complexity:** $O(M \times N)$, where $M$ and $N$ are the lengths of `text1` and `text2`. We iterate through every cell in the 2D grid once.
*   **Space Complexity:** $O(M \times N)$ to store the DP table.

**2. Correctness**
The implementation is **correct**. It accurately implements the standard bottom-up dynamic programming approach for LCS. 
*   **Edge Cases:** Handles empty strings correctly (returns 0). Handles strings with no common characters or identical strings correctly.

**3. Concrete Optimization**
**Space Optimization:** You can reduce the space complexity to **$O(\min(M, N))$**. Since calculating the current row only requires values from the previous row, you only need two rows (or one row plus a variable to store the "top-left" diagonal value). For maximum efficiency, ensure the inner loop iterates over the shorter string.

**4. Key Algorithmic Pattern**
**Dynamic Programming (Bottom-Up)**. Specifically, this is a **multi-sequence DP** pattern used for string alignment and comparison problems.
