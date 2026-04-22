# Minimum ASCII Delete Sum for Two Strings

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-ascii-delete-sum-for-two-strings::1985691602` |
| Topics | String, Dynamic Programming |
| Solved | 2026-04-22 |
| Runtime | 263 ms (beats 58.53079999999975%) |
| Memory | 23.6 MB (beats 58.66159999999996%) |

## Problem Statement

Given two strings `s1` and `s2`, return _the lowest **ASCII** sum of deleted characters to make two strings equal_.

 

**Example 1:**

**Input:** s1 = "sea", s2 = "eat"
**Output:** 231
**Explanation:** Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

**Example 2:**

**Input:** s1 = "delete", s2 = "leet"
**Output:** 403
**Explanation:** Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

 

**Constraints:**

	- `1 <= s1.length, s2.length <= 1000`

	- `s1` and `s2` consist of lowercase English letters.

## Solutions

```Python3
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for j in range(1, len(s2)+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(M \times N)$, where $M$ and $N$ are the lengths of `s1` and `s2`. We iterate through every cell in the 2D DP table.
*   **Space Complexity:** $O(M \times N)$ to store the `dp` table.

**2. Correctness**
*   The solution is **correct**. It properly initializes the base cases (cost of deleting all characters from one string to match an empty string) and correctly implements the transition logic for matching vs. non-matching characters.
*   **Edge Cases:** Handles empty strings, single-character strings, and strings with no common characters correctly.

**3. Concrete Optimization**
*   **Space Optimization:** Since `dp[i][j]` only depends on the current and previous rows (`dp[i-1][j-1]`, `dp[i-1][j]`, and `dp[i][j-1]`), you can reduce the space complexity to **$O(\min(M, N))$** by using a 1D array (and one variable to store the "top-left" value) instead of a full 2D matrix.

**4. Key Algorithmic Pattern**
*   **Dynamic Programming (Bottom-Up):** This is a variation of the **Longest Common Subsequence (LCS)** or **Edit Distance** pattern, where the "cost" is defined by ASCII values rather than unit counts.
