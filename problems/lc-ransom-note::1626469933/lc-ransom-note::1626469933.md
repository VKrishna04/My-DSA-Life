# Ransom Note

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-ransom-note::1626469933` |
| Topics | Hash Table, String, Counting |
| Solved | 2025-05-05 |
| Runtime | 16 ms (beats 65.05100000000002%) |
| Memory | 18.1 MB (beats 100%) |

## Problem Statement

Given two strings `ransomNote` and `magazine`, return `true`_ if _`ransomNote`_ can be constructed by using the letters from _`magazine`_ and _`false`_ otherwise_.

Each letter in `magazine` can only be used once in `ransomNote`.

 

**Example 1:**

**Input:** ransomNote = "a", magazine = "b"
**Output:** false
**Example 2:**

**Input:** ransomNote = "aa", magazine = "ab"
**Output:** false
**Example 3:**

**Input:** ransomNote = "aa", magazine = "aab"
**Output:** true

 

**Constraints:**

	- `1 <= ransomNote.length, magazine.length <= 105`

	- `ransomNote` and `magazine` consist of lowercase English letters.

## Solutions

```Python3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)
        if s1 & s2 == s1:
            return True
        return False
```
