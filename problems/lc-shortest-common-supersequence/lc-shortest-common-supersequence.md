# Shortest Common Supersequence 

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-shortest-common-supersequence` |
| Topics | String, Dynamic Programming |
| Solved | 2026-04-23 |
| Runtime | 342 ms (beats 67.58709999999988%) |
| Memory | 44.4 MB (beats 46.32239999999992%) |

## Problem Statement

Given two strings `str1` and `str2`, return _the shortest string that has both _`str1`_ and _`str2`_ as **subsequences**_. If there are multiple valid strings, return **any** of them.

A string `s` is a **subsequence** of string `t` if deleting some number of characters from `t` (possibly `0`) results in the string `s`.

 

**Example 1:**

**Input:** str1 = "abac", str2 = "cab"
**Output:** "cabac"
**Explanation:** 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

**Example 2:**

**Input:** str1 = "aaaaaaaa", str2 = "aaaaaaaa"
**Output:** "aaaaaaaa"

 

**Constraints:**

	- `1 <= str1.length, str2.length <= 1000`

	- `str1` and `str2` consist of lowercase English letters.

## Solutions

```Python3
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        result = []
        i, j = len(str1), len(str2)
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -=1
        
        while i > 0:
            result.append(str1[i-1])
            i-=1
        while j > 0:
            result.append(str2[j-1])
            j-=1

        return "".join(result[::-1])
```

## AI Review

**1. Complexity**
*   **Time:** $O(N \times M)$, where $N$ and $M$ are the lengths of `str1` and `str2`, required to fill the DP table and backtrack.
*   **Space:** $O(N \times M)$ to store the DP table.

**2. Correctness**
The solution is correct. It successfully finds the Longest Common Subsequence (LCS) and performs a "backtracking" reconstruction. By including characters from both strings but only including the LCS characters once, it guarantees the shortest supersequence. It correctly handles remaining characters when one index reaches zero.

**3. Optimization**
While space can be reduced to $O(\min(N, M))$ to find the *length* of the LCS, reconstructing the *string* typically requires the full $O(N \times M)$ table. A small optimization is to ensure `str2` is the shorter string to slightly reduce the DP table width, though the Big-O remains the same.

**4. Key Algorithmic Pattern**
**Dynamic Programming** (specifically the **Longest Common Subsequence** variant) combined with **Path Reconstruction (Backtracking)**.
