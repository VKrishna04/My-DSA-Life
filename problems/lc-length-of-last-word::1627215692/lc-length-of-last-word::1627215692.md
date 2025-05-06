# Length of Last Word

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-length-of-last-word::1627215692` |
| Topics | String |
| Solved | 2025-05-06 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.7 MB (beats 100%) |

## Problem Statement

Given a string `s` consisting of words and spaces, return _the length of the **last** word in the string._

A **word** is a maximal substring consisting of non-space characters only.

 

**Example 1:**

**Input:** s = "Hello World"
**Output:** 5
**Explanation:** The last word is "World" with length 5.

**Example 2:**

**Input:** s = "   fly me   to   the moon  "
**Output:** 4
**Explanation:** The last word is "moon" with length 4.

**Example 3:**

**Input:** s = "luffy is still joyboy"
**Output:** 6
**Explanation:** The last word is "joyboy" with length 6.

 

**Constraints:**

	- `1 <= s.length <= 104`

	- `s` consists of only English letters and spaces `' '`.

	- There will be at least one word in `s`.

## Solutions

```Python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

```
