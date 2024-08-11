# Longest Substring Without Repeating Characters

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-longest-substring-without-repeating-characters::1351982506` |
| Topics | Hash Table, String, Sliding Window |
| Solved | 2024-08-11 |
| Runtime | 453 ms (beats 5.017000000000014%) |
| Memory | 17 MB (beats 100%) |

## Problem Statement

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

 

**Example 1:**

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

**Example 2:**

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

**Example 3:**

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

**Constraints:**

	- `0 <= s.length <= 5 * 104`

	- `s` consists of English letters, digits, symbols and spaces.

## Solutions

```Python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 1
        if s is "":
            return 0
        for i in range(len(s)):
            st = ""
            for ch in s[i:]:
                if ch not in st:
                    st += ch
                    max_length=max(max_length,len(st))
                else:
                    break
        print(max_length)
        return max_length
```
