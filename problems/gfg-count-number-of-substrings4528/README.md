# Count Number Of Substrings

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-count-number-of-substrings4528` |
| Topics | sliding-window, two-pointer-algorithm, Strings, Dynamic Programming, Algorithms |
| Solved | 2026-06-24 |

## Problem Statement

You are given a string **s** consisting** **of lowercase characters and an integer **k**, You have to count all possible **substrings **that have **exactly k distinct** characters.

**Examples :**

**Input: **s = "abc", k = 2
**Output: **2
**Explanation**: Possible substrings are ["ab", "bc"]

**Input**: s = "aba", k = 2
**Output: **3
**Explanation**: Possible substrings are ["ab", "ba", "aba"]
**Input: **s = "aa", k = 1
**Output: **3
**Explanation****:** Possible substrings are ["a", "a", "aa"]
**Constraints:**
1 &le; s.size() &le; 106
1 &le; k &le; 26
