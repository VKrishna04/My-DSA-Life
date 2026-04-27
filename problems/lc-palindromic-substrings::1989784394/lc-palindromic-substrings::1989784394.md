# Palindromic Substrings

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-palindromic-substrings::1989784394` |
| Topics | Two Pointers, String, Dynamic Programming |
| Solved | 2026-04-27 |
| Runtime | 207 ms (beats 26.074999999999942%) |
| Memory | 27.3 MB (beats 14.048199999999998%) |

## Problem Statement

Given a string `s`, return _the number of **palindromic substrings** in it_.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

 

**Example 1:**

**Input:** s = "abc"
**Output:** 3
**Explanation:** Three palindromic strings: "a", "b", "c".

**Example 2:**

**Input:** s = "aaa"
**Output:** 6
**Explanation:** Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.

## Solutions

### AI-merge proposal

### Alt approach (Python3)

Duplicate resolved — 27 Apr 2026

```Python3
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[0]*l for _ in range(l)]
        count = 0

        for i in range(l-1,-1,-1):
            dp[i][i] = 1
            count += 1
            for j in range(i+1,l):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    count += 1
                else:
                    dp[i][j] = False
        return count
```

### Alt approach (Python3)

Duplicate resolved — 27 Apr 2026

```Python3
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[0]*l for _ in range(l)]
        count = 0

        for i in range(l-1,-1,-1):
            dp[i][i] = 1
            count += 1
            for j in range(i+1,l):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    count += 1
                else:
                    dp[i][j] = False
        return count
```

## AI Review

### Review of Palindromic Substrings Solution

**1. Complexity**
*   **Time Complexity:** $O(N^2)$. The outer loop runs $2N-1$ times (covering all possible centers), and the inner `while` loop expands up to $N/2$ times in the worst case (e.g., "aaaaa").
*   **Space Complexity:** $O(1)$. The algorithm uses only a few integer variables regardless of input size.

**2. Correctness**
The solution is **correct**. By using the $2N-1$ center logic, it elegantly handles both odd-length palindromes (centered on a character) and even-length palindromes (centered between characters). It handles edge cases like single-character strings ($N=1$) and strings with no multi-character palindromes correctly.

**3. Optimization**
While $O(N^2)$ is standard for this problem, **Manacher’s Algorithm** can optimize the time complexity to **$O(N)$**. It achieves this by reusing work from previously processed palindromes via a "mirror" property, though it is significantly more complex to implement.

**4. Key Algorithmic Pattern**
**Expand Around Center.** This pattern avoids the $O(N^2)$ space requirement of Dynamic Programming by identifying all $2N-1$ potential midpoints and expanding outwards as long as the palindrome property holds.
