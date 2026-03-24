# Merge Strings Alternately

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-merge-strings-alternately::1957612804` |
| Topics | Two Pointers, String |
| Solved | 2026-03-24 |
| Runtime | 56 ms (beats 5.666599999999969%) |
| Memory | 19.4 MB (beats 17.745299999999993%) |

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.



Return _the merged string._



 


**Example 1:**




**Input:** word1 = "abc", word2 = "pqr"
**Output:** "apbqcr"
**Explanation:** The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


**Example 2:**




**Input:** word1 = "ab", word2 = "pqrs"
**Output:** "apbqrs"
**Explanation:** Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


**Example 3:**




**Input:** word1 = "abcd", word2 = "pq"
**Output:** "apbqcd"
**Explanation:** Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d


 


**Constraints:**




	- `1 <= word1.length, word2.length <= 100`

	- `word1` and `word2` consist of lowercase English letters.

## Solutions

```Python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i += 1
        return result
```
