# Check if All Characters Have Equal Number of Occurrences

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-check-if-all-characters-have-equal-number-of-occurrences` |
| Topics | Hash Table, String, Counting |
| Solved | 2024-10-20 |
| Runtime | 0 ms |
| Memory | 16.5 MB |

## Problem Statement

Given a string `s`, return `true`_ if _`s`_ is a **good** string, or _`false`_ otherwise_.

A string `s` is **good** if **all** the characters that appear in `s` have the **same** number of occurrences (i.e., the same frequency).

 

**Example 1:**

**Input:** s = "abacbc"
**Output:** true
**Explanation:** The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

**Example 2:**

**Input:** s = "aaabb"
**Output:** false
**Explanation:** The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.
