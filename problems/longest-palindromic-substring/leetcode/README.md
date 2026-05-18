# Longest Palindromic Substring

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-longest-palindromic-substring` |
| Topics | Two Pointers, String, Dynamic Programming |
| Solved | 2024-10-23 |
| Runtime | 2275 ms (beats 19.36370000000023%) |
| Memory | 25.1 MB (beats 13.843799999999993%) |

## Problem Statement

Given a string `s`, return _the longest_ _palindromic_ _substring_ in `s`.

 

**Example 1:**

**Input:** s = "babad"
**Output:** "bab"
**Explanation:** "aba" is also a valid answer.

**Example 2:**

**Input:** s = "cbbd"
**Output:** "bb"

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consist of only digits and English letters.

## Hints

<details>
<summary>Hint 1</summary>

How can we reuse a previously computed palindrome to compute a larger palindrome?

</details>

<details>
<summary>Hint 2</summary>

If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?

</details>

<details>
<summary>Hint 3</summary>

Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

</details>

## Solutions

### Alt approach (Python3)

Duplicate resolved — 24 Oct 2024

```Python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        start, max_len = 0, 1
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        start = i
                        max_len = j - i + 1

        return s[start:start + max_len]

```
