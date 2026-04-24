# Longest Palindromic Subsequence

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-longest-palindromic-subsequence::1987087739` |
| Topics | String, Dynamic Programming |
| Solved | 2026-04-24 |
| Runtime | 580 ms (beats 79.61380000000021%) |
| Memory | 35.6 MB (beats 70.29720000000007%) |

## Problem Statement

Given a string `s`, find _the longest palindromic **subsequence**'s length in_ `s`.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

**Example 1:**

**Input:** s = "bbbab"
**Output:** 4
**Explanation:** One possible longest palindromic subsequence is "bbbb".

**Example 2:**

**Input:** s = "cbbd"
**Output:** 2
**Explanation:** One possible longest palindromic subsequence is "bb".

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists only of lowercase English letters.

## Solutions

```Python3
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*(len(s)) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N^2)$, where $N$ is the length of the string, due to the nested loops traversing the $N \times N$ matrix.
*   **Space Complexity:** $O(N^2)$ to store the 2D DP table.

### 2. Correctness
The code is **correct** and handles standard cases well. 
*   **Edge Cases:** It correctly handles single-character strings (returns 1) and strings with no repeating characters (returns 1). 
*   **Empty String:** If the input were empty, it would return 0 (though LeetCode constraints usually specify $1 \le s.length$).

### 3. Optimization
**Space Optimization:** The current row `dp[i]` only depends on the previous row `dp[i+1]` and its own previous values. You can reduce space complexity to **$O(N)$** by using two 1D arrays (current and previous) or a single 1D array updated in place.

### 4. Key Algorithmic Pattern
**Dynamic Programming (2D Tabulation):** It uses an interval-based DP approach where the solution for a larger substring $[i, j]$ is built from smaller sub-problems $[i+1, j-1]$, $[i+1, j]$, and $[i, j-1]$.
