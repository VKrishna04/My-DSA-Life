# Longest Common Prefix

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-longest-common-prefix::1650472821` |
| Topics | Array, String, Trie |
| Solved | 2025-06-01 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

 

**Example 1:**

**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

**Example 2:**

**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

 

**Constraints:**

	- `1 <= strs.length <= 200`

	- `0 <= strs[i].length <= 200`

	- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Solutions

```Python3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lng = ""
        strs = sorted(strs)
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if (strs[0][i] != strs[-1][i]):
                return lng
            lng+=strs[0][i]
        
        return lng
```
